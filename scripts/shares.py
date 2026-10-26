"""shares/ 下分享稿的文件头读写，share.py 和 expire.py 共用。

分享稿格式：

    ---
    recipient: 给谁
    purpose: 为什么给
    expires: 2026-11-26     （可选，不填默认创建后 30 天，当天删除）
    ---
    正文，也就是发出去的内容。

share.py 发出后会补上 created、gist_id、url、source_commit、status；
expire.py 删除后把 status 改成 deleted 并记下 deleted 日期。
"""

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SHARES = REPO / "shares"
DEFAULT_DAYS = 30
FIELDS = ["recipient", "purpose", "created", "expires", "status", "deleted", "gist_id", "url", "source_commit"]


def read(path):
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise SystemExit(f"{path} 没有文件头")
    head, body = text[4:].split("\n---\n", 1)
    meta = {}
    for line in head.splitlines():
        if line.strip():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
    return meta, body


def write(path, meta, body):
    keys = [k for k in FIELDS if meta.get(k)] + [k for k in meta if k not in FIELDS]
    head = "\n".join(f"{k}: {meta[k]}" for k in keys)
    Path(path).write_text(f"---\n{head}\n---\n{body}", encoding="utf-8")
