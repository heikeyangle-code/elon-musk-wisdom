# 方法层 · 推算规程

> 这一层和前 11 条原则**不是一回事**。
> 原则讲「是什么」——制造比设计难。规程讲「**先看什么、算哪个数、跟什么比、什么时候停**」。
> 每条都有一个他真走过一遍的场合，逐字原文挂在下面；没有原文支撑的不进这一层。
>
> 用法：先按问题命中「触发」，再照「动作」走。动作是可以照做的，不是可以点头的。
> 每条末尾的「失效边界」和内容同等重要——它写的是这条在哪儿开始骗人。

## 规程索引

- **M01** 设计被高估了，制造被低估了
- **M02** 成败不会是竞争造成的
- **M03** 把规模和技术两个都推到最大
- **M04** 先确立它可能，再算它发生的概率
- **M05** 真复用是两次之间只剩维护和加燃料
- **M06** 能量密度翻四倍，机会才到
- **M07** 清图纸重来，别改一个现成的
- **M08** 如果那件事容易，丰田、戴姆勒、奔驰就自己做了
- **M09** 城市是三维的，道路只建在二维
- **M10** 把不可能拆成互不依赖的几条线
- **M11** 限制因子是工程，就把 80% 的时间给它
- **M12** 把「暗」说成「没有光子」，就没那么怕了
- **M13** 技术差距够大，人多、将好、聪明都不算数
- **M14** 先做出来的人赢——要么认真打，要么别上桌
- **M15** 我不管理聪明人，他们管理自己
- **M16** 很多公司把有天赋的工程师压住了
- **M17** 你会得到一个盒子里的盒子
- **M18** 有问题的时候，别只跟你下面那一层开会
- **M19** 好的总工程师不肯来，就别招差的顶上
- **M20** 不是他负责的成就，他答不出细节
- **M21** 你得愿意下死力气去招好人
- **M22** 如果 Nikola Tesla 来投简历，我们会给他面试吗
- **M23** 将军不能不会用剑
- **M24** 公司看着我把人拢起来，所以我做；但我感觉很糟
- **M25** 让团队爱你，不是你的工作
- **M26** 把最难的那部分先拿给人看
- **M27** 两个都不明显更好的时候，直接挑一个走
- **M28** 缩写要经我批准，才准进词典
- **M29** 你要让人相信：有合理的成功机会，而且回报配得上付出
- **M30** 时间表会膨胀到填满你给它的那个数
- **M31** 如果一条时间表很长，那它就是错的
- **M32** 读书的带宽比听人讲话大得多
- **M33** 感觉太顺、或者说不通，那多半是愿望思维
- **M34** 照着做像个滑稽漫画，那这条规矩就该改
- **M35** 没有清理职能，规则只会逐年累积
- **M36** 睡在大家看得见的地方，别睡会议室
- **M37** 重大新技术，三次大迭代才算真好用
- **M38** LEGO 能做到那个精度，车也能
- **M39** 别人一周五十小时、你干一百，你一年干出两倍

---

## M01 · 设计被高估了，制造被低估了

**触发**：你在给一个新产品排工程投入，工时和预算几乎全给了产品本体，制造系统那一栏写着「做完再说」。

**补位**：已有「造机器的机器」（原则 6）和瓶颈那一节（节 24）——它们讲的是「制造更难、最难的那环决定速率」。这里补的是**可执行的投入配比**：那两处没说这个比值是多少。

**他怎么说的**

> Design is overrated, and manufacturing is underrated. There is 1,000 percent, maybe 10,000 percent more work that goes into the production system than the product itself. Especially for a product with new technology. The difficulty of manufacturing is proportionate to the amount of new technology in the product.
> — `corpus/未标年-attack the constraint.txt`

> So when scaling SpaceX, we spent ten to one hundred times more effort on designing the manufacturing system than on designing the Raptor engine. We built the rockets first and the factory later, because building the production system is the harder thing.
> — `corpus/未标年-attack the constraint.txt`

**动作**

1. 把你这个项目这段期间的工时/预算分成两栏：**产品本体**，和**造它所需的那套东西**（设备、产线、工装、供应链、检验、培训）。
2. 算两栏的比值。他的参照区间是 **10 : 1 到 100 : 1**，重的那一头是制造系统，不是产品。
3. 按新技术含量调这个系数：产品里的新技术越多，制造那栏乘的倍数越大（原文判据：The difficulty of manufacturing is proportionate to the amount of new technology in the product）。
4. 顺序上先做出第一个能用的实物，再把工厂当一件**要被设计的东西**设计——不是先建一整套产线，再让产品去迁就它。

**失效边界**：这是给**要量产的硬件**用的。单位成本不随产量走的东西（纯软件、一次性定制、服务）没有一条「造它的系统」的产线，把 10:1 套上去只会吃掉真正的产品能力。成熟品类里制造可以外包，这个比例也不成立——它是「新技术 + 自造」场景的配比。

---

## M02 · 成败不会是竞争造成的

**触发**：你在写风险清单或成败判据，一半条目是竞争对手的名字和他们的动作。

**他怎么说的**

> Our success or failure will not be because of competition. It will be our capability to make a high-quality product at a price people can afford.
> — `corpus/未标年-the factory is the product.txt`

**动作**

1. 写下你这门生意的成败判据，逐条在后面标一个「这条由谁控制」。
2. 主语是竞争对手的条目，删掉——它不可控，写进判据只会引你盯着别人的动作。
3. 剩下的判据必须落成两个自己能读数的量：**产品的质量**，和**价格的相对位置**（他给的合成条件是「以人们付得起的价格做出高质量产品」）。
4. 定期述职只报这两个数，不报对手动向；对手动向当作输入，不当记分牌。

**失效边界**：当竞争位置本身就是护城河时不成立——平台锁定、独家许可、网络效应、赢家通吃，那里成败确实由对手的卡位决定，删掉竞争对手等于删掉了正确的问题。这条只适用于**制造能力主导、产品可被直接比较**的生意。

---

## M03 · 把规模和技术两个都推到最大

**触发**：你在判断一个制造业务处在什么位置，却只盯着一个变量——只盯成本，或只盯技术。

**他怎么说的**

> Two things define manufacturing competitiveness: economies of scale and technology. If you maximize your level of technology and maximize your level of scale, this is obviously going to be the most competitive situation. That’s why plants are so freaking giant.
> — `corpus/未标年-manufacturing is the moat.txt`

> Prototypes are easy and fun. Reaching volume production with a reliable product at an affordable price is excruciatingly difficult.
> — `corpus/未标年-manufacturing is the moat.txt`

**动作**

1. 给这个业务画两轴：**规模**、**技术**。各打一个当前分——相对本行业能达到的上限，不是相对你去年。
2. 找出哪一轴没推到最大。那一轴就是可攻击的约束，先动它；已经满的那轴先别动。
3. 用第二句当兑现判据：做出原型只证明你摸到了第一轴的下限；真正算数的是**可靠的量产品**加上**人们付得起的价**，两条缺一条，规模和技术的分数都不算数。
4. 报进展时报这两轴的位置，不要只报「我们做出了原型」。

**失效边界**：这是重资产制造的逻辑。批量小、定制化、或技术本身快速更替的生意里，把规模最大化会把资本锁死在一个即将过时的产线上——那些场景不该追规模，该追迭代速度。

---

## M04 · 先确立它可能，再算它发生的概率

**触发**：一件事所有人都说做不到，你在算成功概率——但算出来的数低到没有意义，因为你连它「可不可能」都还没定。

**他怎么说的**

> The first step is to establish that something is possible, then the probability it will occur.
> — `corpus/未标年-building the just barely possible.txt`

> In no prior design was full reusability one of the possible outcomes.
> — `corpus/未标年-building the just barely possible.txt`

> But you can’t take a single example and make an entire theory out of it.
> — `corpus/未标年-building the just barely possible.txt`

> Nobody thought this was possible. But we’re not breaking any laws of physics, so we knew it was possible.
> — `corpus/未标年-building the just barely possible.txt`

**动作**

1. 先只回答是/否：**违反物理定律吗？** 不违反，就把它标成「可能」——这一步和概率无关（原文：we’re not breaking any laws of physics, so we knew it was possible）。
2. 反过来查历史：以前的设计里，这件事**有没有被列为「可能的结果」之一**？如果从来没有（In no prior design…），缺口在「可能性」这一步，不在执行——先把一种可能的结果定义出来，再谈概率。
3. 第二步才写下概率，而且写成「需要几次尝试」，不是「成功几率多少」。
4. 有人拿**一个**失败先例证明「这事不行」时（航天飞机之于可复用），判据是：单一案例不构成一条理论——先问那个先例的前提和你的一样不一样。

**失效边界**：「成立可能性」这一步只在**物理**上有效。物理上可能不蕴含会发生——他自己补了后半句：Of course, just because something is possible does not mean it will occur。在人、监管、市场层面没有物理这个中间裁判，把「可能」读成「会成」就是过度外推。

---

## M05 · 真复用是两次之间只剩维护和加燃料

**触发**：你在评估一项「可重复使用」的技术（设备、平台、流程），有人用「它也复用了」来给它算账，你要判断那个复用值不值钱。

**他怎么说的**

> It has to be true reuse, which means rapid and complete reuse. The problem with the space shuttle was only a portion of the system came back, and the reusable parts were incredibly difficult to refurbish. Reuse matters more if it’s rapid and complete—if the only thing we do between flights is maintenance and refuel, like an airplane.
> — `corpus/未标年-building the just barely possible.txt`

> If there is no major work required between flights, then the cost of a flight approaches the cost of propellant.
> — `corpus/未标年-building the just barely possible.txt`

**动作**

1. 不看复用率，看**两次使用之间**要做哪些事。列出来，逐条标注：是维护、加料，还是「拆开重做」。
2. 判据是二值的：**两次之间只剩维护和加燃料**，才算真复用；只要还有一部分要翻修、或者只回来一部分（航天飞机就是这么败的），复用不成立。
3. 算下限：真复用成立时，单次成本**趋近于消耗品成本**（燃料）。用这个下限当目标锚——它告诉你这项技术最多能便宜到哪。
4. 拿这个下限回击「它也是可复用的」：问一句「两次之间你要做多少工」。

**失效边界**：这是针对**设备/硬件**的核算。软件和数据的边际成本本来就接近零，「两次之间要做什么」没有对应物，套上去会得出错误结论。

---

## M06 · 能量密度翻四倍，机会才到

**触发**：你想做一件早就有人想过的事，但不知道怎么判断「现在到底是不是时候」，只能一轮一轮地空等。

**他怎么说的**

> Getting the timing right was important. Lithium-ion batteries were the critical breakthrough needed for compelling electric cars. I knew it became possible to start Tesla because we went from the energy density of lead acid batteries to lithium-ion batteries—about a 4x energy density improvement. If you had a sixty-mile range with a lead-acid battery, you would have about one-hundred-forty-mile range with lithium-ion for the same weight.
> — `corpus/未标年-building the first prototype.txt`

**动作**

1. 找出这件事**卡在哪个使能部件**上——不是「技术不成熟」这种总说法，是一个具体的部件（电池、芯片、传感器、材料）。
2. 查这个部件相对上一代的关键指标倍数。他的判例是**能量密度约 4 倍**（同样重量，续航 60 英里变 140 英里）——倍数到了，产品才从「做不出来」变成「值得开公司」。
3. 用这个倍数卡时机：倍数没到，你的问题是**在等**，不是执行弱；倍数到了，就不该再拿「还早」当借口。
4. 把这个使能指标的当前值写下来，定期重读——它比任何路线图更能告诉你该不该现在动手。

**失效边界**：这条只对**性能受限型**技术成立。有些方向的解锁来自成本曲线下降（靠规模），有些来自标准或许可变化（制度）；那些场景里没有那个「翻几倍」的扳机，需要盯的是另外的变量。

---

## M07 · 清图纸重来，别改一个现成的

**触发**：你在做一个「基于现有产品或平台改造」的新东西，团队默认这条路比从头做便宜。

**他怎么说的**

> We ended up using none of the AC Propulsion technology. Something that looks cool and works as an individual prototype does not necessarily scale. Eventually maybe 7 percent of the parts of the original Tesla Roadster were common with the Lotus Elise. It would have been much smarter to start with a clean-sheet design and not try to modify something else.
> — `corpus/未标年-building the first prototype.txt`

> It was just a flat-out burning dumpster fire of stupidity. One example: The chassis had to be redesigned to fit the battery pack and became 40 percent heavier. This invalidated the crash testing Lotus had done.
> — `corpus/未标年-building the first prototype.txt`

**动作**

1. 先把两个问题分开：它**像不像一个能用的原型**，和它**能不能按量造出来**（原文：Something that looks cool and works as an individual prototype does not necessarily scale）。
2. 数**共用件比例**：新东西里有多少零件和改造的基础件共用。他的判例是 **7%**——共用比例低到个位数，说明「改造」这个前提本身错了。
3. 检查改动有没有**作废原有的验证**：底盘为容纳电池重了 40%，直接把 Lotus 做过的碰撞测试作废。被作废的验证要重新花钱买回来，把这笔算进「改造更便宜」的账里。
4. 判据：共用件比例接近个位数、且关键验证被作废 → 停止改造，清图纸重来（It would have been much smarter to start with a clean-sheet design）。

**失效边界**：当共用平台、共用供应链、共用认证本身就是**战略资产**时（同平台多车型摊薄模具与法规成本），高复用率是有价值的，清图纸重来反而更贵。这条针对的是「拿一个不兼容的原型硬改」，不是所有改造。

---

## M08 · 如果那件事容易，丰田、戴姆勒、奔驰就自己做了

**触发**：你要证明自己的工程有壁垒、值得被投资或值得定价，但手上既没有专利，也没有独家数据。

**他怎么说的**

> The evidence for us solving hard engineering problems is that Toyota, Daimler, and Mercedes buy electric powertrains from us. If it was easy, they would do it.
> — `corpus/未标年-engineering creates value.txt`

**动作**

1. 找出这个领域里**有能力自制、也有钱自制**的几家公司——比你现在强的那些。
2. 看它们**自产还是外购**。它们外购，就是最硬的一份证据：它们不做不是不会，是自己做更贵或更难。
3. 用这份外购清单替你说话，别用「我们技术领先」这种自评。
4. 判据反过来用：如果比你强的玩家都自己做，说明这件事**不构成壁垒**，你的价值主张要重新找。

**失效边界**：这条靠**外部大买家**验证，只在有下游大买家、且外购是常规行为的市场里成立。面向终端消费者的产品没有这个「大厂会不会自己做」的对照系；垄断采购或强制的本地化生产也会把这个信号污染掉。

---

## M09 · 城市是三维的，道路只建在二维

**触发**：有人说某个东西「已经满了 / 到顶了」（车流、带宽、产能、场地），而你还没检查它被用在了几个维度上。

**补位**：已有「极限思维」原则（含隧道的十倍降本算账）。这里补的是**当你说「满了」时的第一步——先数维度，再算余量**。

**他怎么说的**

> Ever notice that cities are built in 3D, but roads are only built in 2D? You could build roads in 3D by building tunnels under cities. You can alleviate any amount of urban congestion with a 3D tunnel network.
> — `corpus/未标年-thinking in limits.txt`

> They don’t realize there’s no real limit to how many levels of tunnel you can have. You can go much farther deep underground than you can build up. The deepest mines are much deeper than the tallest buildings are tall.
> — `corpus/未标年-thinking in limits.txt`

**动作**

1. 当有人说「满了」，先数这项资源**被用在了几个维度**上。道路只用了一维（平面），城市用了三维——差距就在这里。
2. 找出被浪费的那个维度，并验证它的物理余量：往下挖比往上盖的空间大得多（最深的矿比最高的楼深得多）——上限常在一维里被严重低估。
3. 用「把它放大」当工具问一句：如果在第三个维度上铺开，上限还是现在这个数吗？
4. 只有当每个可用维度都被推到物理极限、仍然满时，「满了」才是真约束。

**失效边界**：增加一个维度几乎总要付出另一项物理代价（挖隧道要钱、堆叠要承重、并行要协调），而成本常随维度指数上升。这条只用来**发现被忽略的空间**，不是用来跳过成本核算——能不能加那一维，还得回去算代价。

---

## M10 · 把不可能拆成互不依赖的几条线

**触发**：一个整块的「不可能」横在面前——供应商给的工期、一个系统的交付时间；你要么全盘接受，要么整个推倒，中间没有别的动作。

**补位**：已有第一性原理（原则 1）用同一次 Colossus 当例子，说明「18 到 24 个月」是类比不是约束。这里补的是**拆的粒度**（拆成互不依赖的资源线）和**每条线去租现成替代**这个动作。

**他怎么说的**

> Often, we were told something was impossible, but once we broke it down into its constituent elements, we could solve those.
> — `corpus/未标年-break down the impossible.txt`

> So, we broke that down. We need a building; we need power; we need cooling.
> — `corpus/未标年-break down the impossible.txt`

> Their estimates for how long it would take to complete that were eighteen to twenty-four months. Well, we needed to get that done in six months or we wouldn’t be competitive.
> — `corpus/未标年-break down the impossible.txt`

**动作**

1. 把那个整块的数拆成**互相独立**的组成部分。他的拆法是把训练集群拆成三条线：需要一个房子、需要电、需要冷却。
2. 每条线单独问：它缺的是什么，**市场上有没有现成的东西可以直接拿来用**，而不是照标准做法自己造。房子来不及盖 → 租一座闲置工厂；电不够 → 租发电机摆在楼的一侧；冷却不够 → 租移动制冷机组摆另一侧。
3. 每条线找**最短路径的临时解**，并行推进，不串行。原文里连布线都是四班倒、24/7。
4. 用时间当判据控制节奏：需求是六个月，供应商说十八到二十四个月——那就不是「能不能」，是「必须重拆」。

**失效边界**：拆得动的前提是**这些部分真的互相独立**。各部分之间有强耦合时（改一处连锁改另一处），拆开分别找替代只会得到一堆配不上的东西。而且它依赖**市场上存在可租用的现成余量**——没有闲置产能时，拆完也租不到。

---

## M11 · 限制因子是工程，就把 80% 的时间给它

**触发**：你在推进一件技术上的事，但时间大部分花在管理、协调、融资、对外上，你想确认这个分配对不对。

**他怎么说的**

> If you want to advance civilization, you must address the limiting factor. The limiting factor is the engineering. Therefore, you must address the engineering.
> — `corpus/未标年-engineering is magic.txt`

> I spend 80 percent of my time on engineering.
> — `corpus/未标年-engineering is magic.txt`

**动作**

1. 先定位**限制因子**：你这个领域里，产生「新数据 / 新的实物证据」的那个环节是什么？（物理学靠工程取得新数据——伽利略造了望远镜，才看见木星的卫星。）
2. 数你上个月的时间分配，算出花在那个限制因子上的比例。参照值：**80%**。
3. 低于这个数，就把管理、协调、对外这类事往下压或授权出去，把省下的时间挪进限制因子。
4. 判据：一件事既不在限制因子上、又只产生活动量，它就不该占用你的时间。

**失效边界**：80% 是**技术主导型组织**的配比。当限制因子不在工程上——早期公司的限制因子是活下来（融资）、是拿许可（制度）、是找到第一个客户（销售）——硬把 80% 挪进工程会直接把自己饿死。先找对限制因子，再谈比例。

---

## M12 · 把「暗」说成「没有光子」，就没那么怕了

**触发**：你或团队因为一个模糊的恐惧而不敢动手，而那个恐惧从没被写清楚过。

**他怎么说的**

> When I was a little kid, I was really scared of the dark. But I came to understand “dark” just means the absence of photons in the visible wavelength—four hundred to seven hundred nanometers. I thought, well it’s silly to be afraid of a lack of photons. Then I wasn’t afraid of the dark anymore.
> — `corpus/未标年-engineering is magic.txt`

**动作**

1. 把恐惧写成一个名词，不是一种感受——你实际怕的是「暗」，是「没订单」，是「被拒」。
2. 把这个名词翻译成**可以被测量或核查的定义**。「暗」= 可见波长（400–700 纳米）内没有光子；「没订单」= 某个数低于某个值；「被拒」= 收到的是一句话还是沉默。
3. 站在这个定义上重问一次：它真的威胁到你的存活吗？很多恐惧在被写成物理量之后自己消失——你怕的是「不确定」本身，不是那个量。
4. 翻译之后**仍然成立**的恐惧，才进入「算概率、写最坏情况」那一步去处理。

**失效边界**：这个动作能拆掉的是**因为不知道而生的恐惧**。「暗」能被翻译掉，因为它是个定义问题；真实的、物理上成立的威胁（钱烧完了、人出了事）翻译之后不会变小，只会更清楚——别指望用「翻译成物理定义」消掉一个真实风险。

---

## M13 · 技术差距够大，人多、将好、聪明都不算数

**触发**：你在一个正快速变化的领域里竞争，手上还有一个「更强的对手」（更多资源、更好的人、更大的规模），你在想该往哪儿使劲。

**他怎么说的**

> If there is a big difference in the technologies—even if the other side has more people, better generals, and is smarter—the side with the advanced technology will win.
> — `corpus/未标年-engineering wins wars.txt`

> To use an extreme example (a limit case), if you can shoot lasers from space to any spot on the ground by just pointing at it, it would not matter if you’re fighting Julius Caesar, Heinz Guderian, or Napoleon. They just got lasered from space.
> — `corpus/未标年-engineering wins wars.txt`

> But when fighting outside the Roman empire, they sometimes lost their wars because of their opponent’s technology. When the Romans fought the Scythians, they did not have a good counter to mounted war archers, especially if they got lured into flat terrain. They were pretty much helpless against the technology of a mounted archer.
> — `corpus/未标年-engineering wins wars.txt`

**动作**

1. 先判断当前是不是**技术变化率高的窗口**：有一项新技术在快速迭代、并且能叠加到你的产出/战力上。
2. 是的话，把资源集中到**工程和技术领先**上，别去补规模、补人数、补战术——技术差距大到一定程度，其他变量全部作废。
3. 用极限检验（limit case）测一下：把技术差距推到极端（激光从太空）后，还剩哪些变量能决定输赢？答案若是「没有」，那些变量就不值得优化。
4. 判据落到一句：**比的是谁造新技术造得快**（How fast can we create new technology?）——把「迭代速度」设成主指标。

**失效边界**：变化率**低**时就反过来——技术停滞期胜负回到机动、战术、规模和后勤，这时一心堆技术是浪费。而且这条假设那项技术**真能叠加**到产出上；有些领域的技术优势会被地形、政治、制度吃掉（罗马人在平地碰上骑射的斯基泰人就打不过）。

---

## M14 · 先做出来的人赢——要么认真打，要么别上桌

**触发**：你身处一场「赢家通吃」的技术竞赛，却把它当成一场可以慢慢来、比谁做得好的比赛。

**他怎么说的**

> In Sun Tzu’s The Art of War, there is no chapter on technology. It is an interesting book I’ve read many times. It’s packed with wisdom, but there should be a chapter saying: “If you have a decisive technological advantage, you can win with minimal casualties to your side.”
> — `corpus/未标年-engineering wins wars.txt`

> Most battles in history, because technology moved slowly, were more about maneuvering, tactics, and strategy. But when there’s technological discontinuity, it fundamentally changes the whole situation. Wars in the modern era are very much technology race wars. How fast can we create new technology? The best example would be the nuclear bomb. Anyone who made nuclear bombs first, won. That’s it. End of story.
> — `corpus/未标年-engineering wins wars.txt`

> Play to win, or don’t play at all.
> — `corpus/未标年-engineering wins wars.txt`

**动作**

1. 先分类：这场竞赛是**技术连续**（慢慢比谁做得好）还是**技术断层**（先到者通吃）。判据问一句——第一个做出来的人会不会把其他人全部踢出局？
2. 是断层型，就把目标从「做得比对手好」改成**「比对手先到」**；此时时间是唯一变量，其他优势降为次要。
3. 用「要么认真打，要么别上桌」当入场判据：如果不打算按能在断层里抢先的强度投入，就别进场——半力进场在通吃型竞赛里等于确定出局。
4. 对每个关键里程碑，只报「离第一个做出来还差多少」，不报「比对手领先多少」。

**失效边界**：这是**竞赛/战争框架**，前提是存在一个明确的「先到者通吃」终点。「要么认真打，要么别上桌」用在可以共赢、可以共存的领域是错的——那里全力进场反而是战略失误。这条只该用在真正的零和、赢家通吃的技术竞赛上。

已读 11 个文件；跳过 1 个（`未标年-speed is both offense and defense.txt` —— 其全部逐字内容已在 SKILL.md 原则 10 与 playbooks.md 节 36里写过，抽不出可叠加的新动作）

---

## M15 · 我不管理聪明人，他们管理自己

**触发**：你要把一件事交给一个很强的人，但你拿不准该管到多深——管少了怕跑偏，管多了等于你在替他做。

**他怎么说的**

> I don’t think I manage smart people; they manage themselves. If someone is smart and talented, they can go anywhere and do anything, anytime.
> — `corpus/未标年-create a culture of builders.txt`

> I say, “Look, this is the goal we’re after. Do you agree with this goal? If you do, then let’s try to get it done.”
> — `corpus/未标年-create a culture of builders.txt`

> I’ll provide my opinion along the way. But it’s rare for me to actually insist on a particular thing. Once in a while I’ll say, “You have to trust me on this one. We have to do this, and if it turns out to be a bad decision, we can all hold it against me in the future.”
> — `corpus/未标年-create a culture of builders.txt`

**动作**

1. 交事之前，把目标写成一句话，当面问一句「你同意这个目标吗」。不同意就先谈目标；目标没对齐的时候谈"怎么做"是白谈。
2. 谈成之后，你只提供意见。每次开口前先分清你给的是哪一档：这句话是"我认为"，还是"必须"。
3. 把「必须」留成例外。只在你要推翻对方判断的时候用它，并且当场把坏结果的账记到自己头上——他给的说法是"we can all hold it against me in the future"。他给这一档的定额是 rare：偶尔一次，不是常态。
4. 交之前先查一件事：这个人能不能在高层次上理解整个系统、知道自己在什么时候做了一个坏优化。
   > Another important principle: You want everyone to be able to think like the chief engineer. They need to understand the system at a high level, well enough to know when they are making a bad optimization.
   > — `corpus/未标年-create a culture of builders.txt`

（已有：手册节 27已把"让所有人像总工程师一样思考"单独写成一条；这里补的是它在交付动作里的位置——先查这一条，再谈授权。）

**失效边界**：目标本身不可协商的时候这条不成立——安全线、物理约束、合规红线上没有"你同意吗"这一步，问也只是个形式。另一头也不成立：对方还不具备系统级理解时，"你同意吗"得到的是没听懂就点头，授权会退化成局部最优的集合——他自己给的前置条件就是那句 think like the chief engineer。

---

## M16 · 很多公司把有天赋的工程师压住了

**触发**：你团队里有很强的人，但过去一年你几乎说不出他做成了什么，而大家都很舒服。

**他怎么说的**

> Many companies suppress their talented, driven engineers. Some are suppressed by being so comfortable they don’t produce much. There are a few places in Silicon Valley with good engineers—but what are they producing? The output of that engineering talent seems low, though maybe they are enjoying themselves.
> — `corpus/未标年-create a culture of builders.txt`

> At Tesla, a superb engineer’s talents are used to a greater degree than anywhere else.
> — `corpus/未标年-create a culture of builders.txt`

**动作**

1. 把团队里最强的那几个人列出来，每人后面写一句他过去一年**做出来的**东西——成品、交付、删掉的东西都算；"参与了什么"不算。
2. 对每个人问一句：他的能力被用到了几分。判据不在他忙不忙、也不在他开心不开心——他把"舒服"直接点成了压制的一种形式（"suppressed by being so comfortable they don’t produce much"）。
3. 把差额记在公司的账上，不要记在人的账上：产出低而人不弱，先查的是环境够不够 demanding，而不是先给人下判断。他给的对照信息有三条——事量很大、事情本身有意思、而且不容易。
   > Tesla is not like that. We’re demanding. You’re going to get a lot done and it’s going to be cool work, but it’s not going to be easy.
   > — `corpus/未标年-create a culture of builders.txt`
4. 判据落在"用了多少"，不是"留没留住"：他自己拿 Tesla 当刻度，说的是"一个优秀工程师的天赋在这里被用得比别处多"。

**失效边界**：这条只在你能给出"更 demanding 的替代物"时成立——先把人算成被压住，你手上却没有值得他投入的事，那么加压得到的不是产出，是离职。

---

## M17 · 你会得到一个盒子里的盒子

**触发**：产品里有一处解释不通的重复——两层壳、两道检验、同一个功能做了两遍——没人说得清为什么，而所有人都觉得这是设计问题。

**他怎么说的**

> You can see the organizational boundaries in the product. You’ll often get a box in a box. You realize, “Why is this thing in two boxes?” Turns out, because both teams thought they needed an enclosure, the product ends up with an enclosure in an enclosure.
> — `corpus/未标年-remove organizational boundaries.txt`

> One case from the Tesla Model 3: The battery pack had a top enclosure and the car also has an underbody, right above it. What’s the point of that? That doesn’t make any sense, but because one team enclosed the battery pack and another team wanted to have an enclosed body, it happened.
> — `corpus/未标年-remove organizational boundaries.txt`

> It makes sense from an individual team’s perspective, but you don’t need a cover on the battery—there’s a car on top of it. Putting the cover on the battery pack adds mass and cost, so it should be deleted.
> — `corpus/未标年-remove organizational boundaries.txt`

**动作**

1. 把产品（或流程）里所有"重复了一遍"的地方列出来：两层的壳、两道的检验、两个团队各做一份的表、两个都以为对方要用的接口。
2. 对每一处问一句「这是谁要的」。如果答案是"两个团队各要了一次"，就把这条从设计缺陷栏挪到组织栏——他给的判据就是那句：产品里看得见组织的错。
3. 每件东西单独过一遍必要性：
   > Find the design necessity of every part and every process.
   > — `corpus/未标年-remove organizational boundaries.txt`
4. 答不出必要性的就删——判据可以算：它增加质量和成本，而功能已经被别的东西覆盖了（盖子上面本来就是车）。
5. 删完顺手修那道接缝：让付代价的一方直接够得到做设计的一方。
   > The people on the assembly line should be able to immediately grab a designer or engineer and say, “WHY DID YOU MAKE IT THIS WAY!?’”
   > — `corpus/未标年-remove organizational boundaries.txt`

**失效边界**：这条的前提是你能亲眼看到产品实物——纯流程、纯组织的问题不留形，那得走别的路。还有一条：要删掉的那一件如果在外部供应商手上，"删"这个动作就变成重谈合同，代价不由你单方面定。

