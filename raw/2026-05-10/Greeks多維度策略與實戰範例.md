# Greeks多維度策略與實戰範例

**來源**：https://www.blocktempo.com/option-greeks-delta-gamma-vega-theta/
**日期**：2026-05-10
**主題**：操作策略/選擇權

---

## Greeks 建立多維度策略

搞懂 Greeks 之後，交易策略就能從單一維度提升到多維度，好處是：
- 投資組合多元、完整
- 交易機會增加
- 風險控制能力變好

## Delta

定義：標的資產價格上漲 1 單位，選擇權策略的損益上漲 Delta 單位。

一個選擇權契約的 Delta 值為 -1 ~ +1，越接近價內（in the money）選擇權契約，Delta 絕對值越大。這也代表了越大的 Delta 在履約日時，越有機會被履約，所以 Delta 也可以看成將會被履約的機率。

Delta 和其他 Greeks 隨時都在變化，原因是計算 Greeks 的 input 有標的資產價格以及時間。

## Gamma

定義：標的資產價格上漲 1 單位，選擇權策略的 Delta 上漲 Gamma 單位。

Gamma 可以想像成 Delta 的加速度，如果 Gamma 越大，會讓 Delta 變動的越快。

選擇權契約的到期日越近、履約價越接近價平，其 Gamma 越大。

GameStop 散戶大戰華爾街事件，就是有人利用 Gamma Squeeze 讓華爾街的機構爆倉。

## Vega

定義：標的資產的年化隱含波動率上漲 1%，選擇權策略的損益上漲 Vega 單位。

選擇權契約離到期日越遠，Vega 越大。

波動度交易（Volatility Trading）策略，主要關注的變數就是 Vega 和 Theta。

## Theta

定義：時間每過 1 天，選擇權策略的損益下降 Theta 單位。

選擇權在到期日結算前除了內在價值（Intrinsic value）之外，還會有時間價值。

選擇權契約離到期日越近，Theta 越大。

## 買賣 Call、Put 對 Greeks 曝險的影響

| 操作     | Delta | Gamma | Vega | Theta |
|----------|-------|-------|------|-------|
| 買 Call  | +     | +     | +    | -     |
| 賣 Call  | -     | -     | -    | +     |
| 買 Put   | -     | +     | +    | -     |
| 賣 Put   | +     | -     | -    | +     |

每一筆選擇權交易對 Greeks 曝險的增減，舉例來說，Sell Put 的 Theta 為正，代表每經過一天，Theta 會帶來獲利；而 Vega 為負，所以隱含波動率上升，Vega 會使策略虧損。

## 實戰範例：用 Greeks 建立策略

### 市場情況假設
全球前三大交易所 FTX 倒閉，市場暗藏流動性危機，但幣安 CZ 宣布成立紓困基金救流動性，因此市場反彈。

### 對未來市場預測
因為 CZ 救市，加上通膨、美元下降、全球股市反彈等因素，短線上漲機率較高。但中期利率市場仍然緊繃，既然需要救市代表肯定有大坑需要補，未來還是會爆，市場黑天鵝機率仍高。

### 建立策略邏輯
綜合市場情況與對未來的預測，總結短期看不跌、長期看跌，所以選擇在相同的履約價，賣出短期的 Put、買入長期的 Put，產生正 Gamma、正 Vega、正 Theta 的策略，至於 Delta 可以用期貨隨時調整所以預設為 0，原因是不想判斷漲跌。

兩種思考模式：
1. **就價格點位的角度**：Sell Put 短線不跌破履約價就賺保證金，Buy Put 長線跌破履約價就賺價差。
2. **就 Greeks 的角度**：短期不跌甚至反彈的情況下，市場隱含波動率下降，但因為策略為正 Vega 所以會虧錢。但策略中的 Theta 會賺錢，而且短線（距離到期日越近）期權佔比 Theta 比較重、Vega 比較輕，所以 Sell Put 賺、Buy Put 賠，損益不明顯。而過了一陣子價格暴跌後，策略變成 Vega、Theta 雙賺，而當初 Delta 為 0 所以不會因為價格下跌而虧損，損益狀況大概是短期持平、等長線的大跌出現大賺一筆。

---

## 關鍵字

- Delta 方向性曝險
- Gamma 加速度 Delta變化率
- Theta 時間衰減
- Vega 波動率敏感度
- Greeks多維度策略
- Gamma Squeeze
- 波動率交易 Volatility Trading
- Calendar Spread 日曆價差