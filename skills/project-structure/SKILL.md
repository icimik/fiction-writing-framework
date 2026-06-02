---
name: project-structure
description: 虚构文学项目的目录结构规范。定义项目目录、编号规则、命名约定和转正归档规则。
---

# 项目结构

结构层模块。所有项目统一采用以下目录结构。

## 标准目录

```
项目名/
  README.md                    # 项目入口（当前阶段、下一步）
  STYLEGUIDE.md               # 项目风格总纲
  00-intake/                  # 原始输入（idea/设定原稿）
  01-brief/                   # 立项简报
  02-research/                # 原始调研材料
  03-foundation/              # 世界观、角色、阵营
    souls/                    # 角色灵魂档案
  04-outline/                 # 大纲、章节节拍
  05-rules/                   # 项目专属规则
  06-analysis-research/       # 已裁决的分析结论
  07-writing/
    samples/                  # 样章
    chapters/                 # 正式章节
  08-operations/
    logs/                     # 工作日志
    feedback/                 # 反馈汇总
    retrospectives/           # 复盘
    change-log/               # 变更记录
  09-assets/                  # 插图、附加资源
  10-publication/             # 发布准备、平台文案
  11-quality/                 # 评审、质检、精修资产
  99-archive/                 # 历史归档
```

## 编号规则

- 一级目录用两位数字前缀
- 同一项目内序号不冲突
- 发布目录统一 `10-publication/`
- 质量目录统一 `11-quality/`
- 入口文件统一 `README.md`

## 样章转正

- 直接采纳：文件从 `samples/` 转到 `chapters/`，不保留副本
- 改写转正：正式版写入 `chapters/`，原稿归档到 `99-archive/samples-YYYYMMDD/`
- 转正动作必须写入变更记录和工作日志

## 短篇小说集补充

- `04-outline/短篇矩阵_*.md`
- `06-analysis-research/篇章反雷同审阅_*.md`
- 导入短篇在完成融合评估前放 `99-archive/import-YYYYMMDD/`
