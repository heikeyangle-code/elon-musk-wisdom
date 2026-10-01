# 构建记录 · Build Notes

本文件记录构建这套技能时踩到的 **26 个工具缺陷（F1–F26）** 及其修法。

**为什么公开这些**：其中三个是同一类错误 —— **校验器自称通过，实际什么都没检查**。
这类缺陷最危险，因为它让你在「全绿」的状态下发布坏东西。写下来是为了下次不再犯。

---

# 移植实测发现（PORTING-FINDINGS）

本文件记录把 MDF 用在「79 份文献 / 422 万字符」这一量级语料上时，实际撞到的问题与处置。
全部是跑出来才发现的，不是读文档能读到的。按严重度排序。

---

## F1 · P2 闸门存在「转述洗白」漏洞（设计层 · 已用目录隔离堵住）

**现象**：`scripts/verify_provenance.py:56` 的 `load_corpus()` 只扫两个目录：

```python
for sub in ("raw", "processed"):
    base = root / "sources" / slug / sub
```

**后果**：只要把上一代 AI 蒸馏产物（女娲/仓颉生成的转述文件）放进 `sources/{slug}/raw/`，
那么这些文件里出现的任何句子都会「通过」P2 逐字校验 —— 于是 **AI 的转述给 AI 的引文背了书**，
闸门形同虚设。上游公开文档没有提示这一点。

**处置**：把上一代产物放在 `sources/{slug}/_incoming-refs/`（`raw/` 的**兄弟目录**，落在扫描范围之外），
既当候选线索用，又无法被当作溯源底稿。另写 `tools/audit_prior_contamination.py` 事后反向复查：
对每条出厂引文，检查它是否只存在于 `prior/` 而不在一手语料里。

---

## F2 · `evidence.md` 必须一卡一引（格式硬约束 · 生成器 bug）

**现象**：`parse_evidence_cards()` 把**同一张卡里所有 `>` 行**用 `\n` 拼成一个 `verbatim` 字符串：

```python
"verbatim": "\n".join(quote_lines).strip(),
```

**后果**：若一张 `### 原则 X` 卡下放 3 条引文，拼出来的字符串几乎不可能逐字存在于语料
（除非那 3 条在原文里正好相邻）。我第一版生成器就是这么写的，43 张卡只过了 2 张。

**处置**：改为**一引一卡**（`### 原则 P01 证据 1/3：…`）。修正后 43/43 通过。
另外：`evidence.md` 的 `>` 行**只放目标语言的逐字原文**（本项目为英文），
中文释义一律走 `- 现代转译：` 字段 —— 否则中文会被当成「逐字引文」送进 P2 比对而必然失败。

---

## F3 · `format_version: 6` 必须写进 SKILL.md frontmatter（否则按 legacy 双语包校验）

**现象**：`is_v6_skill()` 靠 frontmatter 里的 `^format_version: 6$` 判定。
`frameworks.zh.json` 里的 `format_version` 只管原则数区间，**不管 SKILL.md 走哪套校验**。

**后果**：漏写这一个字段，`skill` / `package` 阶段会转头按 **legacy 双语包**校验，
报出一串 `MISSING_SECTION [English]`，并**同时**报中文八章缺失（即使八章都在），
很容易误导人以为是章节名写错了。

**处置**：frontmatter 补 `format_version: 6`。

---

## F4 · 案例索引表的 `case_id` 不能加反引号（P5 静默失配）

**现象**：`check_p5_index()` 对表格单元格做：

```python
token = cell.strip()
if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", token):
```

**后果**：写成 `` | `cm-bell-rich-oil-2013` | ``（带反引号）时 `cell.strip()` 仍是
`` `cm-bell-rich-oil-2013` ``，**不匹配** `fullmatch` → 该 case_id 被判定为「未出现在索引中」，
25 个案例全报 `P5_CASE_NOT_INDEXED`。

**处置**：case_id 列写裸 token，不加反引号、不加括号。

---

## F5 · 核心原则子标题必须以「原则」开头（P6 计数）

**现象**：`PRINCIPLE_SUBHEADING_RE = re.compile(r"^###\s*原则", re.MULTILINE)`。

**后果**：核心原则章节里若用「### 一、多元思维模型」这类中文序数标题，
P6 会数出 **0 条**原则并报 `P6_TOO_FEW_PRINCIPLES`。

