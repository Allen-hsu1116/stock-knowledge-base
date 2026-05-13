# Elder-Ray Index 牛熊力量指標

**來源**：https://www.xq.com.tw/xstrader/elder-ray-index/
**日期**：2026-05-11
**主題**：技術分析

---

艾爾德射線 (Elder-Ray Index)，又常被稱為牛熊力量指標 (Bull & Bear Power)，是由擁有精神科醫師背景的傳奇交易員亞歷山大·艾爾德博士 (Dr. Alexander Elder) 所發明。

這套指標的命名極具巧思：「Ray」代表 X 光射線。艾爾德博士認為，K 線圖只是市場的皮膚，而這套指標就是市場的 X 光機，能看穿皮膚底下「多頭（貪婪）」與「空頭（恐懼）」雙方力量的真實骨架。

## 1. 設計理念：精神醫學視角下的「價值共識」

艾爾德射線的底層邏輯，建立在三個行為金融學的假設上：

- **價值共識 (Value Consensus)**：艾爾德認為，指數移動平均線 (通常使用 13 日 EMA) 代表了這段期間內，多空雙方妥協後的「合理價值共識」。

- **多頭的最大推升力 (Bull Power)**：當天的最高價 (High)，代表多頭在盤中最極度貪婪、傾盡全力把價格往上推的極限位置。
  - 公式：Bull Power = High – 13日 EMA
  - 意義：測量多頭能把股價拉離「價值共識」多遠。

- **空頭的最大下砸力 (Bear Power)**：當天的最低價 (Low)，代表空頭在盤中製造最大恐慌、把價格往下砸的極限位置。
  - 公式：Bear Power = Low – 13日 EMA
  - 意義：測量空頭能把股價壓離「價值共識」多深。

## 2. 實戰應用指南

這套指標在視覺呈現上極具特色，它通常包含一個趨勢指標 (EMA) 與兩個柱狀圖 (Bull Power & Bear Power)。這套邏輯能完美解決散戶「順勢交易中找不到進場點」的痛點。

### 最高勝率買點：多頭趨勢中的「空頭力竭」

- **背景**：13 日 EMA 趨勢向上（大方向是多頭）。
- **觸發**：Bear Power 柱狀圖處於零軸之下（股價回檔，空頭發力），但柱狀體開始縮短、向上勾頭。
- **行為學意義**：大趨勢向上，但盤中空頭試圖把價格砸破價值共識（EMA）。當 Bear Power 向上勾，代表「空頭砸盤的力量已經耗盡」，這是順勢交易中極佳的拉回買點。

### 最高勝率空點：空頭趨勢中的「多頭力竭」

- **背景**：13 日 EMA 趨勢向下。
- **觸發**：Bull Power 柱狀圖處於零軸之上，但柱狀體開始縮短、向下彎折。
- **行為學意義**：跌勢中的反彈，多頭傾盡全力也無法繼續將價格推離 EMA，多頭氣力放盡，是極佳的反彈空點。

### 終極反轉訊號：力量背離 (Power Divergence)

- 股價創新高，但 Bull Power 柱狀圖卻比前一波低 → 多頭情緒耗竭，即將見頂。
- 股價創新低，但 Bear Power 的負值柱狀圖卻比前一波淺 → 空頭情緒耗竭，即將見底。

## 3. XScript 指標腳本

```
// 指標名稱：Elder-Ray Index (艾爾德射線 / 牛熊力量指標)
// 理論基礎：Dr. Alexander Elder
Input: Length(13, "EMA 計算週期");
Variable: ValueEMA(0), BullPower(0), BearPower(0);

// 1. 計算市場價值共識 (13 日 EMA)
ValueEMA = XAverage(Close, Length);

// 2. 計算多頭力量與空頭力量
BullPower = High - ValueEMA;
BearPower = Low - ValueEMA;

// 3. 繪圖輸出
Plot1(BullPower, "多頭力量(Bull)");
Plot2(BearPower, "空頭力量(Bear)");
Plot3(0, "價值共識(零軸)");
```

---

## 關鍵字

- Elder-Ray Index
- 牛熊力量指標
- Bull Power
- Bear Power
- 力量背離
- Power Divergence
- 價值共識
- EMA