# Elder-Ray Index 牛熊力量指標

**來源**：https://www.xq.com.tw/xstrader/elder-ray-index/
**日期**：2026-03-05
**主題**：技術分析

---

艾爾德射線 (Elder-Ray Index)，又常被稱為牛熊力量指標 (Bull & Bear Power)，是由傳奇交易員亞歷山大·艾爾德博士 (Dr. Alexander Elder) 所發明。

「Ray」代表 X 光射線。艾爾德博士認為，K 線圖只是市場的皮膚，而這套指標就是市場的 X 光機，能看穿皮膚底下「多頭（貪婪）」與「空頭（恐懼）」雙方力量的真實骨架。

## 設計理念：行為金融學的「價值共識」

- 價值共識 (Value Consensus)：指數移動平均線 (通常使用 13 日 EMA) 代表多空雙方妥協後的「合理價值共識」。
- 多頭的最大推升力 (Bull Power)：當天的最高價 (High)，代表多頭在盤中最極度貪婪、傾盡全力把價格往上推的極限位置。公式：Bull Power = High – 13日 EMA
- 空頭的最大下砸力 (Bear Power)：當天的最低價 (Low)，代表空頭在盤中製造最大恐慌、把價格往下砸的極限位置。公式：Bear Power = Low – 13日 EMA

## 實戰應用

### 最高勝率買點：多頭趨勢中的「空頭力竭」
- 背景：13 日 EMA 趨勢向上（大方向是多頭）
- 觸發：Bear Power 柱狀圖處於零軸之下（股價回檔，空頭發力），但柱狀體開始縮短、向上勾頭
- 行為學意義：大趨勢向上，空頭砸盤的力量已經耗盡，這是順勢交易中極佳的拉回買點

### 最高勝率空點：空頭趨勢中的「多頭力竭」
- 背景：13 日 EMA 趨勢向下
- 觸發：Bull Power 柱狀圖處於零軸之上，但柱狀體開始縮短、向下彎折
- 行為學意義：跌勢中的反彈，多頭傾盡全力也無法繼續將價格推離 EMA，極佳的反彈空點

### 終極反轉訊號：力量背離 (Power Divergence)
- 股價創新高，但 Bull Power 柱狀圖卻比前一波低 → 多頭情緒耗竭，即將見頂
- 股價創新低，但 Bear Power 的負值柱狀圖卻比前一波淺 → 空頭情緒耗竭，即將見底

## XScript 指標腳本

```
Input: Length(13, "EMA 計算週期");
Variable: ValueEMA(0), BullPower(0), BearPower(0);
ValueEMA = XAverage(Close, Length);
BullPower = High - ValueEMA;
BearPower = Low - ValueEMA;
Plot1(BullPower, "多頭力量(Bull)");
Plot2(BearPower, "空頭力量(Bear)");
Plot3(0, "價值共識(零軸)");
```

---

## 關鍵字

- Elder-Ray Index
- 牛熊力量指標
- Alexander Elder
- Bull Power
- Bear Power
- 13日EMA
- 力量背離
- 空頭力竭
- 多頭力竭