**注意矛盾点**：MDF 的「反套公式指令」禁止在**回答里**使用序数标记，
但**核心层文件的章节编号用「原则 1、原则 2」是样板包本身的做法**（`zhang-juzheng-v6` 即如此）。
两者不冲突：禁令管模型输出的表面，不管 skill 文件的目录结构。

**处置**：标题统一为 `### 原则 N：…`。

---

## F6 · `cases.md` 的「对应原则簇」行必须干净

**现象**：`CASE_CLUSTER_RE = re.compile(r"^\*\*对应原则簇：\*\*\s*(\S+)\s*$", re.MULTILINE)`
—— `(\S+)` 后面直接是行尾。

**后果**：写成 `**对应原则簇：** cluster_003（**反例**）` 时，整串 `cluster_003（**反例**）`
会被当成簇名 → 该案例的簇匹配失败，并污染簇计数。反例必须用独立的
`**反例：**` 行（`CASE_COUNTER_FIELD_RE = ^\*\*反例[:：]\*\*`）标注，不能挂在簇行上。

**处置**：簇行只留 `cluster_00X`；反例另起一行。

---

## F7 · 上游 Stage 1A 分片流水线假设 `raw/` 是扁平目录（量级不匹配）

**现象**：`local_source_pipeline.py` 只扫 `raw/` 顶层。本项目语料按
`raw/{pdf,archive,web,book}/` 分子目录组织，结果 `index` 只看到 2 个文件 / 1 个 shard / 16.6k tokens。

**更根本的问题**：上游的分片设计目标是「20–35k token / shard，交给若干 agent 逐个读」。
422 万字符 ≈ **105 万 token**，超出该假设约 30 倍，就算分片正确也读不完。

**处置**：放弃「让 agent 通读」，改为**四层机械挖掘 + 有界精读**：

| 层 | 工具 | 作用 |
|---|---|---|
| 采集 | `tools/harvest.py` | 官网/归档站抓正文 |
| 抽文本 | `tools/pdf_to_text.py`、`tools/ocr_pdf.py` | 文本层直抽；扫描件走 tesseract |
| 去重 | `tools/dedupe_corpus.py` | 5-gram shingle + Jaccard，同一文书从两站下过只留大的（实际干掉 15 个） |
| 挖候选 | `tools/corpus_index.py`（主题卷宗）、`tools/mine_principles.py`（严签名精挖） | 从 422 万字符里捞出约 4 千候选句 → 20 个主题卷宗 + 300 条精挖候选 |
| 精读 | 人/模型 | **只读卷宗与候选（约 150KB，占语料 4%）** |

并把 `sources/{slug}/processed/local_shards/` 脚手架移除 —— 它由不适用本目录结构的
pipeline 生成，留着会触发 `STAGE1A_STATUS_MISMATCH`，而伪造一个 `shard_001_extracts.json`
只是在骗闸门。

**副作用（有价值）**：机械层把「跨域复现」从主观判断变成了**可测量的矩阵**。
`tools/corpus_index.py` 输出的主题覆盖表（来源类型数 × 年份数 × 年份跨度）成为原则资格的硬证据。

---

## F8 · 聚类必须区分「跨来源类型复现」与「同一系列年复述」

**现象**：第一版按「近重复句聚类 + 出现年份数」排序，排在最前面的全是 Wesco 年报里
连抄 13 年的财务套话（`book value` / `per share` / `liquidat…`）。我量的是「重复」，
而年报套话天然高度重复。

**处置**：两处修正 ——
① 加报表体词汇黑名单（`BOILER`），命中 ≥2 个即丢弃；
② 排序主键从「年份跨度」改为 **「来源类型跨度」**（信 / 演讲 / 年会 / 访谈 / 文章），
并加规则：若某簇只出现在**同一系列**年复一年重述，直接丢弃。

**遗留限制（未解决）**：句子级近重复聚类**看不到概念复现** —— 同一原则在 1994 演讲与
2021 年会里措辞完全不同，永远聚不到一起（`--require-types` 一开，60 簇只剩 2 簇）。
因此最终方案不是聚类，而是**主题卷宗**（按主题捞句，交给人/模型做概念层合成）。

---

## F9 · PDF 抽页边界的页眉夹心（部分只修一半）

**现象**：跨页断句时，下一页开头的页眉会插进句子中间。BCS 1982 股东信实例：

```
...so as better to
To Our Stockholders:
                                  ← 空行
disclose the things we would want to be told...
```

**处置**：在 `pdf_to_text.py` 里加了页眉夹心修复（短行 + 无句末标点 + 下行以小写开头 → 删行并接续）。
但**带空行的变体修不掉**（`lines[i+1]` 是空行，条件不成立）。

