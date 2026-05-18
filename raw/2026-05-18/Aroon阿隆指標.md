# Aroon 阿隆指標

**來源**：
- QuantPass：https://quantpass.org/aroon/
- FinLab：https://www.finlab.tw/aroon_indicator/
- TradingView：https://tw.tradingview.com/support/solutions/43000501801/
- MBA智库百科：https://wiki.mbalib.com/zh-tw/%E9%98%BF%E9%9A%86%E6%8C%87%E6%A0%87
- TEJWIN：https://www.tejwin.com/en/insight/%E3%80%90quant%E3%80%91aroon-up-down-strategy/

**日期**：2026-05-18
**主題**：技術分析

---

## QuantPass 來源

阿隆 Aroon 指標是由 Tushar Chande 發明，主要用途是判斷趨勢的產生以及方向與強度。由兩個部分構成：Aroon-up 和 Aroon-down。

### Aroon 指標公式

Aroon-up = ((N - 價格創近期N根最高價到今天的天數) / N) × 100
Aroon-down = ((N - 價格創N根K最低價到今天的天數) / N) × 100

### Aroon 指標應用

- Aroon 指標介於 0 和 100 之間
- 當 aroon_up 達到 100 時，行情處於強勢
- 如果維持在 50~100 之間，表示上升趨勢
- 當 aroon_down 達到 0，表示處於弱勢
- 如果維持在 0~50 之間，表示下跌趨勢
- 當 aroon_down 往上穿越 aroon_up，表明潛在弱勢，預期價格下跌
- 反之 aroon_up 往上穿越 aroon_down 表示行情轉強，預期價格走高

## FinLab 回測結果

FinLab 使用 AROON 指標選股回測，設定25日週期：
- aroonup > aroondown：創高日比創低日較近期發生
- aroonup > 70
- aroondown < 30
- 出場條件：aroonup < aroondown

回測結果：aroonup > aroondown 條件效果最好，但年化報酬只有 6%，與創新高延續度動能策略相比遜色不少。市場一般參數使用下，AROON 指標效果有限，有待進一步優化。

---

## 關鍵字

- Aroon指標
- 阿隆指標
- 趨勢判斷
- Aroon Up
- Aroon Down
- Aroon Oscillator
- Tushar Chande