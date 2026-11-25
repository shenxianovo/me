---
title: "我的 Agent 全局说明"
last_updated: "2026-11-25"
---

# 我的 Agent 全局说明

这是我在自己机器上给 Claude Code、Codex 和 Antigravity 的全局入口：`~/.claude/CLAUDE.md`、`~/.codex/AGENTS.md` 和 `~/.gemini/AGENTS.md` 都是指向这个文件的软链接。做事前先读协作约定：

@~/Code/Personal/me/me/collaboration.md

我的背景、经历和想法在 `~/Code/Personal/me/ME.md`，需要时按需读相关章节。这个仓库是公开的，内容按公开资料使用；修改规则见仓库根目录的 `AGENTS.md`。

## 分工

这一节用于 Claude Code 调度 Codex 和 Gemini；我直接用 Antigravity 时不套这套分工。

- Claude 写规格，界面和文档也由 Claude 自己写。
- 几十行以内的改动、修审查发现的问题、要和界面来回对接口的功能，Claude 自己做。
- 接口和验收已经定下来的成块实现，以及策略和复杂逻辑的讨论，交给 Codex。规格写清范围、约束、验收和要一起改的同类；做完 Claude 审 diff，用真实数据验证。
- 合并前的审查交给 Codex（`--ask`），Claude 核实它报出的问题。
- 大方案 Claude 出一份，同时让 Gemini（`--ask`）独立出一份：只给它我的原话和必要背景，不给 Claude 的草稿和倾向。Claude 合并两份，有分歧以代码和实际数据为准，写明采纳和不采纳的部分及理由。
- 界面文案和交互 Claude 先做一版，再请 Gemini（`--ask`）当顾问改一遍：告诉它这一页给谁用、要让人做成什么、现在的文案和交互。只改几个字的不用。
- 代码分析和事实判断不交给 Gemini；它给的结论 Claude 核实后再用。
- 不同 Agent 不同时改同一个文件。

### 派活

统一用 `~/.local/bin/dispatch`，不直接调 `codex exec` 或 `agy`。任务写成文件，放后台跑；最后一条回复在同目录的 `<文件名>.out.md`，会话 ID 在输出开头。`<agent>` 是 `codex`（`gpt-6.2-astra`）或 `gemini`（`gemini-4-neon`）。

| 用途 | 命令 | 思考强度 |
|---|---|---|
| 实现 | `dispatch <agent> <仓库> <规格.md>` | high |
| 讨论，只读不改 | `dispatch <agent> --ask <仓库> <问题.md>` | xhigh |
| 追加 | `dispatch <agent> [--ask] --resume <会话ID> <仓库> <追加.md>` | 与原任务相同 |

## 写文档

用最少、最精确的语言把需要的信息说全。事实用表格，步骤用编号列表，流程和结构用图。不写防御性的否定和泛泛的建议。

## 提交

Conventional Commits，只写标题，不加 `Co-Authored-By` 之类的署名行。

## 出问题时

偶发的失败照常接受，不为它加重试、去抖或防御性配置。第一次遇到非预期的系统性失败就停下来，说清现象和可选方案，等我决定，不反复重跑或绕过去。
