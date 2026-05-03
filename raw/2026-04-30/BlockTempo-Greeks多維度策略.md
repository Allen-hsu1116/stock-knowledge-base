# 投資科普｜交易員常說的 Delta, Gamma, Vega, Theta 是什麼？機構私藏的選擇權概念

**來源**：https://www.blocktempo.com/option-greeks-delta-gamma-vega-theta/
**日期**：2026-04-30
**主題**：操作策略

---

Greeks（希臘字母）是由選擇權訂價公式 BSM Model 所算出來的數字，代表該選擇權目前對不同風險的曝險程度。5 種風險：Delta、Gamma、Vega、Theta、Rho，Rho 因利率變化佔比太低通常忽略。

## Delta

定義：標的資產價格上漲 1 單位，選擇權策略的損益上漲 Delta 單位。

一個選擇權契約的 Delta 值為 -1 ~ +1，越接近價內 Delta 絕對值越大。Delta 也可以看成將會被履約的機率。

## Gamma

定義：標的資產價格上漲 1 單位，選擇權策略的 Delta 上漲 Gamma 單位。

Gamma 是 Delta 的加速度，Gamma 越大 Delta 變動越快。
到期日越近、履約價越接近價平，Gamma 越大。

GameStop 散戶大戰華爾街事件就是利用 Gamma Squeeze 讓機構爆倉。

## Vega

定義：標的資產的年化隱含波動率上漲 1%，選擇權策略的損益上漲 Vega 單位。

選擇權契約離到期日越遠，Vega 越大。
波動度交易（Volatility Trading）策略主要關注 Vega 和 Theta。

## Theta

定義：時間每過 1 天，選擇權策略的損益下降 Theta 單位。

選擇權契約離到期日越近，Theta 越大。

## 利用 Greeks 建立多維度策略

每一筆選擇權交易對 Greeks 曝險的增減：

| 策略 | Delta | Gamma | Vega | Theta |
|------|-------|-------|------|-------|
| Buy Call | + | + | + | - |
| Buy Put | - | + | + | - |
| Sell Call | - | - | - | + |
| Sell Put | + | - | - | + |

### 實戰範例

市場情況：FTX 倒閉，市場暗藏流動性危機，但幣安 CZ 宣布成立紓困基金。

對未來預測：短期上漲機率較高（CZ 救市、通膨、美元下降），中期黑天鵝機率仍高（需要救市代表有大坑）。

策略邏輯：短期看不跌、長期看跌 → 相同履約價，賣出短期 Put、買入長期 Put。

產生正 Gamma、正 Vega、正 Theta，Delta 預設 0（不判斷漲跌）。

兩種思考模式：
1. 價格角度：Sell Put 短線不跌破履約價賺保證金，Buy Put 長線跌破履約價賺價差。
2. Greeks 角度：短期市場 IV 下降，Vega 偏虧但 Theta 偏賺（短期 Theta > Vega），損益不明顯。中期價格暴跌，Vega、Theta 雙賺，Delta = 0 不因下跌虧損。

## 結論

搞懂 Greeks 能讓交易策略從單一維度提升到多維度：投資組合多元完整、交易機會增加、風險控制能力變好。

---

## 關鍵字

- Greeks
- Delta
- Gamma
- Vega
- Theta
- Gamma Squeeze
- 波動度交易
- 多維度策略