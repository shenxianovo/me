#!/usr/bin/env python3
"""删除到期的分享 gist，并在分享稿文件头里标记已删除。

用法：
  scripts/expire.py                     删除所有到期的
  scripts/expire.py --now <文件>...      不管到没到期，立刻收回这几篇
"""

import datetime
import subprocess
import sys

from shares import SHARES, read, write


def delete_gist(gist_id):
    result = subprocess.run(["gh", "gist", "delete", gist_id, "--yes"], capture_output=True, text=True)
    if result.returncode == 0:
        return
    # 已经被手动删掉的也算删除成功
    check = subprocess.run(["gh", "api", f"gists/{gist_id}", "--silent"], capture_output=True, text=True)
    if "404" not in check.stderr:
        raise SystemExit(f"删除 gist {gist_id} 失败：{result.stderr.strip()}")


def main():
    args = sys.argv[1:]
    force = bool(args) and args[0] == "--now"
    if force and len(args) == 1 or args and not force:
        sys.exit(__doc__.strip())
    paths = args[1:] if force else sorted(SHARES.glob("*.md"))

    today = datetime.date.today()
    for path in paths:
        meta, body = read(path)
        if meta.get("status") != "active":
            if force:
                print(f"跳过 {path}：状态是 {meta.get('status') or '未发出'}")
            continue
        if not force and datetime.date.fromisoformat(meta["expires"]) > today:
            continue
        delete_gist(meta["gist_id"])
        meta.update(status="deleted", deleted=today.isoformat())
        write(path, meta, body)
        print(f"已删除 {path}：{meta['url']}")


if __name__ == "__main__":
    main()
