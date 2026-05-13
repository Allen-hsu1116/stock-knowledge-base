# 選擇權定價與避險參數Greeks進階

**來源**：https://medium.com/defi-taiwan/那些年-沒學好的選擇權-2-6934483b2f78
**日期**：2026-05-10
**主題**：操作策略/選擇權

---

## 選擇權的定價 — Pricing An Option

### 價值就是期望值

一個 Call 只在價格高於履約價時有價值，其價值為價差；一個 Put 則只在價格低於履約價時有價值，其價值同為價差。

選擇權看似複雜的定價其實也是一個「期望值」：已知現在市場價格，還有剩下多久到期，我們大概推算一個選擇權會在剩下期間內移動到 in the money 的機率，並且乘上發生這個事件發生時的價值，就是期望值了。

幾個重要的參數：
- 現價與履約價：只差 1% 就 ITM 的比差 80% 的值錢
- 距離到期日的時間：時間越長，越有機會走到 ITM
- 波動率：波動率越大，越有機會結算時 ITM

### Black-Scholes 公式

Call 的計價公式：C = S × N(d1) - K × e^(-r(T-t)) × N(d2)

簡單拆分：
- S × N(d1)：現價乘上 d1 發生的機率（執行選擇權拿到標的物的價值期望值）
- K × e^(-r(T-t)) × N(d2)：履約價 × 時間價值折價 × d2 發生的機率（執行時要付出的成本期望值）

兩者相減為選擇權的價值。

N(d2) = 選擇權到期日 ITM 的機率 = 選擇權被執行的機率

### 重點

1. Option Value = Intrinsic Value (Cash Value) + Time Value
2. Volatility 是這個公式唯一的未知數 → 反推就是 IV（隱含波動率）

一般股票的年化波動率約為 10~30%，加密貨幣市場波動更大。

## 避險參數 (Greeks)

Greeks 是一群透過定價公式推導出來的數字，用來描述某一個選擇權倉位在特定時間點、市場環境下的特性。若是投資組合中含有多個選擇權倉位，可以把 Greeks 累加起來看整體曝險。

### Delta

一個選擇權的 Delta 定義為，若標的物上升一塊錢，其價值上升或下降的值。

- Long Call: Delta 為正值
- Long Put: Delta 為負值
- ATM Call: Delta ≈ 0.5
- 越深價內: Delta 越接近 1（Call）或 -1（Put）
- 越深價外: Delta 越接近 0

**槓桿概念**：若想用 Call 組合出 ETH 漲幅的 exposure (Delta = 1)，可以買 2 個 ATM Call（每個 Delta 0.5）。ETH 大漲時 Delta 會從 1 變 2，越賺越多；大跌時 Delta 會從 1 變小，越賠越少。這就是 Convexity。

### Gamma

標的物每漲一塊錢，Delta 會漲多少。數學上就是定價公式對 S 的二階微分。

- Long Option: Gamma 恆大於零，價格每次上漲一塊，Delta 都會變高
- ATM 的 Gamma 最大
- 越接近到期日 Gamma 越大

### Theta

每當離到期日近一天，倉位會漲還是跌多少錢。

- Long Option: Theta < 0（時間是敵人）
- Short Option: Theta > 0（時間是朋友）
- Theta 影響力隨到期日接近而加速
- 最後幾天 Theta Decay 最劇烈

### Vega

隱含波動率每上漲 1%，倉位的價值變動多少。

- Long Option: Vega > 0（Long Vol）
- Short Option: Vega < 0（Short Vol）
- 距到期日越遠，Vega 影響力越大
- 距到期日越近，Vega 影響力越小

### Greeks 小結

- **Delta 與 Gamma**：描述倉位如何受標的物價格影響，構成特別的價格曲線，最直觀的訊息是總體倉位的 exposure
- **Theta 與 Vega**：描述倉位如何受時間與波動率影響。離到期日很久時，Vega 影響力較大；靠近到期日，Theta 影響力變大

## Convexity

Convexity 描述的是一條斜率不斷上升的曲線。

Long Option = Long Convexity = Long Gamma
- 賺的時候越賺越多，賠的時候越賠越少
- 這個不對稱收益是有代價的：權利金 + Theta Decay

Short Option = Short Convexity = Short Gamma = Concavity
- 賺有限，賠無限
- 但可以不斷賺取時間價值和權利金

Convexity 的應用：
- DeFi 中的 Uniswap LP 是 Short Convexity（無常損失 = Short Gamma）
- 用選擇權可以對沖 IL：因為 LP 是 Short Gamma，Option 是 Long Gamma

---

## 關鍵字

- Black-Scholes 定價公式
- Delta 方向性曝險
- Gamma 加速度
- Theta 時間衰減
- Vega 波動率敏感度
- Convexity 凸性 非對稱收益
- Intrinsic Value 內在價值
- Time Value 時間價值
- Implied Volatility IV 隱含波動率
- ATM ITM OTM
- Short Vol Long Vol