**最终处置（走上游自己的机制）**：不再硬改抽取器，改用 MDF 的 **`textual_note` 豁免通道** ——
只引用逐字可证的后半段，并在证据卡里写下分歧说明。**分歧记录在案，不是静默放过。**
这也顺带验证了豁免通道确实可用。

---

## F10 · `publish_skill.py` 的元信息提取不读 `frameworks.zh.json`

**现象**：发布后 `gallery/index.json` 的条目出现 `era: Unknown`、`primary_category: philosophy`、
`name_original: 查理·芒格`（应为 Charles Thomas Munger）—— 它从别处猜，没读已写好的框架字段。

**处置**：手工修正 index 条目（`era: 1924-2023`、`primary: enterprise`、
`secondary: [inquiry, conduct]`、`name_original: Charles Thomas Munger`）。发布后**必须核对 index 条目**。

---

## 未完成项（明确记录，不粉饰）

| 项 | 状态 | 原因 |
|---|---|---|
| 运行期对话评测（12 用例 / 7 指标 / P0 旗标） | ❌ 未跑 | 需 DeepSeek 兼容 API key；`--llm off` 模式被设计为拒绝执行外部调用 |
| **附件触发压测**（通过线：附件 ≥2 次被正确触发读取） | ❌ 未跑 | 同上。这是「结构合格」与「运行可用」之间的最后一道门，列为交付后第一优先 |
| 英文版 skill 包 | ⛔ 有意不做 | 上游默认关闭英文分支，理由是该分支从未纳入回归（冻结的 12 题标准集是纯中文）。不做半吊子参数化 |
| 道德化定性 vs 论证省略的区分 | ⚠️ 仅静态记录 | 只有运行期打分（`generic_advice` / `methodology_depth`）能判定某次输出里的 `crazy/stupid` 是表达指纹还是论证省略 |

---

# 第二轮审计发现（由使用者复核发现 · 全部已修）

## F11 · P3 闸门只查 SKILL.md，装进 skill 的附件出处会静默失效（严重）

**现象**：上游 `check_p3_paths` 只接收 `skill_md` 一个参数 —— **它从不检查 `references/*.md`**。
而 `evidence.md` / `voice.md` 的「语料位置」字段写的是**工厂侧路径**
（`sources/charlie-munger/raw/xxx.txt`）。装进 skill 后语料实际在扁平的 `corpus/YYYY-名称.txt`，
于是 43 条出处 + 24 条样本出处**一条都解析不了，P3 却照样报通过**。

**为什么严重**：这个 skill 的核心承诺是「你可以自己去核对原文」。路径全断 = 承诺落空，
而闸门给了一个假的通过信号。

**处置**：
1. `tools/build_corpus_pack.py` 输出 `corpus-map.json`（原路径 → 语料文件名）
2. `tools/relink_corpus_paths.py` 按映射改写三个附件的出处字段，并给每个案例补 `**语料位置：**`
3. **新增 `tools/check_paths.py`** —— 把 P3 扩展到全包（SKILL.md + 全部 references），
   并额外校验「语料地图列出的文件」与「corpus/ 实际文件」一致。这是对上游闸门的补强。

## F12 · v6 包缺 `manifest.json`（publish 只写 gallery，没进安装目录）

`publish_skill.py` 把 `manifest.json`（含各文件 SHA-256）写在 `gallery/{slug}/`，
但安装白名单当时只 cp 了 `SKILL.md` 与 `references/*.md`，**manifest 没进安装目录** ——
运行包缺了哈希清单，就无法验证是否被改动过。已在安装步骤补上。

注：`framework_core.json` 按 v6 参照包**不属于安装套件**（它住在 `output/`）。
本项目额外把它装进安装目录，作为运行时可直接读的结构化证据底座（非规范文件，已标注）。

## F13 · 手写计数与程序事实漂移

`cases.md` 抬头写「共 24 例」，但脚本解析出 **25** 例（第 25 例是后期补的）。
`SKILL.md` 表里看似有 6 个「反」标记，实为 5 个 + 1 个表头。

**教训**：**任何写在正文里的数字都必须由脚本生成或校验，不能手写。**
`relink_corpus_paths.py` 现在会按实际值重写抬头计数。

## F14 · 同一实体两套命名（cluster_00X vs 原则名）

`cases.md` 用 `**对应原则簇：** cluster_009`，`SKILL.md` 索引表用「耐心」，两套体系无对照表。
读者无法对应。