---

## M18 · 有问题的时候，别只跟你下面那一层开会

**触发**：一个问题反复解决不掉，你已经开过几轮会，拿到的全是汇报版本。

**他怎么说的**

> Whenever there are problems to solve, don’t just meet with your managers. Do a skip level, where you meet with the level right below your managers.
> — `corpus/未标年-remove organizational boundaries.txt`

> Physically go to where the problem is, immediately.
> — `corpus/未标年-remove organizational boundaries.txt`

> One of my rules is “Go as close to the source as possible.”
>
> We were trying to determine how thick Starship’s walls should be. Rather than only talking to the company’s executives, I talked to some of the workers actually doing the welding. I asked what they thought was safe. The line workers thought the tank walls could get as thin as 4.8 millimeters.
>
> “What about four?” I asked.
>
> “That would make us pretty nervous,” the workers replied.
>
> “Okay,” I said, “Let’s try four millimeters.”
>
> It worked.
> — `corpus/未标年-remove organizational boundaries.txt`

**动作**

1. 有问题要解决时，先别约你的直属下级——做一次跳级会，见他们下面那一层。
2. 物理上去到问题发生的地方，立刻。不是等排期，是现在。
3. 从干活的人嘴里拿数，不从高管嘴里拿数。他的版本是：高管那边是一个数，焊工说 4.8 毫米，他试 4 毫米。
4. 拿到那个数就去试。判据不是"共识能不能达成"，是"试了行不行"——他在这段话的最后放的是两个字：It worked.

（已有：手册节 35《到源头去》讲的是同一件事，同一段星舰壁厚的逐字原文也在那一节里；这里补的是那个具体的组织动作——跳级会，以及"别只跟你的直属下级开会"这条规则本身。）

**失效边界**：跳级会被当成绕过中层来用的时候，你会同时收到两个损失——中层不再对结果负责，一线的人开始只说你想听的话。这条的理由是"为了把事解决"，不是常规汇报路线的替代品。

---

## M19 · 好的总工程师不肯来，就别招差的顶上

**触发**：一个关键位置空了很久，你在考虑"先招个差不多的顶上"。

**他怎么说的**

> I worked very hard to collect the right expertise when starting SpaceX. I tried hard to find a great chief engineer for the rocket, but good chief engineers wouldn’t join and there is no point in hiring the bad ones. I ended up being chief engineer of the rocket. If I could have found somebody better, maybe we would have had fewer than three failures.
> — `corpus/未标年-retain only special forces.txt`

> The fundamental limitation is exceptional engineers. There are not that many.
> — `corpus/未标年-retain only special forces.txt`

**动作**

1. 把这个位置要交付的东西写成一句话，给候选人定一条最低合格线。线可以定高——他自己给的标准是"最低的及格分是卓越"。
2. 招不到过线的人时，不做"降标准先顶上"这个动作。判据是他那句 there is no point in hiring the bad ones：差的人不是过渡方案，是一笔你要还很久的账。
3. 招不到就自己接过来——他找不到火箭的总工程师，最后是他自己当了火箭的总工程师。
4. 自己接手时，先把代价写成一句预算，而不是等事后才承认：他的版本是回过头才能说的那句话——如果有更好的人，"也许我们就不会失败三次了"。

**失效边界**：这是创业期的标准，他自己限定过（"for companies in the startup phase"）。位置已经可以被流程和分工替代的时候，"空着"的成本会超过招一个中等的人。另一头，"自己顶上"只在你是这件事的第一性理解者时成立——顶上去当总工程师的代价，是他自己认下的那三次失败。

---

## M20 · 不是他负责的成就，他答不出细节

**触发**：你在面试，简历很漂亮，但你判断不出那段成就是他做的，还是他旁边的人做的。

**他怎么说的**

> In interviews, I ask people to tell me the story of their career and some of the tougher problems they dealt with, how they dealt with those, and how they made decisions at key transition points. Usually that’s enough for me to get a good gut feeling about someone. What I’m really looking for is evidence of exceptional ability. Did they face difficult problems and overcome them?
> — `corpus/未标年-recruit for exceptional ability.txt`

> Usually the person who had to struggle with the problem really understands it and they don’t forget if it was difficult. Ask them detailed questions about it, and they’ll know the answers. A person who was not responsible for that accomplishment will not know the details.
> — `corpus/未标年-recruit for exceptional ability.txt`

**动作**

1. 让他从头讲职业经历，重点放进更难的那几个问题：他怎么处理的、在关键转折点上怎么决定的。
2. 挑其中一个他自称解决了的问题，往细节里问——问到你自己能讲出这个问题的机制为止。这一步不考他的知识，验的是他有没有真的在那件事里。
3. 判据有两头：真扛过的人不会忘，而且答得出细节；没扛过的人答不出细节。答不出，就把这段经历从这个人身上划掉。
4. 留一档例外——没有履历证据、但明显很聪明的人，甚至可以没有读完研究生或本科；在他们出成果之前把人招进来。
   > I always ask my teams to give a lot of thought to who should join. I recommend paying close attention to people who haven’t completed their grad or even undergrad, but are obviously brilliant. Better to have them join before they achieve a breakthrough.
   > — `corpus/未标年-recruit for exceptional ability.txt`
5. 过了这一关再看下一关：他自己承认过反向的错（在智力和心性之间选错了），所以能力验完，态度和品格要单独测。
   > I’ve made several hiring decisions where I valued intellect over heart and I think that was a mistake.
   > — `corpus/未标年-retain only special forces.txt`

（已有：手册节 3已写"看态度、技能可以教"，以及看朋友与同僚那条品格判据；这里补的是面试里"验所有权"的那串追问动作。）

**失效边界**：这套追问对"经历造假"有效，对"他没做过难事"的人无效——应届生、转行者、从很平的岗位上出来的人，全会被判成答不出细节；他自己给这一档留了后门（"or at least exceptional aspiration"），所以它不能当唯一的筛子。另一头更难：他说自己有判断工程师好坏的能力，换一个面试官就不是这个前提了——把追问落成记录（写下他答不出的那个细节），否则剩下的只是直觉。

---

## M21 · 你得愿意下死力气去招好人

**触发**：你看上了一个人，但他有一个具体的不来的理由——城市、家人、手上还有别的选择。

**他怎么说的**

> You’ve got to be willing to recruit hard for excellent people. When I was interviewing Bülent Altan for SpaceX, I told him, “I heard you don’t want to move to Los Angeles because your wife works for Google in San Francisco. Well, I just talked to Larry Page, and they’re going to transfer your wife down to LA. So what are you going to do now?” He said he would come work for SpaceX.
> — `corpus/未标年-recruit for exceptional ability.txt`

**动作**

1. 问出那一个具体的理由。判据是它具体到一件可以被解决的事——他听到的不是"不想来"，是"配偶在旧金山为 Google 工作"。
2. 把那个理由当工程问题处理：找到能动这件事的人，直接把障碍拆掉。他的版本是打给 Larry Page，先把配偶调岗这件事办完。
3. 障碍拆掉之后，把选择权交回他手上——"So what are you going to do now?"——不要替他回答。
4. 提前把"值得他为此动身"的那部分准备出来：有意思的工作、好的财务回报、会改变世界的产品、以及一条强的目的感。
   > Having a strong sense of purpose will attract the very best talent in the world. If the work is enjoyable, the financial rewards are good, and the product will change the world—that’s a pretty powerful set of motivators.
   > — `corpus/未标年-retain only special forces.txt`

**失效边界**：这条只在你能动到那个杠杆时成立——多数人没有一条直通 Larry Page 的电话线。更硬的一条：拆障碍之前先确认工作本身是他的理由；那份工作对他没有吸引力的时候，你只是把人从一个他不喜欢的地方挪到另一个。

---

## M22 · 如果 Nikola Tesla 来投简历，我们会给他面试吗

**触发**：你在审招聘流程，怀疑筛子的孔太密——路径不对的好人，第一关就没了。

**他怎么说的**

> Sometimes these things get messed up in recruiting. I sometimes wonder, “If Nikola Tesla applied to Tesla, would we even give him an interview?” It’s not clear. They might say, “This guy came from some weird college in Eastern Europe, he’s got some odd mannerisms, we don’t know if we should give him an interview.” I worry that’s what we’d do. Our response should be, “Man, Nikola Tesla, this kid’s super smart. What does he want? We’ll pay him anything!”
> — `corpus/未标年-recruit for exceptional ability.txt`

**动作**

1. 找三个你真心佩服、但路径非常规的人（非名校、非大厂、头衔难看、脾气怪），把他们的简历放进你自己的筛选流程里跑一遍。
2. 记下他们分别会死在哪一关：学校、前公司、头衔、空窗、面试表现。死掉的那一关，就是你筛子上的洞。
3. 对这类候选人换一个问题：不问"他够不够格"，问"他想要什么"，然后看你给不给得起——他给的态度是"他要什么？我们都给"。
4. 为这类人留一条通道：不由常规筛选判定，直接给面试。

**失效边界**：这条用来防"漏掉好人"，不能当录用标准——路径非常规本身不是优点，它只是不该被杀掉的理由。前提是那个人"明显很聪明"，而这一条依赖有人看得出来；看不出来的时候，该做的是 M06 的追问，不是把筛子拆掉。

---

## M23 · 将军不能不会用剑

**触发**：你在带技术团队，但你上一次亲手做那件事已经是几年前了。

**他怎么说的**

> All technical managers must have hands-on experience. For example, managers of software teams must spend at least 20 percent of their time coding. Solar roof managers must spend time on the roofs doing installations. Otherwise, they are like a cavalry leader who can’t ride a horse or a general who can’t use a sword.
> — `corpus/未标年-frontline leadership.txt`

> Never ask your troops to do something you’re not willing to do.
> — `corpus/未标年-frontline leadership.txt`

> A major failure mode is a high ego-to-ability ratio. If your ego-to-ability ratio gets too high, then you’ve broken the feedback loop to reality.
> — `corpus/未标年-frontline leadership.txt`

**动作**

1. 给你自己（和每个技术管理者）定一个能核查的比例：软件管理者至少 20% 的时间写代码，光伏屋顶管理者上屋顶做安装。比例要落成能查痕迹的形式——提交、安装单、值班记录，不是日程表上的一条。
2. 派活之前先问自己愿不愿意做这件事；不愿意，就先弄清为什么不愿意——是活本身不对，还是你已经离现场太远。
3. 一线的人在做哪几类活，你自己至少各做几次；大事小事都做。
   > Do whatever the task is, whether grand or humble.
   > — `corpus/未标年-frontline leadership.txt`
4. 用"自我/能力比"当仪表：这个比值一高，你收到的信息就已经被你自己过滤过——他说这在 AI 的说法里就是 RL 回路断了。
5. 定期做一件压自我的事，亲手做完最卑微的那个环节，看你自己的判断和一线的人差在哪。
   > Always be smashing your ego. Internalize responsibility. Whether you’re a CEO or any other role, do whatever it takes to succeed.
   > — `corpus/未标年-frontline leadership.txt`

（已有：手册节 38已有"亲手去做几次"和同一句逐字原文；这里补的是那条可核查的 20% 定额，以及 ego-to-ability 这个仪表。）

**失效边界**：20% 是他在软件团队和光伏屋顶上给的两个例子，不是普适常数——照抄数字会产生假动作（日历上占着 20%，手上不产出）。这条治的是"判断是听来的"和"要求别人做你自己不做的事"，治不了能力不足；团队大到一个人覆盖不了的时候，只能把这个比例下派到每个技术管理者，否则它会退化成象征性的露面。

---

## M24 · 公司看着我把人拢起来，所以我做；但我感觉很糟

**触发**：项目刚炸，或者事故刚发生，你要在团队面前说话，而你自己状态很差。

**他怎么说的**

> Managing through big failures is painful and difficult. It feels terrible. The company looks at me to rally them, so I do. But I feel terrible. Failure is a punch in the gut. Even when you’ve got a lot of smart people working super hard to minimize the probability of failure, it’s still there. And it’s quite significant.
> — `corpus/未标年-take responsibility.txt`

> Given the options, I prefer to learn from success.
> — `corpus/未标年-take responsibility.txt`

**动作**

1. 先把两件事分开：你感觉糟，和你现在要做的动作。他的处理是并列的两句——"The company looks at me to rally them, so I do. But I feel terrible." 允许自己承认疼，但别让情绪变成动作的输入。
2. 团队面前只交付动作：事实、下一步、谁负责。他讲失败时放的第一句不是安慰，是"这是一拳打在肚子上"——不掩饰，也不扩写。
3. 复盘时不要只翻失败那一堆。他的偏好写在那一节的最后一句：能选的话，他更愿意从成功里学——找出成功那次条件对上了什么，把它写成可重复的步骤。
4. 你自己的工作表是别人修不了、一直在烂的那些问题，所以失败当下你只从里面挑一件能推进的去做。
   > Particularly, if you’re the CEO, you work on all the worst problems in the company. There’s no point in spending time on things that are going right, so you only spend time on things that are going wrong. Specifically, the things other people can’t fix. The most pernicious and painful problems.
   > — `corpus/未标年-take responsibility.txt`
5. 动作给完之后再谈情绪，顺序反了会变成让别人先照顾你。

（已有：手册节 25已写"你只花时间在出错的事上，尤其是别人修不了的那些"；这里补的是失败当下那一步——把情绪和动作拆开。）

**失效边界**：这条只管当下"怎么动"，不管长期状态，也不是让你忍——压着感觉当没事，你会用一个坏状态去驱动一连串决定。如果失败牵涉到人（有人要担责、有人要离开），"把人拢起来"这一步替代不了给出后果，那是 M11 的动作；缺了那一步，拢起来只是暂时的。

---

## M25 · 让团队爱你，不是你的工作

**触发**：你要给一个人难听的反馈，或者要开掉一个人，你因为"他会难过"而拖着不动。

**他怎么说的**

> It’s not your job to make people on your team love you. In fact, that’s counterproductive. I had a manager who would not fire anyone. I told him, “You can’t tell people they have to get their shit together, and when they don’t get their shit together—nothing happens to them.”
> — `corpus/未标年-feedback over feelings.txt`

> Wanting to be everyone’s friend leads you to care too much about the emotions of the individual in front of you rather than caring about the success of the whole enterprise. Focusing on that one individual can lead to a far greater number of people being hurt.
> — `corpus/未标年-feedback over feelings.txt`

**动作**

1. 把两边的人数写下来：迁就的收益是一个人（避免一个人难过）；不迁就的那一侧是全公司和用户。两个数摆在一起，多数犹豫会自己结束——他给的机制就是那句"只照顾眼前这一个人的情绪，会有更多的人受伤"。
2. 查一遍你的要求后面有没有跟着后果：你上次让人"把事搞好"，他没搞好，然后发生了什么？如果答案是"什么都没发生"，那条要求已经作废了。
3. 给反馈时只谈事不谈人，并且把判据落在对方身上——他看的是这个人的反馈回路、他能不能向别人要批评、他能不能改。
   > I give people hardcore feedback, but I try to always focus on the substance of the discussion. I try to criticize the action, not the person. We all make mistakes. What matters is whether a person has a good feedback loop, can seek criticism from others, and can improve.
   > — `corpus/未标年-feedback over feelings.txt`
4. 坏消息大声说、反复说；好消息小声说一次。
   > All bad news should be given loudly and often. Good news can be said quietly and once.
   > — `corpus/未标年-feedback over feelings.txt`

（已有：手册节 5已写"只谈事不谈人""坏消息大声说""Camaraderie is dangerous"；这里补的是两个能当场算的东西——两边的人数，以及要求后面有没有跟着后果。）

**失效边界**：这个算法需要你能说清"整体"是什么。你自己就是全部员工、或者用户只有一个的时候，两边的人数永远是 1 比 1，它退化成自我说服。另一头更硬：他说"想被喜欢是真正的弱点，而我没有这个弱点"——那是他的自我描述，不是给你的目标；这一条不能靠假装不在乎被喜欢来执行，只能靠把要求后面的后果真的接上去。

---

## M26 · 把最难的那部分先拿给人看

**触发**：你在做一个产品，看的人都说好，但你说不清到底哪一块值得投钱。

**他怎么说的**

> We had a little feature: payments through email. When we showed the system to someone, we’d show the hard part first: the conglomeration of financial services. Nobody was interested.
>
> Then we showed people email payments, which were relatively easy to build, and everybody was interested. So, we focused on email payments. That’s what really got PayPal to take off.
> — `corpus/未标年-listen well correct fast.txt`

> It’s important to take feedback from your environment. If we hadn’t responded to what people said, we probably would not have been successful. It’s important to look for things like that, focus on them, and correct your prior assumptions. You want to close those loops as quickly and clearly as possible.
> — `corpus/未标年-listen well correct fast.txt`

**动作**

1. 把手上这套东西拆成能单独演示的几块，其中包括你花力气最多的那一块——他的顺序是先展示最难的那部分。
2. 分块演示，记录现场反应：哪块没人问，哪块所有人都在问。判据是别人的兴趣，不是你的投入。
3. 按反应重新分资源：把力气挪到"所有人都在问"的那一块，哪怕它在技术上最容易（他的选择是邮箱支付——"relatively easy to build"）。
4. 改口要公开说出来，一次就够：
   > I’m trying to create an accurate mental model of reality. If I have a wrong view on something, or if there’s a nuanced improvement that can be made, I say, “I used to think this, which turned out to be wrong—thank goodness I don’t have that wrong belief anymore.”
   > — `corpus/未标年-listen well correct fast.txt`
5. 不要等反馈上门：专门去要负面的，尤其是向朋友要。他对这条的评语是 hardly anyone does it——所以它是个动作，不是一个态度。
   > Pay close attention to negative feedback, and solicit it, particularly from friends. It’s incredibly helpful.
   >
   > This may sound like simple advice, but hardly anyone does it.
   > — `corpus/未标年-listen well correct fast.txt`

**失效边界**：现场反应是信号，不是结论——PayPal 那一场里坐着的是会给钱的真实用户。演示对象不付钱、不承担代价的时候，再热的反应也不构成证据，这时候要先回答"谁付钱"。

---

## M27 · 两个都不明显更好的时候，直接挑一个走

**触发**：你在两个方案之间来回比较，会开了一轮又一轮，两边各有支持者。

**他怎么说的**

> If there were two options, and one wasn’t obviously better than the other, rather than spend time trying to pick which one was slightly better, we would just pick one and go. Sometimes we were wrong and picked the suboptimal path, but at least we moved fast.
> — `corpus/未标年-listen well correct fast.txt`

> Better to pick a path and keep moving than just vacillate endlessly on a decision.
> — `corpus/未标年-listen well correct fast.txt`

**动作**

1. 先过一句判据：这两个里，有没有一个明显更好？没有明显更好的，就停在这里，不要继续比。
2. 直接挑一个往下走，把比较的时间归零。
3. 选错了记在账上，但记在"速度"那一栏，不记在"判断力"那一栏——他给的账目是：有时候我们选错了，走了次优的路，但至少我们动得快。

（已有：手册节 30讲可逆与不可逆——可逆的决定当天做；这里补的是另一类情形：两个都不明显更好的时候，用什么判据停手。）

**失效边界**：这条只管"哪个都不明显更好"。其中一条会锁死你后面的选项、或者撤回成本很高（人、资本、架构）的时候，它不属于这一类，该走可逆与不可逆那一条。还有一件事要先查：如果其中一条的成本高一个量级，那"看不出明显更好"通常说明你掌握的信息不够，而不是两个选项真的相等。

---

## M28 · 缩写要经我批准，才准进词典

**触发**：团队里开始出现自造缩写，新人开会坐着不说话，得先背一本词典才敢开口。

**他怎么说的**

> The key test for an acronym is to ask whether it helps or hurts communication. An acronym that most engineers outside of SpaceX already know, such as GUI (graphical user interface), is fine to use. It is also okay to use a few acronyms or contractions every now and again, assuming I have approved them. For example, we use MVac and M9 instead of Merlin 1C-Vacuum or Merlin 1C-Sea Level. But they need to be kept to a minimum.
> — `corpus/未标年-simple communication.txt`

> I told people the acronyms needed to stop immediately or I would take drastic action. Unless an acronym is approved by me, it should not enter the SpaceX glossary. If there is an existing acronym that cannot reasonably be justified, it should be eliminated.
> — `corpus/未标年-simple communication.txt`

> No one actually remembers all these acronyms, and people don’t want to seem dumb in a meeting, so they just sit there in ignorance.
> — `corpus/未标年-simple communication.txt`

**动作**

1. 定一条准入规则，并且指名一个人做批准的人：不经批准，新缩写进不了团队的词典（他的版本是 CEO 本人）。
2. 逐条过判据：这个缩写是帮沟通还是害沟通。外面的人本来就认识的（GUI）可以留；只有内部人懂的自造词删。
3. 清存量，不要只管新增——词典里讲不出合理理由的条目一律删掉，不因为它用久了就留。
4. 拿会议现场当检查器：新人在会上坐着不说话、只能先背词典才敢开口，就说明还没清干净。

（已有：手册节 7已写"禁掉自造缩写"，以及"新来的人是否需要一本词典"这条判据；这里补的是准入机制——谁批准、旧条目怎么清、哪些例外可以留。）

**失效边界**：例外本来就在规则里（经批准的少数缩写可以留，比如 GUI、MVac、M9），所以"一个缩写都不许有"不是这条。它治的也只是名词：名字统一了、流程本身还是十步，沟通成本一点没降——那时候要动的是流程，不是词典。

---

## M29 · 你要让人相信：有合理的成功机会，而且回报配得上付出

**触发**：你想让人跟你一起干——加入公司、加入项目、押上时间——而你说不出他们凭什么该来。

**他怎么说的**

> To create a company, you have to convince others to join you in your effort. You have to convince them there is a reasonable chance of success and if there is success, the reward will be commensurate with the effort.
> — `corpus/未标年-a group with a goal.txt`

> When starting a company, create a demonstration, a mock-up, or a sketch. This helps people envision it. Try to get to that point as soon as possible, then iterate to make it as real as possible as fast as possible.
> — `corpus/未标年-a group with a goal.txt`

> Anything can look good on PowerPoint. If you have an actual demonstration, even in primitive form, it is much more effective in convincing people.
> — `corpus/未标年-a group with a goal.txt`

**动作**

1. 把说服拆成两句必须说出来的话：有合理的成功机会；如果成了，回报和付出相称。两句都给不出，就先别招人——你手上还不是一个可加入的东西。
2. 做那个最低保真的可见形态：草图、模型、演示件都算，目标是尽快让别人的脑子里出现画面。
3. 尽快把它变成实物，哪怕粗。判据是两条硬的：能摸到的东西比 PowerPoint 有效；纸上算得再清楚也不算。
   > It doesn’t sink in for people until you actually have a physical object they can use. Even when you can show something works on paper, and the calculations are clear, it’s not the same.
   > — `corpus/未标年-a group with a goal.txt`
4. 优先级放在"尽快"上：先到能演示的那一点，再迭代到真实——他的句式是 as soon as possible，然后 as fast as possible。

（已有：手册节 32已讲"原型先于一切"；这里补的是说服的两个条件句，和草图／模型这一级的阶梯起点。）

**失效边界**：原型解决的是"信不信"，不是"值不值钱"。他自己把结论收在那一节最后一句上：没有好价格的好产品，不构成一家好公司——原型做得再快，也替代不了这一关。

已读 10 个文件；跳过 0 个（10 份语料各自都能叠出至少一条技能里没有的动作；与 SKILL.md／playbooks.md 重合的部分已在对应条目内标注「已有 X，这里补的是 Y」，例如：Minimum passing grade is excellent 与 Money is not the constraint 已由手册节 3、节 32覆盖，The people at the front lines 那一句已由手册节 38覆盖，最短路径沟通已由手册节 4覆盖。）

---

## M30 · 时间表会膨胀到填满你给它的那个数

**触发**：你在估一件事要多久，并且准备把这个天数报出去。卡你的不是"这事要多长"，是"你打算把这个数当上限用，还是当一个你自己都不信的催命符"。

**他怎么说的**

> For internal timelines, we set the most aggressive timelines we can. I do this because there’s a kind of “law of gaseous expansion” for schedules. Whatever time you set, it’s not going to be less than that. It’s rare that something will ever get done faster than the schedule.
> — `corpus/未标年-set aggressive timelines.txt`

> When I cite a schedule, it is actually the schedule I think is true. It’s not some fake schedule I made up. It may be delusional—that is entirely possible, and that has happened from time to time. But it’s never some knowingly fake deadline, ever.
> — `corpus/未标年-set aggressive timelines.txt`

> I do have a habit of being optimistic with schedules.
> — `corpus/未标年-set aggressive timelines.txt`

**动作**

1. 写下你**真信**的那个最短工期。不许写一个你为了逼人而编的假数——他给自己的规矩是：会错是因为乐观，不是因为骗，从没有一个明知假的截止日期。
2. 按气体膨胀定律用它：不管你填几天，实际都不会少于那几天。所以填进去的天数就是上限——把它设成你信的下限，不要设成你的期望。
3. 日期看着不可能达到时，照样立出去，并把这个日期的用途说清：它是对内、对供应商的约束，不是对外的承诺。
   > I want to emphasize that some dates are not dates that will actually be met. For example, the initial release date for the Model 3 at Tesla was an impossible date because there are seven thousand unique components in the Model 3, and our deadline assumed all of them would arrive on time. That won’t happen. But, it was a date for us to hold ourselves (internally) and our suppliers to.
4. 指数增长的那一段单独标出来，不要按线性折算：日历上挪一两个月，结果的百分比差异是巨大的——小时差、大结果差。
5. 记住时间表上每一格都是不可回收成本：钱和设备的损失可以承受，时间不行。
   > I often tell the Tesla team: “It’s okay to scrap equipment or money. It’s not okay to scrap time.”

**失效边界**：这是内部工具。对外报出去的日期就是承诺，而他自己的时间表系统性偏乐观（他本人认过，见上引）。另外，压时间表能压掉的是浪费，不是孕育期：当瓶颈是一段物理上不可压缩的过程（培育、审批、外部排期），把日期往短里设只会让你更晚知道坏消息，不会让它更早发生。

---

## M31 · 如果一条时间表很长，那它就是错的

**触发**：你手上有一条时间表，觉得太长了；或者你在排计划，把一堆事排成了"这个完了再开始那个"的一串。

**他怎么说的**

> The one thing you cannot replace is time.
> — `corpus/未标年-do things in parallel.txt`

> Avoid serialized dependencies. A lot of things have a “gestation period” and there is nothing you can do to accelerate it. If you can have all those things gestating in parallel, that will substantially accelerate your overall timeline. People tend to serialize too much. Put as many gestating elements in parallel as possible.
> — `corpus/未标年-do things in parallel.txt`

**动作**

1. 把计划里所有元素列出来，逐个标一句：它有没有孕育期？（建关系、等审批、招人培养、外部排期——那段你压不动、只能等它长的时间。）
2. 对每个带孕育期的元素问一句：它必须等前一个完成才能开始吗？不是的，今天就把它点着，让它在后台自己长。
3. 算两个总时长：串行总和（把各段孕育期相加）和并行总时长（取最长的那一个）。两个数差多少，就是你靠"排队"白扔掉的时间。
4. 反过来用它当筛子查任何时间表：表越长，越说明里面还有能并行而没并行的东西——"长"本身就是"错"的信号。
   > If a timeline is long, it’s wrong.

**叠加说明**：手册《速度即攻防》（三十六）已讲串行依赖与最长链；这里补的是**"孕育期"这个概念**——识别哪些环节压不动、只能并行——以及"时间长＝错"这条回溯判据。

**失效边界**：并行有代价。同时推进的线超过你真正推得动的数量时，每条都变成半成品，总时长反而变长。而且有些依赖是真串行的（物理上必须先有 A 才能做 B，比如先有发动机才能试飞），硬把它们"并行"是演戏。

---

## M32 · 读书的带宽比听人讲话大得多

**触发**：你要进一个新领域，第一反应是去听讲、看视频、找个人带你——通道选错了，后面全慢。

**他怎么说的**

> the data rate of reading is much greater than when somebody is speaking. What’s the output rate of speech? A couple hundred bits per second, maybe a few thousand per second if you’re going full tilt. You can get several times that by reading. The main reason I didn’t go to lectures in college was because the data rate was too slow.
> — `corpus/未标年-aspire to be less wrong.txt`

**动作**

1. 给你手里的每个信息通道各估一个数据率：一个人讲话约每秒几百比特（全力讲也就几千），阅读是它的数倍。
2. 按数据率排序，先走带宽最大的通道——先读，再找人问，听放最后。
3. 读的时候不许从头读到尾：读几段就判断感不感兴趣，不感兴趣直接跳下一条。
   > I’d recommend everyone read or skim through the condensed version of the Encyclopedia Britannica. You can always skip subjects. If you read a few paragraphs and know you’re not interested, just jump to the next one.
4. 先用一次广撒网把地图拉出来（至少拿到"这片知识长什么样"的粗略地形），再回头挑真正感兴趣的那块深挖——你得先有张全局图，才可能知道自己对哪块真感兴趣。
5. 不要求先有背景。他自学火箭的动作就两条腿：读书 + 找人问。
   > Diving into SpaceX and Tesla, I had to learn how to make hardware. I’d never seen a CNC machine or laid out carbon fiber. I didn’t know any of those things, but if you read books and talk to experts, you can pick them up quickly.
   > I started going to the Palo Alto public library to read about rocket engineering and started calling experts, asking to borrow their old engine manuals.

**失效边界**：数据率高不等于理解率高。手感、判断、隐含知识不在书里，只能在动手或对谈里得到——把"读得快"当成"学得快"，会在需要经验的领域踩空。另外，那几个数据率是他自己的估数，不是测量值。

---

## M33 · 感觉太顺、或者说不通，那多半是愿望思维

**触发**：你手里有一条推得很顺的结论，或者正在做一个"感觉挺容易"的计划。

**他怎么说的**

> Do you have the right fundamental axioms, or truths? Are they relevant? Are you making the right conclusions based on those truths? That’s the essence of critical thinking, and yet it is amazing how often people fail to do that. Wishful thinking is innate in the human brain. You want things to be the way you wish them to be, so you tend to filter out information you shouldn’t.
> — `corpus/未标年-obsess over truth.txt`

> If something ever feels too easy or doesn’t quite make sense…it is probably wishful thinking.
> — `corpus/未标年-obsess over truth.txt`

**动作**

