# 第三方内容声明 · Third-Party Notices

本仓库**不分发**原始语料（`corpus/`）。本文档说明语料的来源、归属，
以及为什么不分发。

## 为什么不分发语料

本技能蒸馏自 **258 份第三方材料** —— 访谈转录、演讲记录、传记、新闻报道、
官方文件。这些内容的著作权**不属于本仓库**：

| 类型 | 例 | 权利状态 |
|---|---|---|
| 传记 | 《Elon Musk》Ashlee Vance / Walter Isaacson | 版权，出版社持有 |
| 编纂语录集 | *The Book of Elon Musk*（Eric Jorgenson 编） | 版权，编者持有 |
| 访谈转录 | The Joe Rogan Experience、Lex Fridman Podcast | 转录稿版权归各播客 |
| 长篇文章 | Wait But Why 系列 | 版权，作者持有 |
| 新闻报道 | Rolling Stone、CNBC、Reuters 等 | 版权，各媒体持有 |
| 官方文件 | SEC 文件、Tesla 10-K | 美国政府文件多为公有领域，公司文件另论 |

**把 258 份第三方文件打进仓库分发，越界了。** 所以本仓库的做法是：

- ✅ 分发**我们的原创工作**：结构、索引、标注、失败边界、路由表
- ✅ 分发**逐字引文**：属于评论、批评、研究性质的引用（fair use 范畴）
- ✅ 分发**来源清单**：每份语料的原始 URL
- ✅ 分发**抓取脚本**：你自己去原始出处取，权利关系在你自己那里
- ❌ 不分发第三方文件本体

## 语料怎么拿

```bash
python3 tools/fetch_corpus.py --out <你的 skills 目录>/elon-musk-wisdom/corpus
```

脚本会读 `skills/elon-musk-wisdom/references/corpus-index.md` 里的来源清单，
逐条从原始 URL 抓取，重建成技能期望的扁平文件名。

**抓取前请自行确认各来源的使用条款。** 个人研究、本地使用与再分发是两回事。

## 逐字引文的性质

`references/evidence.md` 收录 **1113 张逐字引文卡**，每张附出处、语料位置、
置信度（`high` = 本人亲述 / `medium` = 第三方转述）。

这些引文的用途是**支撑判断与可核查**，不是替代原作。读到某条引文想引用，
**请回到原始出处**——`corpus-index.md` 里有 URL。

## 引文准确性

全部 **1319 段引文**经确定性脚本在归一化语料上**逐字回查**，命中率 100%。
回查脚本的思路记录在 `docs/BUILD-NOTES.md`。

这不代表引用在法律上无风险，只代表**引文是准确的**。

## 第三方工具的致谢

- [Mind-Distill-Factory](https://github.com/) —— 本技能使用的蒸馏流水线
- [agentskills.io](https://agentskills.io) —— Agent Skills 开放规范
- [anthropics/skills](https://github.com/anthropics/skills) —— 官方技能模板与结构参考

## 免责

本技能是**独立研究项目**，与 Elon Musk 本人、其任何公司、任何前述权利人
**无关联、无授权、无背书**。

技能中所有观点均为引述与整理，不代表本仓库立场。