**处置**：`SKILL.md` 索引表加「簇」列（`cluster_00X`），并在表后补一段说明两套命名的对照关系。

## 附：本轮我自己的脚本踩的坑（都属低级但静默失败类）

| 坑 | 症状 | 教训 |
|---|---|---|
| `re.findall(r"(19\|20)\d{2}")` 用了捕获组 | 只返回 `"19"`/`"20"`，25 个案例全部映射失败 | 「匹配失败」和「没有匹配」要分开报，别静默 continue |
| 检查脚本 `^` 锚点漏 `re.M` | 只在文件开头匹配，报「0 条映射」却判定为通过 | 自检脚本本身也要有负数用例 |
| shell `for f in $(...)` 遇到含空格的中文文件名 | 路径被拆词，误报大量文件缺失 | 路径处理一律走 Python，别用 shell 拆词 |
| 关键词表用空格、文件名用连字符 | 短名表静默失配，命名半中半英 | 所有字符串匹配前先归一化（`flat()`） |
| 打包脚本不清空目标目录 | 改名后旧文件残留，语料数虚增到 89 | 生成式产物必须先清空目标 |

**这五条的共同点：错误都不报错，只是结果不对。** 所以最终防线是 `tools/check_paths.py`
这类**交叉核对**（地图 vs 实际、索引 vs 案例库、表 vs 正文计数），而不是指望每一步都写对。

---

## 第二轮（马斯克蒸馏）新增：F15–F22

| # | 缺陷 | 触发条件 | 后果 | 修复 |
|---|---|---|---|---|
| F15 | `local_source_pipeline.collect_segments` 用 `iterdir()` | `raw/` 有子目录（本环境的采集工具按来源类分目录） | **分片数为 0**，静默跳过全部语料 | 改 `rglob`，排除 `_duplicates`/`prior`/`_incoming-refs`；`file` 记相对路径 |
| F16 | `split_text` 出口可能超 `max_tokens` | 单文件接近上限 | 单块 60,497 > 60,000 硬上限，`over_limit_shards` 非空 | 出口加不变量：超限块强制再切 |
| F17 | 分片上限写死 30k/50k/60k | 上下文 ≠ 200k 的模型 | 1M 上下文下切出 59 片（应为 14），worker 次数多 4 倍 | 改为 `MDF_WORKER_CONTEXT × 0.30` 推导，保留上游相对值；可用环境变量覆盖 |
| F18 | 摘录额度写死 30–60 条 | 语料远大于上游假设 | 225 万 tokens 只留 60 条 = 丢 97% 素材 | `scale_extract_budget(total_tokens)`：min=`max(30, t/20k)`，max=`max(60, t/8k)` |
| F19 | `index` 不清旧分片 | 重跑 index | 新 manifest 旁残留 45 个陈旧分片文件，worker 会处理过期内容 | 重跑前清空 `shard_*.json` |
| **F20** | **`index` 删除 `*_extracts.json`** | 重跑 index | **误删 7 片 159 条 worker 产出** | 移除该逻辑；确立规则：**补丁可以清自己产出的分片，绝不能清别的阶段的产出** |
| F21 | `validate_user_sources.py` 写死 Windows 路径 | 任何非 Richard-Feynman 的语料 | 脚本完全不可用 | 改为按 slug 取路径 + 自适应额度 |
| F22 | sources 阶段对 `processed/*.json` 全体套提取台账 schema | Stage 1B 产出报告类文件 | 15 条 MISSING_FIELD 假阳性 | 只校验带 `extracts` 列表的文件 |

### 配套新增工具

| 工具 | 用途 |
|---|---|
| `tools/rebuild_from_worker_script.py` | 从 worker 生成脚本复原摘录（AST 取常量 + 归一化语料重定位，不依赖 passage_id） |
| `tools/build_coverage_report.py` | 语料覆盖审计：把零产出分为「同文献另一渲染 / 结构上无引语 / 真缺口」 |
| `tools/build_supplement_shards.py` | 为「真缺口」里的高价值文件建定向补抓分片，走同一 worker 契约 |
| `tools/remap_deduped_paths.py` | 去重后修复引用路径 |
| `tools/install_skill.py` | 通用安装器（避免手工拷贝导致的名字写死类缺陷） |
| `tools/build_voice_md_elon_musk.py` | 表达样本生成（逐字回查后才收录） |

### 一条跨阶段的通用教训

