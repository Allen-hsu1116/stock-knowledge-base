# CCI順勢指標 - TradingView + OANDA 整合

**來源**：https://tw.tradingview.com/support/solutions/43000502001/ + https://www.oanda.com/bvi-ft/lab-education/technical_analysis/commodity-channel-index/
**日期**：2026-05-02
**主題**：技術分析

---

## TradingView CCI定義

順勢指標（Commodity Channel Index, CCI），是技術分析中的動量指標，通過測量價格偏離其統計平均值的變化，來識別超買和超賣水平。CCI是非常著名且廣泛使用的指標，除了超買/超賣水平外，還經常用於發現反轉和背離。

由Donald Lambert創立並於1980年發表，首先出現在當時的Commodities雜誌。

## CCI計算公式

CCI = (Typical Price - 20 Period SMA of TP) / (.015 x Mean Deviation)

Typical Price (TP) = (High + Low + Close)/3

常數0.015是出於縮放目的設置的，透過包含該常數，大多數CCI值將落在100到-100範圍內。

計算均值偏差分為三個步驟：
1. 從該期間的每個典型價格（TP）減去最近的20日簡單移動平均值
2. 嚴格使用絕對值，並對這些數字求和
3. 將步驟2中生成的值除以周期總數

## 超買/超賣

CCI主要功能是識別超買或超賣：

- 可以按照傳統意義確定反轉。但真正的超買/超賣閾值可能因資產而異，波動較大的資產閾值可能為200和-200
- CCI超買和超賣也可以視為動量增加：在看漲趨勢中超買表示趨勢加強，在看跌趨勢中超賣表示趨勢加強

## CCI背離

動量通常在價格變化之前率先變化：

- **看漲背離**：價格跌至較低的低點而CCI跌至較高的低點
- **看跌背離**：價格創出較高的高點而CCI創下較低的高點

## OANDA CCI用法

### 順勢操作

當CCI由下往上突破+100時應買進，由上往下跌破-100時賣出。平倉通常在重新回到±100%內側時進行。

當市場變動劇烈時，CCI會同時超過±100%和±200%，此時不進場交易。

### 與0軸的交叉

CCI在0%時，表示移動平均與現值一致。CCI向上超出0軸＝現值與移動平均的黃金交叉，向下穿過＝死亡交叉。

CCI顯示與平均價格的乖離，使用Typical Price使其性質能敏感反應市場的價格變動。

類似的技術指標有移動平均乖離率，但CCI根據平均差的原則，因此其圖形能反應價格震盪幅度（波動性volatility）。

參數預設14，期間較短容易反應細微價格變動，期間較長則呈現較為和緩的變化。

---

## 關鍵字

- CCI指標
- 背離
- 超買超賣
- 0軸交叉
- Typical Price
- Mean Deviation