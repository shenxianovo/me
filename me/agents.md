---
title: "我的 Agent 全局说明"
last_updated: "2026-11-24"
---

# 我的 Agent 全局说明

这是我在自己机器上给 Claude Code 和 Codex 的全局入口：`~/.claude/CLAUDE.md` 和 `~/.codex/AGENTS.md` 都是指向这个文件的软链接。做事前先读协作约定：

@~/Code/Personal/me/me/collaboration.md

我的背景、经历和想法在 `~/Code/Personal/me/ME.md`，需要时按需读相关章节。这个仓库是公开的，内容按公开资料使用；修改规则见仓库根目录的 `AGENTS.md`。

## 分工

- Claude 写规格、审查，界面和文档也由 Claude 自己写。
- 几十行以内的改动、修审查发现的问题、要和界面来回对接口的功能，Claude 自己做。
- 接口和验收已经定下来的成块实现，以及策略和复杂逻辑的讨论，交给 Codex 的 `gpt-6.2-astra`。规格写清范围、约束、验收和要一起改的同类；做完 Claude 审 diff，用真实数据验证。
- 两边不同时改同一个文件。

### 调用 Codex

统一用 `~/.local/bin/codex-worker`，不直接调 `codex exec`。任务写成文件，放后台跑；最后一条回复在同目录的 `<文件名>.out.md`，会话 ID 在输出开头。

| 用途 | 命令 | 思考强度 |
|---|---|---|
| 实现 | `codex-worker <仓库> <规格.md>` | high |
| 讨论 | `codex-worker --ask <仓库> <问题.md>` | xhigh |
| 追加 | `codex-worker [--ask] --resume <会话ID> <仓库> <追加.md>` | 同原会话 |

## 写文档

用最少、最精确的语言把需要的信息说全。事实用表格，步骤用编号列表，流程和结构用图。不写防御性的否定和泛泛的建议。

## 提交

Conventional Commits，只写标题，不加 `Co-Authored-By` 之类的署名行。

## 出问题时

偶发的失败照常接受，不为它加重试、去抖或防御性配置。第一次遇到非预期的系统性失败就停下来，说清现象和可选方案，等我决定，不反复重跑或绕过去。
