# 考夫曼自適應均線 (Kaufman's Adaptive Moving Average, KAMA)

**來源**：https://www.xq.com.tw/xstrader/考夫曼自適應均線-kaufmans-adaptive-moving-average-kama/
**日期**：2026-05-11
**主題**：技術分析

---

由傳奇量化大師 Perry Kaufman 在其著作《Smarter Trading》中所發明的經典指標，專門用來解決「均線在盤整期被打臉」的問題。

跟傳統均線的差異在於 KAMA 引入了一個「效率係數 (Efficiency Ratio, ER)」。

這個係數的計算公式如下：

- 趨勢盤： 價格直直衝，位移跟路徑很接近，ER趨近於 1。KAMA 會變得非常靈敏（像短期均線）。
- 震盪盤： 價格上下刷，位移很小但路徑很長，ER 趨近於 0。KAMA 會自動停滯，變成一條水平線。

過濾假突破的邏輯：

當市場出現假突破（瞬間暴漲但隨即拉回）時，雖然價格動了，但「路徑」變長了，導致 ER 下降。KAMA 會判定這是「噪音」而拒絕跟隨。只有當價格「穩定且有效率」地移動時，KAMA 才會轉向。

KAMA 的核心哲學是：「當市場充滿雜訊（盤整）時，均線應該停止移動；當訊號明確（趨勢）時，均線應該加速追趕。」

## 2. 計算公式詳解

KAMA 的計算分為三個步驟，邏輯非常嚴謹：

### Step 1: 計算效率係數 (ER)

ER = Direction / Volatility

- Direction = |Close - Close[n]|（價格淨位移，直線距離）
- Volatility = Sum(|Close - Close[1]|, n)（價格總路徑，每日波動總和）

ER 範圍 0~1：
- ER → 1：趨勢明確，價格直衝
- ER → 0：盤整震盪，路徑遠大於位移

### Step 2: 計算平滑常數 (Smoothing Constant, SC)

- FastSC = 2 / (FastEnd + 1)（預設 FastEnd=2，最快EMA週期）
- SlowSC = 2 / (SlowEnd + 1)（預設 SlowEnd=30，最慢EMA週期）
- SC = [ER × (FastSC - SlowSC) + SlowSC]²

平方運算壓抑雜訊，讓 SC 在低 ER 時趨近 SlowSC，高 ER 時趨近 FastSC。

### Step 3: 計算 KAMA

KAMA = KAMA[1] + SC × (Close - KAMA[1])

第一根 Bar 直接用收盤價初始化。

## 3. XScript (XQ 語法) 完整腳本

```
// 指標名稱：Kaufman's Adaptive Moving Average (KAMA)
Input:
Period(10, "計算週期 (ER)"),
FastEnd(2, "最快EMA週期"),
SlowEnd(30, "最慢EMA週期");

Variable: Direction(0), Volatility1(0), ER(0);
Variable: FastSC(0), SlowSC(0), SC(0);
Variable: KAMA_Val(0);

Once begin
FastSC = 2 / (FastEnd + 1);
SlowSC = 2 / (SlowEnd + 1);
end;

Direction = AbsValue(Close - Close[Period]);
Volatility1 = Summation(AbsValue(Close - Close[1]), Period);

if Volatility1 > 0 then
ER = Direction / Volatility1
else
ER = 0;

SC = Power(ER * (FastSC - SlowSC) + SlowSC, 2);

if CurrentBar = 1 then
KAMA_Val = Close
else
KAMA_Val = KAMA_Val[1] + SC * (Close - KAMA_Val[1]);

Plot1(KAMA_Val, "KAMA");
```

## 4. 產品應用：如何利用 KAMA 過濾假突破？

### 情境：假突破 (False Breakout)

- 現象：股價瞬間大漲，突破了前波高點。
- 傳統均線反應：因為價格大漲，傳統 MA (如 5MA) 會立刻勾頭向上，發出買進訊號 → 結果買在最高點，隔天大跌（假突破）。
- KAMA 的反應：雖然價格位移（分子）變大了，但如果這次突破是伴隨著劇烈的上下刷洗（分母 Volatility 更大），ER 值反而會很低。
- 結果：KAMA 線會保持水平，甚至幾乎不動。
- 策略意義：這告訴交易者：「價格雖然動了，但效率很低，這不是穩健的趨勢，不要追價！」

### 情境：真趨勢 (True Trend)

- 現象：股價穩步推升，每天都漲一點點，回檔很淺。
- KAMA 的反應：位移大，但總路徑也短（因為沒有多餘的震盪）。ER 值接近 1。
- 結果：KAMA 會突然加速，緊緊貼著價格上揚。
- 策略意義：這是高效率趨勢，大膽買進！

### 總結

KAMA 就像是一個「有潔癖」的均線。它痛恨雜訊，只有在趨勢非常乾淨時才會進場。

---

## 關鍵字

- KAMA
- 考夫曼自適應均線
- 效率係數 ER
- 假突破過濾
- 自適應移動平均線