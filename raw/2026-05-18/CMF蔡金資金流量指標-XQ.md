# Chaikin Money Flow (CMF，蔡金資金流量)指標

**來源**：https://www.xq.com.tw/xstrader/chaikin-money-flow-cmf%EF%BC%8C%E8%94%A1%E9%87%91%E8%B3%87%E9%87%91%E6%B5%81%E9%87%8F%E6%8C%87%E6%A8%99/
**日期**：2026-01-15
**主題**：技術分析

---

介紹過TSV 與 MFI 之後，類似概念設計出來的技術指標，還有Chaikin Money Flow (CMF，蔡金資金流量) ，把這三個指標一起應用，可以對個股目前的漲跌量能關係，有更清楚的理解。

CMF 由技術分析大師 Marc Chaikin 研發，它的核心哲學是：「收盤價相對於當天震盪區間的位置，結合成交量，最能揭示機構法人的真實意圖。」 它是判斷「吸貨（Accumulation）」與「派發（Distribution）」最精確的量化工具之一。

## 一、 CMF 的計算邏輯 (The Formula)

CMF 的計算分為三個步驟，其核心在於 「貨幣流量乘數 (Money Flow Multiplier)」：

### 1. 貨幣流量乘數 (Money Flow Multiplier, MFM)

這是 CMF 的靈魂，它觀察收盤價落在當天高低點的哪個位置：

MFM ={(Close – Low) – (High – Close)}/{High – Low)

- 如果收在最高點，乘數為 +1。
- 如果收在最低點，乘數為 -1。
- 如果收在正中間，乘數為 0。

### 2. 貨幣流量金額 (Money Flow Volume, MFV)

將乘數乘以當天的成交量：

MFV = MFM * Volume 

### 3. CMF 指數

通常取 21 天（約一個月週期）的 MFV 總和除以成交量總和：

對於研究型散戶來說，CMF 提供了比 RSI 更具支撐性的「證據」：

### 1. 零軸穿越 (The Zero Line)

- CMF > 0： 代表市場處於累積（吸貨）狀態。持續在 0 以上代表機構買盤穩定，這是多頭趨勢的健康標誌。
- CMF < 0： 代表市場處於派發（出貨）狀態。
- 高於 +0.20： 極強的多頭動能，代表資金高度集中流入。
- 低於 -0.20： 極強的空頭壓力。

### 3. 背離訊號 (Divergence) —— 最重要的領先警示

- 多頭背離： 股價創新低，但 CMF 卻在零軸附近攀升或轉正。這通常代表大戶在低檔「接刀」，是中線底部的重要訊號。
- 空頭背離： 股價創新高，但 CMF 卻在走低甚至轉負。這代表股價上漲是靠散戶情緒（Low Quality Volume），大戶已先行撤離。

以下是這個指標的腳本：

```
// CMF 指標實作
input: Length(21, "計算週期");
variable: MFM(0), MFV(0), CMF_Value(0);

// 計算貨幣流量乘數
if High <> Low then
MFM = ((Close - Low) - (High - Close)) / (High - Low)
else
MFM = 0;

MFV = MFM * Volume;

// 計算 CMF
if Summation(Volume, Length) <> 0 then
CMF_Value = Summation(MFV, Length) / Summation(Volume, Length)
else
CMF_Value = 0;

Plot1(CMF_Value, "CMF");
Plot2(0, "零軸");
```

---

## 關鍵字

- CMF
- Chaikin Money Flow
- 蔡金資金流量
- 背離
- 零軸穿越
- 吸貨派發