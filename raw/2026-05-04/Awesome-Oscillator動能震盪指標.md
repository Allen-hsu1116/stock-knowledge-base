# Awesome Oscillator動能震盪指標

**來源**：https://sabiotrade.com/blog/awesome-oscillator-the-gift-from-bill-williams
**日期**：2026-05-04
**主題**：技術分析

---

## Awesome Oscillator 動能震盪指標

The Awesome Oscillator, developed by Bill Williams, is a unique market analysis tool that stems from his trading system, which is based on the notion that market movements are inherently chaotic. This indicator appears as a histogram in a separate window below the main chart, with bars colored green or red, depending on the movement's direction relative to a zero line.

### 計算公式

Awesome Oscillator = SMA(5) – SMA(34)

其中SMA使用的是中位數 (High + Low) / 2，而非收盤價。這區別了AO與MACD——MACD使用收盤價計算。

AO屬於震盪指標群，但沒有固定的刻度（沒有超買超賣區間）。

### 優勢

1. **多功能性**：在股票和貨幣市場都表現良好
2. **易取得**：在大多數交易平台上都有，包括手機版
3. **不重繪（No Repainting）**：訊號不會隨時間消失
4. **有效性**：作為Bill Williams交易策略的一部分，在實踐中已證明其有效性
5. **自足性**：獨立分析價格運動的各個方面，不需要額外的分析工具

### 缺點

1. **訊號滯後**：雖然是震盪指標，但仍有輕微延遲
2. **固定設定**：開發者嵌入的設定不能更改，只能使用現有參數（5期和34期）
3. **短時間框架假訊號**：在短時間間隔上傾向產生過多雜訊，日內交易者不太喜歡

### 三種交易訊號

#### 1. 背離訊號（Divergence）

當AO的方向與價格趨勢不同時，產生背離訊號。在重要支撐壓力位出現背離時尤其有效。

- **看跌背離**：價格創新高但AO沒有創新高 → 可能反轉向下
- **看漲背離**：價格創新低但AO沒有創新低 → 可能反轉向上

Bill Williams還定義了「碟形」（Saucer）訊號：
- **看漲碟形**：AO在零軸上方，連續三根柱狀圖，中間的比兩邊的低 → 續漲訊號
- **看跌碟形（Inverted Saucer）**：AO在零軸下方，連續三根柱狀圖，中間的比兩邊的高 → 續跌訊號

#### 2. 零軸交叉訊號（Zero Line Cross）

- AO柱狀圖從下方穿越零軸 → 買入訊號
- AO柱狀圖從上方穿越零軸 → 賣出訊號

**重要**：零軸交叉是AO三種訊號中最不可靠的，通常需要其他過濾工具確認。單獨依賴此訊號開倉可能導致較多的假進場。

#### 3. 雙峰訊號（Twin Peaks）

- **看漲雙峰**：AO在零軸下方出現兩個低點，第二個比第一個高，且兩者之間沒有穿越零軸 → 買入訊號
- **看跌雙峰**：AO在零軸上方出現兩個高點，第二個比第一個低，且兩者之間沒有穿越零軸 → 賣出訊號

### AO + Parabolic SAR組合策略

買入條件：
- Parabolic SAR移動到圖表下方（點位在價格下方）
- AO已在零軸上方，最後一根柱狀圖為綠色

賣出條件：
- Parabolic SAR在圖表上方
- AO從上方穿越零軸
- AC（加速震盪指標）畫出紅色柱狀圖

停損設在Parabolic標記的價位，獲利在Parabolic SAR換邊時出場。此策略在小時圖上表現最佳。

### 使用建議

1. 兩條移動平均線：慢線34期判趨勢方向，快線5期找進場機會
2. 避免減少趨勢組件的期間以避免市場雜訊
3. 最可靠的訊號是零軸穿越，表示強趨勢運動
4. 在不活躍市場中，「碟形」訊號可能只是小幅價格變動
5. 最佳交易時段為歐洲和美國交易時段
6. 在M30以上時間框架使用，最好不低於H1
7. 用布林通道等通道指標確認AO訊號
8. 「鱷魚」指標（Bill Williams另一工具）最適合與AO搭配使用
9. 用成交量指標驗證背離訊號

---

## 關鍵字

- Awesome Oscillator
- Bill Williams
- 動能震盪指標
- 零軸交叉
- 背離訊號
- 碟形訊號
- 雙峰訊號
- Parabolic SAR
- 鱷魚指標