1. 把结论拆成三步来查：① 它底层的公理（你当成"真的"的那几条）是不是真的；② 这些公理跟当前这个问题相不相关；③ 结论是不是真从这些公理推出来的。
2. 三问里任何一问答"不"，整条结论作废，回到公理重来——不要在原来的结论上修修补补。
3. 装一个廉价触发器：只要某个计划"感觉太容易"或者"哪里说不通"，先假定那是愿望思维，然后专门去找被自己过滤掉的那部分信息。
4. 配套把默认偏差往回调一格：即使看起来要赢，也先假设自己在输。
   > That’s why I always assume we’re losing, even when it looks like we might win.

**叠加说明**：手册《愿望思维》（二十九）已讲过滤器与合取概率；这里补的是**"公理三问"这条对推理链本身的结构检查**，以及"感觉太顺"这个触发器。

**失效边界**：三问能查推理结构，查不出你压根没列上来的那条公理——你不知道它存在，就写不出它。缺的那条只能靠外部视角或实测补上。所以这条不是"多想一会儿"的替代品，它只保证你不把已有的材料用错。

---

## M34 · 照着做像个滑稽漫画，那这条规矩就该改

**触发**：你按一条明文规定在做事，做的时候自己都知道这事看着不对，但流程就是这么写的。

**他怎么说的**

> In general, always pick common sense as your guide. If following a “company rule” is obviously ridiculous in a particular situation, such that it would make for a great Dilbert cartoon, then the rule should change.
> — `corpus/未标年-simplicity wins.txt`

**动作**

1. 把这条规则放进当前这个具体情形里跑一遍，只看一件事：照做的结果像什么。
2. 判据：如果照做明显荒谬到"能画成一格滑稽漫画"，问题不在执行、在这条规则——改规则，不是改员工。
3. 改的时候，拿本行业的常识当基准，不拿规则当基准：规则是为某个当时的情形定的，常识是当下这一刻的现场。
4. 把同一个问句下到每个环节上——他蹲在电池产线上三个月做的就是这件事：
   > For three months I was at the gigafactory trying to help fix battery production. It’s a lot of little things. I look at every tiny part of each process and ask, “Is this process necessary?”

**失效边界**：常识是"某个行业、某个人的常识"。在你还不懂行的领域，荒谬感可能来自你的无知，不来自规则——这时该先补齐那张知识树，再动规则。另外，规则常常是为一个你看不见的风险定的，删之前要能说出它当初防的是什么、并追到那个提出的人。

---

## M35 · 没有清理职能，规则只会逐年累积

**触发**：你发现自己（或你的组织）每隔一段时间就新增一条规则、一段流程、一道审批，却从来没有拿掉过任何一条。

**他怎么说的**

> Regulators and legislators create new rules and regulations every year, but don’t put any effort into removing them.
> — `corpus/未标年-regulation accumulation.txt`

> Without a cleansing function for rules and regulations, they accumulate every year. This is a problem.
> — `corpus/未标年-regulation accumulation.txt`

**动作**

1. 先接受默认状态：规则系统的设计里没有"删除"，只增不减。所以每加一条新的，先默认有一堆旧的该被拿掉。
2. 指定一个清理职能——谁负责定期删除规则、流程、审批，而不只是负责新增。没有这个常设职能，"清理"永远排在"新增"后面，等于没有。
3. 用一条判据看系统是不是已经堵死：出现"往左也违法、往右也违法"——所有选项都被规则占掉，人动不了。
   > You get into these Orwellian situations where going left is illegal and going right is illegal. There isn’t anything you can do that is legal.
4. 你自己要反对一条规则时，只用一个门槛：这条本意好的规则，实际没产生好结果。给不出这个理由就不反对——他的合规覆盖是"一亿条里反对五条"。

**叠加说明**：原则《质疑要求》已讲"要求必须追到人""每条追不到人的按不存在处理"；这里补的是把删除做成一个**常设职能**（谁来做这件事），以及"两头都违法"这条堵死判据。

**失效边界**：这套东西只能在"你已经完全合规"的前提下用——先合规、再申诉、最后才谈改，跳过前两步去"清理规则"是在找死。而且规则的堆积是政治问题，不是工程问题；他能算清自己那"一亿比五"的比例，但没给出让一个政治系统内生出清理职能的办法。

---

## M36 · 睡在大家看得见的地方，别睡会议室

**触发**：危机里你要求团队拼命，而你自己也在拼——但没人看得见你。

**他怎么说的**

> If there was a crisis situation, I slept on the floor. Most of the time I did not sleep in a conference room because people could not see me in the conference room—I slept on the floor in the factory. Otherwise how would people know? They wouldn’t. Seeing is believing. I slept on the floor outside the conference room so they could see I was there.
> — `corpus/未标年-sleep on the factory floor.txt`

**动作**

1. 危机时先把"你在哪"当成一个信息问题，而不是舒适问题：团队能不能看见你？
2. 选位置的标准是可见性，不是安静度——他睡车间地板、睡会议室门外，就是不睡会议室里，因为会议室里没人看得见。
3. 把你的付出做成别人能撞见的：凌晨四点倒在车间、几小时后在同一层醒来。团队看见的不是苦，是"CEO 都肯吃这个苦，我也能"。
   > When the team is being asked to work super hard, I have to be right there with them and they have to see it. If I fall asleep in the middle of the factory floor at four in the morning and wake up four hours later, they see that. They are like, “If the CEO is willing to take that level of pain, I can do it too.”
4. 反过来做一次检查：你要求别人做的每一件难事，你自己在场吗、可见吗？不可见的付出会被打折，等于没付。

**叠加说明**：手册《一线领导与责任》（二十五）已讲"要到现场""他得看见你在"；这里补的是把**可见性本身当成一个可设计的变量**——连睡在哪，都按"能不能被看见"来选。

**失效边界**：可见性放大的只是"你在受苦"这件事。团队本来就不认同这件事该做，你睡得再显眼也没用，会被读成表演。而且这条正是他被批评最狠的地方——一百小时周有真实的人在付代价，他自己都劝人别学。

---

## M37 · 重大新技术，三次大迭代才算真好用

**触发**：你在给一项全新的技术排时间、编预算，默认它会一次做成。

**他怎么说的**

> It generally takes three major iterations of any major new technology to have it work really, really well.
> — `corpus/未标年-give people more for less.txt`

> One way to look at technology is like rendering an image in successive levels of detail. The first layer of the image is very blurry and things are out of place. Then with the next pass, it gets a bit more defined and things start to shift into place. And you do another pass and another pass, and eventually it’s refined and actually works.
> — `corpus/未标年-give people more for less.txt`

**动作**

1. 排计划和预算时，按三次大迭代来估，不是一次到位——他给的经验值是：重大新技术一般要三次大迭代才好用。
2. 每一版的任务不同：第一版只求把技术跑通，后面每一版才谈优化。
   > In the early days of cell phones, laptops, and gasoline cars, they were considered toys for rich people. You need to go through this phase of having an expensive car available to few in order to build the low-cost car available to many. The first version is simply about making the new technology work. Then, you work to optimize.
3. 先定位你现在在第几版：如果还在第一版，就不要拿规模、成本、良率去考核它——那些是二、三版的问题。
4. 用渲染的比喻校准预期：第一遍就是又糊又错位，每再扫一遍才有一点东西归位。这是过程，不是失败。

**失效边界**："三次"是他给的经验数，不是定律。不同的技术要的次数不同，有的比三次多，有的根本到不了"好好用"。把这个数当预算的起点，别当承诺或保证。

---

## M38 · LEGO 能做到那个精度，车也能

**触发**：你给别人定了一个很高的精度、公差目标，有人（或者你自己）说"做不到"。

**他怎么说的**

> Also, go for extreme levels of precision. One of the examples we use at Tesla is LEGO blocks. LEGO is super precise. The press-fit comes down to a quarter millimeter or less, and each one is exactly the same. LEGO doesn’t work if the press-fit is too soft or too hard. If it’s too soft, the press-and-click won’t stick; if it’s too hard, you can’t get it on. They can make something that is a tiny fraction of a millimeter accurate and it’s a low-cost plastic toy. If LEGO can be that precise, so can a car.
> — `corpus/未标年-give people more for less.txt`

**动作**

1. 别去争论那个精度"能不能做到"，先去找一个便宜的、量产的、公开在卖的东西，它已经做到了这个数。
2. 拿那个东西当存在性证明：一块低成本塑料玩具都能把配合精度做到四分之一毫米以内，那"车做不到"这句话就没有根据。
3. 找到了，目标保留，问题从"能不能"变成"用什么工艺"；找不到，就说明要么目标不成立，要么你真得发明一套新工艺——这两种答案都比空争论值钱。
4. 顺便看清"精度"是两端的约束，不是越高越好的单边参数：LEGO 的配合太松就不咬、太紧就按不上，两头都是失败。

**叠加说明**：原则《极限思维》讲的是"算物理极限、看离它多远"；这里补的是一个具体的取证动作——**用一个便宜的实物当存在性证明**，把"做不到"换成"哪一个已经做到了"。

**失效边界**：找到一个已经做到的东西，只证明它"物理上可行"，不证明"在你要的成本和产能下可行"——LEGO 做得到，因为它只做这一件事、量又足够大。直接拿它当你的成本依据，会低估难度。

---

## M39 · 别人一周五十小时、你干一百，你一年干出两倍

**触发**：你在算"我这队人能不能比对手更早把东西做出来"，而你的唯一优势是愿意多干。

**他怎么说的**

> Do the simple math: Somebody else is working fifty hours a week and you’re working one hundred. You’ll get twice as much done in a year.
> — `corpus/未标年-work like hell.txt`

> If other people are putting in forty-hour workweeks and you’re putting in one hundred, what takes them a year, you will achieve in four months.
> — `corpus/未标年-work like hell.txt`

**动作**

1. 算一个比值：你的周工时 ÷ 对手的周工时。50 对 100 是 2 倍，40 对 100 是 2.5 倍。
2. 把这个比值折算成时间：别人一年的量，你用四个月。拿这个数判断"我能不能在别人之前把它做出来"。
3. 同一张纸上必须写代价那一栏，不能只算收益。他自己给这条定的使用说明是应急、不是常态。
   > I’ve done many many stretches of one-hundred-hour weeks—true one-hundred-hour weeks, sleeping roughly six hours per day. I would not recommend that. That’s for emergencies, not all the time.
4. 自查强度刻度：一年有几天你完全没做有意义的工作？他的答案是"两三天"——这是这条纪律在他身上的量级，你自己定一个自己能承受的数。
   > How many days a year do I not put in some meaningful amount of work? Maybe two or three.

**叠加说明**：原则《硬核节奏》已讲"时间是唯一货币""算每一分钟的价格"；这里补的是另一个算法——**用周工时比换算成时间倍数**（别人一年 vs 我四个月），以及必须同时记的那一栏代价。

**失效边界**：工时比算的是投入，不是产出。它默认两个人每小时产出相同，这在需要判断和创造的工作里不成立——多干两倍不一定多做两倍。而且这是他最受批评的地方：长时间硬核有真实的人在付代价，他公开承认大批人因此离开，并明确说"我不推荐"。
> With that said, I would say this to twenty-something me: I think there’s some merit to not being too intense, and enjoying the moment a bit. Occasionally stopping to smell the roses would probably be a good idea.
> — `corpus/未标年-work like hell.txt`

已读 10 个文件；跳过 1 个（`未标年-seek the nature of the universe.txt`：整章是哲学与信念——"我的哲学基础是我对宇宙本质的好奇""总意识 = 人数 × 人均意识"——语料里没有可执行的动作，按硬规则 3 跳过）

---

# 补料新增（第二轮全语料补料，108 条）

## M40 · “Genetics is just too slow”——选赛道先算一次完整迭代要多久

**触发**：你在两条技术路线或两个赛道之间选，理由都是“前景好”，但两条路的验证周期差一个量级。

**他怎么说的**

> Genetics is just too slow, that’s the problem. For a human to become an adult takes twenty years. We just don’t have that amount of time.

— `corpus/2017-waitbutwhy com 2017 04 neuralink html.txt`

**动作**
1. 给每条候选路线写下“一次完整迭代”要多久——从你做出一个改动，到你能拿到一个可信的结果。
2. 把这个数换算成“在我这段预算/这段时间里，它能跑完几次”。
3. 判据：他拿遗传学当反例，理由是这类事快到头的一次迭代要**二十年**（人到成年）。周期长到这个量级的路线，不管前景多好，都不是他现在能押的——先排除，再谈别的。
4. 在周期可承受的那几条里再比前景和回报。

**失效边界**：这条筛的是“你个人能压注的速度”，不是“这件事该不该做”。基础物理、需要长期随访的医学这类必须长周期的领域不能因此不做，只是不该用“我再快一点”的方式去推它。而且原文这句是他在**解释自己为什么没去搞遗传学**，不是一条普适禁令。

## M41 · 用“自由度”给 AI 排下一关

**触发**：你要判断一个 AI/自动化系统还差多远、下一步会攻下什么，手上只有零散的“它已经能做到 X”这种信息。

**他怎么说的**

> I mean, you’ve got these two things where AlphaGo crushes these human players head-on-head, beats Lee Sedol 4 out of 5 games and now it will beat a human every game all the time, while playing the 50 best players, and beating them always, all the time. You know, that’s like one year later.
>
> And it’s on a harmless thing like AlphaGo right now. But the degrees of freedom at which the AI can win are increasing. So, Go has many more degrees of freedom than Chess, but if you take something like one of the real-time strategy competitive games like League of Legends or Dota 2, that has vastly more degrees of freedom than Go, so it can’t win at that yet. But it will be able to. And then there’s reality, which has the ultimate number of degrees of freedom.

— `corpus/2017-waitbutwhy com 2017 04 neuralink html.txt`

**动作**
1. 把这项系统已经赢下的任务按“自由度”（可选动作的组合数）从低到高排：国际象棋 < 围棋 < 实时策略游戏（Dota 2 / 英雄联盟）< 现实。
2. 在它还没赢、但自由度只高一级的那一档上找下一关——他的例子是：围棋已经拿下，下一个是自由度大得多的实时策略，再下一个是自由度最多的现实。
3. 判据要连时间刻度一起用：围棋从“赢不了顶尖人类”到“每次都能赢前 50 名”，他给的间隔是**一年**。用这个速度去估下一关。
4. 排完看终点：把“打败人类冠军”这类里程碑降级成中途站，不要当终点——现实才是自由度最多的那一关。

**失效边界**：自由度只是难度的一个维度。数据能不能拿到、奖励能不能被定义，同样决定一关攻不攻得下——真机操作、长时序任务、没有明确奖励的任务，自由度不高也可能长期攻不下。

## M42 · “There’s basically a road network to every neuron”——沿现成的路网进去

**触发**：你要把一个东西送进封闭系统（人体、机器、组织、市场）的每一个末端，第一反应是“新开一条通路”。

**他怎么说的**

> “The least invasive way would be something that comes in like a heart stent like through a femoral artery and ultimately unfolds in the vascular system to interface with the neurons. Neurons use a lot of energy, so there’s basically a road network to every neuron.”

— `corpus/2017-waitbutwhy com 2017 04 neuralink html.txt`

**动作**
1. 先问这个系统里有没有已经铺到每个末端的**现成路网**——他给的例子是血管：神经元耗能大，所以每个神经元本来就有一条毛细血管通到（“there’s basically a road network to every neuron”）。
2. 找这条路网的入口，越小越好，从已经存在的开口进（他的版本是股动脉）。
3. 进去之后利用它自己的形态把器件展开到位（unfolds in the vascular system），而不是从外面开个孔插进去。
4. 判据是侵入性：他明确把这条评为 the least invasive way——同样能到终点，选不需要新开孔的那条。

**失效边界**：借现成路网要受它的口径和拓扑限制——能过去的东西大小有限、路径不可控。而且他讲的是这条路径“最少侵入”的性质，不是他已经做成的时间表，这仍是构想。

## M43 · “You’d need a Lasik-like machine”——把不可规模化的手工环节先换成机器

**触发**：方案技术上成立，但每一个单位的交付都要一个稀缺的、训练多年的专家亲手做，于是规模上限从一开始就被这个人数封顶。

**他怎么说的**

> “The machine to accomplish this would need to be something like Lasik, an automated process—because otherwise you just get constrained by the limited number of neural surgeons, and the costs are very high. You’d need a Lasik-like machine ultimately to be able to do this at scale.”

— `corpus/2017-waitbutwhy com 2017 04 neuralink html.txt`

**动作**
1. 在方案里找出“只有专家能做”的那一步。他点名的瓶颈不是手术本身，是**神经外科医生的数量**和随之而来的高成本。
2. 把“这一步由专家手工完成”直接标成方案缺陷：即使技术成功，产能也被这个人数锁死。
3. 把“自动化流程”设成设计目标，而不是后期优化项——他给的样板是 Lasik，一个可自动执行的过程。
4. 判据：没有那台机器，方案里就不该出现 “at scale” 这个词。

**失效边界**：可自动化的前提是这一步的输入可标准化、出错可承受。专家不可替代的场合（判断本身、不可逆的一刀）只能把自动化压到前置准备环节，不能整段替换。

## M44 · “The first use of the technology will be to repair brain injuries”——先修已经坏掉的功能

**触发**：一项新技术要选第一个落地场景，而它远期的想象空间比近期大得多。

**他怎么说的**

> The first use of the technology will be to repair brain injuries as a result of stroke or cutting out a cancer lesion, where somebody’s fundamentally lost a certain cognitive element. It could help with people who are quadriplegics or paraplegics by providing a neural shunt from the motor cortex down to where the muscles are activated. It can help with people who, as they get older, have memory problems and can’t remember the names of their kids, through memory enhancement, which could allow them to function well to a much later time in life—the medically advantageous elements of this for dealing with mental disablement of one kind or another, which of course happens to all of us when we get old enough, are very significant.
>
> We are aiming to bring something to market that helps with certain severe brain injuries (stroke, cancer lesion, congenital) in about four years.

— `corpus/2017-waitbutwhy com 2017 04 neuralink html.txt`

**动作**
1. 把场景按“功能已经丢失、且丢失得最明确”排序——他列的顺序是：中风 / 切除癌灶 / 先天造成的脑损伤 → 四肢瘫、截瘫（从运动皮层到肌肉激活点的神经旁路）→ 老年记忆退化（记不住孩子的名字）。
2. 第一个上市场的选“损伤最确定、收益最可测”的那一档，不选想象空间最大的那一档。他给的承诺是**约四年**做出一件帮助某些严重脑损伤的东西。
3. 让后续增强能力从修复这条线上长出来，不要另起一条：同一台设备先服务失能者。
4. 判据里还有一个隐含条件——这些场景里有现成的患者、现成的临床路径和现成的评估方式，所以“有用”这件事可以被第三方测出来。

**失效边界**：这条是“先做能证明的”，不等于增强类应用不重要，也不保证顺序——他那个四年是乐观的目标。对没有现成需求、只能靠你自己教育市场的技术，这条不适用。

---

## M45 · 《去卫星上试：如果它更好，为什么没人把它装在卫星上》

**触发**：有人（或你自己）在两条技术路线之间争，双方都给得出说得过去的效率、成本、前景论证，而现场没有人拿得出实测数据。

**他怎么说的**

> Cost is bad for fuel cells, but that is only one of many bad dimensions. If fuel cells were in any way better than lithium batteries, they would at least be used in satellites, some of which cost over $500 million. They are not.
— `corpus/2015-waitbutwhy com 2015 06 how tesla will change.txt`

**动作**
1. 找出你那个领域里**成本几乎不构成约束**的应用场景——他找的是卫星（`some of which cost over $500 million`）。
2. 看去卫星上跑的是哪条路线。判据是**它已经用谁**，不是「它的参数理论上更好」。
3. 如果更划算的那条路线在钱几乎不算数的场合都没有被采用，就把「它在等成本下降」这个理由划掉——**在钱不算数的场合都没赢，说明它输的不是钱。**
4. 反过来也一样用：一条路线能在最不在乎钱的场景里存活，说明它至少有个真实的优势维度值得你去查。
**失效边界**：这个检验只对**已经存在很久、且有人真的需要**的技术成立。新技术还没进过这个场景，是因为它太新（没有资历、没有认证、没有供应），不是因为不好——这时它证明的是「还没轮到」，不是「不行」。而且它只反驳一个理由（成本），不反驳其他理由（安全、寿命、认证）。

## M46 · 《两条路线，从头算到轮子，别比单点效率》

**触发**：两条技术路线在某个环节上互有胜负（一边效率高、一边更便宜、一边更快），支持者各拿自己那一段的数据说话，比不出结果。

**他怎么说的**

> If you take electricity coming from a solar panel and charge a battery, you can get ~90% efficiency. Simple and cheap. Instead, if you use that electricity to split water, separate the hydrogen with extreme purity, pressurize it to crazy levels (or, even worse, liquefy), transfer it to a giant (even in liquid form) hydrogen storage tank in the car and then recombine it with oxygen to generate electricity, you would be lucky to get ~20% efficiency. Expensive, complex, bulky and super inefficient. It loses on every dimension, including refuel time when pack swap is factored in.
— `corpus/2015-waitbutwhy com 2015 06 how tesla will change.txt`

**动作**
1. 把两条路线都从**同一个起点**开始画：他是从 `a solar panel` 开始画的，不是从电池或氢罐开始。
2. 把路径上每一步的损耗按顺序列出来、连乘：太阳能→电池是 `~90%`；太阳能→电解水→提纯→加压（或液化）→储运→车载储罐→燃料电池再发电，结果是 `~20%`。
3. 把**没被算进效率的维度**也摊到同一张表上：他是 `Expensive, complex, bulky and super inefficient`，再加上 `refuel time` 这一项。判据不是「哪条效率高」，是**哪条在所有维度上都不输**。
4. 收口用一句二值判断：`It loses on every dimension` —— 如果一条路线在所有维度上都不占优，就不必再谈「各有优劣」，直接砍掉；如果它在某个维度（比如补能时间）能扳回来，那一项必须写进表里再判。
**失效边界**：连乘隐含假设是**每一步独立、损耗可乘**，这在路径里有耦合（余热回收、规模效应、材料复用）时会低估真实值。另外这是**稳态比较**：它算不出学习曲线——一条路线今天 20%、每年稳步爬 5%，和一条已经撞到理论上限的 90%，三年后的答案可能反过来。这条只能用来砍掉「全维度都输」的选项，不能用来给「暂时落后但斜率陡」的选项判死刑。

## M47 · 《查谁在给裁判发工资》

**触发**：你所在的行业里，规则、标准、认证、评价体系明显对在位者有利，而官方口径一切正常。

**他怎么说的**

> You want a situation where it’s truly competitive, where companies aren’t gaming the system, and where the rules are set correctly. We must be on the alert for regulatory capture, where the referees are secretly working for a player. Players should not control the referees, which can happen.
— `corpus/未标年-www elonmuskbook org bonus chapters book of -2.txt`

> Look at the tobacco industry and how long they fought any research and regulation about smoking. That's part of why I helped make the movie, _Thank You For Smoking_. It shows just how pernicious it can be when companies achieve regulatory capture of our government. It’s bad.
— `corpus/未标年-www elonmuskbook org bonus chapters book of -2.txt`

**动作**
1. 列出管着你这个行业的所有「裁判」：监管机构、标准组织、认证机构、行业协会、常被引用的研究机构、仲裁与评级方。
2. 对每一个查它的钱和人从哪来：预算来源、理事名单、旋转门履历、赞助与咨询合同。判据就是他给的定义——**裁判的薪水是不是从一个球员那里流过来的**（`the referees are secretly working for a player`）。
3. 对每一条让你吃亏的规则，往回追它出台时谁在场、谁出钱、谁受益。他给的判例是烟草业对吸烟研究的拖延；他自己还为此参与拍了《Thank You For Smoking》。
4. 结论分两栏写：**规则本身不合理**，还是**规则合理但裁判被占**。这两栏的应对完全不同——前者去改规则，后者先去动那笔钱。
**失效边界**：这条是**诊断工具，不是行动依据**。裁判被俘的举证门槛很高，「我不知道他为什么这么判」和「他被收买了」是两件事；把后者当结论说出来，你要承担的代价通常比你先查清楚要高。另外他这套是在「我已经完全合规」的前提下用的（见 `references/playbooks.md` 节 16）：先把合规做到位，再去动规则。

---

## M48 · 数外包层级：要往下走几层才有人在切金属

**触发**：一个东西的价格远高于它的物理成本，或者你在决定「自己做还是买」。

**他怎么说的**

> They outsource to subcontractors, and then the subcontractors outsource to sub-subcontractors, and so on. You have to go four or five layers down to find somebody actually doing real work—cutting metal, shaping atoms. Every level above that tacks on cost—it’s overhead to the fifth power.

— `corpus/2015-waitbutwhy com 2015 08 how and why spacex wi-2.txt`

**动作**

1. 把这个东西的最终价格画成一条链：从你付钱的那一层开始，逐层往下写供应商，直到写不动为止。
2. 数一条数：**从你到「真正在切金属、塑原子」的那一层，中间隔了几层？** 他给的参照是四到五层。
3. 逐层标注这一层做什么：如果某层不改变物的形态、只做撮合与开票，它的加价就是纯开销。
4. 判据：出现「每层只是加一次价」的结构时，改设计（内化、合并、换供应商），而不是继续谈价。

**失效边界**：只有在「物的形态可以被追溯」的硬件系统里成立。软件、服务、金融这些没有「切金属那一层」的领域，这条数不出东西；另外，层级少也可能意味着你在替别人承担风险，删层之前先确认这一点。

## M49 · 先看合同形式，再看承包商的动机：cost-plus 就是在买延期

**触发**：你要签/评审一份长期外包或服务合同，或者一个供应商永远「快好了」。

**他怎么说的**

> Boeing and Lockheed just want their cost-plus gravy trains. When you’ve had success for too long, you lose the desire to take risks. We can’t get to Mars with that system. They have an incentive to never finish the job.

— `corpus/未标年-rockets from first principles.txt`

**动作**

1. 找出合同的价格公式：是成本加成（实报实销 + 固定比例利润），还是固定价/封顶价。
2. 算一遍激励方向：在这个公式下，**承包商多花钱、多延期，利润是升还是降**。
3. 判据：若利润随成本上升，就不要把「按期完成」写进期望里——先改公式（封顶、里程碑付款、固定价），再谈执行。
4. 附加检查：对方在这件事上成功多久了？他把「成功太久」直接连到「不想冒风险」。

**失效边界**：当工作内容本身就不可预先界定（前沿研发、不确定性极高的科研），cost-plus 是合理的选择——此时不能改公式，只能靠里程碑与独立核查来控制。

## M50 · 进一个新硬领域：读书 → 追问「谁在真正干活」→ 把三十年的人都凑到一个房间 → 出一个默认设计

**触发**：你要进一个自己完全不懂的行业，而且打算自己干。

**他怎么说的**

> I started reading quite a bit about rockets, trying to understand why they’re so friggin’ expensive.

> I looked at the suppliers NASA had been relying on. With suppliers like Boeing and Lockheed, you’re screwed.

> I put together a feasibility study with a team of engineers who were involved in all major launch vehicle developments over the last thirty years. We met over a number of Saturdays in early 2001 to find the smartest way to approach launch cost and reliability, and we came up with a default design.

— `corpus/未标年-rockets from first principles.txt`

**动作**

1. 先读书，但只读一类：**解释「为什么这么贵」的书**，不是这个行业的技术全史。
2. 去问「现在这条链上谁在真正干活」——把供应商名单从头查到「切金属的那一层」，这一步产出的是一张成本结构图，不是技术方案。
3. 组一个小队，标准是**参与过过去三十年该领域几乎所有主要型号的人**（不论他现在在谁家）。
4. 用固定节奏（他用的是一连串周六）开会，任务只有一个：找到成本和可靠性上最聪明的做法。
5. 判据：产出物必须是一个 **default design（默认设计）**——一个具体到可以开始做的基线，不是一份研究报告。
6. 地点检查：搬去这个领域人才密度最高的地方（他选洛杉矶）。

**失效边界**：第一到第四步都需要一个已有三十年历史的行业供你调人；在新出现的领域（没有三十年型号史）这条调不出人，只能靠自己做原型迭代。

## M51 · 把总目标换算成日速率，跟自报的日速率对一次账

**触发**：你或团队提出了一个总量目标（"砍掉一万亿"）和一个日/周节奏。

**他怎么说的**

> Our goal is to reduce the deficit by a trillion dollars. So from a nominal deficit of two trillion, to try to cut the deficit in half to one trillion. Or looked at it in total federal spending to drop the federal spending from seven trillion to six trillion.

> Our goal is to reduce the waste and fraud by $4 billion a day, every day, seven days a week. And so far, we are succeeding.

— `corpus/未标年-singjupost com transcript of elon musk doge .txt`

**动作**

1. 写下总量目标与可用时间：一万亿赤字削减，时间框是 130 天（他自己在同一场访谈里给的期限）。
2. 拿总量除以天数：**一万亿 ÷ 130 ≈ 每天 77 亿**。
3. 把这个数跟他实际自报的日速率比：**40 亿/天**（`$4 billion a day, every day, seven days a week`）。
4. 判据：日速率 × 天数 ≥ 总量，路径才成立；否则要么改总量，要么改天数，要么改速率——**三选一必须显式改一个**，不能靠「大部分工作」这种模糊收尾。

**失效边界**：这个方法只在**支出/削减是连续可加**的量上成立；对不可逆的动作（一次性的关停、裁撤）不能按日速率折算。另外这个数只检验**内部一致性**，不检验口径（他的「浪费」与财政账上的「赤字」不是同一个账本）。

## M52 · 砍之前量两三次，并且事先把错误标准讲清楚

**触发**：你要做一批不可逆或半不可逆的削减，而外界在说你「先开枪再瞄准」。

**他怎么说的**

> Well, I do agree that we actually want to be careful in the cuts, so we want to measure twice, if not thrice, and cut once. And actually, that is our approach. They may characterize it as shooting from the hip, but it is anything but that.

> Which does not say that we don’t make mistakes. If we were to approach this with the standard of making no mistakes at all, that would be like saying someone in baseball has got to bat 1,000. That’s impossible. So when we do make mistakes, we correct them quickly, and we move on.

— `corpus/未标年-singjupost com transcript of elon musk doge .txt`

**动作**

1. 在切之前，对同一条削减做两到三轮独立复核（他的措辞是量两次、不行就量三次），再动手。
2. 动手之前先公开错误标准：**目标不是零错误**（他直接用 1.000 打击率把零错误证伪），而是「错了多快能纠回来」。
3. 预留一条明确的纠错通道，并且规定纠错的代价必须小于不做的代价。
4. 判据：每一条被撤销的削减，都必须能在决策记录里指认出它当时通过的是哪两轮复核、缺了哪条信息——查不出来的，说明前两轮是形式主义。

