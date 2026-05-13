# Aroon 阿隆指標實戰判讀

**來源**：
- https://quantpass.org/aroon/
- https://www.tejwin.com/en/insight/%E3%80%90quant%E3%80%91aroon-up-down-strategy/
- https://www.finlab.tw/aroon_indicator/

**日期**：2026-05-04
**主題**：技術分析

---

## 原文整理

### 什麼是 Aroon 指標

Aroon 指標由 Tushar Chande 於 1995 年發明，主要用途是判斷趨勢的產生以及方向與強度。它由兩個部分構成，分別為 Aroon-Up 和 Aroon-Down。

### Aroon 計算公式

Aroon-Up = ((N - 價格創N日最高價到今天的天數) / N) × 100
Aroon-Down = ((N - 價格創N日最低價到今天的天數) / N) × 100

一般預設 N = 25（25日週期）。

### Aroon 指標的應用方式

Aroon 指標介於 0 和 100 區間：

- Aroon-Up 達到 100 時，行情處於強勢
- Aroon-Up 維持在 50~100 之間，表示上升趨勢
- Aroon-Up 向下跌破 50 時，表示向上的趨勢正在失去動力
- Aroon-Down 達到 0 時，表示處於弱勢
- Aroon-Down 維持在 0~50 之間，表示下跌趨勢
- Aroon-Down 向下跌破 50 時，表示向下的趨勢正在失去動力
- 兩個指標都在低位，表示股價沒有明確的趨勢（盤整）
- 指標在 70 以上，表示趨勢十分強烈
- 指標在 30 以下，表明相反的趨勢正在醞釀

### 交叉訊號

- Aroon-Down 往上穿越 Aroon-Up：表明潛在弱勢，預期價格開始趨於下跌
- Aroon-Up 往上穿越 Aroon-Down：表示行情開始轉強，預期價格會走高

### Aroon Oscillator

Aroon-Osc = Aroon-Up - Aroon-Down

- 正數時，代表創高日離近期較近，創低日較遠，股票處於創高的強勢過程
- 負數時，代表股票正在下跌創低的過程
- 在 0 附近時，是典型的無趨勢特徵，股票處於盤整階段

### TEJ 回測策略條件

**進場條件**：Aroon Up > 80 且 Aroon Down < 45 → 買進
**出場條件**：Aroon Down > 55 且 Aroon Up < 45 且兩指標差距 > 15 → 賣出
**加碼條件**：Aroon Up > 55 且 Aroon Down < 45 且差距 > 15 且投入本金 ≤ 20%本金 且有充足現金

### FinLab 回測結果

- aroonup > aroondown 的條件回測效果最好，但年化報酬只有 6%
- 與「創新高延續度動能策略」相比效果遜色
- 市場一般參數使用下無法得到太好效果，需要進一步優化

---

## 關鍵字

- Aroon指標
- Aroon-Up
- Aroon-Down
- Aroon-Oscillator
- 趨勢判斷
- 動量指標
- Tushar Chande