# 鱷魚線 Alligator 指標與碎形交易

**來源**：https://tradeciety.com/fractals-trading-use-alligator-williams-chaos-theory, https://concords.moneydj.com/z/glossary/glexp_5140.djhtm, https://www.dcnfutures.tw/news/details.php?id=2052, https://www.oanda.com/bvi-ft/lab-education/technical_analysis/moving_average-displaced/, https://www.fx110.com.tw/special/9584
**日期**：2026-05-16
**主題**：技術分析

---

## 鱷魚線 Alligator 指標

鱷魚線（Alligator）是 Bill Williams 在 1998 年提出的技術指標，旨在判定趨勢方向與盤整狀態。它由三條不同週期的平滑移動平均線（SMMA）組成，分別代表鱷魚的顎（Jaw）、齒（Teeth）、唇（Lip）。

### 公式

**藍色顎線（Jaw）**：
1. Median Price: MPt = (Ht + Lt) / 2
2. 取 MPt 的 13 日平滑移動：EMPt = EMPt-1 + 2 / (13+1) × (MPt - EMPt-1)
3. 取 8 天前的 EMPt 值作為當天的顎線值：JWt = EMAt-8

**紅色齒線（Teeth）**：
1. Median Price: MPt = (Ht + Lt) / 2
2. 取 MPt 的 8 日平滑移動：EMPt = EMPt-1 + 2 / (8+1) × (MPt - EMPt-1)
3. 取 5 天前的 EMPt 值作為當天的齒線值：TWt = EMAt-5

**綠色唇線（Lip）**：
1. Median Price: MPt = (Ht + Lt) / 2
2. 取 MPt 的 5 日平滑移動：EMPt = EMPt-1 + 2 / (5+1) × (MPt - EMPt-1)
3. 取 3 天前的 EMPt 值作為當天的唇線值：LPt = EMAt-3

### 核心概念

- **鱷魚睡覺（盤整）**：三條線糾纏在一起，表示市場處於盤整狀態
- **鱷魚醒來（趨勢啟動）**：三條線開始分開，表示趨勢即將開始
- **多頭排列**：由下而上依顎→齒→唇排列，鱷魚醒來覓食，看多
- **空頭排列**：由下而上依唇→齒→顎排列，鱷魚吃飽閉嘴，看空
- **睡眠越長，飢餓越大**：盤整越久，突破後的行情越大

### 碎形 Fractal 交易法

碎形（Fractal）是 Bill Williams 系統的第一維度，是進出場訊號的基礎：

**定義**：
- 向上碎形：連續 5 根 K 線，中間那根的最高價最高（兩側各有兩根較低的高點）
- 向下碎形：連續 5 根 K 線，中間那根的最低價最低（兩側各有兩根較高的低點）

**有效性判斷**：
- 向上碎形必須高於紅色齒線才是有效碎形
- 向下碎形必須低於紅色齒線才是有效碎形
- 在齒線另一側的碎形為無效碎形

**無效碎形變有效碎形**：原來的無效碎形，經過幾天紅色齒線不斷下降/上升後，原碎形超過幾天後的紅色齒線，則無效碎形變成有效碎形。

**交易規則**：
- 採用最新的碎形為準，新碎形出現後，之前的碎形即不可再用
- 上漲突破有效的向上碎形是作多訊號
- 跌破有效的向下碎形是作空訊號
- 在 Buy Stop 訂單放在有效向上碎形高點上方一個 tick
- 在 Sell Stop 訂單放在有效向下碎形低點下方一個 tick

### Bill Williams 混沌交易法五維度

Bill Williams 的混沌交易法將市場結構分為五個維度：
1. **碎形（Fractal）**：第一維度，進場訊號
2. **動能（Momentum / AO）**：第二維度，加碼訊號
3. **加速/減速（AC）**：第三維度，加碼訊號
4. **區域（Zone）**：第四維度，加碼訊號
5. **平衡線（Balance Line / Alligator）**：第五維度，加碼訊號

### 與其他 Bill Williams 指標的組合

- **Alligator + Fractal**：最基礎的組合，用 Alligator 判斷趨勢方向，用 Fractal 找進場點
- **Alligator + AO**：AO 確認動能方向，配合 Alligator 的趨勢判斷
- **Alligator + Gator Oscillator**：Gator 顯示 Alligator 三條線之間的收斂/發散程度
- **Alligator + AC**：AC 確認動能加速或減速

### 實戰操作步驟

1. **觀察鱷魚狀態**：先看三條線是糾纏（睡覺/盤整）還是分開（醒來/趨勢）
2. **確認趨勢方向**：線分開後，看排列方式確認多空
3. **尋找有效碎形**：趨勢方向確認後，找有效的碎形進場點
4. **設定進場單**：在有效碎形的高低點設 Stop Buy/Sell
5. **用 AO/AC 加碼**：進場後根據動能指標加碼
6. **出場**：鱷魚開始收斂（線糾纏）時出場

### 使用建議

- 推薦使用較大時間週期（4小時圖、日線圖）
- 預設參數（13/8/5，偏移 8/5/3）不用更改
- 市場約 70% 時間盤整、30% 時間趨勢，鱷魚睡覺時不要進場
- 嘴唇在上方不做空，嘴巴在下方不做多
- 價格在嘴唇上方只買入，價格在嘴巴下方只賣出

---

## 關鍵字

- 鱷魚指標
- Alligator
- Bill Williams
- 碎形
- Fractal
- 顎線齒線唇線
- SMMA
- 置換移動平均線
- 混沌交易法
- 趨勢判斷
- 盤整過濾