**失效边界**：这条只适用于**可撤销的削减**。不可逆的削减（关停产线、裁撤岗位、公开指控）不适用「改了就行」——对它们，前两轮复核必须换成不可逆决策的门槛（见 playbooks 三十「可逆与不可逆」）。

## M53 · 从一个物理需求出发造一台新硬件：每台电机都自己设计

**触发**：你要做的硬件，市场上没有任何一家做成了可用的成品，且供应链不存在。

**他怎么说的**

> And its an entirely new supply chain. With Optimus we’ve had to design the whole robot from physics first principles. We’re designing every motor, every gear. The hands are extremely difficult to design. A properly dexterous robot hand is very difficult. One of the hardest things to engineer, and then we can scale production. At first Optimus will do small tasks, and then it will get gradually more sophisticated.

— `corpus/2026-whatsuptesla com 2026 03 01 full transcript .txt`

**动作**

1. 先写清成品必须满足的物理需求（扭矩、精度、能耗），不要从现成零件的参数表往回凑。
2. 逐件自己设计：他做的粒度是**每一台电机、每一个齿轮**——因为买来的零件会把别人的折衷方案固化成你的性能上限。
3. 把最难的那一件单独立项排期：他点名的是**灵巧手**（"One of the hardest things to engineer"）。
4. 排序：先做**有用**（能完成小任务），再逐步提高复杂度，最后才谈规模量产与供应链——他的顺序是 "make it useful, then you have to scale production"。
5. 判据：如果一台机器的关键部件里，有一半以上是你无法说明其参数为何如此的采购件，那这台机器还处在「拼装」阶段，不是你从第一性原理做出来的。

**失效边界**：只有当**供应链不存在或供应商的产品根本达不到你的需求**时，逐件自研才划算；反过来，当他原话里的前提消失（市场上已有可用方案），自己设计每一个齿轮就是浪费——这时要先用 methods M08（看比你强的玩家是自己做还是外购）。

---

## M54 · 存量替换的年限账：存量 ÷ 年产量

**触发**：你要估一个「全面替换」要多久（车队电动化、员工换代、设备更新、平台迁移），或者有人说「只要立刻都换成新的就行」。

**他怎么说的**

> Like there’s a vast base of industry, vast transportation system. Like there’s two and a half billion cars and trucks in the world. And the new car and truck production, (1:22:30) if it was a 100% electric, that’s only about 100 million per year. So, it would take — If you could snap your fingers and instantly turn all cars and trucks electric, it would still take 25 years to change the transport base to electric. It makes sense because how long does a car and truck last before it goes into the junkyard and gets crushed? About 20 to 25 years.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 09 .txt`

**动作**

1. 写下**存量**：世界上（或你系统里）现在有多少台/多少人/多少套在运行。
2. 写下**年新产量**（或年新增人数）——不是「能造多少」，是**实际每年出厂/入职的量**。
3. 算 `存量 ÷ 年产量` = 在最理想条件下、100% 新品都换成目标物的替换年限。
4. 跟**资产寿命**对比：这个年限通常由寿命封顶（他给的数：车 20–25 年）。若 `存量 ÷ 年产量` 远小于寿命，收缩点在「旧的最好也还能用」；若接近或大于寿命，收缩点在**产能**。
5. 用这个数去砍别人的估计：任何「立刻就能全换掉」的说法，先拿这两个数除一下。

**失效边界**：这套算法只对**耐用、只能靠换新来升级**的存量成立。能就地升级的东西（软件、可在旧硬件上迭代的产品、能改造的设备）没有这个年限；存量本身在快速增长的行业里，`存量 ÷ 年产量` 会随时间变化，要每个季度重算。

## M55 · 让历史上有分歧的人达成一致，才允许显示那条更正

**触发**：你要设计一个纠错/评审机制，或者判断一条「更正」可不可信；也可以用来判断自己的评审流程是不是被单方立场污染。

**他怎么说的**

> For a Community Note to be shown, people who have historically disagreed on a subject must agree. That's the magic of it. It makes sense that if people who in the past have disagreed, agree about something, it's probably true.\[154\]
— `corpus/未标年-www elonmuskbook org bonus chapters book of -7.txt`

> Community Notes is fantastic at correcting falsehoods by adding context. We make a point of not removing anything but only adding context. Now, that context could include, ‘This is completely false and here's why.’ No one is immune to this. I'm not immune to it and neither are advertisers.
— `corpus/未标年-www elonmuskbook org bonus chapters book of -7.txt`

> Wikipedia is hierarchical, whereas Community Notes is not. I can't change a Community Note if you put a gun to my head. With Community Notes, all the data and code are one hundred percent open-source. You can completely trace and recreate any note in the system independently. If there was any interference, you'd notice immediately.\[154\]
— `corpus/未标年-www elonmuskbook org bonus chapters book of -7.txt`

**动作**

1. 给每个参与者记一份**历史立场档案**：过去在各类主题上站哪边。
2. 一条更正只有在**历史上立场相反的两组人都同意**时才放行——判据不是「多数票」，是「原本对立的人达成了一致」。
3. 全程**只加语境、不删原文**（他的原话：not removing anything but only adding context）。原文留着，让读者看见「这句话被更正过」。
4. 把数据和代码**全部开源**，让任何外部的人都能独立复现同一条更正——这样「有没有被干预」变成可验证的，而不是可声称的。
5. 用「一条错误更正能存活多久」当质量指标（他给的读数：几天甚至几小时内就被改掉）。
6. 明确写明**没有豁免**——他自己、平台、广告主都在这套之下（见案例：Uber 的广告被标注）。

**失效边界**：这套要求存在**两拨真实存在、且会表达的对立群体**。只有单一立场、或者一方不敢/不能在平台上发言时，「历史分歧者达成一致」退化成同温层的自我确认，比多数票更糟。另外它靠「只加不删」维持可追溯，若前提换成「必须删除违规内容」，这条设计就不适用。

## M56 · 把看不见的危害换算成「波长 → 阈值」再决定怕不怕

**触发**：你（或团队）对一个看不见的危害有模糊的恐惧——辐射、电磁场、某种污染物、某个风险指标——而没有人说得清它到底是什么量。

**他怎么说的**

> The question is what wavelength. If you have a very short wavelength or high frequency photon, that is capable of causing DNA damage. But we're talking about ultraviolet and beyond, cell phones are not even close.
— `corpus/未标年-www elonmuskbook org bonus chapters book of -5.txt`

> The thing that causes problems in a nuclear bomb explosion are particles. The helium nuclei are like tiny cannon balls. Those will rip right through you, like you got shot. Bad things will happen. That's also called radiation, but it's really particles colliding.
— `corpus/未标年-www elonmuskbook org bonus chapters book of -5.txt`

> Cell phones are not emitting particles. Our phones emit photons, but the most they can do is slightly warm up your ear, and only by a tiny amount. If you had a hand warmer that was very mild, that's your phone. That is not going to cause DNA damage, so don't worry about it.\[3\]
— `corpus/未标年-www elonmuskbook org bonus chapters book of -5.txt`

**动作**

1. 先把那个名词拆成**到底是哪种物理量**：是光子，还是粒子？（他把「辐射」一词底下的两件完全不同的东西分开——核爆口里致命的是被加速的粒子，不是光子。）
2. 若确定是光子，**查波长/频率**——DNA 损伤的阈值在紫外及更短，再短才更狠。
3. 把你要评估的源放进这个坐标里，跟阈值比：手机「跟紫外线差得远」，所以不进风险计算；它唯一的效应是「把耳朵略微加热一点」。
4. 只有跨过阈值的那一类，才进入下一步（算概率、写最坏情况）。

（已有 M12：把恐惧翻译成一个可核查的物理定义，例如「暗 = 400–700 纳米内没有光子」。这里补的是**第二步的具体判据**——同一句「辐射」下，先分光子/粒子，再查波长与阈值，比阈值低的不进风险账。）

**失效边界**：这套只在危害**确实由那个物理量决定**时成立。有的风险不由单一阈值决定——剂量累积、长期暴露、多因素协同、生态与制度传导——那些情况下还原成波长/阈值会漏掉真正的机制。另外他自己对核电的判据也不是零风险，是「相对煤电小 100–1000 倍」（见引文），不是「无害」。

---

## [案例]

## M57 · 换完要多少年：存量 ÷ 年产能（再用寿命复核）

**触发**：你在估一件"全世界都换掉"的事要多久；或者有人报了一个转型时间表，你想知道那是物理约束还是政策决心。

**他怎么说的**
> Like there’s a vast base of industry, vast transportation system. Like there’s Two and a half billion cars and trucks in the world. And the new car and truck production, if it was a 100% electric, that’s only about 100 million per year. So, it would take — If you could snap your fingers and instantly turn all cars and trucks electric, it would still take 25 years to change the transport base to electric. It makes sense because how long does a car and truck last before it goes into the junkyard and gets crushed? About 20 to 25 years.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 09 .txt`

