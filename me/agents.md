---
title: "我的 Agent 全局说明"
last_updated: "2026-11-22"
---

# 我的 Agent 全局说明

这是我在自己机器上给 Claude Code 和 Codex 的全局入口：`~/.claude/CLAUDE.md` 和 `~/.codex/AGENTS.md` 都是指向这个文件的软链接。做事前先读协作约定：

@~/Code/Personal/me/me/collaboration.md

我的背景、经历和想法在 `~/Code/Personal/me/ME.md`，需要时按需读相关章节。这个仓库是公开的，内容按公开资料使用；修改规则见仓库根目录的 `AGENTS.md`。

## 分工

- Claude 写规格、审查，界面和文档也由 Claude 自己写。
- 已经定下来的实现交给 Codex 的 `gpt-6.2-sol`。规格写清范围、约束和验收；做完 Claude 审 diff，用真实数据验证。
- 策略和复杂逻辑先和 `gpt-6.2-astra` 讨论，思考强度 high 以上。
- 两边不同时改同一个文件。

## 写文档

用最少、最精确的语言把需要的信息说全。事实用表格，步骤用编号列表，流程和结构用图。不写防御性的否定和泛泛的建议。

## 提交

Conventional Commits，只写标题，不加 `Co-Authored-By` 之类的署名行。

## 出问题时

偶发的失败照常接受，不为它加重试、去抖或防御性配置。第一次遇到非预期的系统性失败就停下来，说清现象和可选方案，等我决定，不反复重跑或绕过去。