**凡「清理/重置」逻辑，必须显式列出它有权删除的文件模式。** F19 与 F20 是同一类错误的两次发作：一次清得太少（陈旧分片残留），一次清得太多（删掉别人阶段的产出）。两次都发生在「顺手加一行清理」的时候。


## F23：`verify_provenance` 的 blockquote 正则会把空 `>` 分隔行吞进引文

**症状**：evidence.md 里任何**跨多段**的引文（段间用单独的 `>` 行分隔，Markdown 标准写法）
会被解析成 `...This applies to any given ton.>Adding each ton...` —— 多出一个字面 `>`，
于是 P2 判定「未逐字出现在语料中」，最长逐字前缀正好停在段落边界。

**根因**：`BLOCKQUOTE_RE = re.compile(r"^>\s?(.*?)\s*$", re.MULTILINE)`。
`\s` 包含 `\n`，所以匹配单独的 `>` 行时，`\s?` 吃掉换行、`(.*?)` 捕获下一行的
开头 `> `，`\s*$` 再吃掉行尾。等价于把两行粘成一行并多带一个 `>`。

**为什么此前没暴露**：原有 90 张卡全是单段引文，没有一张用 `>` 段落分隔符。
本包新增算法五步的证据卡（多段原话）后立即踩中。

**修复**：两处 `\s?` → `[ \t]?`，并把 `\s*$` → `[ \t]*$`（同样的越界风险）。

```
BLOCKQUOTE_RE      = re.compile(r"^>[ \t]?(.*?)[ \t]*$", re.MULTILINE)
BLOCKQUOTE_LINE_RE = re.compile(r"^>[ \t]?(.*)$")
```

**教训（与 F19/F20 同类）**：正则里的 `\s` 在 `re.MULTILINE` 下是越界的——
它跨行。凡「按行解析」的地方，行内空白必须写成 `[ \t]`。

## F24：P3 路径闸门有两个盲区，导致 4 条坏语料路径长期隐形

**症状**：`references/evidence.md` 里有 4 张卡指向**不存在的安装期语料文件**
（如 `corpus/2026-whatsuptesla com 2026 02 24 elon musk with .txt` —— 真名尾部是
`with d.txt`）。全部闸门都显示通过。

**两个独立根因**：

1. **`check_p3_paths` 只扫 `SKILL.md`，不扫 `references/*.md`。**
   而 `evidence.md` 恰恰是全包引用最多的文件（333 条路径）。
2. **`BACKTICK_PATH_RE` 的字符类是 `[A-Za-z0-9_./-]` —— 不含中文。**
   所以 `corpus/未标年-the algorithm.txt` 这种文件名**根本匹配不到**，
   等于所有中文语料路径都在闸门之外。

**为什么此前没暴露**：`SKILL.md` 里的引用以 `references/*.md` 为主（纯 ASCII），
中文路径集中在 `evidence.md` 与 `playbooks.md`，而这两个文件不在扫描范围。