> Yeah. I mean, horses were tricky. You know, back when Manhattan had like 300.000 horses, then figure out like if a horse lives 15 years, you got 20,000 horses dropping dead every day or every year, I should say. Every year, it’s 20,000 horses. If there’s 300,000 horses in a 15-year lifespan.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 24 .txt`

— `corpus/2021-elonmuskinterviews wordpress com 2021 02 09 .txt`

**动作**
1. **数存量**：这个系统里有多少台/多少头/多少套在用。他的例：全世界 25 亿辆汽车与卡车；曼哈顿 30 万匹马。
2. **数年新增**：全行业一年能造多少。他的例：即便 100% 电动，也就约 1 亿辆。
3. **算下限**：存量 ÷ 年产能 = 就算今天起全部切换、产能也跟得上，换完要多少年。他的例：25 年。
4. **用寿命复核**：这个系统的自然更换周期是多少。他的例：车 20–25 年报废弃。两个数应当接近；差得远，说明你漏了存量增长或报废速度。
5. **顺手算淘汰侧**：存量 ÷ 寿命 = 每年要处理的淘汰量。他的例：30 万 ÷ 15 年 = 每年 2 万匹死马。

**失效边界**：这只算物理周转。政策可以强制提前报废、补贴可以让产能暴涨、使用强度的变化（共享化）可以改分母——这些都不在式子里。它给的是"换完"的时间，不是"开始起作用"的时间；而且它是用今天的产能算的，产能曲线自己也在动。

## M58 · 自动标注：让算力先猜，人只改错

**触发**：你有一个需要人海标注的数据集，从零标注的人力估出来让你想放弃。

**他怎么说的**
> Auto labeling is essential. Because especially when you got like surround video – to label surround video from scratch is extremely difficult. It takes humans such a long time to even label one video clip, like several hours. Or, to auto label it, we just apply a lot of compute to the video clips to pre-assign and guess what all the things are that are going on in this surround video.
>
> Yeah. And then all the human has to do is like tweak, like say, adjust what is incorrect. This increases productivity by a factor 100 or more.
— `corpus/2022-elonmuskinterviews wordpress com 2022 02 16 .txt`

**动作**
1. **先算从零标注的人力**：他的例是环绕视频——标一个片段要"好几个小时"。
2. **改成模型预标注**：用算力先把标签铺上去，允许它是猜的（pre-assign and guess）。
3. **人只做修正**：把工序从"标注"改成"改错"（tweak / adjust what is incorrect）。
4. **判据按倍数看**：他的参照是**100 倍以上**。达不到，说明预标注错得太多、修正成本把收益吃回去。

**失效边界**：预标注错误率一旦高到要人逐帧核对，修正成本会反超从零标注。它还把成本从人力挪到算力——你得有算力余量。最后一条最隐蔽：模型猜什么、人就标什么，预标注会把系统性偏差直接固化进数据集。

## M59 · 发布时点：先写下「比人好多少才算够」

**触发**：你手上有一个"部分指标已经比现状好、但还不完美"的新东西，放不放出去。

**他怎么说的**
> Vehicle safety is probabilistic. There’s some chance any time a human driver gets in a car that they will have an accident that is their fault. The odds are never zero. The key threshold for autonomy is: How much better does autonomy need to be than a person before you can rely on it?
>
> About a million people die every year in car accidents and about ten million per year have serious injuries. Bringing the day of self-driving sooner translates directly to lives saved and injuries avoided. The sooner, the better. A lot of lives will be saved and made better.
>
> Tesla deployed partial autonomy immediately because when used correctly, it was already significantly safer than a person driving by themself. It would be morally reprehensible to delay release simply for fear of bad press or some mercantile calculation of legal liability.
— `corpus/未标年-the last human drivers.txt`

**动作**
1. **把阈值写成一个问句**：它要比人好多少，你才肯把判断权交给它？——前提是承认分子分母都不为零（The odds are never zero）。
2. **把分母固定成别人能核的数**：他的例是每年约 100 万人死亡、1000 万人重伤。
3. **检查"部分能力"是否已经显著更安全**——他的判据是 when used correctly, it was already significantly safer。
4. **判据是双向的**：已经显著更安全就立刻上，延迟的代价按命算（morally reprehensible to delay）；没有更安全，第 1 步那个问句就过不去。

**失效边界**：只用在"失败可承受、且对比基准是可测的人"的场景。不可回滚的高后果场景（手术、载人飞行）没有"先上再看"这一档。他给的前提必须在场：significantly safer 和 used correctly——误用会把结论整个推翻。

## M60 · 把那个数钉在每次会议的第一张幻灯片上

**触发**：你已经选好了一个记分牌，或者不知道该拿什么当记分牌。

**他怎么说的**
> I told the team I want the latest data on miles per intervention to be the starting slide at each of our meetings. If we’re training AI to drive, what do we optimize? The answer is higher miles between interventions. It is motivating to watch each day as the miles per intervention increases.
— `corpus/未标年-the last human drivers.txt`

**动作**
1. **选一个每天都能读到新值的数**：他的例是"两次干预之间的平均里程"。
2. **把它固定成每场会议的第一页**（the starting slide at each of our meetings）——不是附在报告后面，不是季度汇报一次。
3. **每天记录**，让"它在动"本身可见（It is motivating to watch each day…）。
4. **判据**：这个指标选对没有，看它能不能每天给你一个新数字。

**（已有：手册节 2已写「给一个可计分的单一指标」和那句 Video games without a score are boring；这里补的是把它落成会议纪律——每次会议的第一张幻灯片。）**

**失效边界**：一个数一旦成了会议首页，就会开始被优化成那个数本身。所以它必须是刷不动的物理量（见手册节 39的判据：如果我铁了心刷它，我能怎么刷）。

## M61 · 资产值多少钱：先算它每周被用多少小时

**触发**：你要给一个"自动化/共享化"改造估值，或者判断这笔改造值不值得投。

**他怎么说的**
> An autonomous car is arguably worth five to ten times more than a car that is not autonomous.
>
> This autonomy shift is massive, because you could suddenly have five times the utility of the car you currently have. Say a normal passenger car gets ten to twelve hours a week of usage. An autonomous car could be used fifty to sixty hours a week.
— `corpus/未标年-the last human drivers.txt`

**动作**
1. **算现状利用小时**：他的例是普通乘用车每周 10–12 小时。
2. **算改造后的上限**：他的例是自动驾驶车每周 50–60 小时。
3. **取比值**：约 5 倍使用小时 → 他给的估值倍数是 5–10 倍（"arguably worth five to ten times more"）。
4. **判据**：价值增量按小时算，不按功能条目算。

**失效边界**：小时数能不能上去是需求问题，不是技术问题——共享意愿、停放、保险、分配规则，任何一个卡住，倍数就不成立。他自己的句式也是带前提的（If this is true…）。

## M62 · 换路线之前，先去读对手已经测出来的数

**触发**：一条技术路线要选型，你有偏好，但候选路线里有硬伤。

**他怎么说的**
> I should say the whole reason I switched us from… Raptor, at one point, was going to be a hydrogen engine. But hydrogen has a lot of challenges. It’s very low density, it’s a deep cryogen, so it’s only liquid very close to absolute zero, requires a lot of insulation. So it is a lot of challenges there.
>
> And I was actually reading a bit about Russian rocket engine development. And at least the impression I had was that Soviet Union, Russia and Ukraine, primarily, were actually in the process of switching to methane oxygen. And there are some interesting tests and data for Isp like they were able to get up to a 380 second Isp with the methane oxygen engine, and I was like, wow, okay, that’s actually really impressive. So I think you could actually get a much lower cost… like in optimizing cost per ton to orbit, cost per ton to Mars, I think methane oxygen is the way to go. And I was partly inspired by the Russian work on the test ends with methane oxygen engines.
— `corpus/2022-elonmuskinterviews wordpress com 2022 02 16 .txt`

**动作**
1. **列出候选路线的硬约束，不列好处**。他的例：氢密度很低、是深冷剂（只在接近绝对零度时是液体）、要大量隔热。
2. **去找别人已公开的试验数据**，别只信自己的评估。他的例：苏联/俄/乌在转向甲烷-氧，试验做到约 380 秒 Isp，他的反应是"哇，这确实很能打"。
3. **用最终目标函数选型**。他的目标函数是每吨入轨 / 每吨到火星的成本，不是任何单一指标好看。
4. **承认来源，然后自己复现试验**（his words: I was partly inspired by the Russian work on the test ends）。

**失效边界**：只有一家有数据、且数据无法核实时不成立；另外"别人在转"不等于"别人转成了"——他引的是试验数据，不是路线图或宣传稿。

## M63 · 评预测记录：先补齐样本，再决定怎么判

**触发**：你要评判一份预测记录（别人的或自己的），或者你正被一堆"他明明说错过"的例子围住。

**他怎么说的**
> As far as our predictions are concerned, the media tends to report all the wrong ones and ignore all the correct ones. I’ve had a long career in multiple industries. If you list just my sins, I sound like the worst person on Earth. But if you put those in the context of what I’ve done right, it makes much more sense.
>
> The longer you do anything, the more mistakes you will make, cumulatively. If you sum up just the mistakes, it sounds like I’m the worst predictor ever, which is not the case.
>
> For radical technology predictions, the point is not that it was a few years late, but that it happened at all. That’s the more important part.356
— `corpus/未标年-set aggressive timelines.txt`

**动作**
1. **先把样本补齐**：列出全部公开预测，而不是只列被报道的那些——他给的机制是"做得越久，累积的错误越多"，只挑错误当然算出最差的预测者。
2. **每条标一个结果**：发生了 / 没发生 / 还没到时间。
3. **判据用"发生没有"，不用"准时没有"**——他的原话限定在激进的技术预测上：重点不是晚几年，而是到底发生了没有。
4. **把分母写清楚**：做了多少年、总共多少句话，再算命中率。

**失效边界**：这条只对**激进的技术预测**成立，那是他自己的限定。社会、政治、市场类预测没有"物理上终会发生"这个兜底，不能用"迟早会实现"免责。

## M64 · 用守恒律把「不可能」和「代价极大」切开

**触发**：有一族方案都说能绕开某个约束（飞行汽车、磁悬浮飞行、"用磁场抵消重力"）。你想一次性判掉它们。

**他怎么说的**
> There’s a fundamental momentum exchange with the air. So, you must accelerate. There’s like this — There’s a sudden — You have a mass, and you have gravitational acceleration. And mass times — Your mass times gravity must equal the mass of airflow times acceleration of that airflow to have a neutral force. MG=MA
— `corpus/未标年-sonix ai resources full transcript joe rogan.txt`

**动作**
1. **写出守恒量**：要让一个质量悬停，必须有东西被往下推。他点的对象是空气——你要制造动量交换。
2. **写平衡式**：MG = MA。MG 大就掉，MA 大就升，没有第三种。
3. **问一句"多出来的升力从哪来"**：找不到被推走的对象，这一族方案就不成立。
4. **分两档回答，别混**：违反守恒（不可能）／不违反守恒但要付极端代价（他承认强磁场"磁路"原理上可行，代价是"会造成大量破坏"，不如用直升机）。

**（已有：methods M09 讲「先数维度」——城市是三维、道路只建在二维；这里补的是同一次对话里的另一半动作：用守恒律把"能不能"和"代价多大"切开。）**

**失效边界**：它只能否掉"声称绕开了守恒"的说法，否不掉"代价极高但物理上成立"的方案。而且这是他对着闲聊给出的判断，没有量化的破坏半径或成本。


## [案例]

## M65 · 先把地球能拿到的太阳能量算成分数，再决定算力建在哪

**触发**：你在给一个耗电巨大的设施选址（训练集群、工厂、数据中心），而所有人都默认「建在地上」。
**他怎么说的**
> The Earth only receives roughly one or two billionth of the sun’s energy. So if you want to have something that is say a million times more energy than Earth could possibly produce, you must go into space.

> And in space, you’ve got continuous solar. You actually don’t need batteries because it’s always sunny in space. And the solar panels actually become cheaper because you don’t need glass or framing. And the cooling is just radiative.

> So my estimate is that actually the cost of electricity, the cost effectiveness of AI in space will be overwhelmingly better than AI on the ground so far. Long before you exhaust potential energy sources on Earth. Meaning, I think even perhaps in the four or five year time frame, the lowest cost way to do AI compute will be with solar powered AI satellites. So I’d say not more than five years from now.
— `corpus/2025-whatsuptesla com 2025 11 19 full transcript .txt`

**动作**
1. 先算上限：把方案能拿到的能量写成「占太阳总输出的几分之一」。地球的数是**约十亿分之一到二十亿分之一**——这是地面方案的天花板，不是当前利用率。
2. 列出地面方案必须背的每一项约束，逐条标价：土地、并网、**电池储能**、组件封装（玻璃与构架）、**对流/水冷散热**、检修。
3. 把太空方案对同样的清单逐项对比：光照连续（无昼夜，所以**不需要电池**）、无玻璃与构架因此组件更便宜、散热靠辐射。
4. 判据：**每度电的成本**谁低。他给的答案是太空将「压倒性地」更低，时间窗是**四到五年**，而且在那之前地面能源还没被用尽——也就是这不取决于地球能源耗尽。
5. 顺手问一句自己有没有执行这件事的现成能力：他的原话是「这时候有一家太空公司就很方便」。

**失效边界**：这是发电与散热口径的比较，不是全成本口径——发射、在轨维护、辐射环境下的器件寿命都不在这笔账里（他也没算）。数字（十亿分之一、四到五年）是他本人的估数，不是测量值。别拿这条直接去否掉地面方案。

## M66 · 把「用户时长」换成「不后悔的用户分钟」

**触发**：你在用使用时长、DAU、停留时长当增长记分牌，数字在涨但你不确定是不是真的好。
**他怎么说的**
> As we’re measuring sort of the total user minutes, but not just user minutes, unregretted user minutes, which I think that that’s the key figure of merit. For example, TikTok has a very high usage. But I often hear people say: “Well, I spent two hours on TikTok, but I regret those two hours.”
— `corpus/2023-elonmuskinterviews wordpress com 2023 03 17 .txt`

**动作**
1. 保留原来的时长指标（它是可测的），但在它旁边加一列：**用户事后怎么评价这段时间**。
2. 拿一个极端参照做校准——他自己用的是 TikTok：使用量极高，但用户会说「我花了两个小时，可我后悔这两个小时」。
3. 判据写成一句话，然后拿它去问真实用户：**「你用掉的这半小时，你事后觉得是好事吗？」** 只有答案是「是」的那部分时长才计入你的记分牌。
4. 对着这个新数重做优先级：凡是能把「后悔时长」转成「不后悔时长」的改动，排在能把总时长做大的改动前面。

**失效边界**：这条需要一个**能问得到的用户群体**和可收集的事后反馈；纯 B 端、或用户不会回头评价的产品里，「后悔」这一列填不出来。另外它是主观量——不同人会给出不同答案，所以它只能用来**比较自家版本之间的变化**，不能拿来横向排名。（已有：手册节 39讲怎么选记分牌；这里补的是一个具体指标及其校准参照。）

## M67 · 关键团队卡住时，跳过一级去逐个追问，看谁冒出来

**触发**：一个重要团队（发动机、关键模块、产线）做不出来，负责人已经换了还是不行。
**他怎么说的**
> I remember that he spent a couple of months doing what he calls skip-level, which means instead of meeting with his direct reports on the Raptor team, he would meet with the people one level below them. So he would skip a level and meet with them. I just asked them what they’re doing and I drill them with questions and he said, “This is how I figure out who’s going to emerge.”
— `corpus/未标年-lexfridman com walter isaacson transcript.txt`
**标注**：Isaacson 转述。

**动作**
1. 不定新的负责人。先花**几个月**做跳级会：不跟你的直属下级开，跟他们的下一层逐个开。
2. 会上只做一件事：问他在做什么，然后往细节里反复追问（他的说法是 drill them with questions）。
3. 观察谁**不被问乱**、答得直接、答得出机制——Isaacson 记的那个人（Jacob McKenzie）的特点是「答案非常直白，他不慌」。
4. 判据落在**后续产出**上，不是当场表现：他把这个人提上来管 Raptor，之后是「至少一周造一台」。
5. 认领代价：这条要你先承认现任负责人不行，而不是替他把会开了。

**失效边界**：跳级会被当成绕过中层来用，你会同时收到两个损失——中层不再对结果负责，一线开始只说你想听的（手册节 18 / M18 已写这一点）。这里的增量是**用途不同**：不是用来解决问题，是用来**选谁上**；因此它要求你已经在准备换人，而且你必须真的把提拔兑现，否则这几个月只会让所有人学会对你表演。

## M68 · 把「必须专家手工」当不可规模化的证据，然后像 LASIK 一样机器人化

**触发**：你在设计一项要覆盖几百万人（或几百万台）的技术，而流程里有一道必须专家手工完成的环节。
**他怎么说的**
> So it's like LASIK, so if this is done by neurosurgeons, there's no way it can scale to large numbers of people. And it needs to scale to large numbers of people because I think ultimately we want the future repeated, to be determined by a large number of humans.

> It's got to be like LASIK, like if LASIK had to be hand done, done by hand by a person, that wouldn't be great. It's done by a robot. And the ophthalmologist just needs to make sure your head's in my position and then they just press a button and go.
— `corpus/2019-lex fridman 2 2019.txt`

**动作**
1. 把流程拆成步骤，逐条标注「这一步是不是必须由专家现场完成」。
2. 对每一个「是」的步骤算一行数：**按这个速度，一年能覆盖多少人？** 判据不是它的效果好，是它**能不能到几百万**——他的原话是必由神经外科医生做就绝无可能到那个量级。
3. 把那一步的**人类角色降级为把关和按按钮**，把动作交给机器（LASIK 里医生的职责只是确认头的位置，然后按按钮）。
4. 用「人类角色的目标是什么」校准该删什么：如果专家真正要交付的是结果（诊断出病），那任何与结果无关的替代指标都可以让位——他把这条用在医学上时是先问「他到底要交付什么」。
5. 顺手同向做：把整条流程里的传感器与输入通道也过一遍第一性原理（人类只靠视觉完成同一任务 → 你有理由保留雷达/LiDAR 这种「人类不需要的拐杖」吗）。

**失效边界**：医学与人身安全的步骤上，机器人化的门槛是法规与责任，不是技术——把一个必由专家做的步骤交给机器，在很长一段时间里会先撞上合规，不是先撞上产能。另外这条**只适用于要上量的东西**：一次性、定制化、无法复数的流程里，把专家换成机器是纯粹的浪费。（已有：M07、M38 讲「量产难」，这里补的是**用「人类角色的目标」反推该自动化哪一步**这个判据。）

---

## M69 · 设计拖太久，就把设计改掉

**触发**：一个设计／方案已经拖了，团队的默认反应是加人、加班、延工期。
**他怎么说的**
> just taking the general approach of, if a design is taking too long, the design is wrong, and therefore, the design must be modified to accelerate progress. And one of the most fundamental errors made in advanced developments is to stick to a design even when it is very complicated and to not strive to delete parts and processes.
— `corpus/2021-elonmuskinterviews wordpress com 2021 03 21 .txt`
**动作**
1. 先把「拖」当信号处理：问的是这个设计本身有没有问题，而不是先问资源够不够（原文判据：if a design is taking too long, the design is wrong）。
2. 改的方向不是优化，是**删零件、删工序**（to strive to delete parts and processes）——他把「死守一个非常复杂的设计、不去删」点成先进研发的第一大错。
3. 判据：改完之后进度能不能被加速。加速不了，说明删得还不够。
4. 拿他的判例对标：碳纤维方案太慢，直接换成钢，而不是把碳纤维做快。
**失效边界**：不适用于瓶颈是物理上不可压缩的孕育期（M31：审批、培育、外部排期）——那里拖不是设计的错。安全线与合规线也不在可删清单里（见 M35：先合规，再申诉）。

## M70 · 比两个方案，用「理论值 × 可达效率」而不是理论值

**触发**：两个技术方案在纸面能量／成本上差不多，或者一个在纸面上明显更好。
**他怎么说的**
> So, you actually want to say, ‚what is the actual achievable combustion efficiency times the theoretical chemical energy?‘ That’s the real number, and this is where methane starts to look really good.
— `corpus/2021-elonmuskinterviews wordpress com 2021 03 21 .txt`
**动作**
1. 把两个方案的理论值并排列出来（他举的是煤油与甲烷的理论化学能）。
2. 各自乘上**实际可达的效率**——不是最优工况，是你真能稳定拿到的那个数（他给的是：煤油很难过 96%，甚至 95%；甲烷轻松 98、稍努力 99）。
3. 用乘积比高低（原文：what is the actual achievable combustion efficiency times the theoretical chemical energy? That's the real number）。
4. 回头查你手上的宣传数据：如果某个方案的优势只在理论值上成立，那它不是优势。
**失效边界**：可达效率必须是你自己的实测或行内实测值；拿供应商给的最好工况代进去，这条就退化成「谁的 PPT 好看」。两个方案的可达效率都接近上限时，乘积的差别会消失，比较要回到成本与工况。

## M71 · 自动化的验收口径：每英里事故数、四档概率、比人好 200%

**触发**：要证明一个自动化系统（驾驶、机器人、任何替代人的系统）达到「可以不再要人盯着」的标准。
**他怎么说的**
> Die Automation muss also unter Umständen 200 oder 300% sicherer sein als eine Person.
> Vorfälle pro Meile.
> Ja, Todesopfer wären der Faktor, aber es gibt nicht so viele Todesopfer, um in der Größenordnung statistisch relevant zu sein. Aber es gibt genug Verkehrsunfälle; es gibt weit mehr Unfälle als Todesopfer. Sie können also abschätzen, wie hoch die Wahrscheinlichkeit eines Verkehrsunfalls ist. Dann gibt es noch einen weiteren Schritt, nämlich die Wahrscheinlichkeit von Verletzungen. Und die Wahrscheinlichkeit von bleibenden Verletzungen und die Wahrscheinlichkeit von Todesfällen. Und all diese Zahlen müssen viel besser ausfallen als beim nicht autonomen Fahren, um mindestens ca. 200%.
> Wenn Sie ein System haben, das auf oder unter einem menschlichen Zuverlässigkeitsniveau liegt, dann ist eine Fahrerüberwachung sinnvoll. Aber wenn Ihr System um vieles besser und zuverlässiger ist als ein Mensch, dann hilft die Fahrerüberwachung nicht viel.
> Und, wie ich schon sagte: Wenn Sie sich in einem Aufzug befinden, wollen Sie dann wirklich, dass eine beliebige Person mit einem großen Hebel den Aufzug zwischen den Stockwerken bedient? Darauf würde ich nicht vertrauen. Ich hätte lieber die Knöpfe.
— `corpus/2020-elonmuskinterviews wordpress com 2020 12 22 .txt`
**动作**
1. 把单位定成**每英里事故数**（Vorfälle pro Meile），不是事故总数，也不是里程碑条数。
2. 按严重度分四档统计：事故、受伤、永久性受伤、死亡；主指标用事故数——死亡数太少，达不到统计显著（这一点他自己点明了）。
3. 把门槛写死成一个倍数：比人的可靠性高 200%（他给的是 200 或 300%）才谈取消人工监控。
4. 先判断系统在人类可靠性之上还是之下：在之**下**，人工监控才有价值；在之上，监控帮不上忙（他甚至认为人介入会降低安全性）。
5. 拿电梯当参照系：曾经需要司机，自动电梯更安全之后，「让人拿着操纵杆」反而成了风险。
**失效边界**：200–300% 是他给的估数，不是法规值；各辖区门槛不同，替代对象的基线也要自己先测。数据量在事故档上不显著时，这条会把你拖进「永远不够的数据」，此时按下一条用接管样本补。

## M72 · 把每一次人工接管都记成一次错误

**触发**：训练或验收一个自动化系统，需要标注「什么时候它不行」。
**他怎么说的**
> Wenn also jemand den Autopiloten ausschaltet und selbst übernimmt. Man sollte alle Eingaben als Fehler zu betrachten. Wenn der Benutzer aktiv werden musste, stimmt etwas nicht; jede Eingabe ist ein Fehler.
— `corpus/2020-elonmuskinterviews wordpress com 2020 12 22 .txt`
**动作**
1. 把用户／操作员的每一次介入都先当失败样本收进来（原文：jede Eingabe ist ein Fehler）。
2. 分不清「用户本来就想自己开」还是「系统出错」时，先统一按错误处理，同时在功能上把这类接管消掉——他的做法是发布自动变道／自动下匝道／自动过路口，让这类接管不再发生。
3. 反向样本也要：没有接管的那一堆，才是「正确轨迹」的训练集。
4. 进度指标用接管率下降，不用新功能条数。
**失效边界**：接管数据带噪声，不分类就直接学，会把「用户的偏好」学成「系统的对错」。这条要求同时维护场景类别。

## M73 · 补贴随网络价值上升而递减

**触发**：你在花钱买第一批用户，拿不准该给多少、给多久。
**他怎么说的**
> We started off first by offering people twenty dollars if they opened an account and twenty dollars if they referred anyone. Then we dropped it to ten dollars. Then we dropped it to five dollars. As the network got bigger and bigger, the value of the network itself exceeded any sort of carrot that we could offer.
> We probably spent $60 or $70 million in incentives to build that network. That seems like a lot, but it built a very valuable network. The relative cost depends on your scale. That’s a peanut to Google.
— `corpus/未标年-unite and conquer.txt`
**动作**
1. 先按可承受的成本给双边补贴（他起手是开账户 20 美元、推荐一个人再给 20 美元）。
2. 每过一个阶段下调一档（20→10→5 美元），判据是他那句：网络本身的价值会超过你能给的任何胡萝卜。
3. 总预算挂在「这张网值不值这笔钱」上，而不是挂在「这笔钱占现在营收多少」上——他花了 6000–7000 万美元，并折算成「对 Google 是花生米」。
4. 同时查另一栏：如果你的增长靠销售团队、市场副总裁和广告预算，那你买的不是网络效应。
**失效边界**：补贴一停增长就停，说明买的是量、不是网络——这时继续递减只是把问题推迟。他的「花生米」算法依赖规模，小公司照抄会算错。

## M74 · 用老厂当负面清单，去设计新厂

**触发**：你要再建一个厂、再做一次同样的业务，而老的那套里有一堆说不清的蠢动作。
**他怎么说的**
> And then the Shanghai factory, we designed out all of or as much of the foolishness as we could think of that exists at Fremont and Nevada.
> The Model 3 bodyline in Fremont, for example, was only ever meant to do 5,000 cars, Model 3s, a week, and it’s doing 7,000 (40:00) – and with turning off a bunch of unnecessary things that were being done.
— `corpus/2021-elonmuskinterviews wordpress com 2021 06 29 .txt`
**动作**
1. 先把老系统里所有「我们为什么还这么干」的动作列成一页清单——不清算账，只清算动作。
2. 在新系统里逐条设计掉（原文：we designed out all of or as much of the foolishness as we could think of）。
3. 从「关掉不必要在做的动作」开始，不是从买新设备开始（原文：turning off a bunch of unnecessary things that were being done）。
4. 收益按同一产线的产出比读：原设计 5,000 辆/周、实际 7,000 辆/周，同一产线多 40%，同时边际成本下降。
**失效边界**：换址的外部条件会变（他自己补了一句：中国供应商在多数情况下比美国更高效），所以老厂的「蠢」有一部分是当地条件造成的，抄清单前逐条问它在新地方蠢不蠢。没有「下一个厂」的定制业务也用不上这条。

---

## M75 · 把装机容量折成稳定出力：除以 4 到 5

**触发**：有人报给你一个很大的装机数字（光电、风电、算力峰值、带宽），你要判断它能顶多少「全年不停」的出力。

**他怎么说的**
> So China is—I believe Chinese production capacity on solar is 1,500 gigawatts a year, and they’re deploying over 1,000 gigawatts a year of solar. Now, you know, for continuous solar load, you divide that by roughly 4 or 5. Call it around 250 gigawatts of steady-state power paired with batteries.
— `corpus/2026-whatsuptesla com 2026 01 27 transcript elon .txt`

**动作**
1. 先分清你手上这个数是**装机容量**还是**稳定出力**。装机容量是晴天正午的瞬时值，不是全年能靠得住的量。
2. 折稳定出力：除以 4 到 5（他给的是 "divide that by roughly 4 or 5"）。他拿中国的 1,000 吉瓦年装机往下折，得到大约 250 吉瓦稳定出力。
3. 拿这个折后数去和需求比，不要拿装机数去比。他的对照组是美国平均用电 500 吉瓦 —— 折完约等于美国一半。
4. 折的时候把储能算进去：他这句的前半句是 "paired with batteries"，折算的前提是配电池。

**失效边界**：4 到 5 是**带电池的光伏**折出来的系数，跟纬度、天气、季节、储能时长都有关；换到风电、水电、或者不配储能的场景，这个数不成立。它治的是「把标称值当实际值」，不是给你一个通用常数。

## M76 · 先做量级四舍五入：太阳占了 99.8%

**触发**：你在几个能量 / 资源来源之间分配投入，或者有人拿一个小项来对赌大项。

**他怎么说的**
> So the sun is 99.8% of the mass of the solar system. Jupiter is about 0.1%, and everything else is miscellaneous.
— `corpus/2026-whatsuptesla com 2026 01 27 transcript elon .txt`

**动作**
1. 把候选来源的存量或功率列出来，各写一个数。
2. 找出量级差：他的版本是太阳 99.8%、木星约 0.1%、其余是零头。
3. 做一次粗算外推：把小的那个加倍、加三倍、甚至整个烧掉，看最大的那个变不变。他的判据是——**再烧掉三个木星，太阳的能量仍然四舍五入到 100%**。
4. 判据：若一项在四舍五入后仍然占 100%，**停止在其余项上投入优化**，把资源挪到那个主导项（和它上面那层约束）上。
5. 用主导项反推工程方向：既然太阳是 100%，那就把「在太空收太阳」当成长期路线（他给的动作是发射太阳能 AI 卫星）。

**失效边界**：这是**长期、总量**尺度的算账。在短期和局部，小项可以是致命的——电网里 0.1% 的谐波能烧设备，项目里 0.1% 的股权能决定控制权。**量级四舍五入只在你说得清时间尺度和范围时成立**，否则它会让你漏掉那个卡住整体的小数。

## M77 · 判断一条战线还值不值得烧钱

**触发**：你在资助或参与一件长期、烧钱、对手极强的项目，需要决定「加码」还是「退出」。

**他怎么说的**
> My probability assessment of OpenAI being relevant to DeepMind/Google without a dramatic change in execution and resources is 0%. Not 1%. I wish it were otherwise.
> Even raising several hundred million won't be enough. This needs billions per year immediately or forget it.
— `corpus/未标年-www lesswrong com posts 5jjk4cdnj9ta7ugxr op.txt`

**动作**
1. 先把结论写成一个概率，不写形容词。他的写法是 "0%. Not 1%."——**把「不太可能」逼到一个小数点后面的数**，让它可以被检验。
2. 写出这个概率成立的前提：他写的是「执行和资源没有戏剧性变化」（without a dramatic change in execution and resources）。
3. 把要达到的量级算成钱和时间：对手的年度开销 × 你需要的年限 = 你真正要拉到的资金。他的数是**每年几十亿美元，而且必须立刻**。
4. 拿你的实际可动员资金去对那个数。差一个量级 → 概率就往 0 走；差半个量级 → 谈「戏剧性变化」是什么、由谁做。
5. 判据落成一句可执行的话：**要么现在就上到那个量级，要么别上桌**（他自己的话："This needs billions per year immediately or forget it."）。同时保留一句「我希望我错了」——他写完立刻补了 "I really hope I'm wrong."

**失效边界**：这套算法**默认对手的支出可以查到**（他是从公开的论文产量、GPU 数量、招聘规模推出来的）。查不到对手开销时，「每年几十亿」这种数就只能靠猜，那这套算账退化成情绪。另一头：这个判据只用于「必须赢的正面竞争」；对**不必赢、只需要存在**的事（探路、备份、公益研究），0% 的成功率也不构成退出的理由——他自己后来就是对 OpenAI 不满但也没能让它消失。

## M78 · 找到约束后，先问「解除它的最便宜办法」

**触发**：你已经定位到那个卡住整体的约束（算力、产能、人手），正准备按行业惯例去解决它。

**他怎么说的**
> Ok. Let's figure out the least expensive way to ensure compute power is not a constraint
— `corpus/未标年-www lesswrong com posts 5jjk4cdnj9ta7ugxr op.txt`

**动作**
1. 把约束写成一句具体的短缺：不是「算力不够」，是「下个月要多少块 GPU 级的算力」。
2. 不要先问「标准做法是什么」，先问**最便宜的解除办法是什么**——他把这句话当指令写给团队（原文见上面那条引文，句首就是「我们来找出……最便宜的办法」）。
3. 如果这个约束能拆成互不依赖的几条线，就各自去市场上找现成余量、并行推进，不要串着做。（**已有**：`references/methods.md` M10 已把「房子 / 电 / 冷却」这种拆法写成规程；**这里补的是他 2017 年对算力这一项约束给出的同一个动作**，比 Colossus 那次早了七年。）
4. 判据是约束消失而不是方案好看：只要短缺那项不再是瓶颈，手段可以是租、借、临时、甚至丑的。
5. 记下这条指令的成本对账线：当时的背景是那台集群要在一两个月里把 GPU 数量提高十倍 —— **那个数字来自 Ilya Sutskever 的更新邮件，是 Ilya 的话，不是马斯克的话**。

**失效边界**：**便宜方案常常买不到确定性**。他自己的偏好就是「宁要可随时被关掉的便宜口子，不要带义务的稳定合同」（同一批邮件里连着出现）。所以当约束是「安全 / 合规 / 客户数据」这类不可失手的项时，「最便宜」这个问句不适用——那里的正确问句是「最不可撤销的做法是什么」。

## M79 · 治理设计：先算出自己的票数和影响力，再对照最低舒适线

**触发**：你在谈股权、董事会席位、合伙人投票权，双方都在说「控制权」但没有数字。

**他怎么说的**
> At the sixteen person board level, we would have 7/16 votes and I'd have a 25% influence, which is my min comfort level.
— `corpus/未标年-www lesswrong com posts 5jjk4cdnj9ta7ugxr op.txt`

**动作**
1. 把结构写成一个具体的人数：他把目标定成 12 人董事会（他说如果这个董事会真要决定世界的命运，大概更像 16 人）。
2. 数出自己的票数。他的算法是：A 轮四席 + 普通股三席，在 16 人董事会里是 **7/16**。
3. 把票数换成影响力百分比，和一条自定的下限比：他给的数是 **25%**，并且明说这是 "my min comfort level"。
4. 把增减董事的规则一起定死：他给的机制是「增删董事需要除一人之外全体同意」——**用程序把单方面改变结构的门关上**。
5. 判据：低于自己的最低舒适线就不签；高于它，就不要再去追求「绝对控制」这种没法写进章程的词。

**失效边界**：25% 是他一条具体的舒适线，不是普适阈值——它取决于你要保护的是什么（他当时要保护的是 AGI 的控制权，不是回报率）。另一头：**这条在设计阶段有效，在崩盘阶段无效**——同一场谈判里，票数算得再清楚，对方一旦判断你的动机不可信，数字就不再是问题所在。所以这条要配一条更前面的检查：**先确认双方对「权力最终应该落在谁手里」这个前提有共识**。

---

## M80 · 谁赢：数量乘击杀比

**触发**：你要判断一场消耗型的技术冲突（军备、平台、产能）里谁占上风，而两边各有支持者，一方说「我们技术更好」，另一方说「我们量更大」。

**他怎么说的**
> Well I think we probably need to invest in drones, the United States is strong in terms of technology of the items, but, the production rate is low, so, it is a small number of units, relatively speaking, but I think that basically there is a production rate issue with the rate, like if you say how fast can you make drones, imagine there is a Drone conflict. The outcome of that Drone conflict will be based on: How many drones does each side have in that particular skirmish times the kill ratio… so let’s say that the United States would have a set of drones that have a high kill ratio, but then, the other side has far more drones. If you have got a 2 to 1 kill ratio, and the other side has four times as many drones, you are still going to lose.

— `corpus/2025-whatsuptesla com 2025 04 27 elonatwestpointp.txt`

**动作**
1. 把胜负写成一条乘法：**该次交锋中本方可投入的数量 × 击杀比**。两个因子分开取数，不要用「谁技术先进」这种合成印象。
2. 各算一个数，然后**相乘再比**，不比单项。他给的例子里 2 : 1 的击杀比对上 4 : 1 的数量，结果是输。
3. 找出你这边哪个因子低：技术强但产量低 → 问题在**生产率**（原文 production rate issue）；产量大但击杀比低 → 问题在技术。
4. 把这个乘积当成资源分配判据：往能提高乘积的那一侧投，而不是往已经领先的那一侧投。
5. 对「能不能规模化」单独取一份证据：他给美国工业基础的原话是 "It can scale. But it is not currently scaling."——「能扩」和「在扩」是两个状态，别混。

**失效边界**：这条只在**消耗型对抗**里成立——双方都在用可复制的单位互耗。一旦出现非对称的单点决定（一颗核弹、一次斩首、一个排他性标准），乘法链断掉，数量和击杀比都不作数。它也默认击杀比在整场对抗里保持不变；如果一方能改变对手的击杀比（反制手段上线），得重新取数。

## M81 · 火星着陆的验收函数：撞击坑数量保持不变

**触发**：你在给一件高风险的一次性任务定「什么时候可以送人」，而手上只有一堆「测试通过／不通过」的条目，拼不出一个终局判据。

**他怎么说的**
> The first missions to Mars are all about making sure the rocket can land safely. So, the first missions are focused on confirming that we can land without generating more craters on Mars. We want the crater count on Mars to stay constant—no new craters. As long as we don’t increment the crater count on Mars, and we feel confident that future missions are safe for people, then we would send people.

— `corpus/2025-whatsuptesla com 2025 06 22 sandy munro and .txt`

**动作**
1. 先找那个**不可接受的外部后果**，把它变成一个可以被数出来的量。他的量是「火星上的撞击坑数量」——撞出新的坑就等于这次任务失败了。
2. 把这个量设成**单调计数器**：目标不是「增加成功次数」，是「保持某个数不变」。
3. 用「计数不增加」当放行条件：只要还在增加，就不进入下一阶段（在他的场景里是「送人」）；不增加且对后续任务的安全有信心，才放行。
4. 把这条计数规则**公开写进任务目标**（他是在访谈里公开说的），让「不增加」成为不可协商项，而不是成功后追加的评估。
5. 对「信心」这一条另设判据：不要用「测试全过」，用「未来任务对人是安全的」这个可反驳的句子。

**失效边界**：这条只适用于**后果不可逆、且后果可以被计数**的场景（污染、事故、数据损坏、医院感染）。后果不可数的时候（声誉、信任、士气），「保持计数不变」会退化成只盯着能测的那一项。另一头：把计数器设得太宽（只数「大坑」），会让「小失败」积累到不可逆——计数器的粒度本身要单独论证。

## M82 · 先数窗口，再谈计划

**触发**：你在排一件受外部周期限制的事（发射、财报、考试、审批、行业展期），第一反应是画一条连续的时间线。

**他怎么说的**
> You only get to do this every two years, roughly, because Earth and Mars align every 26 months for a launch window. So, you really have a small number of opportunities in our lifetime—maybe 15 or 20.

— `corpus/2025-whatsuptesla com 2025 06 22 sandy munro and .txt`

**动作**
1. 先把连续时间换成**窗口数**：周期多长、一个窗口一次、你这辈子还有几个。他的版本是 26 个月一次、一生大概 15 到 20 次。
2. 数**手上能填满几个窗口**：他把下一窗口的距离说成 18 个月，并据此给出「能不能赶上」的判断（50/50）。
3. 用窗口数当预算：一次失败等于**一个窗口**，不是「晚一点」。所以每个窗口该带几件东西、带什么，按「我只有 N 次机会」来决定（他的数是三到五艘）。
4. 反查依赖：他说要赶上下一个窗口还欠两件事——解决一批技术问题、以及在轨加注燃料。把「欠什么」列出来，作为该窗口能不能守住的直接依据。

**失效边界**：窗口的周期必须是**外部给定、无法压缩**的。内部项目里，「这个季度必须出」往往是人为设的（那就该走 M30 的激进时间表，而不是「只有 N 次机会」的稀缺逻辑）。把人为期限当成物理窗口，会把团队推到无谓的赌桌上。

## M83 · 让犯罪付不起钱：把单次作恶成本从不到一美分抬到八美元

**触发**：你在设计一个开放系统（社区、市场、API、投票）的防滥用机制，默认方案是加审核、加人工、加规则。

**他怎么说的**
> The point of this is to make crime not to pay. Because right now to create a bot on Twitter cost less than a penny. The cost of crime is so cheap, and that’s part of why crime and hateful conduct pays. But if somebody risks losing even eight bucks, it’s too expensive to now have 100,000 fake accounts because they have to spend $800,000 a month as opposed to $800 a month.

— `corpus/2023-elonmuskinterviews wordpress com 2023 01 19 .txt`

> Yes, so if you’re payment verified with blue checkmark, then you will be prioritized.

— `corpus/2023-elonmuskinterviews wordpress com 2023 01 19 .txt`

**动作**
1. 先算**单次作恶的成本**，把它写成一个数。他的基线是「在 Twitter 上造一个机器人账号成本不到一美分」。
2. 算**规模化作恶的成本倍数**：十万个假账号在单次不到一美分时是 800 美元/月；在单次 8 美元时是 80 万美元/月。同一个行为，成本差三个数量级以上——这就是「让犯罪付不起」的全部机制。
3. 加一道**与身份绑定的付费门槛**，让每个单位都被计价。他选的是每月 8 美元（原话：8 美元，相当于很多人一杯拿铁的钱）。
4. 在付费之上**叠第二层认证**：他明说是在「搭车」支付系统的认证机制，并同时用 Apple 的认证（"another layer of security"）。
5. 用**排序**而不是封禁来收割收益：验证用户优先进入搜索、回复与提及，未验证的（机器人、喷子）被压到后面。他的类比是谷歌：第一页足够好，就没人翻到第八页。
6. 收尾时给出**下限值**：这套东西能换到的是「恶意内容的可见度极低」，不是「归零」——他自己说的是「坏东西被推到很下面」，然后「犯罪不再划算，他们就不试了」。

**失效边界**：这条假设作恶者是**成本敏感的**（要规模化、要算 ROI）。对付不为钱、或者由外部资金供养的行为者（国家级行动、一次性破坏），抬高价格不起作用，反而是把「谁是行为者」这个信息拱手让出。另一头：付费门槛会把付不起钱的普通用户一起挡在外面——这笔社会成本要单独记账，不能只算防滥用的收益。

## M84 · 一个数判断通胀还是通缩，并且给出时点

**触发**：你在判断宏观环境往哪走（通胀还是通缩），手上有一堆说法互相矛盾。

**他怎么说的**
> I think actually the only thing that can solve the debt situation is AI and robotics. But it will be more than it might cause. I guess it probably would cause significant deflation because, you know, deflation or inflation is, it’s really the ratio of goods and services produced to the change in the money supply.
>
> So like, if goods and services output increases faster than the money supply, you will have deflation. If goods and services decrease, if real goods and services output increases slower than the money supply, you have inflation. It’s that simple. People are trying to make it more complicated than that, but it’s, it just isn’t.

— `corpus/2025-whatsuptesla com 2025 12 09 elon musk conver.txt`

**动作**
1. 把问题压缩成**两个增速的比值**：实际商品与服务产出的增速，对比货币供应量的增速。
2. 判断方向：产出增速 > 货币增速 → 通缩；产出增速 < 货币增速 → 通胀。不用别的变量。
3. 取两个当前数：他说美国赤字约 2 万亿美元量级、货币供应以这个规模在增；而 AI 到目前为止**还没有**把商品服务产出推到那个速度之上——所以现在是通胀那一侧。
4. 给出切换时点：他的判断是「大概三年内」，产出增速会超过货币增速，随后通缩、「利率归零」、债务问题变小。
5. 把它当可反驳的预测使用：三年后回来对一次账。这正是这条的价值——它给出的是一个**能被证伪的时间点**，而不是一个方向感。

**失效边界**：这个判据是**长期宏观**的，不适用于季度级别，也不能用来指导一个具体资产的价格。它默认「实际产出」这个数是可以被度量的——在一些行业里（服务、软件、免费内容）产出的度量本身争议极大。另外他这段话里明确区分了事实与主张：前半段（比值判据）是他给的推理，后半段（三年）是他自己标为猜测的预测。

## M85 · 投资三步筛：产品、路线、团队

**触发**：你要判断一家公司（或者一个项目／一个内部创业方向）值不值得投时间或钱，手上只有短期价格和一堆故事。

**他怎么说的**
> Well, but I think you can generally say, you know that if it’s long term for a company, then you can say like, well, does that—is that—do you like the products or services of that company and is it likely to—do you like the product roadmap? Do you like—it seems like they make great products and they’re likely to make great products in the future. If that’s the case, then I would say that’s probably a good company to invest in.
>
> And I think you also want to believe in the team. So if you say, well, that’s a talented and hard working team, they make good products today, they seem to be still motivated to make things in the future, then I’d say that’s a good company to invest in. Yeah.
>
> And now that won’t solve for the daily fluctuations which happen and sometimes are pretty extreme, but over time that is the right way to invest in stocks because a company is just a group of people assembled to create products and services.

— `corpus/2025-whatsuptesla com 2025 12 09 elon musk conver.txt`

**动作**
1. 过第一问：**今天的产品／服务**好不好？用你自己的使用体验回答，不用财报。
2. 过第二问：**产品路线**——他们接下来还做得出来好东西吗？（他的原话把 roadmap 单独列了一问。）
3. 过第三问：**团队**——有才华、够拼、而且**看起来还被激励着继续做东西**。注意第三个子项是「未来动机」，不是「过去的功绩」。
4. 三问全过 → 买；买入后接受日常剧烈波动，不再用价格重判。他的收尾句是"don't worry too much about the daily fluctuations"，以及理由：公司就是一群人聚在一起做产品和服务（与 playbooks 节 32同一句判断）。
5. 反向自检：三问里任何一问答不上，就不要用「长期看会好」来补——那是把路线问题替换成了信念问题。

**失效边界**：这套筛子量的是**产品型公司**，量不到结构性的东西——他自己在同一次对话里也承认，看公司要额外看「有没有人能用更便宜的方式替代它」这类因素。对靠牌照、靠资产、靠网络效应的生意，「产品好不好」不是主要变量。另一头：他自己说过很少买股票、没有组合（"I don't really buy stocks"），所以这是他在被追问下给出的一般性判据，不是他的实操。

## M86 · 付款审计三件套：支付代码、备注字段、联系得上收款人

**触发**：你在审一笔持续外流的支出（对下属、外包、代理、供应商），对方总能给出一个听起来正当的用途，而你查不到钱到底去了哪。

**他怎么说的**
> I mean, some of them are very basic efficiencies, like just adding in requirements for federal payments, that any given payment must have an assigned congressional payment code and a comment field with something in it that's more than nothing.
>
> That trivial seeming change, my guess is probably saves $100 billion or even $200 billion a year, because there were massive numbers of payments that were going out with no congressional payment code and with nothing in the comment field, which makes auditing the payments impossible.
>
> So they should have said, why can the Defense Department, or now the Department of War, why can it not pass an audit? It's because the information is not there. It doesn't have the information necessary to pass an audit. It does not exist is the issue.

— `corpus/2025-whatsuptesla com 2025 12 09 elon musk conver.txt`

> You know, we get this thing, saying, “oh, you’ve got to send this thing for whatever. You know, it’d really be, this is going to children in Africa.” And I’m like, “yeah, but then why are the wiring instructions for Deloitte and Touche, Washington, D.C.? Because that’s not Africa.”
>
> So can you please connect us with the recipients of this money in Africa? And then there gets silence. We just want to literally talk to the recipients. That's it.

— `corpus/2025-whatsuptesla com 2025 12 09 elon musk conver.txt`

**动作**
1. **强制两个字段**：每一笔付款必须带一个可归属的科目代码（他的版本是 congressional payment code）＋一个非空的说明字段。目的不是好看，是让「审计成为可能」——他给的理由是原来这两栏为空，"makes auditing the payments impossible"。
2. **用「能不能过审计」当验收**：一个组织过不了审计，他的判断是「不是能力问题，是信息不存在」（"It does not exist is the issue"）。
3. **核对收款方与用途的地理／身份一致性**：说钱给非洲儿童，汇款指令却指向华盛顿某咨询公司——这一步不需要复杂工具，只需要看一眼两栏是否对得上。
4. **要求直接联系收款人**：他的判据动作是「把收款人接进来」；对方给不出联系、只给理由 → 不付。原话是「接不上人，我们就不会打这笔钱」。
5. **预判对方的反应**：他的观察是「你一停掉欺诈性付款，骗子不会来认罪，他们会开始喊你断了穷人救命钱」。所以第二步要预先准备好「我停的是哪一类、依据是哪两个字段」，而不是临场辩解。
6. 收尾动作：**把「救救熊猫」这类不可反驳的善意理由当成风险信号**。他的原话是"who doesn't want to save the baby pandas? They're adorable. But then it turns out no pandas are being saved."——可反驳的判据只有一个：给我看实物（"can you send us a picture of the panda?"）。

**失效边界**：这套东西靠**字段的可归属性和收款人的可接触性**成立，前提是你有权要求对方填写并提供联系方式。对个人对个人的转账、或者对方本身就在法律上匿名（某些捐赠通道），第 4 步做不到。另一头，他自己给这两个字段的效果的定性是"my guess"——1000 亿到 2000 亿美元/年是他标明的估数，不是审计结果，引用时要保留这个标签。

## M87 · 把「两周」压成「到周日下午」

**触发**：有人告诉你某件事需要两周／一个月，你觉得不合理但说不出哪里不合理。

**他怎么说的**
> It turns out that during a meeting, he asked them how long it would take to remove staff cars from the lot and start digging the first hole for the Boring Company tunnel. The answer: two weeks.
>
> Musk asked why, and when he gathered the necessary information, he concluded, "Let's get started today and see what's the biggest hole we can dig between now and Sunday afternoon, running 24 hours a day." Within three hours, the cars were gone and there was a hole in the ground.

— `corpus/2085-www rollingstone com culture culture feature.txt`

**动作**
1. 先问「要多久」，拿到那个数（这里是两周）。
2. **问为什么**，然后**去收集必要信息**——原文的顺序是先问 why、再 gather the necessary information，不是立刻砍数字。
3. 把问题**换一种问法**：不问「要多久才做完」，问「**到某个固定截止点为止，我们能做出的最大量是多少**」。他给的句式是"the biggest hole we can dig between now and Sunday afternoon"。
4. 把强度条件一并写进问题里：24 小时不停。不是要求加班，是把「连续作业」当成这个重定义里的一个参数。
5. 立即开工（"Let's get started today"），不等讨论结束。
6. 用结果对账：三小时内车清完、地上有坑。把「两周」和「三小时」这两个数并排记下来，作为下次估工期的校准。

**失效边界**：这里的「两周」包含的是**许可、协调、行政流程**，不是物理工期——所以压缩掉的是浪费。若那段时间里含真正的孕育期（浇筑养护、审批排期、外部供应商交期、人的培养），按截止点重定义不会让它变快，只会把风险推到后面。另外这条的外部条件是有人能当场拍板动用资源；没有这个授权时，第一步就做不完。

## M88 · 六步科学方法（作者按其原话整理）

**触发**：你要给一个结论做验证，或者要教别人怎么「求真」，手上只有「要科学」这种空话。

**他怎么说的**（原文标明是作者按他的原话整理的版本：*Here's how he defines it for his purposes, in mostly his own words*）
> 1\. Ask a question.
>
> 2\. Gather as much evidence as possible about it.
>
> 3\. Develop axioms based on the evidence, and try to assign a probability of truth to each one.
>
> 4\. Draw a conclusion based on cogency in order to determine: Are these axioms correct, are they relevant, do they necessarily lead to this conclusion, and with what probability? 5. Attempt to disprove the conclusion. Seek refutation from others to further help break your conclusion. 6. If nobody can invalidate your conclusion, then you're probably right, but you're not certainly right.
>
> “That’s the scientific method,” Musk concludes. “It’s really helpful for figuring out the tricky things.”

— `corpus/2085-www rollingstone com culture culture feature.txt`

**动作**
1. 提出问题（写成一个问句）。
2. 收集尽可能多的证据。
3. 从证据里**定出公理，并给每一条标一个为真的概率**——这一步是关键差别：公理不是「对／错」，是带概率的。
4. 推出结论，并同时回答四个问题：这些公理对不对、**相不相关**、是否**必然**推出这个结论、以什么概率。
5. **主动去推翻它**：去找反驳，也请别人来推翻。
6. 判据是「**没人能推翻**」而不是「很多人同意」——而且即使如此，也只能说「很可能是对的」，不能说「确定对」（原文：you're probably right, but you're not certainly right）。
7. 与此配套的诊断句：他给常见的失败模式起名叫**愿望思维**——"They engage in wishful thinking. They ignore counterarguments." 以及那句推理方式的原话："It's true because I said it's true," but not because it's objectively true。用它识别第 3 步有没有被跳过。

**失效边界**：这是一个**整理稿**，不是他的逐字原话（原文自称 in mostly his own words），引用时不能当逐字引用。另一个更实际的边界：第 5 步「怎么算推翻」没有给标准——什么算有效反驳、谁有资格反驳，这条没有答案，所以它容易被做成「找了三个同事来打圆场」。

---

## M89 · 想把噪音压下去，就把作恶成本从「钱」换成「更硬的约束」

**触发**：你的平台／系统被自动化账号、水军、机器人刷了，你现在想靠「提高门槛」解决，但不知道该卡在哪一环。

**他怎么说的**

> The issue is that creating a fake account is just extremely cheap. It’s maybe as a 10th of a penny or some very small amount of money. By sort of charging $8 a month, it raises the cost of a bot or troll by somewhere between a 1,000 or 10,000. But there’s a detail here, which I think is appreciated by very few people, but that’s also very important, which is, it’s not just the money. Because you could say, well, wouldn’t a state actor have $8 million a day to create a million fake accounts? Well, yes, they’ve got the budget. But here’s the problem: they don’t have a million credit cards, and they don’t have a million phones. That’s the actual kicker. There’s no way to overcome that.

> This is why I think that the only way for any social media company to solve this is with a mild paywall – a paywall for prominence. And that people will just default to looking at comments and mentions from those that are verified. And you really won’t see much of the rest. I think it’s the only solution. I cannot think of any other path to having a good system.
— `corpus/2022-elonmuskinterviews wordpress com 2022 11 11 .txt`

**动作**
1. 先算**作恶的边际成本**：造一个假账号花多少。他给的数是「约十分之一美分」。
2. 设计一个收费，把那个成本抬高 **3–4 个数量级**（他的版本是每月 8 美元，抬高 1,000 到 10,000 倍）。
3. 关键一步：**别停在钱上**。问一句「对手真掏不出这笔钱吗」，然后去找那个**钱买不到的硬约束**。他给的判据是：国家行为体有预算，但**「他们没有一百万张信用卡，也没有一百万部手机」——That’s the actual kicker。**
4. 收费同时只买「能不能被推到大家面前」，不买「能不能发言」（即上面那条 freedom of speech / freedom of reach 的切分）。
5. 判据：如果你**想不出第二条路**（他原话 I cannot think of any other path to having a good system），就把它当成唯一解去执行；想得出第二条，先试第二条。

**失效边界**：这套的前提是你的对手是**规模化作业**的（要一次性开几十万个号）。真人、低频、单点的滥用，收费只能让门槛变高，不会让它消失——他后面也补了「这会变贵，他们最终会停手」，讲的是概率下降，不是归零。另外，把「上了信用卡」当成身份真实，等于把可信度外包给支付网络：没有卡、没有手机的人会被整个挡在门外，这是一条真实且未被这条规程处理的代价。

## M90 · 数供应商的层数：数到那个在切金属的人为止，每一层都是被加上去的开销

**触发**：你的采购价高得没有道理，你想知道贵在哪里，而所有人给你的答案都是「行业就这样」。

**他怎么说的**

> Second, there’s a tendency in big aerospace companies to outsource everything. That’s been trendy in many industries, but aerospace has done it to a ridiculous degree. They outsource to subcontractors, and then the subcontractors outsource to sub-subcontractors, and so on. You have to go four or five layers down to find somebody actually doing real work—cutting metal, shaping atoms. Every level above that tacks on cost—it’s overhead to the fifth power. I began to understand why things were so expensive.
— `corpus/未标年-rockets from first principles.txt`

**动作**
1. 拿一个零件，把供给链**从你往上逐层写出来**：你的直接供应商、它的分包商、分包商的分包商……
2. 数到一个**真正在干活的人**为止——他给的判据是动作动词：谁在 cutting metal, shaping atoms。他数出来是**四到五层**。
3. 把这个层数当成成本乘数记账：每一层都在往价格上**贴一层管理费**，他的说法是 `it’s overhead to the fifth power`。
4. 判据：如果切金属的那个人在第四、第五层，那你要么**把层数砍掉**（自研／直采），要么接受每一层都收你一笔。

**失效边界**：层数本身不是罪——当每一层都在做**真实的专业化工作**（特种工艺、认证、危险品资质），砍掉它反而更贵、更危险。这条针对的是**只经手不增值**的转包层（他举的正是 aerospace 把外包做成惯例的那一类）。数的时候要能说清每一层到底做了什么，说不出的一层才算那一层。

## M91 · 想知道最快的做法，就先造一个极限情形，再问「为什么不能是那个」

**触发**：你在删掉／重构一个环节（零件、步骤、传感器），需要判断「这东西真的必要吗」，而团队给你的是既有设计的惯性。

**他怎么说的**

> Again here, we try to think in the limit of physics. The problem with landing legs is they add mass, we have to protect them during reentry, and we have to get a giant rocket from wherever it landed back onto the launch stand. That’s tricky. I was trying to think of the limit. What’s the fastest way to achieve reusability?

> It would be to land on the launch stand. Why not just have it land on the arms of the tower it launches from?
— `corpus/未标年-building the just barely possible.txt`

**动作**
1. 先把被质疑的那个东西的成本**列成条目**——他的例子是着陆腿：① 增加质量，② 再入时得额外保护它，③ 还得把一支巨箭从落点搬回发射台。
2. 把问题从「这个零件要不要」改成**「最快的那条路长什么样」**（his words: What’s the fastest way to achieve reusability?）。
3. 自己先答出那个极限解——**让火箭直接落回发射台**——然后再问一句「为什么不这么做」。
4. 把「为什么不」逐条变成工程问题来解决（不是「这很荒唐」）：既然要落在发射台上，就让塔上的机械臂接住它。判据落在动作上：**接住它的，正是当初把它放进发射环的那对臂。**

**失效边界**：极限解只是**找目标的工具，不是目标本身**——他这条能成立，是因为落回发射台在物理上确实可能，且塔臂的精度也被做出来了。在你没有对面工艺之前，先按极限解下重注会锁死自己。另外，极限化会把成本挪到别处（这里是从火箭挪到地面塔架），算账时必须把新长出来的那一端记上。

## M92 · 消耗战的算账：看数量 × 杀伤比，别看单机性能

**触发**：你在做一件「我们的东西比对手好，但对手量很大」的判断，或者在为一件高性能设备辩护。

**他怎么说的**

> “Well I think we probably need to invest in drones, the United States is strong in terms of technology of the items, but, the production rate is low, so, it is a small number of units, relatively speaking, but I think that basically there is a production rate issue with the rate, like if you say how fast can you make drones, imagine there is a Drone conflict. The outcome of that Drone conflict will be based on: How many drones does each side have in that particular skirmish times the kill ratio… so let’s say that the United States would have a set of drones that have a high kill ratio, but then, the other side has far more drones. If you have got a 2 to 1 kill ratio, and the other side has four times as many drones, you are still going to lose.”
— `corpus/2025-whatsuptesla com 2025 04 27 elonatwestpointp.txt`

**动作**
1. 把一个战局／市场写成两个因子的乘积：**这一场里各方的数量 × 各自的杀伤比**。
2. 把对手的数量优势换算成倍数，和自己的质量优势并排放在一起比。
3. 判据用他自己给的那组数：**你是 2 : 1 的杀伤比，对手是 4 倍的数量——你仍然会输。** 也就是说，数量倍数超过质量倍数时，质量优势不构成胜负保障。
4. 结论落到产能上：如果数量是主导项，就先去解决 **production rate**（他把美国的问题就定成这一条：技术强、产量低），而不是继续提高单件性能。

**失效边界**：这是**消耗型对抗**的算术——双方可以互相消耗、单位可以互换。当质量优势已经跨过一个断层（对方的东西完全打不到你、或者根本造不出来）时，这个乘积式作废，参见「技术差距够大，人多、将好、聪明都不算数」。同样不适用于可以共存、不互相消耗的场景。

## M93 · 只取原始光子计数：拿掉图像后处理，把延迟拿回来

**触发**：你在做实时感知／控制回路，数据在管线里被「先处理得好看一点」再喂给下游。

**他怎么说的**

> High frame rate, low latency, low jitter. One of the things we’re moving towards now is no post-processing of the image through the image signal processor. What happens for almost all cameras is that there’s a lot of post-processing done in order to make pictures look pretty. We don’t care about pictures looking pretty. We just want the data, so we’re moving just raw photon counts.

> The image that the computer sees is actually much more than what you would see if you represented it on a camera. It’s got much more data. And even in very low light conditions, you can see that there’s a small photon count difference between the spot here and the spot there, which means that it can see in the dark incredibly well because it can detect these tiny differences in photon counts, like, much better than you would possibly imagine. And then we also save 13 milliseconds on latency.
— `corpus/2022-elonmuskinterviews wordpress com 2022 01 29 .txt`

**动作**
1. 先把目标定成三个词：**高帧率、低延迟、低抖动**（High frame rate, low latency, low jitter）——不是「画质好」。
2. 找出管线里那段「让图好看」的处理（image signal processor 里的后处理），问一句它服务的是人眼还是下游算法。
3. 判据：**下游不需要好看的图，需要数据**（his words: We don’t care about pictures looking pretty. We just want the data）——那就把那段去掉，直接取原始光子计数。
4. 把这个动作换算成时间：他的版本是**省回 13 毫秒**（八路相机、每路约 1.5–1.6 毫秒），并且强调在暗光下反而看得更好，因为保留了光子的微小计数差。
5. 把整条链路的时间从「光子打到传感器」一直记到「执行器动作」，逐段标注，不只看某一级。

**失效边界**：这是**机器消费数据**的场景。当最终消费者是人眼（相机、显示器、医学影像、审片），后处理是产品的一部分，删掉它换来的延迟没有意义。另外，原始数据的代价是训练与存储全都要重做——他自己说这是 a quite big reset，需要重训整个系统；不算这笔的人会发现省下的延迟被重训吃掉了。

## M94 · 先算抖动，再算延迟：固定延迟可以补偿，抖动不能

**触发**：你在优化一个控制回路的响应时间，团队报给你的指标是「平均延迟」。

**他怎么说的**

> Actually, jitter is more of a challenge than the latency. Latency is like you can anticipate and predict, but if you’ve got a stack-up of things going from the camera to the computer, through then a series of other computers, and finally to an actuator on the car – if you have a stack-up of tolerances, of timing tolerances, then you can have quite a variable latency, which is called jitter. And that makes it hard to anticipate exactly how you should turn the car or accelerate because if you’ve got maybe 150, 200 milliseconds of jitter, then you could be off by about 2.2 seconds. And this could make a big difference.
— `corpus/2022-elonmuskinterviews wordpress com 2022 01 29 .txt`

**动作**
1. 把固定延迟和抖动**拆成两个数**：固定延迟（例如 150 毫秒）可以写进模型、直接补偿掉。
2. 单独量**抖动的幅度**：他举的情形是 150 毫秒延迟外加 0–100 毫秒的抖动——于是实际延迟在 150 到 250 毫秒之间，**中间那 100 毫秒你不知道怎么处理，基本是随机的**。
3. 判据：先把抖动压掉，再谈延迟。他把这句说死了——`getting rid of jitter is extremely important`。
4. 找抖动的来源在**链路里哪一段**：他点出的是从相机到计算机、再穿过一串计算机、最后到执行器的这串**时间公差叠加**（stack-up of timing tolerances）。
5. 把执行侧的控制频率也列进来：他的数是从 10 赫兹提到 100 赫兹，最坏情况延迟从 100 毫秒降到 10 毫秒。

**失效边界**：抖动只有在**回路要预测未来**时才致命（控制、自动驾驶、交易）。一次性的离线任务里，抖动只是排期问题，压它不如压总时长。另外他给的那个「抖动 150–200 毫秒 → 位置可能偏 2.2 秒」是他自己的换算，当量级看待，不要当成可移植的公式。

## M95 · 感知输出必须是矢量空间——那之后控制问题就退化成电子游戏

**触发**：你在做一个「感知 + 决策」的系统，进度一直卡在决策端，你想知道该往哪一端投人。

**他怎么说的**

> It’s a lot of freaking software, man, a lot of smart lines of code. For sure, in order to create an accurate vector space… so like, you’re coming from image space, which is like this flow of photons going to the cameras. And then, since you have this massive bitstream in image space, and then you have to effectively compress a massive bitstream corresponding to photons that knocked off an electron in a camera sensor and turn that bitstream into vector space.

> By vector space, I mean, you’ve got cars and humans and lane lines and curves and traffic lights and that kind of thing. Once you have an accurate vector space, the control problem is similar to that of a video game, like Grand Theft Auto or Cyberpunk. If you have accurate vector space. It’s, the control problem is… I wouldn’t say it’s trivial. It’s not trivial. But it’s not like some insurmountable thing. But having accurate vector space is very difficult.
— `corpus/2022-elonmuskinterviews wordpress com 2022 01 29 .txt`

**动作**
1. 把输入到输出写成两步：**原始比特流 → 矢量空间 → 控制**。矢量空间是他定义的那组东西：车、人、车道线、弯道、红绿灯，每样带位置与运动。
2. 用一句判据决定钱投哪端：**矢量空间准了以后，控制问题「跟电子游戏差不多」**（his words: the control problem is similar to that of a video game）。
3. 所以难点在第一步——把海量比特流压缩成矢量空间。他给的量化说法是：控制问题 not trivial，但 not insurmountable；**难的是拿到准确的矢量空间**。
4. 按这个分配人力：绝大部分投在感知 → 矢量空间的转换，不要在控制逻辑的细枝末节上反复打磨。
5. 顺着这条继续走，他还给了一个方向：把「组装矢量」这一步本身也搬进神经网络，而不是用手写代码拼（他把手写那一段叫 assembling the giant bag of points，并说它已经碰到局部最优）。

**失效边界**：这个分解成立的前提是**环境规则相对完备**（道路系统本来就是按被动光学 + 神经网络设计的）。在规则本身不确定、对手会主动针对你的场景里，「矢量空间准了控制就好办」不成立——控制端的博弈才是主战场。另外他自己也承认这条路难得超出预期（比 he thought it’d be 还难），所以别把「电子游戏」读成「不难」。

## M96 · 验收标准定成「比现状好 N 倍」，不是「等于现状」

**触发**：你要给一个替代人工／替代既有方案的新系统定验收线，大家在争「够不够好」。

**他怎么说的**

> We want a standard that is not just equivalent to a human but much better than the average human. I think it’s got to be at least two or three times higher safety than a human, two or three times lower probability of injury than a human before we would actually say, “Okay, it’s okay to go.” It’s not gonna be equivalent, it’s gonna be much better.
— `corpus/2022-elonmuskinterviews wordpress com 2022 01 29 .txt`

**动作**
1. 先把「够用」换成「等于谁」：他这个场景的基线是 average human，不是「不差于最差的人」。
2. 把线再抬一档，**写成一个倍数**：他给的是**安全性至少 2–3 倍于人、受伤概率至少低 2–3 倍**，而且提前说清判据不是 equivalent。
3. 把这条当成对外沟通的前提：不达倍数不上线，避免「差不多可以了」的滑坡。
4. 配套的信心判据用趋势不用承诺：他看的是**每百万英里的干预次数在快速下降**，用趋势外推达标时间，而不是拍一个日子。

**失效边界**：这条把他的场景（涉及人身安全、公众接受度低）的数直接搬走了。在娱乐、内部工具、个人效率这类场景，2–3 倍是过高的门槛，会把产品永远卡在验证里。另外，把线定高不等于**能证明**达标——他后面自己补了一步「还得向监管证明」，那一步是独立成本，别漏算。

## M97 · 从材料的市场价往上推，得出那个「白痴指数」

**触发**：你要判断一个东西到底贵在哪里，手边只有它的售价和「行业一贯就这么贵」这句解释。

**他怎么说的**

> “What is a rocket made of? Aerospace-grade aluminum alloys, plus some titanium, copper, and carbon fiber. Then I asked, what is the value of those materials on the commodity market? It turned out that the materials cost of a rocket was around two percent of the typical price.”
— `corpus/未标年-innovatorind com first principles part 1.txt`

**动作**
1. 先写出**材料清单**——他列的是航空级铝合金，加上一些钛、铜、碳纤维。清单要写到能查价的粒度。
2. 第二问是**这些材料在大宗商品市场上的价格**（his words: what is the value of those materials on the commodity market?）。
3. 用「材料市场价 ÷ 典型售价」得出那个比值。他算出来的火箭是**百分之二**。
4. 判据：这个比值越小，说明中间夹的东西越多——那就把中间环节（设计、转包层、惯例定价）逐段拿出来问一遍，而不是接受售价。

**失效边界**：材料价是**成本的下限，不是可实现的价格**。他事后补了这句（`but you can’t take a single example and make an entire theory out of it`）——一个 2% 的比值只说明空间大，不说明你能拿到它；能不能拿到要看工艺、产能、认证。把这个比值直接当成定价依据，会得到一个交付不出来的报价。

（已有：手册节 2已用同一次算账讲「白痴指数」的原始出处（魔法棒 / 只有火箭成本的百分之二，源自 `2015-waitbutwhy com 2015 11 the cook and the chef.txt`）。这里补的是**这条推理链本身的四步动作**——材料清单 → 大宗市场价 → 比值 → 回查中间环节——原文来自第三方文章转引他的访谈，条目内已注明出处。同一文件里另有一句 `Physics teaches you to reason from first principles rather than by analogy`，与 `SKILL.md` 已收的「reasoning by analogy」那条是同一件事，不重复收。）

## [案例]

## M98 · 「false dawns」——把「差临门一脚」当成曲线形状问题

**触发**：一个 AI / 自主系统 / 长周期项目的进度一直在涨，但每次都感觉「快好了」，然后卡住；你又说不清是方向错了还是不够努力。

**他怎么说的**

> there are just so many false dawns with self-driving, where you think you’ve got the problem, have a handle on the problem, and then it, nope, turns out, you just hit a ceiling. Because if you were to plot the progress, the progress looks like a log curve. It’s like a series of log curves.
— `corpus/2022-elonmuskinterviews wordpress com 2022 06 23 .txt`

> And you start getting to these, what I call local maxima, where you don’t realize basically how dumb you were. And then it happens again.
— `corpus/2022-elonmuskinterviews wordpress com 2022 06 23 .txt`

**动作**
1. 把进度画成曲线，标出它开始变平、单位投入产出递减的那一个点。
2. 把当前这个点**直接命名为「局部最大值」**，并按他的说法假设你不知道自己当时有多蠢——先默认看不到顶。
3. 问一句：要越过这个平台，是不是必须先解决**另一个大得多的问题**？他在 FSD 上给出的答案是「是」，而且给出了原因：道路网是为生物神经网络和眼睛设计的，所以要让电脑做这件事，就得先解决真实世界的 AI 和视觉。
4. 判据：答案是「是」→ 你要投的不是这一层的优化，是那个底层问题；答案是「不是」→ 继续在曲线上找下一个平台。
5. 报告进度时用「离越过这个平台还差什么」，不要用「预计还差几个月」——他自己在同一段里先说了「我今年确实有信心」，随后又说「也可能一年后我们又坐在这里说，又过了一年」。

**失效边界**：曲线趋平也可能是市场或物理到顶，不是每个平台后面都还有一层。而且这条不给时间——它对「是不是方向对」有用，对「还要多久」没用。

（补位：这条与手册节 29「愿望思维」相关但不同——那条查的是推理，这条查的是**曲线形状**。）

## M99 · 把不可扩展的人工作业改造成「人只当编辑」的飞轮

**触发**：流程里有一道靠人做、且随规模线性增长的工作——标注、审核、录入、判读。

**他怎么说的**

> In the beginning, it was taking several hours to label a 10-second video clip. This is not scalable.
— `corpus/2022-elonmuskinterviews wordpress com 2022 06 23 .txt`

> you have to have surround video, and that surround video has to be primarily automatically labeled with humans just being editors of making slight corrections to the labeling of the video and then feeding back those corrections into the future auto labeler, so you get this flywheel
— `corpus/2022-elonmuskinterviews wordpress com 2022 06 23 .txt`

**动作**
1. 先量这道工序的单位成本。他的判据数字是：给一段 10 秒视频打标签要花几个小时 → 直接判「这不可扩展」。
2. 改上游的**数据形态**，而不是先改这道工序的效率。他做的两件事：把 8 路摄像头同步成同一时刻的一整幅 surround 画面；再给画面加上时间维，变成 surround video。
3. 把人的角色从「生产者」改成「编辑」：自动标注先出一版，人只做小幅修正。
4. 把修正回灌给自动标注器，让它下一轮更准——他用的词是 flywheel，飞轮转起来之后，自动标注器能吃进海量视频并保持高精度。
5. 判据：这道工序的时间/成本随规模上升要接近不涨。

**失效边界**：前提是上游能被标准化成同一种形态（同步、同一时刻、同一批次），做不到这个前提，飞轮转不起来。判断类、不可逆的活也不能交给飞轮——那属于手册节 23里「删错了加不回来」的那一类。

（补位：方法层 M23 讲的是技术管理者要亲手做；这里补的是把**人工环节本身**当成要被替换的瓶颈。）

## M100 · 给一条侵入性流程定「当天进出」的上限

**触发**：你在设计一个需要侵入、停机、或打断用户日常的流程。

**他怎么说的**

> The only way you can achieve the level of precision that is needed is with an advanced robot.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 07 .txt`

