---
title: "写代码这几年"
last_updated: "2026-10-26"
---

# 写代码这几年

## 命令行和服务器

大一自学了 MIT 的《The Missing Semester of Your CS Education》，然后在 Windows 上装了 WSL，开始用起类 UNIX 命令行。Linux 是我自己找课、自己搭环境入门的，没等学校的操作系统课。

云服务器也是大一开始玩的。当时 Azure 给学生每年 100 美元额度，按当时的价格，我算着够租两台 1 核 CPU、1 GiB 内存（1C1G）的小机器，一开始只租了一台。那时候想试试服务器和部署，能白嫖就很开心了。

一开始租它就是想挂个博客。博客挂上了，之后很长时间没管。那会儿只是想把自己做的东西放到云上跑，没想过搭什么基础设施。

大二下（2025 年春）以后有新项目要部署，才把这台吃灰的服务器重新用起来。第一个部署的是什么，我记不清了，可能是换了框架的新博客。我也想过是不是 Heartbeat 的后端，可 Heartbeat 是后来才做的，大概是记混了。博客框架换过好几次，名字都忘了。总之是项目要部署，我才开始正经用服务器，没有为了玩运维去玩运维。

后来部署的东西越来越多。到 2026 年 10 月，当初那台 Azure 学生机变成了三台低配 Linux 服务器：Docker Compose 跑着十几个服务，有 Orisumi 的前后端，也有别的个人项目；GitHub Actions 自动构建、发布；Prometheus 和 Grafana 收指标、看指标；Uptime Kuma 探活、告警。我还自己写了个认证授权服务，给别的项目提供 OAuth2 这些能力。

入口都挂在我的 [GitHub 主页](https://github.com/shenxianovo)上，有 [Orisumi 文档站](https://docs.orisumi.dev/)、[服务状态](https://status.shenxianovo.com/)和[个人博客](https://blog.shenxianovo.com/)。我的[在线简历](https://github.com/shenxianovo/homepage/blob/main/content/resume.mdx)管这套叫「3 台小鸡搭的简陋基建」，还写了句「虽然只有一个人用，但弄个看板还是很好玩吧……」。折腾这些就挺好玩的，用的人多不多无所谓。

## C# 和《软件构造基础》

大二下有门课叫《软件构造基础》，是我大学里印象最深的课，主要因为它让我从零做出了一个完整的软件项目，老师也还行。课要用 C#，我就在大二上结束的寒假提前找教程学了 C# 和 Unity 基础，结果越学越喜欢。

之后用 C# 碰了 UWP，又转到 WinUI，顺带看过 WPF，再后来用 ASP.NET 写后端。C# 就这么成了我写个人项目最常用的语言之一。

这门课的[平时作业](https://github.com/shenxianovo/SoftwareConstruction)和[结课作业 DAW](https://github.com/shenxianovo/DAW) 都还在 GitHub 上。

## 用 AI 写代码的方式在变

- 大一下（2024 年春）：把代码复制到浏览器里的 AI 对话框，再把回答复制回编辑器。这时候留下的一个早期项目是 [moegirlLyricProcess](https://github.com/shenxianovo/moegirlLyricProcess)，用 C++ 处理萌娘百科上的歌词，[第一次提交](https://github.com/shenxianovo/moegirlLyricProcess/commit/67ef1bbcd9b6e8cd514ac69bf3bf8fdbe406bd2f)在 2024 年 4 月 10 日。
- 大二下（2025 年春）：在 VS Code 里用 GitHub Copilot。《软件构造基础》的结课作业就是 Copilot 帮着写的，不过 MVVM、XAML、Tab 页面跳转、依赖注入这些，还是得我自己一个个学。
- 大三下（2026 年春）：慢慢换成 Claude Code、Codex 这类能自己干活的编程 Agent。

印象最深的有三次。

第一次是从浏览器里复制粘贴，换成在 VS Code 里用 Copilot 内联编辑。不用再在浏览器和编辑器之间来回搬代码，AI 总算进了写代码的地方。现在回头看，当年的「代码补全」已经有种被时代抛弃的感觉了。

第二次是 Opus 4.6 出来。大二下做 DAW，要自己画音频的波形图和频谱图。每次把所有数据重画一遍太慢，只能画屏幕上看得见的那段，再按缩放比例换不同粒度去采样。麻烦在于一换粒度，短暂的峰值和突变就可能丢掉，画出来还容易断开。2025 年春做作业时，我拿当时的 Gemini 2.5 Pro 试过（[2.5 Pro 是 2025 年 3 月出的](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/)，[3 Pro 到 11 月才出](https://blog.google/products-and-platforms/products/gemini/gemini-3-gemini-app/)），一直没弄好，项目里还留着一条[「Gave up implementing spectrogram. QAQ」的提交](https://github.com/shenxianovo/DAW/commit/304aee939e7269a0e4739bc6b2cabe8f102894ad)。Opus 4.6 出来以后，我拿这个老问题试了试，几句话就弄好了。以前 AI 搞不定的具体工程问题，新模型突然就能搞定，这是我第一次这么直观地感觉到，比什么评测分数都有说服力。GitHub 上 2026 年 3 月 20 日那批提交就是这次干的，有[重做波形组件](https://github.com/shenxianovo/DAW/commit/0eca792a1a4b6cd3c11f87d6726c56b942bad1ec)、[拆分音频服务](https://github.com/shenxianovo/DAW/commit/9536fdb6624dc9f62c2f5689cece479e94561b5f)等，算一次集中重构，没有从头重写 DAW。

第三次是从 Copilot 换到 Claude Code 和 Codex。以前是在编辑器里补全、帮忙改一小块，现在是把整个任务交给 Agent，让它自己看代码库、改文件、跑工具、验证结果。后来我在个人项目和实习里大量用 AI 写代码，就是从这里开始的。
