# Chande Kroll Stop 錢德克羅停損指標

**來源**：知識庫內部整理，基於 Tushar Chande & Stanley Kroll《The New Technical Trader》
**日期**：2026-05-10
**主題**：技術分析/風險管理

---

Chande Kroll Stop 是由 Tushar Chande 和 Stanley Kroll 在《The New Technical Trader》一書中提出的追蹤停損指標。它是 Chandelier Exit 的進階版，使用雙重 ATR 過濾和兩條停損線（做多停損線與做空停損線），提供更穩健的趨勢追蹤出場機制。

## 計算公式

### 基本變數
- ATR(n)：n 週期的平均真實波幅
- Highest High(n)：n 週期內最高價
- Lowest Low(n)：n 週期內最低價

### 做多停損線（Stop Long）
1. 第一層：Highest High(n) - ATR(n) × 乘數
2. 第二層（最終做多停損線）：取過去 x 週期內第一層的最高值
   - Stop Long = MAX(第一層, x 週期)

### 做空停損線（Stop Short）
1. 第一層：Lowest Low(n) + ATR(n) × 乘數
2. 第二層（最終做空停損線）：取過去 x 週期內第一層的最低值
   - Stop Short = MIN(第一層, x 週期)

### 預設參數
- ATR 期間（n）：10
- 乘數：2
- 第二層回顧期間（x）：20

## 核心特色

### 雙重過濾機制

第一層 ATR 計算初步停損位，第二層取回顧期間內的極值做最終過濾。這個雙重過濾比 Chandelier Exit 的單層過濾更穩健：

- Chandelier Exit：最高價 - ATR × 乘數（一層過濾）
- Chande Kroll Stop：MAX(Highest High - ATR × 乘數, 過去 x 週期)（雙重過濾）

雙重過濾的效果是：即使在劇烈波動的行情中，停損線也不會突然跳動，減少被洗出場的次數。

### 兩條停損線同時顯示

做多停損線和做空停損線同時繪製在圖表上，形成一個「停損帶」（Stop Zone）：
- 價格在做多停損線上方 → 多頭趨勢持續
- 價格在做空停損線下方 → 空頭趨勢持續
- 價格在兩線之間 → 趨勢不明，觀望

這比 Chandelier Exit 只提供一條線更完整，可以直接判斷多空狀態。

---

## 關鍵字

- Chande Kroll Stop
- 錢德克羅停損
- 追蹤停損
- ATR停損
- 雙重過濾停損
- 趨勢追蹤出場