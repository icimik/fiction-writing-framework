---
name: fiction-writing-framework
description: 基于当前 framework 的虚构文学创作执行技能。可从一句话设定启动，完成设定、大纲、样章、评审与迭代闭环。
metadata: 
  version: 1.5
  author: Kimmy Liu (@kenpusney)
---

# 虚构文学创作 Skill

## 适用范围

- 从一句话设定启动新项目。
- 生成或重写世界观、角色、分卷大纲、章节样稿。
- 对已有稿件执行评审、改写与复盘。
- 对已有项目与历史材料进行重组后续写。
- 对短篇小说集执行拆分、归档、统稿与反雷同修订。
- 对外部导入的同世界观资产执行融合评估、重写归并与基线统一。
- 对完整长篇执行整书审读、中文表达精修、终稿评审、发布准备与校样收口。

## 核心原则

1. 先保结构，再修表达
- 任何精修先确认"这一章要完成什么叙事任务"，再动句子。
- 未经明确要求，不擅自改动结构、因果链、角色关系、时间顺序、信息释放顺序和章尾钩子。

2. 过程资产必须沉淀
- 每一轮创作、改稿、评审、发布收口，都要留下可追溯的文档资产。
- 框架能力靠项目层资产反向验证后再固化进框架。

3. 分阶段裁决，不无限返工
- 样章期允许较大改动，分卷期允许结构性修补，终稿期以收口和统一为主。
- 当问题已从正文级下降到校样级、发布口径级时，必须停止正文大修。

4. 中文表达服从中文习惯
- 不把"译得通"当成"写得像中文"。
- 不用概念化判断代替人物动作、物件、场景和口语。
- 不追求句句漂亮，优先保证冷硬、具体、克制和可读。

## 文学性底线

1. 文学性不是慢节奏，而是"情节有效 + 意义密度高"。
2. 角色不是观点容器，而是价值冲突中的行动者。
3. 主题不靠口号表达，靠可追溯的行为后果表达。
4. 修辞不为华丽服务，优先为叙事清晰与情绪强度服务。
5. 反套路的核心不是反常识，而是高可信的意外。

## 中文生成核心约束

本节约束对所有项目生效，优先级高于任何项目级文档。

### 约束起因

LLM 的中文输出默认带有翻译腔，根源不是"不懂中文语法"，而是内部推理以英语逻辑组织句子，再用中文词汇填充表面。结果是：句子逻辑正确，但不像中文母语者会写出的文字。

这个问题不能只靠事后精修（阶段 7）解决。必须在生成环节就施加结构性约束。

### 入口级反模式

以下模式在生成任何中文正文时必须主动规避：

1. 压缩名词式主语：把"他的失业导致的经济压力使得……"拆回"他失业了，钱紧了，……"。中文信息承载单元是动词，不是名词短语。
2. 抽象主语 + 使役动词：把"这种不确定性让他感到焦虑"改回"他不知道下个月怎么办"。
3. 连接词过密：一个句群内保留一个关键连接词。
4. 概念先行：小说先给场面和动作，结论由读者自己得出。
5. 情绪标签代替展示：不写"他感到复杂的情绪"，写他做了什么、碰了什么、停在哪里。
6. 被动语态过频：中文被动句发生率远低于英语。
7. 前置修饰堆叠：名词前超过两层修饰立即拆句。
8. 段尾情绪总结：用物件、时间或未完成的动作收尾。
9. 对白书面腔：日常对话中人不会说"我认为我们需要重新评估当前的财务状况"。
10. 段落结构雷同：连续三段以上使用相同的内部节奏时，强制打散。

### 生成时硬规则

1. 生成每段正文后，立即检查：主语是不是抽象名词？如果是，换回人或物。
2. 每个段落结尾检查：是不是情绪或概念总结句？如果是，换成物件、动作或未完成的事。
3. 连续三段检查：内部结构是否雷同？如果是，强制打散节奏。
4. 对白检查：日常场景的对白是不是书面腔？人物在这个体力和情绪状态下会不会这么说？
5. 每章回读一次：像一个中文故事，还是一篇翻译稿？

