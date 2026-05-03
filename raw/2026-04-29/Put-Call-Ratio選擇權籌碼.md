# Put Call Ratio – 選擇權未平倉比例分析

**來源**：https://quantpass.org/put-call-ratio/ + https://gooptions.cc/put-call-ratio/
**日期**：2026-04-29
**主題**：籌碼面分析

---

## Put Call Ratio 介紹

期交所每天盤後公布選擇權買權和賣權的數據。Put/Call Ratio 分為成交量版和未平倉量版。

### 成交量的 Put/Call Ratio

- 公式：Put 成交量 / Call 成交量
- PCR 越大 → Put 交易比 Call 活絡 → 市場偏空看待

### 未平倉量的 Put/Call Ratio

- 公式：PCR = Put 全體市場未平倉量 / Call 全體市場未平倉量
- 未平倉 PCR 被解讀為「散戶指標」
- 原因：選擇權多為散戶參與，散戶傾向買 Put（看空保護）和買 Call（看多投機）
- **但賣方才是大戶**，所以 PCR 的反向解讀：
  - PCR 數值越高 → 散戶偏空（買很多Put），大戶偏多 → **未來看多**
  - PCR 越低 → 散戶偏多（買很多Call），大戶偏空 → **未來看空**

### 實戰技巧

1. **搭配支撐壓力表看細節**：把每日選擇權未平倉口數和支撐壓力表的最大增量比對
2. **看 Call Put 籌碼內容組成**：分辨是誰在買、誰在賣
   - 價平附近大戶賣方多 → 區間盤整機率高
   - 價外極端大量 → 可能有極端行情

### MultiCharts 交易策略範例

- Data1 放台指期、Data2 放未平倉 P/C ratio
- 當 P/C ratio 大於某閾值 → 做多
- 當 P/C ratio 小於某閾值 → 做空
- 加上 K 棒濾網可提高勝率

---

## 關鍵字

- Put Call Ratio
- PCR
- 選擇權未平倉量
- 散戶指標
- 賣權買權比
- 選擇權籌碼