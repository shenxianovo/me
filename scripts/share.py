#!/usr/bin/env python3
"""把一篇分享稿发成 secret gist，并把 gist 信息写回它的文件头。

用法：scripts/share.py shares/<文件>.md
"""

import datetime
import subprocess
import sys

from shares import DEFAULT_DAYS, REPO, read, write


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__.strip())
    path = sys.argv[1]
    meta, body = read(path)

    if meta.get("gist_id"):
        sys.exit(f"{path} 已经发过了：{meta.get('url')}")
    for key in ("recipient", "purpose"):
        if not meta.get(key):
            sys.exit(f"{path} 的文件头缺少 {key}")
    if not body.strip():
        sys.exit(f"{path} 正文是空的")

    today = datetime.date.today()
    expires = meta.get("expires") or (today + datetime.timedelta(days=DEFAULT_DAYS)).isoformat()
    if datetime.date.fromisoformat(expires) <= today:
        sys.exit(f"过期日 {expires} 不晚于今天")

    commit = subprocess.run(
        ["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    # gh gist create 默认就是 secret
    result = subprocess.run(
        ["gh", "gist", "create", "--filename", "shenxianovo.md", "-"],
        input=body.lstrip("\n"), capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.exit(f"创建 gist 失败：{result.stderr.strip()}")
    url = result.stdout.strip().splitlines()[-1]

    meta.update(
        created=today.isoformat(),
        expires=expires,
        status="active",
        gist_id=url.rstrip("/").rsplit("/", 1)[-1],
        url=url,
        source_commit=commit,
    )
    write(path, meta, body)
    print(f"{url}（{expires} 删除）")


if __name__ == "__main__":
    main()
