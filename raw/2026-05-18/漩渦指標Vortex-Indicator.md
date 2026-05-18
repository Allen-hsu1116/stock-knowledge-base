# 漩渦指標 Vortex Indicator (VI)

**來源**：https://www.xq.com.tw/xstrader/%E6%BC%A9%E6%B8%A6%E6%8C%87%E6%A8%99/
**日期**：2026-05-18
**主題**：技術分析

---

漩渦指標 (Vortex Indicator, VI) 是由 Etienne Botes 和 Douglas Siepman 於 2010 年一月發表在《Technical Analysis of Stocks & Commodities》雜誌上的指標。靈感來自於流體力學中的「漩渦流」。

- 核心原理：
大多數指標只看收盤價，但漩渦指標關注「波幅的連續性」。它測量價格向上移動的能量 VI+與向下移動的能量 VI-之間的距離。

當正向漩渦流 VI+強勢穿過負向漩渦流 VI- 時，代表一股強大的上升氣流已經形成，這通常不是假突破，而是真實的趨勢結構改變。

- 為什麼能過濾假突破？
它對「盤整」非常敏感。在沒有明確趨勢時，VI+ 與 VI- 會糾纏在一起（像 DNA 雙螺旋）。只有當兩者「開口顯著擴大」時，才視為有效訊號。這比單純的均線交叉更難造假。

VI 的價值在於它不僅僅是「趨勢指標」，它更是一個能量流向指標。它解決了傳統均線（MA）最大的痛點：均線只能告訴你「過去」發生了什麼，但 VI 試圖告訴你目前的趨勢能量是否足以延續。

## 1. 漩渦指標 (VI) 的核心意義

VI 的靈感來自於奧地利自然學家 Viktor Schauberger 對水流漩渦的研究。他發現水流的能量是透過螺旋運動產生的。

在金融市場中，VI 將這種概念轉化為兩股力量的博弈：

- 正向漩渦VI+： 買方力量。試圖將價格推向比昨天更高的高點。
計算：今日最高價與昨日最低價的距離。

- 負向漩渦 VI-： 賣方力量。試圖將價格推向比昨天更低的低點。
計算：今日最低價與昨日最高價的距離。

## 2. XScript (XQ 語法) 完整腳本

```
Input: Length(14, "計算週期");
Variable: VM_Plus(0), VM_Minus(0);
Variable: Sum_VM_Plus(0), Sum_VM_Minus(0), Sum_TR(0);
Variable: VI_Plus(0), VI_Minus(0);
Variable: TR(0);

// 1. 計算單根 K 線的漩渦移動量 (Vortex Movement)
// 邏輯：今天的高點離昨天的低點有多遠 (多頭力道)
VM_Plus = AbsValue(High - Low[1]);

// 邏輯：今天的低點離昨天的高點有多遠 (空頭力道)
VM_Minus = AbsValue(Low - High[1]);

// 2. 計算真實波幅 (True Range)
TR = TrueRange;

// 3. 進行週期累加 (Summation)
Sum_VM_Plus = Summation(VM_Plus, Length);
Sum_VM_Minus = Summation(VM_Minus, Length);
Sum_TR = Summation(TR, Length);

// 4. 計算最終指標數值 (歸一化)
if Sum_TR <> 0 then begin
VI_Plus = Sum_VM_Plus / Sum_TR;
VI_Minus = Sum_VM_Minus / Sum_TR;
end;

// 5. 繪圖輸出
Plot1(VI_Plus, "VI+ (多頭)");
Plot2(VI_Minus, "VI- (空頭)");
Plot3(VI_Plus-VI_Minus,"差額");
```

## 3. 實戰應用

#### A. 標準用法：交叉訊號 (Crossover)

- 買進： 紅線 (VI+) 由下往上穿過 綠線 (VI-)。
- 賣出： 紅線 (VI+) 由上往下穿過 綠線 (VI-)。
- 缺點： 在盤整時會頻繁交叉（假訊號）。

#### B. 進階用法：閾值確認 (Threshold Confirmation)

為了過濾假突破，您可以設定一個「有效區間」：
- 邏輯： 只有當 VI+ 大於 1.1 且 VI- 小於 0.9 時，才認定多頭趨勢正式展開。
- 意義： 這代表買方力道不僅僅是贏過賣方，而且是「壓倒性」的勝利。

#### C. 與 MACD 的差異

- MACD 是基於均線的收斂發散，反應較慢。
- VI 是基於價格的高低點幾何關係，反應通常比 MACD 快，且對「轉折」更敏感。

## 4. 針對「假突破」的特別觀察

當價格創新高，但 VI+ 沒有同步創新高（甚至開始下滑），這就是著名的頂部背離 (Bearish Divergence)。

這通常是主力在拉高出貨的徵兆，是過濾「假突破真拉回」最強力的訊號之一。

---

## 關鍵字

- 漩渦指標
- Vortex Indicator
- VI+
- VI-
- 趨勢判斷
- 假突破過濾
- 能量流向
- 背離