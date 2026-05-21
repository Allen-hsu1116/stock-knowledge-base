# 斬波指標 Choppiness Index (CHOP)

**來源**：https://www.xq.com.tw/xstrader/%E6%96%AC%E6%B3%A2%E6%8C%87%E6%A8%99choppiness-index-chop/
**日期**：2026-05-18
**主題**：技術分析

---

這是由澳洲商品交易員 E.W. Dreiss 開發的指標，它利用 「分形幾何 (Fractal Geometry)」 的概念來量化市場的「混亂程度」。

- 核心原理： 它不是方向性指標（不告訴你漲跌），而是「狀態指標」。

數值範圍 0~100。

- CHOP > 61.8： 市場處於高度混亂（Choppy）、無序震盪。這時候任何突破都極可能是假的。

- CHOP < 38.2： 市場處於高效趨勢中，趨勢正在運行。

- 如何用它確認趨勢？ 這是一個完美的「濾網 (Filter)」。

當你的主策略（如 MACD 或 突破策略）發出買進訊號時，檢查 CHOP。

- 如果 CHOP > 50，忽略訊號（視為假突破）。
- 如果 CHOP < 50，確認訊號（趨勢有效）。

## 1. 核心數學與公式詳解

CHOP 的數學基礎建立在混沌理論與分形幾何 (Fractal Geometry) 之上。它利用價格的「幾何維度」來判斷市場效率。

- 概念邏輯：
  - 高效率（趨勢）： 價格走勢像一條直線，兩點之間距離最短。這時 CHOP 數值低。
  - 低效率（盤整）： 價格走勢像一團亂麻，雖然走了很長的路（波動大），但最後沒移動多少距離。這時 CHOP 數值高。

#### 計算公式

步驟拆解：

- 真實波幅 (True Range, TR)： 計算每日的波動幅度（包含跳空缺口）。
- 路徑總長 (Sum of TR)： 將過去 N 天的 TR 加總。這代表價格實際「走過的路」。
- 直線距離 (Range)： 過去 N 天的最高價減去最低價。這代表價格實際「產生的位移」。
- 對數比率： 計算「路徑總長」與「直線距離」的比率，並取對數（Logarithm）。這就是在計算分形維度。

公式：CHOP = 100 * LOG10( SUM(ATR(1), n) / ( MaxHi(n) - MinLo(n) ) ) / LOG10(n)

## 2. 指標意義與數值解讀

CHOP 的數值範圍在 0 到 100 之間，與費波南希數列 (Fibonacci) 密切相關：

- CHOP > 61.8 (盤整/混亂)：
  - 意義： 市場處於高度混亂狀態，缺乏明確方向。
  - 能量觀點： 這通常代表「能量正在壓縮」，就像彈簧被壓縮一樣。數值越高，未來爆發大行情的機率越高。
  - 操作建議： 空手或進行區間操作（高出低進），切勿追價。

- CHOP < 38.2 (趨勢)：
  - 市場處於高效趨勢中，可順勢操作。

- 38.2 ~ 61.8 (過渡區)：
  - 市場正在轉換體制，訊號不明確。

## 3. XScript (XQ 語法) 完整腳本

```
// 指標名稱：Choppiness Index (CHOP)
// 作者：E.W. Dreiss
Input: Length(14, "計算週期");
Variable: TR(0), SumTR(0);
Variable: MaxHi(0), MinLo(0), RangeLen(0);
Variable: CHOP(0);

// 1. 計算真實波幅 (True Range)
TR = TrueRange;

// 2. 計算分子：路徑總長 (過去 N 天波動總和)
SumTR = Summation(TR, Length);

// 3. 計算分母：直線位移 (過去 N 天的高低區間)
MaxHi = Highest(High, Length);
MinLo = Lowest(Low, Length);
RangeLen = MaxHi - MinLo;

// 4. 核心公式計算
if RangeLen > 0 and SumTR > 0 then begin
Value1 = SumTR / RangeLen;
CHOP = 100 * Log(Value1) / Log(Length);
end else begin
CHOP = 50;
end;

// 5. 繪圖輸出
Plot1(CHOP, "Choppiness Index");
Plot2(61.8, "盤整界線 (Fib 61.8)");
Plot3(38.2, "趨勢界線 (Fib 38.2)");
```

## 4. 實戰應用

可以將 CHOP 定位為 「假突破過濾神器」：

#### 應用 A：突破策略的「保險絲」

- 痛點： 用戶常抱怨：「看到布林通道開口打開就追進去，結果馬上反轉被套牢。」
- 解法： 當您的策略發出「突破訊號」時，背後先檢查 CHOP。
  - 情境 1： 價格突破新高，但 CHOP > 60。判定： 這是假突破機率極高。
  - 情境 2： 價格突破新高，且 CHOP < 50。判定： 趨勢有效，可進場。

#### 應用 B：抓「起漲點」 (The Squeeze)

- CHOP 最迷人的地方在於極值。
- 當 CHOP 數值飆升到 70 以上（極度壓縮），代表波動率低到極點。這就像是暴風雨前的寧靜。
- 可以設計一個選股條件：「尋找 CHOP > 70 的股票」。這份清單就是 「即將變盤（大漲或大跌）」 的潛力股清單。

### 總結

CHOP 是一個 「中立」 的指標，它不帶有多空偏見。這正是它強大的原因，因為它客觀地描述了市場的結構效率。

---

## 關鍵字

- Choppiness Index
- CHOP
- 斬波指標
- 波動指數
- 趨勢判斷
- 盤整判斷
- 分形幾何
- E.W. Dreiss
- Fibonacci 61.8
- 假突破過濾