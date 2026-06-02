---
name: chinese-writing-constraints
description: 中文虚构文学生成的核心语言约束。当需要生成、改写或精修任何中文小说正文时，必须先读取此 skill。
---

# 中文生成约束

知识层模块。为 fiction-create、fiction-rewrite、fiction-review 提供中文语言规格。

## 核心问题

LLM 中文输出默认带翻译腔——内部推理以英语逻辑组织句子，再用中文词汇填充。必须在生成环节施加结构性约束，不能只靠事后精修。

## 参考文档

| 文档 | 内容 | 何时读 |
|------|------|--------|
| `references/anti-patterns.md` | 12 种反翻译腔模式 + 正面特征 | 生成任何中文正文前 |
| `references/checking-process.md` | 三阶段检查 + 自检 8 问 | 生成任何中文正文前 |
| `references/refine-methods.md` | 重述法、锚文本法、分层法、删减法 | 精修阶段 |
| `references/现代汉语_词汇规范.md` | 词汇规范 | 需要语言学依据时 |
| `references/现代汉语_语法规范.md` | 语法规范 | 需要语言学依据时 |
| `references/现代汉语_修辞规范.md` | 修辞规范 | 需要语言学依据时 |

## 执行要求

生成中文正文前，必须已读 `anti-patterns.md` 和 `checking-process.md`。精修前必须已读 `refine-methods.md`。