**修复**：
- 路径正则放宽为 `` `([^`\s]*?[^`\s/]\.(?:md|json|py|txt))` ``
- `check_p3_paths` 扫描 `[SKILL.md] + references/*.md`
- `corpus/X` 是**安装期路径**（产出目录里没有），改为与
  `~/.pi/agent/skills/*/corpus/` 的实际文件名核对，新增 `P3_DANGLING_CORPUS`
- 加自检：注入一个假语料路径 + 一个假 references 路径，确认两者都被抓到

**教训（与 F19/F20/F23 同类）**：**校验器的覆盖面本身需要被校验。**
「所有闸门通过」不等于「所有东西都被检查过」——要问的是
**这个闸门看了哪些文件、用了什么正则、哪些内容它看不见**。

## F25：`install_skill.py` 只装固定清单里的附件，拆出的新附件在安装后断链

**症状**：把核心层压缩后，11 条原则的完整版移到 `references/principles.md`，
`SKILL.md` 里 11 处指向它。`publish_skill.py` 正常发布，六阶段闸门全过，
**但安装目录的 `references/` 里没有 `principles.md`** —— 运行期 11 条指针全部悬空。

**根因**：`install_skill.py` 用一份写死的 `ATTRS` 清单决定装哪些附件：

```
for n in ATTRS:
    if (src / "references" / n).exists():
        plan.append(...)
```

`ATTRS` 是「三件套」`{cases, evidence, voice}.md`（v6 规格的命名），
外加后来手工加进去的几个。**任何新加的附件都不在清单里，于是不会被装。**

**为什么闸门没抓到**：`P3` 校验的是**产出目录**（`output/{slug}/`）里的路径可解性 ——
那里 `principles.md` 确实存在。**没有一道闸门校验「安装后的包」是否自洽。**

**修复**：改为 glob 全部 `references/*.md`，清单只用于「缺失必需附件」的告警：

```
ref_src = src / "references"
if ref_src.exists():
    for _f in sorted(ref_src.glob("*.md")):
        plan.append((_f, dst / "references" / _f.name))
```

**同时记录一个更早的同类隐患**：`publish_skill.py` 的 `copy_package()` 已经用的是
`refs_src.glob("*.md")`，所以发布侧没问题 —— **两侧行为不一致**才是这个 bug 能存活的原因。
**教训：同一条规则（「包里有哪些附件」）在两个脚本里各写一遍，就一定会分叉。**

**校验建议**：新增一道 `install-selfcheck`：安装后比对
`output/{slug}/references/*.md` 与 `~/.pi/agent/skills/{slug}-wisdom/references/*.md`
的文件名集合，不一致即报错。

---

## F26：P3 的正则排除了空格，而语料文件名全都带空格 —— 闸门「通过」了，实际一条都没查

**发现方式**：给技能新增 `references/methods.md`（39 条推算规程，含 81 条
`corpus/<扁平名>.txt` 引用）。新增后跑 `validate_output.py package` —— **通过**。
但没有立刻相信这个「通过」，而是回头数了它**实际扫到几条路径**：

```
修复前：
  SKILL.md     15 条   corpus/   0
  cases.md      1 条   corpus/   0
  evidence.md   1 条   corpus/   0
  methods.md    0 条   corpus/   0     ← 文件里有 96 条，一条没看见
  playbooks.md  1 条   corpus/   0
  合计 18 条，其中 corpus 引用 0 条
```

**根因**：`BACKTICK_PATH_RE = re.compile(r"`([^`\s]*?[^`\s/]\.(?:md|json|py|txt))`")`
里的 `[^`\s]` 把空白排除在路径之外。而 `build_corpus_pack.py` 生成的扁平名一律是
`<年或未标年>-<标题>.txt`，**标题里的空格全部保留**：

```
corpus/未标年-attack the constraint.txt
corpus/未标年-do things in parallel.txt
corpus/未标年-retain only special forces.txt
```

于是**全部 563 条 corpus 引用对 P3 隐形**。F24 修的是「只扫 SKILL.md」「字符类不含中文」，
这次是同一条正则的第二层缺陷 —— 中文能匹配了，**空格不能**。

**修复**：拆成两条正则并用。

```python
# 带已知目录前缀时允许路径内部含空格
BACKTICK_PATH_PREFIXED_RE = re.compile(
    r"`((?:corpus|references|scripts|tools|gallery|sources)/[^`\n]*?\.(?:md|json|py|txt))`")
# 裸文件名（`SKILL.md`）不容许空格，避免把整句中文误当路径
BACKTICK_PATH_BARE_RE = re.compile(r"`([^`\s]*?[^`\s/]\.(?:md|json|py|txt))`")
```

前缀正则要求**反引号后紧跟 `corpus/`**，所以 `` `读 references/methods.md` `` 这类
中文包裹的引用不会被误匹配成路径 —— 既补上了空格，又没有引入假阳性。

**修复后**：

```
  SKILL.md     15 条   corpus/   0
  cases.md     43 条   corpus/  42
  evidence.md 317 条   corpus/ 316
  methods.md   96 条   corpus/  96
  playbooks.md 40 条   corpus/  39
  voice.md     70 条   corpus/  70
  合计 581 条，其中 corpus 引用 563 条 —— 全部可解
```

**教训**：
1. **闸门报「通过」不等于闸门查过东西。** 每次新增附件后，要**数它扫到了几条**，
   而不是看它脸色。F24 的教训是「校验器覆盖面本身需要被校验」，F26 证明这条要
   **每加一个附件就重做一遍** —— 不然同一个盲区会以新的形态复发。
2. **路径里的空格是一类独立的失败模式。** 两条不同的缺陷（不扫文件、不含中文、
   不容空格）叠在同一条正则上，修掉前两个之后第三个才露出来。

**校验建议**：给 P3 加一条硬性自检 —— **扫到的路径数必须 ≥ 反引号内 `.md/.txt/.json`
出现次数**；若 P3 扫到的 corpus 引用为 0 而技能里存在 `corpus/` 字样，直接判失败。
