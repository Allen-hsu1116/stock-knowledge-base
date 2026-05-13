# Stochastic RSI 隨機RSI

**來源**：
- https://tw.tradingview.com/support/solutions/43000502333/
- http://bwtdteaching.blogspot.com/2009/10/rsistochastic-rsi.html
- https://academy.binance.com/en/articles/stochastic-rsi-explained
**日期**：2026-05-04
**主題**：技術分析

---

## 什麼是 Stochastic RSI

Stochastic RSI（隨機RSI）是將隨機震盪指標的計算方式應用在 RSI 值上，由 Tushar Chande 和 Stanley Kroll 在1994年出版的《新技術交易員》中提出。

標準 RSI 衡量一段時間內的平均價格變化，而 Stochastic RSI 則增加 RSI 的敏感度，更精確地衡量超買或超賣狀態。

## 計算公式

StochRSI = (RSI - Lowest Low RSI) / (Highest High RSI - Lowest Low RSI)

- RSI：時間週期內的 RSI 值
- Lowest Low RSI：時間週期內 RSI 的最低值
- Highest High RSI：時間週期內 RSI 的最高值

14日 StochRSI 的基準：
- StochRSI = 1：RSI 在14日內創新高
- StochRSI = 0.8：RSI 接近14日內高點
- StochRSI = 0.5：RSI 在14日高低範圍中間
- StochRSI = 0.2：RSI 接近14日內低點
- StochRSI = 0：RSI 在14日內創新低

有些版本會將結果乘以100，使範圍變為0-100。

## 參數設定

- RSI 長度：預設14（計算RSI的時間週期）
- 隨機長度：預設14（計算隨機指標的時間週期）
- K：預設3（%K平滑期數）
- D：預設3（%D平滑期數）

## 如何觀察

### 超買/超賣
- StochRSI 高於0.8（或80）→ 超買
- StochRSI 低於0.2（或20）→ 超賣
- 上升趨勢中找超賣進場點
- 下降趨勢中找超買進場點

### 背離
- 正乖離（底背離）+ StochRSI 回升至0.2以上→ 可能上升趨勢
- 負乖離（頂背離）+ StochRSI 回落至0.8以下→ 可能下降趨勢

### %K與%D交叉
- %K上穿%D→ 看漲訊號
- %K下穿%D→ 看跌訊號

## 重要提醒

1. StochRSI 是「指標的指標」，距離價格兩步之遙，可能與實際價格走勢短暫脫節
2. 速度比標準 RSI 快很多，產生更多訊號（包括好訊號和壞訊號）
3. 必須與其他工具或指標結合使用
4. 使用趨勢線或基本圖表型態分析可幫助識別主要趨勢
5. 不要用 StochRSI 做與潛在趨勢相反的交易
6盪市場中容易產生頻繁的假訊號

## 與標準 RSI 的區別

| 特徵 | RSI | Stochastic RSI |
|------|-----|----------------|
| 計算基礎 | 價格 | RSI 值 |
| 靈敏度 | 中等 | 很高 |
| 訊號頻率 | 較少 | 較多 |
| 超買/超賣 | 70/30 | 0.8/0.2 |
| 鈍化問題 | 有 | 加劇 |
| 適用場景 | 趨勢判斷 | 精確進出場時機 |

---

## 關鍵字

- Stochastic RSI
- 隨機RSI
- StochRSI
- 超買超賣
- 背離
- RSI靈敏度
- %K %D交叉