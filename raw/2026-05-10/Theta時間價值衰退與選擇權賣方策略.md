# Theta時間價值衰退與選擇權賣方策略

**來源**：
- https://www.opkevin.cc/深入了解選擇權中的theta：時間對選擇權價值的影響/
- https://www.passiveseeds.com/stock-and-options/theta-for-option-sellers-why-time-decay-is-the-ultimate-friend/
- https://medium.com/defi-taiwan/那些年-沒學好的選擇權-2-6934483b2f78
- https://slashtraders.com/en/blog/option-greeks/
**日期**：2026-05-10
**主題**：操作策略

---

## Theta是什麼

Theta（θ）是選擇權希臘字母之一，衡量選擇權價值隨時間流逝的衰減速率。

公式：Θ = ∂V/∂t（選擇權價格對時間的偏微分）

白話文：每過一天，其他條件不變，選擇權價格會變動多少。

- 選擇權買方：Theta為負值，每天都在虧損時間價值
- 選擇權賣方：Theta為正值，每天坐享時間價值流逝

### 時間價值的本質

選擇權價值 = 內在價值（Intrinsic Value）+ 時間價值（Time Value / Extrinsic Value）

內在價值是「現在立刻結算可以拿到的價值」，時間價值是「因為還沒到期，未來可能變成價內的機率價值」。

所有選擇權到期時，時間價值歸零——這就是Theta的戰場。

## Theta衰退的三大特性

### 1. 非線性加速：越接近到期衰退越快

Theta衰退不是線性的，而是加速的：

- 距到期300天→299天：幾乎沒有感覺
- 距到期30天→29天：開始有明顯衰退
- 距到期2天→1天：時間價值可能腰斬

比喻：像融化的冰塊，越接近消失融化越快。

對賣方的啟示：最後30天是Theta衰退的「黃金收割期」，但Gamma風險也最大。

### 2. 價平（ATM）選擇權Theta最大

- ATM（At-the-Money）：Theta絕對值最大，因為不確定性最高
- ITM（In-the-Money）：Theta較小，因為大部分價值已經是內在價值
- OTM（Out-of-the-Money）：Theta較小，因為時間價值本身就不多

對賣方的啟示：賣ATM選擇權收取最多時間價值，但Delta風險也最大。

### 3. 週選 vs 月選的Theta差異

- 週選擇權：最後幾天Theta衰退極快，適合短線賣方
- 月選擇權：Theta衰退較平緩，適合中長線賣方
- 實務建議：賣方選擇30-45天到期的選擇權，平衡Theta收益與Gamma風險

## Theta與其他Greeks的交互關係

### Theta vs Gamma：時間與波動的對價

這是選擇權最重要的對價關係：

- Long Option：Long Gamma（賺波動）、Short Theta（賠時間）
- Short Option：Short Gamma（賠波動）、Long Theta（賺時間）

**白話文**：你付的權利金，本質上就是在「買Gamma、賣Theta」。

賣方收的權利金，就是在「賣Gamma、買Theta」——用承擔波動風險換取時間價值。

### Theta vs Vega：時間與波動率的拉扯

- 離到期日越遠：Vega影響力大，Theta影響力小
- 離到期日越近：Theta影響力大，Vega影響力小

實務啟示：
- 買方在遠月選擇權主要對抗Vega風險
- 賣方在近月選擇權主要收割Theta收益
- 30天左右的選擇權，Theta和Vega影響力最均衡

### Delta-Gamma-Theta三角關係

以Long Call為例：
- Delta > 0：標的漲我賺
- Gamma > 0：漲越多Delta越大，賺越多
- Theta < 0：每過一天都在虧時間價值

Convexity的本質：Long Option的收益曲線是凸的（convex），「賺的時候越賺越多，賠的時候越賠越少」——但這個不對稱收益的代價就是Theta衰退。

## 選擇權賣方的Theta收割策略

### Covered Call掩護性買權

最保守的Theta策略：持有現股+賣出Call

- 收取權利金，降低持股成本
- 股價不漲或小跌：賺權利金
- 股價大漲：股票被叫走，少賺上漲但權利金落袋
- 風險：股價大跌的下行風險仍在

### Cash-Secured Put現金擔保賣出

想買股票但想便宜買：

- 賣出Put收取權利金
- 股價維持在履約價之上：權利金全收
- 股價跌破履約價：以較低價格買入股票（扣掉權利金後成本更低）
- Theta收益：每天時間價值流逝都在賺

### Iron Condor鐵兀鷹

中性策略，同時賣出Call Spread和Put Spread：

- 四個腿都是賣方，Theta收益最大
- 預期股價在區間內盤整時最適合
- 定義風險：最大虧損是履約價差減去權利金
- Theta衰退在30天內最明顯

### 對角價差Diagonal Spread

垂直價差+時間價差的混合體：

- 買遠月ATM/ITM選擇權（Long Theta影響小）
- 賣近月OTM選擇權（Short Theta衰退快）
- 同時賺取近月的Theta衰退和遠月的Vega/Vega差
- Rolling策略是殺手鐧：近月到期後再賣下一期，持續收租

## Theta衰退的風險管理

### 1. Gamma風險：Theta的影子敵人

賣方賺Theta，但承擔Gamma風險：

- 股價大幅波動時，Gamma讓Delta急速變化
- 賣方損失可能遠超收取的權利金
- 解法：通常在到期前14天左右平倉，避開Gamma風險最大的最後兩週

### 2. 波動率風險（Vega）

IV突然飆升（如財報、重大事件）：

- 選擇權價值暴漲，賣方帳面虧損巨大
- 解法：避開財報日前後、重大事件前賣出選擇權

### 3. 被指派風險

- 賣出選擇權可能被提前指派
- 尤其是除息前的Call，容易被提前指派
- 解法：注意除息日，避免在除息前賣深度價內Call

### 4. 部位控制

- 賣方的獲利有限（最多收權利金），虧損可能無限
- 解法：嚴格部位控制，單一交易風險不超過帳戶的2-5%

## 實戰Theta判讀要點

1. **看Theta絕對值**：Theta=-5代表每天虧5點（買方），或每天賺5點（賣方）
2. **看Theta/Gamma比值**：Theta/Gamma比值高的策略，時間價值收益占優勢
3. **看時間價值佔比**：時間價值佔權利金比例高的選擇權，Theta衰退的絕對金額大
4. **週選賣方黃金期**：最後5天Theta衰退最猛烈，但Gamma風險同步放大
5. **月選賣方穩定收割**：30-45天到期，Theta衰退與Gamma風險的甜蜜點

---

## 關鍵字

- Theta
- 時間價值衰退
- Time Decay
- 選擇權賣方
- Covered Call
- Iron Condor
- Gamma風險
- 選擇權Greeks
- 價平選擇權
- 週選月選