> And we feel confident about getting the link procedure, the installation of a link, done in under an hour. So you can basically go in in the morning and leave the hospital in the afternoon. And it can be done without general anesthesia.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 07 .txt`

**动作**
1. 定位那个「精度不够就做不成」的环节。他的判断是：要达到所需精度，唯一的路是用高级机器人——所以自动化不是后期优化项，是这条流程能不能成立的前提。
2. 给整条流程定一个上限，他的版本是「一小时以内」：早上进医院，下午出医院。
3. 把「不需要全身麻醉」写成设计约束，不是可选项。
4. 判据：用户当天的生活不被打断——他不是按手术成功率来定流程，是按「你当天能不能照常回家」来定。

**失效边界**：需要长期观察、多次介入、或术后必须留观的流程不适用。这条买的是体验和产能，代价是前期必须把自动化先做出来——没有那台机器，这个时间上限只是宣传语。

（补位：这条与手册节 23第四、五步（加速要放最后、自动化放最后）方向相反，但**不冲突**：那里的前提是流程本身该不该存在还没查清；这里的前提是流程已被判定必须存在，于是自动化成为前置条件。）

## M101 · 把大数字除到一个你能想象的量上

**触发**：你要人接受（或否决）一个巨大的数——十万亿美元、240 TWh、两千万辆、0.2% 的土地。

**他怎么说的**

> Now, if you look at the total world economy, it’s just under 100 trillion. If this was spread out, say over ten years, it would be 1% of the global economy. Over 20 years, it would be half a percent of global economy. This is not a big number relative to the global economy.
— `corpus/2023-elonmuskinterviews wordpress com 2023 04 28 .txt`

> So that would be a good number because there’s two billion cars and trucks in the world that are in active use. So 20 million would be then 1% of the global fleet per year.
— `corpus/2022-elonmuskinterviews wordpress com 2022 03 23 .txt`

**动作**
1. 选一个对方已经接受的**分母**：全球经济规模、地球陆地面积、在用车辆总数、已耕作土地占比——分母必须是他本来就有直觉的量。
2. 做除法，只报结果。他现场做过的三个：十万亿美元摊到十年 = 全球经济的 1%（摊到二十年是 0.5%）；风电光伏占地 < 0.2%，而今天集约耕作的陆地是 12.5%（差一个数量级以上）；两千万辆/年 = 全球 20 亿辆在用车队的 1%。
3. 判据：除完之后，如果结果小于一个他已经在接受的量（比如一年化石燃料基础设施投资的 60%），那这个「巨大」不构成否决理由。
4. 反向同样用：除完仍然很大的数，才是真障碍。

**失效边界**：分母换一个，结论就会翻——按年摊和按剩余时间摊是两个答案。而且「总量可行」不等于「分配可行」：谁出钱、谁让地、谁承担就业转移，除法都算不出来。这条只解决「量级是否吓人」，不解决「谁来做」。

（补位：手册节 39讲的是「换一个刷不动的记分牌」；这里补的是**归一化**——同一个数换分母。）

## M102 · 故意把假设压到悲观一侧，再把算式公开

**触发**：你在做一个长期估算，结论很大，一定会被质疑乐观。

**他怎么说的**

> And we’re being conservative here. It could be better than a half. But we’re trying to have assumptions that are reasonable and not overly optimistic, in fact, slightly pessimistic.
— `corpus/2023-elonmuskinterviews wordpress com 2023 04 28 .txt`

> I certainly would invite others to check our calculations because they may arrive at different conclusions.
— `corpus/2022-elonmuskinterviews wordpress com 2022 06 23 .txt`

**动作**
1. 把每个关键假设往悲观一侧推一格再算。他的两个实例：能效提升「其实不止省一半」，他仍然只按省一半算；资本开支真算下来约 6 万亿，他主动把它写成 10 万亿。
2. 把白皮书、全部假设、全部算式公开。
3. 明确邀请别人来验算——原话是「我肯定会邀请别人来核对我们的计算，因为他们可能得出不同的结论」。
4. 判据：只有在悲观假设下仍然成立的结论，才拿出去讲。

**失效边界**：刻意悲观会让人低估机会，也会把真正的风险点埋在「反正更坏也成立」里。这条的用途是**说服**，不是**预测**——要预测，该用中位数假设。

（补位：手册节 29讲「合取概率」是把好消息摊开相乘；这条是它的对面——把**每一个假设**单独往坏里推。）

## M103 · 「为什么它还没有发生」——先区分意愿缺失和路径缺失

**触发**：一个领域停滞了几十年，所有人（包括你）都在说「没人愿意做这件事」。

**他怎么说的**

> The original idea for SpaceX wasn’t to create a company. It was to figure out why we hadn’t sent people to Mars. I thought maybe we’d lost the will to explore. I thought we had to create the will to explore. But that was wrong.
— `corpus/未标年-the only one crazy enough for space.txt`

> We have not lost the will to explore; people just did not think there was a way forward. If people don’t think there’s a way, then they won’t continuously bash their head against the wall for progress.
— `corpus/未标年-the only one crazy enough for space.txt`

> Once people realized, “There is a way to do this,” we got a lot of support.
— `corpus/未标年-the only one crazy enough for space.txt`

**动作**
1. 去查**原始计划表**，不听转述。他的动作是：去 NASA 网站找「什么时候去火星」的排期。
2. 看结果的性质，而不只是看时间。他发现那里什么都没有——不是排期一推再推，是**根本没有日期**。
3. 换假设。他的第一版假设是「我们失去了探索的意愿」，他后来判定这版是错的（原话：But that was wrong）；正确版本是「人们只是不认为有路可走」。
4. 判据在两句话里：不认为有路的人不会持续拿头撞墙；而一旦「有路」这件事被人看见，支持自己会来（Once people realized, "There is a way to do this," we got a lot of support.）。
5. 所以你的产出物是**那个可见的路**（他最后给的是一条便宜的常规航线），不是一篇恢复热情的呼吁。

**失效边界**：确实存在真的没有意愿的情形；而且「造路」需要的资源量级是火箭级的，个人与小团队做不到——这时该做的是手册节 40里的另一件事：站到一个需求已经存在、只是还没被满足的位置上。

（补位：手册节 40讲「技术不会自己变好、需求要造」；这里补的是**诊断顺序**——先分清是没意愿还是没路径，再决定去说服还是去造路。）

## M104 · 把「可逆性」写成一场要演出来的测试

**触发**：你在设计一个要植入、长期绑定、或让用户做出承诺的东西，而「以后还能拿掉」只是文档里的一句话。

**他怎么说的**

> This is a very important thing to demonstrate – its reversibility. If you have a Neuralink, and then you decide you don’t want it, or you want to get an upgrade, and the Neuralink is removed, is it removed in such a way that you’re still healthy and happy afterwards? And what Dorothy illustrates is that you can put in the neural link, remove it and be healthy, happy, and indistinguishable from a normal pig.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 07 .txt`

**动作**
1. 把可逆性列成一条**验收项**，写明它的判据：拿掉之后，个体仍然健康、快乐，并且**与没装过的正常个体无法区分**。
2. 真的做一次完整循环再演一次：装进去 → 用一段时间 → 取出来 → 展示状态。他在演示里用三只猪分工完成了这三段（一只没装、一只装过又拆掉、一只带着两个月大的植入物在跑）。
3. 判据不写在纸面规格里，写在现场表现里：他宣布它的方式是「这就是现场演示的美妙之处」——演示失败也是一种数据。
4. 升级路径也要提前想：他说的原话里包含「或者你想升级」这个理由——把换新也算进可逆性里。

**失效边界**：这个测试证明的是「拆得掉」，不证明「拆了没损失」；而且他自己把这个演示的定位说得很清楚——这场发布会的主要目的是招人，不是临床结论。

（补位：方法层 M07 讲改造会作废已有的验证；这里补的是**把可逆性当作一个要跑一遍的测试用例**。）

## M105 · 选材料先算吨位，再谈性能

**触发**：你要为一个要上千万件、上亿吨级的产品选材料（电池化学、结构材料、耗材）。

**他怎么说的**

> The not common materials can’t scale.
— `corpus/2022-elonmuskinterviews wordpress com 2022 03 23 .txt`

> There’s enough lithium ore in the United States to electrify all of Earth. If the United States was the only place producing lithium, there’s enough domestic material to electrify Earth. It’s very common. The limiting factor is the refining of the lithium into battery-grade lithium hydroxide or lithium carbonate. That’s the actual limiting factor.
— `corpus/2023-elonmuskinterviews wordpress com 2023 04 28 .txt`