### 详细模式清单与示例

见 `references/01-domain/language/中文生成约束.md`。

该文档是生成时的操作手册，不是语言学参考。**生成任何中文正文前必须读。**

## 文档结构

```
references/
  01-domain/                  领域知识（原则 + 规则 + 检查项，按主题自包含）
    worldbuilding.md           世界观
    character.md               角色
    plot.md                    情节
    narrative.md               叙事
    rhetoric.md                修辞与文风
    genre.md                   类型适配与连载策略
    editing-review.md          审阅与改稿
    reference-and-sources.md   参考文本与资料来源
    language/                  中文语言规格
      中文生成约束.md            生成时操作手册（最高优先级）
      00.index.md              语言规格索引
      现代汉语_词汇规范.md
      现代汉语_语法规范.md
      现代汉语_修辞规范.md
  02-process/                  流程层
    stages.md                  标准创作流程（唯一执行入口）
    collaboration.md           多 Agent 操作流程
    project-structure.md       项目结构模板
  03-resources/                资源层
    templates/                 文档模板集
    checklists.md              质量检查清单
    reusable-rules.md          可复用规则库
  04-governance/               治理层
    update-mechanism.md        框架更新机制
    project-governance.md      项目治理与复盘机制
    change-log.md              框架变更记录
    market-research/           市场研究基线
```

## 快速入口

创作者入口：
1. `references/02-process/stages.md`
2. `references/02-process/project-structure.md`
3. `references/03-resources/templates/README.md`
4. `references/03-resources/checklists.md`
5. 若中文表达是硬约束，再读 `references/01-domain/language/00.index.md`

Agent 入口：
1. `SKILL.md`
2. **`references/01-domain/language/中文生成约束.md`（涉及中文正文生成时必读，不可跳过）**
3. `references/02-process/stages.md`
4. `references/03-resources/checklists.md`
5. `references/02-process/project-structure.md`
6. `references/04-governance/update-mechanism.md`
7. 若需做发布前或阶段性体量核验，运行 `scripts/count_manuscript_words.py`
8. 若需追溯中文语言学依据，查 `references/01-domain/language/00.index.md`
9. 若需生成 `epub / html / pdf` 出版文件，运行 `scripts/build_publication_with_pandoc.py --project-root <项目目录> --config <构建配置.json>`；默认样式与示例配置见 `assets/`

## 输入契约

必填字段：
1. 类型与题材
2. 目标体量（字数或章数）
3. 目标读者
4. 创作目标（新建/续写/重写/审阅）
5. 运行模式（通用创作/网文连载/短篇小说集）

阶段 0 执行门槛补充字段：
1. 平台与更新节奏
2. 风格边界与禁用项

一句话启动缺省策略：
- 未给创作目标：默认"新建"。
- 未给类型与题材：按关键词自动归类，无法判定则默认"都市异能"。
- 未给目标读者：默认"18-35 岁网文读者，偏剧情驱动"。
- 平台：默认"待定（按通用创作标准输出，可后置适配）"。
- 更新节奏：默认"每周 3 更"。
- 目标体量：默认"长篇，预计 120 章"。
- 禁用项：默认"无现实敏感映射、无超出设定边界的能力跳变"。

## 执行摘要

标准执行链：
1. 立项
2. 导入融合
3. 设定
4. 规划
5. 样章
6. 反馈
7. 持续生产
8. 周期复盘
9. 整书中文表达精修
10. 中文重塑（条件触发，非必经）
11. 终稿级多方评审
12. 发布准备 / 校样准备
13. 结项复盘与框架反哺

多 Agent 基本循环：
1. Writer 产出稿件
2. Reviewer 评审
3. Reader 反馈
4. Editor 汇总、下发改稿指令并做阶段裁决
5. Writer 改稿并完成联动更新

## 多 Agent 角色

