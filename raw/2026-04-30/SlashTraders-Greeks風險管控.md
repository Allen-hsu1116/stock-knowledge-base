# 學會選擇權希臘字母才能輕鬆管控風險

**來源**：https://slashtraders.com/en/blog/option-greeks/
**日期**：2026-04-30
**主題**：操作策略

---

## Delta

Delta 是選擇權價格相對於標的價格變動的變化量。

- ATM Call Delta = 0.50：標的漲 $1，Call 漲 $0.50
- ATM Put Delta = -0.50：標的漲 $1，Put 跌 $0.50
- OTM Delta 較小，ITM Delta 較大

Delta 也可視為到期時 ITM 的機率：
- Delta 0.75 = 75% 機率 ITM
- Delta 0.50 = 50%
- Delta 0.25 = 25%

買賣不同選擇權類型的 Delta 正負：
| 策略 | Delta | 獲利方向 |
|------|-------|---------|
| Buy Call | 正 | 看多 |
| Buy Put | 負 | 看空 |
| Sell Call | 負 | 看空 |
| Sell Put | 正 | 看多 |

用正 Delta 做多頭交易（Bull Put Spread），用負 Delta 做空頭交易（Bear Call Spread）。

## Gamma

Gamma 是 Delta 相對於標的價格變動的變化量，也是選擇權價格的加速度。

同一到期日，ATM 的 Gamma 最大，越遠離市價 Gamma 越低。
同一履約價，越接近到期日 Gamma 越大：
- 35天到期 Gamma 1.26
- 6天到期 Gamma 3.39

接近到期日時 Gamma 放大，導致大幅不可預測的損益變化。
因此通常在到期前 14 天左右平倉以降低 Gamma 風險。

## Theta

Theta 是選擇權價值相對於時間的變化量，永遠為負（時間流逝 = 價值衰減）。

Theta 衰減速度：
- 約 90 天到期時衰減較慢
- 低於 30 天到期時衰減加速

這就是為什麼賣方通常賣約 30 天到期的選擇權，讓 Theta 衰減夠快可以獲利了結。

## Vega

Vega 是選擇權價值相對於 IV 變動的變化量。

高低 IV 對權利金的影響：
| 股票 | 股價 | IV | ATM Call 價值 |
|------|------|-----|--------------|
| SPY | $459.87 | 19% | $9.38 |
| MDB | $497.85 | 55% | $34.50 |

高 IV = 貴的選擇權 → 賣方利潤空間大
低 IV = 便宜的選擇權 → 買方成本低

| 策略 | Vega | 獲利方式 |
|------|------|---------|
| Buy options | 正 | IV 擴張 |
| Sell options | 負 | IV 收縮 |

## Theta + Vega 實戰：賣高報酬 Strangle

篩選條件：
- DTE > 30（安全的 Theta 衰減）
- IV Perc > 67%（IV 偏高，有收縮空間，Vega 有利）
- Open Interest > 100,000（流動性好）
- Market Cap > $10B（避免被操控）
- Squeeze = False（避免 IV 即將擴張）
- Strangle BP < $1000（分散風險）

---

## 關鍵字

- Delta
- Gamma
- Theta
- Vega
- Greeks
- IV Percentile
- Strangle
- Gamma Risk
- Theta Decay