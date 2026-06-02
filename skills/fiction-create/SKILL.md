---
name: fiction-create
description: 虚构文学创作执行。当用户要从零启动新项目、续写章节、规划大纲、生成世界观和角色设定、写样章时触发。
---

# 创作

流程层模块。从一句话设定启动，完成设定、大纲、样章与持续生产。

## 约束读取

开始前必须读取：
- `chinese-writing-constraints`（涉及中文正文时）
- `project-governance` 的 references/stages.md（阶段定义）

按需读取：`narrative-knowledge`、`intimacy-levels`、`market-research`。

## 输入

必填：类型与题材、目标体量、目标读者、创作目标、运行模式。

缺省：未给目标默认"新建"；未给类型/读者则询问用户。

## 阶段执行

按 `project-governance` 的 references/stage-details.md 执行：

**立项**：前提句 → 世界观 → 角色 → 结构选型。模板见 `templates` 的 references/立项/。

**规划**：分卷大纲 → 章节规划 → 伏笔台账。模板见 `templates` 的 references/规划/。

**样章**：写样章 → 三方审阅。生成前必读 `chinese-writing-constraints`。

**持续生产**：按批次写章节 → 周期复盘 → 联动更新。模板见 `templates` 的 references/运营/。

## 输出

- 中文输出
- 每次交代：输入摘要、当前阶段、产出清单、下一步
- 项目结构按 `project-structure` 执行
