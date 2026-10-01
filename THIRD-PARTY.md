# 第三方内容声明 · Third-Party Notices

## 语料来源与权利归属

本仓库的 `skills/elon-musk-wisdom/corpus/` 收录 **258 份公开来源的文本**，
共约 **9,235,950 字符**，时间跨度 **1971–2026**。

**这些内容的著作权属于各自的原始权利人，不属于本仓库。**

| 类型 | 份数 | 体积 | 例 | 权利状态 |
|---|---|---|---|---|
| 访谈 / 演讲转录 | 104 | 4.5 MB | TED、Khan Academy、IAC 火星演讲、西点军校演讲、股东会 | 转录稿版权归各主办方/播客 |
| 播客转录 | 30 | 1.8 MB | The Joe Rogan Experience、Lex Fridman Podcast | 转录稿版权归各播客 |
| 书籍 / 编纂集 | 97 | 0.4 MB | *The Book of Elon Musk*（Eric Jorgenson 编） | 版权归编者/出版方 |
| 媒体报道 | 23 | 1.1 MB | Rolling Stone、CNBC、Reuters、Forbes | 版权归各媒体 |
| 传记 | 3 | 0.8 MB | Ashlee Vance《Elon Musk》、Walter Isaacson 相关 | 版权归作者/出版社 |
| 官方文件 | 1 | 0.2 MB | SEC 文件、Tesla 10-K | 美国政府文件多为公有领域 |

**本仓库以研究、评论、引用为目的汇集这些材料，不代表有权再授权。**
若要商业使用或再分发，请自行核实每一份的条款。

## 我们做了什么、没做什么

- ✅ 收录原始文本，保证每一条引文**可回查**
- ✅ 标注每份材料的**出处 URL**（见 `tools/corpus-sources.json`，254/258 条）
- ✅ 提供**完整性校验**（`tools/corpus-checksums.json`，逐文件 md5）
- ✅ 明确区分**本人亲述**（`high`）与**第三方转述**（`medium`）
- ❌ 不声称对语料拥有任何权利
- ❌ 不对二次分发授权

## 逐字引文的性质

`references/evidence.md` 收录 **1113 张逐字引文卡**，每张附出处、语料位置、置信度。

这些引文的用途是**支撑判断与可核查**，不是替代原作。读到某条引文想正式引用，
**请回到原始出处** —— `references/corpus-index.md` 与 `tools/corpus-sources.json` 里有 URL。

## 引文准确性

全部 **1319 段引文**经确定性脚本在归一化语料上**逐字回查**，命中率 **100%**。
构建方法与踩过的坑记录在 `docs/BUILD-NOTES.md`。

**这证明引文准确，不构成法律意见。**

## 第三方工具致谢

- [Agent Skills](https://agentskills.io) —— 开放规范
- [anthropics/skills](https://github.com/anthropics/skills) —— 官方技能结构与模板参考
- Mind-Distill-Factory —— 本技能使用的蒸馏流水线

## 免责

本技能是**独立研究项目**，与 Elon Musk 本人、其任何公司、任何前述权利人
**无关联、无授权、无背书**。

技能中所有观点均为引述与整理，不代表本仓库立场。

若你是某份材料的权利人，认为本仓库的收录超出了合理使用范围，
请开 issue 或按仓库联系方式提出，我们会移除对应文件。
