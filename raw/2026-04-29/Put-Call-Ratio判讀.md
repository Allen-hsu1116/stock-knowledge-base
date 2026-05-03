# Put/Call Ratio 判讀 — 散戶指標與實戰技巧

**來源**：
- https://quantpass.org/put-call-ratio/
- https://gooptions.cc/put-call-ratio/
**日期**：2026-04-29
**主題**：籌碼面分析

---

## 量化通 QuantPass 文章內容

期交所每天盤後會公布選擇權買權和賣權的數據。Put/Call Ratio 分為成交量和未平倉量。

### 成交量的 Put/Call Ratio

用 Put 的成交量除以 Call 的成交量。Put/Call Ratio 越大，代表 Put 的交易較 Call 的交易活絡，市場偏空看待。

### 未平倉量的 Put/Call Ratio（PCR）

PCR = Put 全體市場未平倉量 / Call 全體市場未平倉量

未平倉 PCR 越大，代表 Put 的未平倉量大於 Call 的未平倉量，市場氣氛偏空。

但未平倉 PCR 又被解讀為散戶指標。原因是選擇權多為散戶參與，因此 PUT/CALL 相除的比值，可大致看出台指選擇權市場裡散戶與大戶的心態；所以 PCR 數值越高代表未來看多，反之 PCR 越低代表未來看空。

### 交易策略範例

- 把台指期 data1 和未平倉 P/C ratio data2 放入 MultiCharts
- 簡單策略：當 P/C ratio 大於某個數值就做多，小於某個數值就做空
- 可加上 K 棒濾網提升勝率

---

## Gooptions 文章重點

### Put Call Ratio 兩個交易技巧

1. **看未平倉量的 PCR** — 賣權未平倉量除以買權未平倉量，反映散戶多空情緒
2. **對照支撐壓力表最大增量** — 把每日選擇權未平倉口數和支撐壓力表的最大增量進行比對，找相關蛛絲馬跡

### PCR 的反向解讀

PCR 本質是散戶指標：
- PCR 偏高 → 散戶偏空（買很多 Put）→ 逆向思考偏多
- PCR 偏低 → 散戶偏多（買很多 Call）→ 逆向思考偏空

---

## 關鍵字

- Put/Call Ratio
- PCR
- 散戶指標
- 選擇權未平倉量
- 逆向思考
- 支撐壓力表