**动作**
1. 先把需求折算成**吨位**，不是折算成功率指标。他给的量级：要先算「几千万吨」，最终可能「几亿吨」。
2. 判据是一句硬话：这个规模下用的材料**必须是常见材料**，不常见的材料没法规模化。他把石墨烯这类「人人都爱」的材料直接按这个判据放到一边。
3. 落到具体选型上，他是按需求分层配的：铁磷酸和锰做大头（铁是地球上质量占比最高的元素），镍只留给飞机、远洋船和超长途车船。
4. 算完之后还有一个反向检查：美国境内的锂矿就够电气化整个地球，真正的限制因子是**精炼**——也就是说「够不够」和「能不能用上」是两个问题，别把后者当成储量问题。

**失效边界**：常见材料是**规模化**的约束，不是性能约束——在小批量、高性能、不在乎吨位的场景（航天、军工、限量产品），这条不适用，那时该选最优性能而不是最丰产。另外，把「限制因子是精炼」当成结论会漏掉资本与许可这两层。

（补位：这条在 playbooks / methods 里没有对应条目。）

## M106 · 把隔离层加在真正的界面上，而不是把整个环境做成无菌

**触发**：你的工艺里有一个「污染/杂质/噪声」问题，现行做法是把整个环境做到极致干净，代价是所有人都得穿防护服、所有流程都变慢。

**他怎么说的**

> So I think they’re getting clean rooms wrong by the way, in these modern fabs. I’m going to make a bet here.
— `corpus/2026-whatsuptesla com 2026 01 10 elon musk talk w-2.txt`

> They just maintain wafer isolation the entire time, which is actually the default for fabs. The wafers are transported in boxes of pure nitrogen gas under a slight positive—
— `corpus/2026-whatsuptesla com 2026 01 10 elon musk talk w-2.txt`

> Like it’s pretty hard for anything that’s combusting to live without oxygen. Yep. So let’s talk about—so you like, you can kill the bugs just by putting a nitrogen blanket.
— `corpus/2026-whatsuptesla com 2026 01 10 elon musk talk w-2.txt`

**动作**
1. 先问污染真正发生在**哪一个界面**上。他给的判断是：现代晶圆厂把洁净室做错了——它们在把整栋楼做成无菌，而真正要保护的只有晶圆表面。
2. 把隔离加在那一个界面上：晶圆全程装在有轻微正压的纯氮盒子里运输，从头到尾不接触环境。
3. 用物理性质封边：燃烧需要氧气，所以无氧环境本身就抑制了大部分微生物与颗粒问题——他的原话是「氮气毯就能杀死虫子」。
4. 判据是**人那一侧的限制被整段删掉**：他说自己能在那座 2 纳米厂里吃汉堡、抽雪茄，因为要隔离的是晶圆，不是人。

**失效边界**：这条把可靠性全部押在封装上——一旦封装破损，露出来的那一片直接报废。而且要说明白：他自己把这句说成「我下个注」（I'm going to make a bet here），本批语料里**没有**这座厂建成或验证的结果，它是一个公开下注，不是已完成的案例。

（补位：手册节 23第一步讲的是「把要求变得没那么蠢」；这里补的是同一动作在**工艺设计**上的形态——不是改工艺参数，是把被隔离的对象换掉。）
---

## M107 · 用个体实测替换群体统计

**触发**：你在一个用群体统计给个体定价或评分的行业里（保险、信贷、风控、招聘筛选），而你手上有这个个体自己的实时行为数据。
**他怎么说的**
> The car insurance industry is incredibly inefficient because they’ve got all these middlemen, from the insurance agent all the way to the final reinsurer. There are a half dozen companies each taking a cut.
>
> Insurance is driven by statistics, so even if you’re a good driver at twenty years old, it’s extremely expensive. Tesla allows for real-time insurance based on how you actually drive the car. If you drive the car in a safer way, you pay lower insurance. Our insurance is based on how you drive, not how people who fit your demographic have driven historically.
— `corpus/未标年-a whole new kind of car company.txt`
**动作**
1. 写下你现在用的那个类别变量（年龄、邮编、行业、学历、前公司），以及它在替谁做决定。
2. 数一遍这条链上有几个中间环节在各自抽成——他的版本是"从保险代理一直到最后一家再保，有半打公司在各拿一道"。
3. 找出这个产品能拿到的**个体实时行为**（他的例子是"你实际怎么开车"），用它替换类别做定价。
4. 判据：同一份保单，按行为定价和按人群历史定价能给出不同价格，而且用户能通过改变行为改变自己的价格——他给的原话是 based on how you drive, not how people who fit your demographic have driven historically。
**失效边界**：只有行为能被低成本持续测量、且样本量够支撑定价时才成立。低频、不可观测的风险（一次性大额事件、没有遥测的场景）只能退回群体统计。另一头是这条的代价：用行为定价等于把统计歧视换成行为监控，语料里他没处理隐私与公平这一面。

## M108 · 训练眼睛：把「好看／难看」拆到能说出为什么

**触发**：你知道设计重要，但你评价一个东西时只能给出形容词（高级、廉价、土），说不到具体。
**他怎么说的**
> You can train yourself. You can make yourself pay attention to “why.” You can learn to bring subconscious awareness into conscious awareness. Look closely and carefully. Look at each object’s geometry.
>
> If you’re trying to make a perfect product, attention to detail is essential.
— `corpus/未标年-a whole new kind of car company.txt`
**动作**
1. 停止给形容词，先只问一个问题：这个东西为什么让我觉得好看或难看——他给的动作就是 pay attention to "why"。
2. 把答案拆到可核查的层面：几何、形状、比例，以及它在不同的光下是什么样。
3. 每天做一件，并把它写下来——他把这当能力训练：把潜意识里的判断提到意识层。
4. 判据落在两处：你能不能说出具体细节（而不是"整体感觉"）；以及产品层面——他要做完美产品时，注意细节是必要条件。
**失效边界**：他自己说这是双刃剑——训练之后，任何一点不对都会让他抓狂。而且练出来的是"看见细节"的能力，不是"让所有人同意"；审美有共性也有个体差异。最后一条：它不替代功能取舍——他把最难的一关说成把审美和功能合在一起（七座、五个大人两个孩子，还要好看）。

## M109 · 跨领域移植：去别的行业找已经解决过的同一类问题

**触发**：你要在一件事上做出别人没做过的改进，但本行所有人都在同一套做法里。
**他怎么说的**
> “Try. Just try thinking of interesting ideas. Read about many fields and cross-fertilize ideas. For example, SpaceX used automotive mass-manufacturing techniques, and Tesla applied space industry materials optimization. That’s a superpower.”
— `corpus/2025-whatsuptesla com 2025 05 06 elonatwestpointp.txt`
**动作**
1. 先写下你真正要解决的问题的结构（不是"做更好的火箭"，而是"把大批量制造的成本压下来"）。
2. 列出 3–5 个**别的行业**，它们解决过同构的问题。
3. 逐个问"这行的手艺搬过来会怎样"——他给了两个现成模板：SpaceX 搬汽车业的大批量制造技术；特斯拉搬航天业的材料优化。
4. 判据：能找到"已在别处被验证过"的现成做法，就不必从头发明；他把这个习惯叫一种 superpower。
**失效边界**：移植的前提是问题结构同构，不是名字像。借来的做法必须能对上你这行的真实约束（批量、公差、认证、监管），否则得到的是一个在你这儿不成立的最优解。他给的两个例子两边都是工程学；搬到组织、激励、人的问题上，"手艺"不可直接搬。

## M110 · 约束不在能量，在「没人愿意把电厂建在自己后院」

**触发**：你在给一个耗能巨大的计划（算力、制造、数据中心）选址，默认"电不够"就是硬约束。
**他怎么说的**
> There are very few people who want a power plant in their backyard. So if we wanted to, say, double the electricity usage of the United States, which is on average about 500 gigawatts, we would have to build about twice as many power plants, which I don’t think most communities are super excited about.
>
> Current human civilization uses much less than a trillionth of the Sun’s energy output, which is humbling to think about.
>
> The Sun is 99.8% of all mass in the solar system, and most of the remaining is Jupiter.
— `corpus/2026-whatsuptesla com 2026 06 05 spacexai ipo roa.txt`
**动作**
1. 先算这份资源的物理上限：太阳占太阳系 99.8% 的质量；人类文明现在用掉的是太阳输出的"不到一万亿分之一"——按这个口径，把用量放大一百万倍，仍不到太阳的一百万分之一。
2. 再算地面这条路要新建多少硬件：美国平均用电约 500 吉瓦，翻倍就要再建一倍的电厂。
3. 把约束从"能量"改写成"选址与社会接受度"——他的判据是"很少有人愿意把电厂建在自己后院"。
4. 于是动作变成换场地（把发电和数据中心移出大气层），而不是省电；换算口径是他给的：从地球约 1 太瓦/年，从月球可以做到一千太瓦以上。
**失效边界**："上限很高"不等于"现在便宜"。这条只证明能量不是理论瓶颈；把"上面有无限能量"读成"不用管电网、散热、发射成本"就是误读。他的语境是太空算力的长期扩张，不是当下的电价判断。

## M111 · 招苦差事的人：先把代价一条不落地说完

**触发**：你要招人去做一件又苦又险、回报不确定的事（硬技术项目、远地项目、救火任务）。
**他怎么说的**
> the sales pitch for going to Mars is, “It’s dangerous, it’s cramped. You might not make it back. It’s difficult. It’s hard work.” That’s the sales pitch.
>
> And it’s very important to emphasize that Mars, especially in the beginning, will not be luxurious. It will be dangerous, cramped, difficult, hard work.
— `corpus/2022-elonmuskinterviews wordpress com 2022 10 01 .txt`
**动作**
1. 把代价一条不落写进招募陈述。他的版本是五条：危险、拥挤、可能回不来、难、苦工。
2. 一条都不软化——他的原话是"这就是销售话术"。
3. 说清"不奢华"是初期状态，不是阶段性问题（他的限定词是 especially in the beginning）。
4. 判据：招到的人知道自己在换什么。他承认只有一小部分人想去，而他要的是"想去 × 去得起或能拿到赞助"这个交集的百万量级——用代价筛人，而不是用愿景筛人。
**失效边界**：只有当你确实能给出相称的回报时才成立——他自己的说服公式是两句（已有 `references/methods.md` M29）：要有合理的成功机会，成功后回报要与付出相称。代价讲全了而回报说不出，那就只是劝退。而且"苦"不能等于"没意义"：这段话的场合是去火星，不是给普通岗位找一个筛选器。（本段末尾那句 But it will be glorious 是 Chris Anderson 接的话，不是马斯克的原话，不作引用。）

---

## M112 · 估算只做到数量级

**触发**：你要给一个高度不确定的量报数（里程、成本、工期），而精确到小数在物理上买不到。
**他怎么说的**
> So it’s really just you’re trying to—when you’re trying to guess something where there’s a lot of uncertainty, just try to get the estimate to the nearest order of magnitude, closest factor of ten. And that’s why I said probably around ten billion kilometers or six billion miles.
— `corpus/2025-whatsuptesla com 2025 11 11 elon musk talks .txt`
**动作**
1. 写下你要的那个数，先别管精确值。
2. 把它归到最近的 10 的幂上，并写出上下两个界。他的原例：自驾驶需要多少里程——"落在 100 亿公里（约 60 亿英里）那一侧，而不是 10 亿公里那一侧；但不会是 1000 亿公里"。
3. 判据：你的答案要落在**最近的 factor of ten** 上；不要求落在小数点后。
4. 报数时把这个量级和它的界一起报出去，别报一个假装精确的单一数字。
**失效边界**：只在"不确定性极大、精度买不到"的量上成立。能实测的量（良率、良品数、现金能撑几天、退货原话）不要用数量级代替实测——那些数你查得到，查得到就不该估。

## M113 · 每个阶段先找限制因子，再动手

**触发**：你想推进一件事，手上有十个方向，不知道劲该往哪使；或者你上一次认定的瓶颈已经通了，该重找。
**他怎么说的**
> Chips and electricity are the two limiting factors.
> I built the chip team from scratch and the AI team from scratch. It was just because it became a limiting factor.
> But, yeah, it’s basically something as a limiting factor, and then we take actions to address the limiting factor.
— `corpus/2025-whatsuptesla com 2025 11 11 elon musk talks .txt`
**动作**
1. 写下当前系统的限制因子。他这次给的是两个，两个都要单独列：**芯片**和**电力**——不是一个词，是两条并列的通道。
2. 判断这个限制因子是不是"外面拿不到"的东西（供应商产能上限）。是 → 自己建。他建芯片团队和 AI 团队都不是战略规划，是"它变成了限制因子"。
3. 每隔一段重问一次：限制因子换了没有？换了就把人和钱挪过去（现在限制是芯片和电力，不是三年前的产能）。
4. 判据：一件事既不在限制因子上、又不改变限制因子，就不该占用你现在的资源。
**失效边界**：**已有** methods M11「限制因子是工程，就把 80% 的时间给它」——那一条给的是**配比**；这一条补的是"限制因子会换，所以要先找、并反复重找"。M11 的失效边界照样适用：限制因子不在工程上时（活下来、拿许可、拿客户），照搬这条会把自己饿死。

## M114 · 按段切分一天，压掉上下文切换

**触发**：你同时管几件事，一天被切得稀碎，晚上想不出今天推进了什么。
**他怎么说的**
> Well, I have a lot of inbound communication. So… it’s information triage. I try to segment the days so that there’s not too much context switching because arguably, context switching is difficult.
— `corpus/2025-whatsuptesla com 2025 12 12 elon musk in con.txt`

> if you had to context switch every 3 seconds or every 30 seconds or every 3 minutes, the context switching cognitive penalty would be very high.
— `corpus/2025-whatsuptesla com 2025 12 12 elon musk in con.txt`
**动作**
1. 先给你的切碎程度定位：这个下午是 3 秒切一次、30 秒切一次，还是 3 分钟切一次？他给的是一个梯度——越短，认知惩罚越高。
2. 把一天**分段**（segment the days），同一段里只碰一件事；跨业务（特斯拉 / X / xAI / SpaceX / 私人）不放在同一段。
3. 把必须处理的来信降级成"信息分诊"（information triage），别让它决定你这一段的主题。
4. 判据：一天结束，你能不能指出哪一段产出了什么。指不出来，说明段没切，只是把碎切得更碎。
**失效边界**：这条治的是**输入导致的切换**，治不了"业务本身就在同一时刻出事"。紧急情况下切换是必要的；把它当纪律用来挡掉所有打断，会让你错过真正该被立刻处理的那件事。

## M115 · 用仿真找包线，然后在包线内发射

**触发**：你要做一件一次性、高风险、不能在地面全测的事。
**他怎么说的**
> When SpaceX or Tesla runs simulations to understand how a car, robot, or spaceship will work, we run thousands of them on the computer. The simulations we actually pay attention to are the most interesting ones. The simulation where everything goes perfectly on the rocket? We don’t really look at that; it’s fine, but boring. We test all sorts of oddball failure modes, but we don’t waste time on the ones where the rocket just explodes instantly on the pad because that’s not interesting either. So we hunt for the envelope of flight paths where the rocket can actually make it to orbit without blowing up, we find those boundaries, and then when we launch the real rocket we do everything possible to stay inside them.
— `corpus/2025-whatsuptesla com 2025 12 12 elon musk in con.txt`
**动作**
1. 跑几千次仿真，不要只跑一次"标准工况"。
2. 丢掉两类结果：一切完美的那次（没有信息）、以及一上架就爆掉的那种（也没有信息）。
3. 找**能成功的边界**——那些刚好能到、再多一点就炸的界；把边界画成一张图。
4. 真发射时，一切动作围绕"待在边界之内"来做。
5. 判据：你手上有没有那张"边界在哪"的图？没有，说明仿真跑了但没读。
**失效边界**：仿真给你的是**边界**，不是**保证**。**已有** playbook 节 37讲"炸掉的原因都不在风险清单上"——两条合起来用：用仿真把已知的边界压出来，用真飞去买那些"未知的未知"。

## M116 · 从一个最小可批准的动作起步

**触发**：一个巨大工程、许可或合规把你卡在起点，你连第一步该去哪个窗口都不知道。
**他怎么说的**
> They don’t really care about the existential nature of a pit. You just say, like, I want a pit. It’s a hole in the ground. Then we got the permit for the pit, and we dug the pit in like, I don’t know, three days, two, three days. Actually, I think two, 48 hours, something like that.
— `corpus/2021-elonmuskinterviews wordpress com 2021 01 25 .txt`

> And dug this big pit, and we showed Eric the pit. Like, obviously it’s just a pit. But hey, a hole in the ground is better than no hole in the ground.
— `corpus/2021-elonmuskinterviews wordpress com 2021 01 25 .txt`
**动作**
1. 把那个大工程缩到一个最小的、能**单独申请**的动作——一个"坑"。
2. 申请那个最小动作，不要附带说明它的宏大用途（"他们并不真的关心一个坑的存在主义意义"）。
3. 用最快速度把它做出来：他那次是 48 小时连做、四班倒、约 40 多小时出成品。
4. 拿这个最小成品去见一个关键人物，让他看见实物。
5. 判据：你手上有没有一个"已经是实物"的东西？没有，说明你还在 PPT 阶段。
**失效边界**：这是"先做出来"的动作，**不是绕过审批**——他拿的仍然是许可，只是把许可拆到最小。**已有** playbook 节 32讲"原型先于一切"；这里补的是在审批最严的环境里，"那个最小动作"具体长什么样。

## M117 · 把"我预测"和"我希望"分成两栏

**触发**：你在讲一件关于未来的事，听众把你的预测当成你的主张，或者反过来替你把两件事合并。
**他怎么说的**
> I just want to separate what I wish would happen from what I predict will happen, because people get confused about that. They think that what I predict is what I want. What I predict to happen is not the same as what I want to happen. If I could, I would certainly slow down AI and robotics, but I can’t.
— `corpus/2025-whatsuptesla com 2025 12 12 elon musk in con.txt`
**动作**
1. 两栏写：左栏"**我预测会发生**"，右栏"**我希望发生**"。
2. 两栏不一致时，主动说出来，别让人替你合并——他的例子：他希望放慢 AI 与机器人，但预测放慢不了。
3. 说话时把归属讲清："这一句是预测，那一句是愿望。"
4. 判据：别人把两栏读混时，你要能立刻指出哪一句属于哪一栏。
**失效边界**：**已有** playbook 节 29讲愿望思维，治的是"把自己过滤掉的信息找回来"；这里补的是**对外表达时的两栏切割**，解决的是别人的误读。注意它不能用来免责——如果你只用它说"我只是预测"，却从不说明你希望什么，那它就是推卸而不是切割。

---

## M118 · 把"贵"拆成材料价、组织开销和垂直整合三步

**触发**：一个行业的报价高到反常（火箭、卫星、设备、代工），你怀疑"物理上就该这么贵"。
**他怎么说的**
> If you look at what it costs to build a rocket, the raw materials — aluminum, titanium, copper, etc. — if you were to buy those materials at market rates and just melt them down, the cost of the materials is actually quite low. It’s on the order of a couple percent of the cost of the launch vehicle. And so the question is, why is everything else so expensive? And the answer is really just overhead and inefficiency in the way things are done. So by simplifying the design and doing vertical integration — basically building almost everything ourselves — we think we can bring the cost down dramatically.
— `corpus/2026-whatsuptesla com 2026 04 07 elon musk 2003 s.txt`
**动作**
1. 查出这件东西**大宗原材料**的市场价（铝、钛、铜这一级），按用量算总价。
2. 拿它除以现行售价，算占比。他的判例是**"a couple percent"（百分之几）**。
3. 判据：占比很低 → 贵在物理之外，**问题被定义成组织问题**（开销与低效）；占比很高 → 别做这个白痴指数计算，先谈材料本身。
4. 组织问题走两个动作：**简化设计**（减少零件数）＋**垂直整合**（把外购的环节收回来自己造）。他用"几乎没有外包"和"30 人、没有律师和会计"作为这条的实施状态。
**失效边界**：这是**自造型制造**的算法。供应商体系本身就构成价值时（专用设备、认证件、小批量高精度件），把成本全归于"低效"会得出错误结论；另外这个算法要求你有把工序收回来的工程能力，没有的话第 4 步只是姿态。
（已有：playbooks 节 2与 cases 案例 1、案例 2 已有"魔法棒／白痴指数／原材料只占极小比例"；这里补的是 **2003 年的最早出处**，以及把结论落到**两个具体动作**——简化设计、垂直整合——而不是停在"看清比例"。）

## M119 · 火星人口的时间表算法：先定人口，再数交会窗口

**触发**：一个跨代目标（火星城市、能源替代、行业标准换轨）被人问"什么时候"，而你只能给感觉。
**他怎么说的**
> It’s probably between 20 and 50 total Mars rendezvouses
— `corpus/2016-spaceflightnow com 2016 09 27 spacexs elon m.txt`
> It’s probably anywhere from 40 to 100 years to fully achieve a self-sustaining civilization on Mars.
— `corpus/2016-spaceflightnow com 2016 09 27 spacexs elon m.txt`
**动作**
1. 写下**完成的人口门槛**（他给的是 100 万居民）。
2. 找出这个系统的**窗口周期**：火星发射窗口每约 **26 个月**一次（记者原话是 `Mars launch windows occurring every other year`）。
3. 把"需要的总运力 ÷ 每次窗口能送的量"折算成**交会次数**。他给的结果是 **20–50 次**。
4. 用次数乘窗口周期换算成时间：**40–100 年**——这就是他报出来的数。
5. 报数时按"次数 + 年数"两个量报，不给单点日期。他同一次讲话里把 2024 年那次发射称作 `an aspiration`（愿望）而不是计划。
**失效边界**：只适用于**由固定周期窗口驱动**的长期目标（航天窗口、药物审批、换届、种植周期）。由需求或竞争速度驱动的目标没有这个固定分母，算出来只会是假的精确。另外这个区间极宽（20–50），它的用途是**排除不合理的期待**，不是排项目计划。

## M120 · 经济体量算法：产出 = 人均生产率 × 人口

**触发**：你要判断一项通用技术（机器人、AI、自动化）值多少钱，或者有人拿"基本收入"来谈它的社会后果。
**他怎么说的**
> I also think it unlocks an immense amount of economic potential because when you think about… what is the output of an economy, it is productivity per capita times the population per capita. Once you have humanoid robots, the actual economic output potential is tremendous. It is really unlimited. Potentially we could have an economy ten times the size of the global economy where no one wants for anything.
— `corpus/2025-whatsuptesla com 2025 05 14 elon musks talk .txt`
**动作**
1. 把经济体量写成两个因子的乘积：**人均产出 × 有效人口**。
2. 判断这项技术动的是哪个因子：**人口侧**（把机器算成"有效人口"）还是**生产率侧**（让人均产出变高）。人形机器人走的是第一条。
3. 按改变后的因子重算总量。他给的量级是：**可能是一个十倍于今日全球经济、且无人匮乏的经济体**。
4. 把分配问题单独拿出来算——他给的不是"普遍基本收入"，是 `universal high income`（译：任何人都能得到想要的商品与服务）。这一步是**分配端的目标设定**，不是第 3 步的推导结果。
**失效边界**：这是**潜力上限**的算法，不是预测。他说的原话是 `Potential` 与 `ultimately`；把它当几年内的预测来安排投资会踩空。而且这条只算总量，不含约束（能源、材料、土地、政治）——他自己在同一次讲话里另外提到能源是瓶颈。

## M121 · 悬停类交通工具的判据：先算气流账 MG = MA

**触发**：有人提出一个"飞起来就没交通问题了"的方案（飞行汽车、悬浮平台、个人飞行器），你要判断它可行不可行。
**他怎么说的**
> There’s a fundamental momentum exchange with the air. So, you must accelerate. You have a mass, and you have gravitational acceleration. Your mass times gravity must equal the mass of airflow times acceleration of that airflow to have a neutral force. MG=MA.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 03 .txt`
> Like, if you want a flying car, just put some wheels on a helicopter.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 03 .txt`
**动作**
1. 写出平衡式：**M×G =（空气质量流率）×（气流的加速度）**。要悬停，两边必须相等。
2. 代入你的载重和重力加速度，反解出**每秒需要向下加速多少空气**。
3. 用这个气流量去推两件事：**噪声**（他给的判据是"想想玩具无人机有多吵、吹多大风，再想象一千倍重"）和**对地面的扰动**。
4. 判据：算出来的气流规模意味着噪声与风无法被接受 → 这个方案的"没有路"的收益被"邻居不干"的成本吃掉。他的结论是这条路绕不过去（`There is definitely no way around it.`）。
5. 反查方案里有没有宣称靠"磁"或其他无气流机制悬停——按第 1 步直接否掉。
**失效边界**：这是**在接近地球表面的空气里、靠向下推空气悬停**的判据。固定翼、火箭、以及在有轨/太空环境里不适用（不需要持续向下推空气）。另外它只否掉"悬停式个体交通"，不否掉"在特定场景下用直升机"—他自己说的替代品就是直升机加轮子。

## M122 · 太阳能屋顶的规格判据：先分版本，再算 0.5–1.5 倍

**触发**：你要给一个"本身也是建材"的产品定规格和分版（太阳能屋顶、一体化窗、承重地板……）。
**他怎么说的**
> So, like, it depends on whether your roof’s new or old. So, if your roof’s new, you don’t want to replace the roof. You want to put solar panels on the roof.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 24 .txt`
> Yeah. So, generally, yes. I would say it’s probably for most. It’s going to vary, but anywhere from more than you need to maybe half. Like, call it half to 1.5 of the energy that you need, depending on how much roof you have relative to living space.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 24 .txt`
**动作**
1. 先按**用户此刻的真实状态**分版本，不按产品线分。屋顶分两种：**新屋顶** → 卖加装式面板（别让人换屋顶）；**本来就要换屋顶/盖房子** → 卖嵌电池的瓦片。
2. 对每个版本算产能量级：以**家庭能耗的 0.5–1.5 倍**为区间。
3. 用**屋顶面积 ÷ 居住面积**这个比值定落在区间哪一头。
4. 判断真正约束在哪一环：他给的顺序是 **电视没关系，空调是问题**——所以耗电侧要先看空调，而不是总用电量。
5. 定硬性指标时带上**寿命**：他给的判据是"屋顶要能用大概 30 年"，所以测试周期必须以年计，不能以季度计。
**失效边界**：这是**住宅、温带/日照正常**的场景。年均日照、遮蔽、电价与并网政策会整体平移这几条；而且"0.5–1.5 倍"是他自己给的粗略区间（`call it`），不是测量值。

## M123 · 用"断线还是坏端点"判断该修还是该绕

**触发**：一个系统局部失效，团队在讨论"修好它"。
**他怎么说的**
> And like when you have a severed spinal cord, you essentially have broken wires. And so, if you can just jump over those wires and transmit the signals over those wires, you can give somebody the ability to walk again, naturally.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 27 .txt`
**动作**
1. 把系统重述成**信号链路**：上游（产生意图/数据）—— 通道 —— 下游（执行）。
2. 分类：**通道断**（线）还是**端点坏**（产生端/接收端）。
3. 通道断 → 不修线，做**旁路**。他的做法是在断点之后再加一个植入体，做一个 `neural shunt`。
4. 判据是二值的：**上游还有信号、下游还听得懂**，两个都成立，旁路就成立；他的措辞是"我确信长期可以恢复全身运动"。
5. 只有端点坏时才回到替换/重建那条路。
**失效边界**：这条依赖"两端还活着"。很多长期断链的实际情况是上游代表区已经退化（不用则废），那时绕过去也没有信号可送。另外这条给出的是**方向**，不是工程方案——他自己给的长期量词是 `long term`。

## M124 · 挑替代测试模型的三条判据：像、抗造、养得起

**触发**：你要测一个"放进活体/放进真实环境"的东西，但直接上目标对象太贵或太险。
**他怎么说的**
> And then, yeah, the pigs are actually quite similar to people. So, if we’re going to figure out things for people, then pigs were a good choice. And they’re also quite robust creatures, like little tanks.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 27 .txt`
> So, if the device is lasting in the pig, as it lasted there for two months, and still going strong, then that’s a good sign that the device is robust for people.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 27 .txt`
**动作**
1. 列候选对象，按**与目标的解剖/结构相似度**筛（他们的口径是颅骨厚度相同、硬脑膜相似）。
2. 加第二条：**抗造**——因为这个测试的目的是把设备往极端工况里折磨（他用的比喻是"小猪像小坦克"，会撞、会滚、会用头顶）。
3. 加第三条：**可养、成本低、福利好维持**（他们另一条原话是"让猪开心很容易"）。
4. 定判据时盯**存活时长**：他给的结果是设备在猪体内"持续两个月仍然健壮"，据此推断对人体也健壮。
5. 报告时把结论写成**相关性判断**（"这是好迹象"），不写成等价（"人身上一定行"）。
**失效边界**：这三条挑的是"能扛住物理折磨"的模型，挑不出生理机制上的等价物。所以它能验证**耐久与封装**，不能验证**功能与安全性**——他自己的措辞是 `she went for two months` 这类时长证据。

## M125 · 新硬件定价：先找一个被接受的同类价格当锚，再清点能借的零件

**触发**：你在给一个从没卖过的新硬件定价，只有成本估算。
**他怎么说的**
> I think we want to get the price down to a few $1,000, something like that. And I think that’s possible, I think it should be possible to get it similar to LASIK.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 27 .txt`
> And then the device electronics itself, I think, will not be very expensive because it actually does use a lot of the parts that are made in extremely high volume in 10s of millions of units for smartphones, as well as smartwatches and wearables in general.
— `corpus/2021-elonmuskinterviews wordpress com 2021 05 27 .txt`
**动作**
1. 先给一个**会被接受的量级**，不给成本加成。他的锚是 **"几千美元"**（译，原话 `a few $1,000`），并对标 **LASIK**（一个已经存在、已经有人愿意付的同类消费医疗价格）。
2. 把这个价格倒过来压成本：**清点有哪些部件可以直接借用量产消费电子的零件**（手机、手表、可穿戴——年产量上千万级，单价被摊过了）。
3. 只对**无法借用**的那部分花钱自研：他们的例子是神经放大器和芯片算法（做定制 ASIC），其余借现成。
4. 把"包括自动手术在内"的总价当目标口径——他的措辞是 `inclusive of the automated surgery`。
5. 报定价时说明起点会更高：`at first, I think it's going to be, you know, quite expensive, but that price will very rapidly drop`。
**失效边界**：锚定的前提是**存在一个可比的、已被接受的支出**（LASIK 之于眼科手术）。没有这种锚时，用别的行业的价格会给出错误的目标。另外"借用量产零件"要求你的量最终能上到同一量级——几百台的量级借不到那个单价。