1. Writer（创作 Agent）：输出设定、大纲、章节草稿与改稿版本。
2. Editor（编辑 Agent）：审阅结构与叙事问题，汇总各方反馈，形成改稿清单。
3. Reviewer（评审 Agent）：按 Rubric 与检查清单执行规则化评审与问题定位。
4. Reader（读者 Agent）：以不同读者画像给出体验反馈。整书阶段补充连读体验、口径一致性、弃读风险位置。

角色操作流程入口：`references/02-process/collaboration.md`

## 入口级硬约束

- 生成任何中文正文前，必须已读 `references/01-domain/language/中文生成约束.md`，并在生成过程中执行其三阶段检查。
- 单次只变更一个对象；整书精修和发布准备时，对象粒度分别升级为"章节对象"或"整书/发布资产包对象"。
- 任何正文改写必须整章重写或按整章回读，不做局部查找替换式修补。
- 用户要求逐字逐句精修时，只改表达，不改结构、因果、人物关系与章尾钩子。
- 不创建 `.bak`、`_old` 等正文副本。
- 改动后必须同步更新日志、变更记录，以及被触发的设定、评审、发布资产。
- 当问题已下降到校样、措辞、发布口径层，必须停止正文大修，转入发布收口。

## 使用方式

0. 若任务涉及中文正文生成、改写或精修，先读 `references/01-domain/language/中文生成约束.md`。不可用"事后精修会处理"为由跳过。
1. 再读 `references/02-process/stages.md`。所有阶段动作、停改规则、终稿与发布流程以该文件为准。
2. 再读 `references/03-resources/checklists.md`。所有阶段验收以该清单为准。
3. 按需调用 `references/03-resources/templates/README.md`。
4. 涉及方法细节时查 `references/01-domain/` 对应分册。
5. 若需统计作品正文字数，优先运行 `scripts/count_manuscript_words.py <项目目录>`；默认统计 `07-writing/chapters/`，按“每个中文字符算 1 字、每个英文单词算 1 字、标点不计”输出总字数与分文件明细。
6. 若需构建发布产物，优先运行 `scripts/build_publication_with_pandoc.py --project-root <项目目录> --config <构建配置.json>`；脚本支持平铺章节与分卷目录两种正文结构，默认输出 `epub / html / print html / pdf`。

## 唯一执行入口

1. `references/02-process/stages.md`
2. `references/03-resources/checklists.md`
3. `references/03-resources/templates/README.md`
4. `references/02-process/project-structure.md`

## 日志要求

每个关键动作必须可追溯：
- 为什么做（设定原因/决策依据）
- 做了什么（变更内容）
- 完成到什么程度（完成度）
- 有什么风险（未决问题）

长篇项目补充要求：
- 章节生产批次要记。
- 正文精修批次要记。
- 整书评审与终稿裁决要记。
- 发布准备与校样收口要记。
- 结项后的框架反哺也要记。

## 推荐模板入口

1. `references/03-resources/templates/模板_Reviewer评审单.md`
2. `references/03-resources/templates/模板_Editor汇总与改稿指令.md`
3. `references/03-resources/templates/模板_联动更新清单.md`
4. `references/03-resources/templates/模板_整书中文表达审读提要.md`
5. `references/03-resources/templates/模板_发布前最终核对单.md`

## 输出约束

- 输出必须为中文。
- 每次输出至少交代：输入摘要、当前阶段、产出清单、下一步动作。
- Editor 输出必须保持"三段式"：汇总反馈 → 改稿指令 → 验收结论。
- 关键结论必须能追溯到 Reviewer / Reader / 日志 / 变更记录等来源。
- 若框架在项目中被新问题逼出新规则，结项时必须回写框架层文档。

## 交付底线

项目级：
- 所有项目都需提供：前提句、受众描述、主冲突、分卷结构。
- 长篇连载项目还需提供：读者画像、反馈处理记录、周/月/N章/分卷复盘。

章节级：
- 所有章节都需提供：推进目标、核心冲突、章末钩子。

变更级：
- 所有改动都需提供：变更原因与影响说明。
