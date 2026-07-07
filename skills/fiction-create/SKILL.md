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
- 验证门槛：能用一句话说明"主角-冲突-目标-代价"；类型与读者明确。

**设定完善**：世界观设定 → 角色设定 → 创作规则手册。模板见 `templates` 的 references/立项/。
- 长篇连载项目必须在样章前建立 `STYLEGUIDE.md`，模板见 `templates` 的 references/立项/模板_STYLEGUIDE.md。
- 三个及以上持续复用的主要角色必须建立 `SOUL.md`，模板见 `templates` 的 references/样章/模板_SOUL.md。
- 验证门槛：世界观能力体系有限制/代价/弱点；角色有创伤/动机/弧光；`STYLEGUIDE.md` 和 `SOUL.md` 已建立。

**规划**：分卷大纲 → 章节节拍 → 伏笔台账。模板见 `templates` 的 references/规划/。
- 分卷大纲需包含：卷目标、小高潮、灵魂黑夜、卷末钩子。
- 前三章节拍必须覆盖：世界观入口、主角动机、首个冲突闭环。
- 伏笔台账需登记：埋设位置、预期回收节点、回收状态。
- 验证门槛：结构选型已固定；大纲与节拍对齐；伏笔台账已建立。

**样章**：写样章 → 三方审阅。生成前必读 `chinese-writing-constraints`。
- 生成前必须已读 `chinese-writing-constraints` 的 references/anti-patterns.md 和 references/checking-process.md。
- 生成前必须已读项目 `STYLEGUIDE.md` 和相关角色 `SOUL.md`。
- 验证门槛：三方审阅通过（Reviewer + Reader + Editor）。

**持续生产**：按批次写章节 → 周期复盘 → 联动更新。模板见 `templates` 的 references/运营/。
- 每 5-10 章检查一次伏笔台账与主线推进比例。
- 章节改写后建议触发 `fiction-review` 验证改写质量。
- 验证门槛：工作日志已更新；联动更新清单已勾检。

## 输出

- 中文输出
- 每次交代：输入摘要、当前阶段、产出清单、下一步
- 项目结构按 `project-structure` 执行
