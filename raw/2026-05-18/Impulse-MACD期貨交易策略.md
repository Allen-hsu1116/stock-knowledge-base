# Impulse MACD 期貨交易策略

**來源**：https://www.tejwin.com/insight/impluse-macd-%e6%9c%9f%e8%b2%a8%e4%ba%a4%e6%98%93%e7%ad%96%e7%95%a5/
**日期**：2025-11-06
**主題**：技術分析

---

## 前言

LazyBear 是在國際知名交易平台 TradingView 上極具影響力的指標開發者。他創作了大量廣受歡迎的客製化技術指標，其開源的程式碼啟發了全球無數量化交易員與技術分析愛好者。LazyBear 的指標通常專注於改善傳統指標的延遲性，並結合獨特的市場觀察來捕捉趨勢與動能。

本次採用的「Impulse MACD」即為他的代表作之一。此指標並非傳統的指數平滑異同移動平均線（MACD），而是進行了顯著的改良：它使用零延遲的雙指數移動平均線（DEMA）來更快速地響應價格變化，並結合平滑化（SMMA）的高低價通道來判斷市場的「衝量」（Impulse）。其核心思想是，只有當價格動能與趨勢方向一致時，產生的交易信號才更具價值，藉此過濾掉部分盤整行情中的雜訊。

## 投資標的與回測期間

以台灣指數期貨（台指期, TX）作為唯一的交易標的，使用每日的最高價、最低價與收盤價資料進行指標計算與回測。實際回測期間訂為 2019 年 1 月 1 日至 2025 年 9 月 12 日。

## 核心邏輯

### 1. 指標系統 (Indicator System)

1. 計算 HLC/3（高、低、收盤價的平均）
2. 使用零延遲雙指數移動平均（DEMA）來快速反應價格變化
3. 透過價格與高/低價平滑移動平均通道（SMMA）的關係，計算出主要的動盪指標 md（快線）
4. 對 md 進行簡單移動平均，得到信號線 sb（慢線）

### 2. 進場信號 (Entry Signal)

- 當快線 md 由下往上穿越慢線 sb 時，產生買進信號
- 當快線 md 由上往下穿越慢線 sb 時，產生賣出信號

### 3. 出場與風險管理 (Exit & Risk Management)

採用基於 ATR（平均真實波幅）的移動停損（Trailing Stop-Loss）機制。停損點會隨著價格朝著對倉位有利的方向動態調整，藉此鎖定利潤並嚴格控制下檔風險。

### 4. 合約轉倉 (Contract Rolling)

在期貨合約到期前，策略會自動將即將到期的合約平倉，並在新近月合約上建立相同的部位，以確保回測的連續性。

## 指標計算函數關鍵邏輯

### _smma 函數（平滑移動平均線）

計算 SMMA（Smoothed Moving Average），計算方式為：
- 第一個值使用 SMA
- 之後每個值 = (前一個 SMMA × (period - 1) + 當前值) / period

### calculate_indicators 函數

1. hlc3 = (high + low + close) / 3
2. atr = ATR(high, low, close, atr_len)
3. High_smma = SMMA(high, ma_len)
4. Low_smma = SMMA(low, ma_len)
5. hlc3_zlema = DEMA(hlc3, ma_len)
6. md = hlc3_zlema > High_smma ? hlc3_zlema - High_smma : (hl3_zlema < Low_smma ? hlc3_zlema - Low_smma : 0)
7. sb = SMA(md, sig_len)

**參數設定**：
- ma_len = 30
- sig_len = 8
- atr_len = 20
- atr_multiplier = 3.25

## 倉位管理與風險控制

- 使用 _get_tx_chain_state 輔助函數確認整個台指期產品鏈的總持倉口數，避免轉倉期間重複下單
- 無倉位時：根據買賣信號建立多頭或空頭倉位（1口）
- 持倉時：啟動 ATR 移動停損機制
  - 多頭：停損價 = 當前價 - 3.25 × ATR，只往上調整
  - 空頭：停損價 = 當前價 + 3.25 × ATR，只往下調整
- 轉倉：到期前 5 天自動將舊合約平倉，在新月合約上建立相同部位

---

## 關鍵字

- Impulse MACD
- LazyBear
- DEMA
- SMMA
- ATR移動停損
- 期貨交易
- 台指期
- 趨勢追蹤
- 零延遲均線