---

## M126 · 审支出、审流程：找那个愿意替它出面的人

**触发**：你怀疑一大笔支出、一大堆流程里混着一批没人真正需要的东西，但没有任何一份文件能告诉你哪一条是。
**他怎么说的**
> So it's just a lot of work going through the vast expenses of the federal government and just really asking questions, what's this money for? Are you sure it's actually being used? Well, many times we can't even find anyone who defend it. So for a lot of the expenses, there is actually no defender at all.
> I mean, we find situations where there are millions of software licenses where with zero people using them, zero, exactly. This is the quizzical expression. You're like, surely if there's millions of software licenses, someone should be using them. No.
— `corpus/未标年-techpolicy press transcript elon musks doge .txt`
**动作**
1. 逐条列出来。他的量级是「几百万条 line items」，做法是同意/不同意的二值判断，不做优先级排序。
2. 每条问两个问题：这笔钱是干什么的？你确定它真的在被用？
3. 去找愿意替这条支出出面的人。找不到辩护人的，就是可以被停的那一批——他说很多时候「甚至没人知道这笔钱为什么在花」。
4. 走终止流程。他给的时间预期是慢的：从停到走完程序，可能半年，也可能将近一年。
**失效边界**：「没有辩护人」测的是发声成本，不一定测出价值。受惠者分散、辩护要承担政治成本的时候，没人出面不代表这东西没用。这套动作在你能逐条看到实物（账目明细、许可清单）时有效；只有汇总数的时候，它退化成猜。
**说明**：它的反面是 `references/playbooks.md` 算法第一步「要求必须追到一个人」——那条问的是提出者是谁；这里问的是有没有人愿意当辩护人。

## M127 · 把芯片块数换算成发电容量

**触发**：你在给一个集中式算力集群做电力预算，手上有芯片型号和块数。
**他怎么说的**
> So the actual—roughly every 110,000 GB 300s inclusive of networking, CPU, storage, cooling, margin for servicing power is roughly 300 megawatts.
> It’s roughly—or think about it like a way to think about it is like 330,000. What you need at the generation level to service, probably service 330,000 GB 300s, including all of the associated support, networking and everything else, and the peak cooling and to have some power margin reserve is roughly a gigawatt.
> Well, it gets pretty freaking hot in Memphis, so you’re going to have like a 40% increase on your power just for cooling.
— `corpus/2026-whatsuptesla com 2026 02 24 elon musk with d.txt`
**动作**
1. 不要用「标称功耗 × 块数」。他直接把这种做法否掉——那是没做过硬件的人算出来的数。
2. 逐项把被忽略的乘数乘上去：网络硬件、CPU 与存储、按全年最坏那一天的峰值制冷需求（他给的数是再 +40%，并且前提是你不接受热天关机）、以及为检修而必须离线带走的余量（他给的是再 +20~25%）。
3. 换算成发电端口径，不要停在 IT 端口径。他给的两组比值：约 11 万块 GB300 含全部配套 ≈ 300 兆瓦；约 33 万块 ≈ 1 吉瓦（发电端、含峰值制冷与备用量）。
4. 判据：算出来的数是「要装多少发电能力」，不是「芯片参数表上写了多少」。两个数差约三倍，这个差额就是能不能开机的地方。
**失效边界**：那几个系数是随地点和季节变的（他说的是孟菲斯），照抄数字等于把一个气候常数当成物理常数。而且这条只适用于集中式恒功率集群；边缘算力（他自己另讲的车、机器人）走的是另一条账，见「用夜间余量给边缘设备充电」。
**说明**：已有 `references/playbooks.md` 节 24的「三、把标称值算成真实值」收了同一段的定性话（Besides the GB 300…）；这里补的是可算的乘数与换算比值（+40%、+20~25%、110,000:300MW、330,000:1GW）。

## M128 · 追瓶颈追到那一道不可替代的工序

**触发**：一件事整体卡住，你也知道大概卡在哪个部件，但说不清为什么换不掉、要等多久。
**他怎么说的**
> The limiting factor, you can get everything except the blades. They call the blades and vanes. You can get that 12 to 18 months before the vanes and blades. The limiting factor of the vanes and blades, and there are only three casting companies in the world that make these and they’re massively backlogged, is this Siemens.
— `corpus/2026-whatsuptesla com 2026 02 24 elon musk with d.txt`
**动作**
1. 从整机往上走一层，问「哪一样是买不到、或者要等最久的」。他给的例子是燃气轮机：整机可以排产到 2030 年之后，但再往上游，叶片和导叶（vanes and blades）要等 12 到 18 个月。
2. 把限制因子落到供应者数量上：能做的只有三家铸造公司，而且全都严重积压。只有三家、又全都排队——这就是限制因子本身。
3. 判据两种走向：自己做那一道工序（他的原话是 SpaceX 和 Tesla 大概得自己做叶片），或者绕开它（换路线、换设计、降规格）。
4. 顺带验一下这个判断是不是常识：他说这不是机密，你随便打电话问任何一家轮机制造商都会得到同样的答案。
**失效边界**：这条能把「最紧的那一环」找出来，但它不告诉你值不值得自己下场——自己建一道高温合金铸造工序的代价，可能远高于换路线。另一个前提是你的产量诉求大到值得自己做；小批量时这条只会让你误判。

## M129 · 验收一个新系统：看老系统有没有被关掉

**触发**：你在交付一个用来替代旧工具的新系统（新编译器、新平台、新流程、新供应商），验收标准还没定死。
**他怎么说的**
> But the acid test here, and what I’ve told the Dojo team is like, it’s successful if the software team wants to turn off the GPU cluster. But if they want to keep the GPU cluster on, it’s not successful.
> I guess the proof’s in the pudding.
— `corpus/2021-elonmuskinterviews wordpress com 2021 11 19 .txt`
**动作**
1. 先把判据写死成行为，不是写成性能:老系统的使用者愿不愿意把它关掉。他的原话：Dojo 成功的标志是软件团队想把 GPU 集群关掉。
2. 反向也成立：如果他们还留着 GPU 集群，就是不成功——哪怕新系统的跑分更好看。
3. 验收那天去查这个行为（旧集群的开关状态、旧流程还有没有人在走），而不是去读新系统的指标报告。
**失效边界**：它把「内部用户的偏好」当最终判据，而内部用户可能有惰性，也可能为了保住预算而不肯关掉旧的。所以它成立的场景是：新旧两条路都在你手里、你有权关掉旧的。对外部用户不适用。
**说明**：与 `references/methods.md` M26（把最难的那部分先给人看）方向相近但不同：那条看的是外部反应，这条看的是内部用户愿不愿意放弃旧工具。

## M130 · 要提速率，就把「迭代次数 × 单次进步」两项拆开算

**触发**：你要改善的是速率本身（模型训练、工艺改善、产品迭代），而不是某一版的结果。
**他怎么说的**
> just in general innovation is how many iterations, and what is the average progress between each iteration. And so, if you can reduce the time between iterations, the rate of improvement is much better.
— `corpus/2021-elonmuskinterviews wordpress com 2021 11 19 .txt`
**动作**
1. 把速率写成两项的乘积：迭代次数，和每次迭代的平均进步。
2. 只压第二项的时间。他的例子：同样一次训练，从两天变成两小时「是个大事」。
3. 判据换掉：不问「这一次能做多好」，问「这一次到下一次要多久」。
4. 如果算下来次数已经很多而进步很小，问题就不在速率上，回头查方向。
**失效边界**：单次进步被榨干之后，单纯加大迭代次数只是在烧资源（频繁重训的小步改进，可能不如一次结构改变）。而且它要求你能测出「单次进步」，测不出来时它退化成「更快地瞎试」。

## M131 · 算「置换要多久」：存量 ÷ 年产量

**触发**：你要判断一个「换掉全部存量」的目标要多久（电动化、设备更换、系统迁移、标准替换），有人说几年就能做到。
**他怎么说的**
> there’s two and a half billion cars and trucks in the world. And the new car and truck production, (1:22:30) if it was a 100% electric, that’s only about 100 million per year. So, it would take — If you could snap your fingers and instantly turn all cars and trucks electric, it would still take 25 years to change the transport base to electric.
> how long does a car and truck last before it goes into the junkyard and gets crushed? About 20 to 25 years.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 09 .txt`
**动作**
1. 查存量。他给的数是全球 25 亿辆汽车与卡车。
2. 查年产量上限，并且按最乐观的假设算——他假设的是「新增产量 100% 都是电动的」，那就是约 1 亿辆/年。
3. 相除：25 亿 ÷ 1 亿/年 = 25 年。这就是「全部换完」的下限，跟政策意愿无关。
4. 拿寿命核对一遍：车到报废大约 20 到 25 年——两个数对上，说明这个下限是存量结构决定的，不是执行力问题。
**失效边界**：只在「一换一」成立时有效。有两件事会打破它：保有量本身还在增长（新增的存量永远换不完），或者存在加速退役的手段（强制报废、以旧换新）——后者会同时缩短寿命和拉高年产量。

## M132 · 把物理问题先写成一条守恒式（力平衡版）

**触发**：你在判断一个飞行器或运动体的方案（更高、更快、更省），用直觉和行业惯例说不清它到底能不能成立。
**他怎么说的**
> the way to think about a plane is it’s a force balance.
> Air density drops exponentially, but drag increases with the square, and exponential beats the square.
— `corpus/2021-elonmuskinterviews wordpress com 2021 02 09 .txt`
**动作**
1. 把不加速的状态写成守恒式：重力、升力、推力、空气阻力四项平衡。
2. 逐项看它随你要改的那个变量怎么变。他的关键一步是看高度：空气密度随高度指数下降，阻力随速度平方上升——指数打败平方。
3. 由这条得出反直觉结论：越高越省，到某个高度可以用比三万五千英尺更少的每英里能量做到超音速。
4. 于是真正的约束被挪到别处：既然巡航几乎不耗能，关键就变成电池的能量密度能不能把你抬上去（克服引力势能），以及下降时能不能把那份势能收回来——他说那样连备用燃料都不需要。
**失效边界**：这是巡航段的账。起飞和爬升是另一组约束（能量密度、推重比），他把最难的一关放在那里。另外「指数打败平方」只在这个区间成立，接近真空之后升力本身也没了。

## M133 · 判断「搬到太空是不是更便宜」时的乘数账

**触发**：你在比较一件设施放在地面还是放在轨道上（算力、太阳能、制造），各方给的都是总体报价。
**他怎么说的**
> And when you take into account now put it in space and it’s five times cheaper because it’s five times—in fact, no, it’s 10 times cheaper because you don’t need any batteries.
> you’re going to get about five times the effectiveness of solar panels in space versus the ground. And you don’t need batteries.
— `corpus/2026-whatsuptesla com 2026 02 24 elon musk with d.txt`
**动作**
1. 先算掉地面上的损失：大气一项约 30%；再加上昼夜、季节、云。
2. 得到单块电池板在天上是地里的大约五倍发电量（他自己的口径是 five times）。
3. 再去掉配套电池那一大块成本——他给的账是因此总成本再降一半；两块合起来，同样是「十倍便宜」的量级。
4. 于是结论只剩一个变量：入轨成本。他的判断是只要入轨成本足够低，最便宜的算力地点就是太空，而且他给了一个带日期的赌注：36 个月、大概 30 个月。
**失效边界**：这条账的分子全是收益，分母只有一项（入轨成本）。太空侧的散热、抗辐射、维修与折旧他在这段里没算——这几项任一大到一定程度，账就会翻。所以它的成立条件全写在「一旦入轨成本足够低」那句里；在那之前，它只是一个阈值判断，不是一个现值比较。

## M134 · 用夜间余量给边缘设备充电

**触发**：你在给分布式用电设备做电力规划（车队、机器人、边缘算力），担心电网撑不住。
**他怎么说的**
> the actual peak power production in the US is over 1,000 gigawatts. But the average power usage because the day night cycle is 500.
> So if you can charge at night, there’s an incremental 500 gigawatts that you can generate at night.
— `corpus/2026-whatsuptesla com 2026 02 24 elon musk with d.txt`
**动作**
1. 查两个数：平均用电量与峰值发电能力。他给的美国数：平均约 500 吉瓦，峰值发电能力超过 1000 吉瓦。
2. 差额就是夜里闲着的那约 500 吉瓦——它不需要新建任何东西。
3. 把可以延后的充电挪到夜里：边缘算力的功率是摊在一片区域上的，不是集中在一点，所以它吃得下这个余量。他的结论是「所以特斯拉在边缘算力上不受限」。
4. 反向对照着看：集中式算力要的是 24 小时恒功率，没有这个余量，所以他的判断是「你要是想把算力集中起来，你会很难把它开机」。
**失效边界**：它依赖电网夜里真的有空着的容量——有些电网是白天靠光伏、夜里靠气电的结构，裕度不在同一个地方。而且「平均 vs 峰值」算出的是上限，本地输配电的瓶颈可能更紧。

## M135 · 安全规则不要挂在识别能力上

**触发**：你在给一个有分类器/模型的系统定安全底线（自动驾驶、内容审核、风控、机器人）。
**他怎么说的**
> the prime directive is ‘don’t crash’.
> whatever it is, don’t hit it. Even if it’s a UFO that crash-landed on the highway – still don’t hit it. It should not need to recognize it in order to not hit it.
— `corpus/2021-elonmuskinterviews wordpress com 2021 11 19 .txt`
**动作**
1. 先把底线写成一句不含条件的话。他的版本是四个字：别撞。
2. 检查这条规则有没有偷偷依赖「认出来是什么」。他点名的错法是：规则写成「识别到 X 就刹车」——那识别失败时规则就消失了。
3. 加一条不依赖识别的兜底：不管那是什么，都不要撞上去。他的原话场景是——哪怕高速公路上迫降了一架 UFO，也还是不要撞它。
4. 判据：把分类器整个关掉，这条规则还成立吗？成立才是兜底，不成立就是被挂在了识别上。
**失效边界**：这条只解决「底线」那一层，不解决「怎么做得好」——它不给性能，只保证最坏情况下不越线。而且它要求你有另一个不依赖识别的感知通道（雷达、超声、几何、物理围栏），否则那句话落不成代码。

## M136 · 算新建制造能力的时间：建厂 → 投产 → 爬良率 → 高良率量产

**触发**：你要估一条要新建的制造能力（自建产线、自建晶圆厂、自建铸造）的时间表。
**他怎么说的**
> The point is you’ve got to build the fab and you’ve got to start production, then you’ve got to climb the yield curve and reach volume production at high yield. That from start to finish is a five year period.
— `corpus/2026-whatsuptesla com 2026 02 24 elon musk with d.txt`
**动作**
1. 把工期拆成四段，不要合并：建厂；开始生产；爬良率；达到高良率量产。
2. 把四段加起来。他给的总账是五年——而且他补了一句，这句话你去问 TSMC 或三星，得到的也是同一个数。
3. 判据：所以「现在就下单」不等于「五年后拿到产能」，而是「五年后才刚刚开始有产能」。这就是他为什么要自己下场。
4. 同一段里他给的另一个判据是：现有产线的产能早就被订满了（他说他们已经把能订的都订了），所以排队不是选项。
**失效边界**：五年是他对先进制程晶圆厂的账；成熟制程、封装、模组产线要短得多。把它当通用常数会高估一切自制计划。另一头，这条不包含「订不到设备」的时间——他自己另讲的那条（先用常规设备上量、再改设备）就是用来绕开这五年的。

## M137 · 算车队规模：周转时间 ÷ 发射间隔

**触发**：你要估一个循环系统需要多少台设备（火箭、车、机器、工位），有人按产能目标反推。
**他怎么说的**
> So if you can use a ship every, say 30 hours, you could do it with 30 ships, but we’ll make more ships than that.
> you could probably do it with as few as like 20 or 30. It really depends on how quickly the ship has to go around the Earth and the ground track before the ship has to come back over the launch pad.
— `corpus/2026-whatsuptesla com 2026 02 24 elon musk with d.txt`
**动作**
1. 先定速率。他给的量级是一年 10,000 次，也就是大约每小时一次。
2. 再测单台的周转时间：从出发到回到出发位置要多久。他给的口径是「如果一艘船 30 小时能来回一次」。
3. 相除：10,000 次/年 ÷（365×24/30）≈ 需要 20 到 30 艘。这就是最小台数。
4. 判据：这个数只由周转时间决定，不由你想造多少决定——他同一段里说，还是会造得比这个多。
**失效边界**：前提是周转时间可测且稳定；冗余、检修、故障率都会把它拉长，他本人也承认「这取决于船绕地球一圈再回到发射台要多久」。而且这是理想值：它假设每一台都能无缝接上下一班。

## M138 · 先把「投放位置」选在你能看见的地方

**触发**：你要启动一件需要别人相信你在真的做的事，而你的信用还没建立。
**他怎么说的**
> I wanted to start a tunnel from where I could see it from my office at space X.
> So I said let's just carve off a part of the parking lot across the road so I can see if it's, if anything's happening or not.
— `corpus/未标年-www moonshots io episode 177 elon musk trans.txt`
**动作**
1. 把第一段的位置选在你自己的视线里。他的原话：想从 SpaceX 办公室看得见的位置开挖，于是把马路对面停车场切一块出来。
2. 判据是「能不能看见有没有在动」，不是选址有多合理、规模有多经济。
3. 规模先小到几乎没有风险——他自己把这件事称作「只是在地上挖个洞」，并且现在进展的说法也只是「不错」。
4. 同时把这件事从「顿悟叙事」里摘出来：他明确否认那是某天开车时的灵光一现。
**失效边界**：可见性优先会牺牲选址合理性，长期干下去必须重排。这条只适用于「先证明我在做」那一段；过了那一段还按可见性选址，就是在为表演付工程成本。

---

## M139 · 先列出会最大改变未来的东西，再从里面挑自己能做的

**触发**：你在选方向：手上几个机会都说得通，或者刚毕业、要转行，不知道该往哪押。
**他怎么说的**
> When I was in college, there were five things that I thought would be – I mean, I thought these were actually… I would not regard this as a profound insight but rather an obvious one. The internet would fundamentally change humanity because it’s like, humanity would become more of a superorganism because the internet is like a nervous system.
— `corpus/2021-elonmuskinterviews wordpress com 2021 06 07 .txt`
> In college, he thought about what he wanted to do with his life, using as his starting point the question, “What will most affect the future of humanity?”
— `corpus/2015-waitbutwhy com 2015 05 elon musk the worlds .txt`

（上句为 waitbutwhy 作者的转述引语，标为 `> ` 但**不是**他的逐字原话，按硬规则 2 标注。）

**动作**
1. 写下你判断会**最大改变人类未来**的 3–5 项，标准是影响面而不是赚钱难度。他的版本是：互联网、可持续能源、太空、AI、改写人类基因。
2. 逐条标注「我能不能参与」。他当年级掉了一项——「改写人类基因」，理由不是够不着，而是他自己也说不清影响是正还是负。**认为影响可能为负的方向，自己不接。**
3. 在剩下的里挑出你可以直接动手的那一项当起点。他选了可持续能源，并且第一步做的是能量储存（高能量密度电容），不是整车。
4. 用一句反向话筛最后一遍：这项如果我不做，「我不确定它会怎么发生」吗？不成立就降级成业余爱好。
**失效边界**：这条假设你对未来有独立判断，而不是跟着市场共识走。另一头，列完之后你一条都够不着，那它就是愿望清单——先回去补那张知识树（playbooks 节 20）。

## M140 · 缺一套工艺，就去每年砸几十亿的那一行借

**触发**：你的行业卡在一个精度/良率问题上，本行业的做法几十年没变过。
**他怎么说的**
> I wanted to use advanced chip-making equipment to make capacitors that were precise at a molecular level. You know, just a level of precision that was sort of unheard of in capacitors. Like, capacitor’s energy is a function of its area and a separation distance. So if you have a very tiny separation distance, and you can inhibit quantum tunneling, like… – things get pretty esoteric, so you got to inhibit quantum tunneling give very short gap, and then you could, in theory, get to very high energy densities by making capacitors in the way that you would make an x86 processor. And since there are 10s of billions of dollars going into chip-making R&D, that I thought there might be a way to make an advanced capacitor using chip-making equipment instead of the conventional means.
— `corpus/2021-elonmuskinterviews wordpress com 2021 06 07 .txt`
**动作**
1. 把你卡住的那个物理量写出来。他的版本是电容的两极间距，以及为缩短间距必须抑制的量子隧穿。
2. 找一个每年投入几十亿美元改进**同一类物理量**的其它行业。他的判据是芯片业：那边有几十亿 R&D 在替你摊薄开发成本。
3. 把那一行的设备/工艺当现成工具拿来用，而不是在本行业惯例路径上改。
4. 判据落在成本上：**借来的工艺之所以值得，是因为别人已经付过开发费**。付不出来（那行也没有规模投入）就不值得借。
**失效边界**：这条依赖「有另一行在做同一件事」。找不到那一行，你面对的是从零发明，时间尺度完全不同。另一头，借来的工艺会带来那一行的约束：产能排队、规格不匹配、被卡在别人的供应商后面。

## M141 · 使能技术一换代，立刻弃掉自己原来的押注

**触发**：你为一个方向投了很多年，现在出现了另一条路，你在纠结要不要继续。
**他怎么说的**
> No, I think with the advent of high-energy lithium-ion batteries, a capacitor is not the right path.
> It’s unnecessary. (30:00) I think it’s probably physically possible, but it’s unnecessary at this point.
— `corpus/2021-elonmuskinterviews wordpress com 2021 06 07 .txt`
**动作**
1. 写下你这条路依赖的「使能部件」是哪一个，以及当年它为什么是唯一解。他的版本是超级电容，因为当年电池能量密度不够。
2. 查那个使能部件这几年的关键指标。锂离子电池起来了，你那条路的唯一性就没了。
3. 做二值判断：**它在今天还是最优解吗？** 不是就直接宣布弃掉，不用等它「物理上做不出来」——他给的措辞是：大概物理上可行，但现在没必要。
4. 把弃掉的结论公开说一次，用他的句式：I used to think this, which turned out to be wrong。
5. 与 M06 分工：M06 讲「使能倍数没到就别动手」，这里讲**倍数被别人抢到之后要立刻放手**。
**失效边界**：只在使能部件确实换掉了最优解时成立。很多搁置是「还没到时候」，那时的正确动作是等，不是弃——把「没必要」和「暂时做不到」混起来，会反复砍掉正在爬坡的东西。

## M142 · 它不是 10，也不是 1000，最可能是 100：先定数量级

**触发**：有人给你一个大到无法执行的目标（「把世界搬离化石能源」这类），你需要把它变成可以派活的数字。
**他怎么说的**
> It’s about a hundred, roughly. It’s not 10; it’s not a thousand. Most likely, a hundred.
— `corpus/2021-elonmuskinterviews wordpress com 2021 01 21 .txt`
**动作**
1. 把目标换成一个**可以数的实体单位**：多少座工厂、多少条产线、多少台设备。他的版本是 Gigafactory 的座数。
2. 先猜数量级再算细节，答案要能落在两三个档之间。他的原话：不是 10，也不是 1000，最可能是 100。
3. 用这个数反推节奏：单座投资额 × 座数 = 总账单，再除以年数，得到每年的资本支出要求。
4. 判据是它能不能拿去派活：每一座对应哪个区域、什么时候动工。派不出去的数，说明还是口号。
**失效边界**：数量级估值的误差可以到两三倍，他给的是「100」这种档位，不是预算。而且单位选择本身含假设：把「工厂数」当单位，你就默认了解法是集中式制造——换成「屋顶数」，答案会完全不同。

## M143 · 一千辈子都不撞一次，才算够安全

**触发**：你要给一个安全关键系统定验收线，而团队和公众都在问「什么时候才算够安全」。
**他怎么说的**
> It’s never going to be perfect. No system is going to be perfect, but if you say it’s perhaps – the car is unlikely to crash in a hundred lifetimes, or a thousand lifetimes, then people are like, OK, wow, if I were to live a thousand lives, I would still most likely never experience a crash, then that’s probably OK.
— `corpus/2021-elonmuskinterviews wordpress com 2021 01 21 .txt`
**动作**
1. 先承认基线不是零：**任何人开车出事都只是概率不为零**。他明说 It’s never going to be perfect。
2. 把可靠性写成一个人能感受的尺度，而不是一个百分数。他的换算方式是：如果「一千辈子都不太可能遇到一次碰撞」，人们会接受。
3. 拿新系统和人的基线比，不跟完美比。判据是 **how much better does autonomy need to be than a person**。
4. 给出一批具体读数撑住标准——他在同一场给的读数是自动与手动每英里事故率差一个数量级。
**失效边界**：阈值只看统计不够。他自己给了反例的雏形：即使死亡减少九成，死去那一成的人仍会追责，活着的那九成没有感知。这条只解决工程判据，解决不了政治判据，两个要各自过关。

## M144 · 把成本算成每吨多少钱，再跟上一代比两个倍数

**触发**：你要评估一项技术改进值多少，而别人给你的是「便宜很多」这种形容词。
**他怎么说的**
> But still, our best-case marginal cost of launch, not taking into account overhead allocation, is about $15 million.
> Yeah, for 15 tons to orbit. Which is quite big. SpaceX – over the last year or so – has delivered about, I think, roughly two-thirds of all payloads to orbit of Earth. And most of the remaining third is China, and then everyone else is kind of miscellaneous. But it’s still $15 million, most because…
> Basically, Falcon 9 is effectively about half to a third of the cost of alternatives because of the reuse of the boost stage. With Starship, we should be able to get to the point where it’s maybe 1% the cost of an expandable system.
> Yeah, the marginal cost of launch we think can be done…. could be potentially under a million dollars for over 100 tons to orbit.
> Yes. 100 tons likely, and with refinements of the design, probably 150 tons. So essentially, it will be 10 times the payload of Falcon 9 for 15 times lower cost.
— `corpus/2021-elonmuskinterviews wordpress com 2021 10 07 .txt`
**动作**
1. 把成本换成单位量成本：钱 ÷ 有效载荷。他的现状数是约 1500 万美元 / 15 吨。
2. 写下目标档位，同样用单位量表达：他给的目标是低于 100 万美元送 100 吨以上。
3. 算两个倍数，一个都不能少：**载荷倍数**（约 10 倍）和**单位成本倍数**（约 15 倍）。只报其中一个都会误导。
4. 为差额找机构性原因，不要归给「技术进步」。他的归因是：猎鹰 9 只回收了助推级和整流罩，仍然每次丢掉上面级——「每次都要丢掉那架小飞机」。
**失效边界**：他明确说过这个数**不含间接费用分摊**，所以它是下限不是定价。另一头，倍数只在可比口径下成立：换载荷类型、轨道、复用次数，单位成本都会变。

## M145 · 它相当于便宜一万到一万五千美元的燃油卡车

**触发**：你的产品标价高于竞品，客户的第一反应是「贵」。
**他怎么说的**
> But the actual economics are even better than that because the cost of electricity is much less than the cost of gasoline. So when you look at the actual cost of ownership here, it's... You're paying much less for electricity than you are for the gasoline. You're paying much less for maintenance. There's no oil changes, no smog checks, no nothing, none of that stuff. So your maintenance is low, your cost of operations are low. And so it's actually comparable to a truck, a gasoline truck, that's 10 to $15,000 less.
— `corpus/未标年-www rev com transcripts tesla cybertruck eve.txt`
**动作**
1. 把两边的**持有成本项**列全：能源单价差、保养项，以及他列出的那些消失项——没有换机油、没有排放检测。
2. 把差额折成一个「等效燃油车价格」：他的结论是这台车相当于便宜一万到一万五千美元的燃油卡车。
3. 把这个等效价写进攻势话术，替换掉「我们更省」这种形容词。
4. 判据：折算后如果仍更贵，就不能用这套讲法——那时问题在标价，不在算法。
**失效边界**：折算依赖电价、油价、使用强度三个假设，任意两个变动都会翻结论（低利用率、高电价地区完全不成立）。他给的是美国场景、补贴前价格。

## M146 · 把价格定对，市场就会自己工作

**触发**：你发现市场在做一个明显不划算的行为，而所有参与者都很「理性」。
**他怎么说的**
> And the obvious thing to do is have a carbon tax; it’s a no-brainer. I don’t know, 90 plus percent of economists would say this, and, I think, of physicists. The market system works well if you’ve got the right price on things.
— `corpus/2021-elonmuskinterviews wordpress com 2021 06 07 .txt`
**动作**
1. 找到那个**被按零计价的成本**（他的是碳排放）。
2. 给它定一个不为零的价格。他的论述是：市场在价格正确时工作得很好，价格为零或很低时，人的行为必然跟着错。
3. 让这个价格随时间上升，用它牵引替代技术（他顺带提到 sequestration 的投入会随之起来）。
4. 判据：如果所有人都「理性」地做着同一件明显不划算的事，先查价格，不要查人。
**失效边界**：这条需要一个能征税、能改价的机构；个人和小组织只能在自己的账里做（把内部转移价格改对）。他自己也承认这是政治问题不是工程问题——不落地的话，它只是诊断。

## M147 · 断了连接也不能卡在那里

**触发**：你设计的系统依赖外部连接（云、蜂窝网、平台），而它的失效方式是「一断就废」。
**他怎么说的**
> Well, we think we can put a lot of intelligence locally in the robot and it certainly needs to be enough intelligence that if the robot gets disconnected, like if it’s a bad cellular signal or there isn’t Wi-Fi, you know, Optimus can’t just get stuck. It needs to have enough local intelligence that it can still do useful things, even if it loses the connection, kind of like the car.
— `corpus/2026-whatsuptesla com 2026 04 22 tesla q1 2026 ea.txt`
**动作**
1. 列出系统对外部连接的依赖项，逐条问：断了会怎样。
2. 把安全与基本可用性的那部分挪到本地。标准用他给的那句：**断了连接也要能做有用的事，不能卡在那里**。
3. 拿一个已存在的合格样本当参照系：车不需要蜂窝网或 Wi-Fi 就能安全驾驶。
4. 把「需要大模型才能回答的那部分」单独隔离（他的例子是语音和大模型问答），让它的失效不连带主体功能。
**失效边界**：本地化的代价是算力、功耗、成本和 OTA 复杂度；对成本极度敏感的产品不成立。而且「本地放多少」的边界会随外部网络可靠性变化——网络本来就可靠的场景里，过度本地化是浪费。


---

## 四、[案例] 有情境、有决策、有结局的具体事件

