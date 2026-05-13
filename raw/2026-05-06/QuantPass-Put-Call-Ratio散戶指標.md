# Put Call Ratio - 好用的散戶指標、選擇權未平倉比例分析

**來源**：https://quantpass.org/put-call-ratio/
**日期**：2026-05-06
**主題**：籌碼面分析

---

期交所每天盤後會公布選擇權買權和賣權的數據。
Put/Call Ratio 分為成交量和未平倉量。
若是「成交量的 Put/Call Ratio」，就是用 Put 的成交量除以 Call 的成交量。
若是「未平倉量的 Put/Call Ratio」，即「用 Put 的未平倉量除以 Call 的未平倉量之比例」的意思。

## 成交量的 Put/Call Ratio

在成交量的 Put/Call Ratio 方面，若 Put/Call Ratio 越大，代表 Put 的交易越較 Call 的交易活絡，市場偏空看待。

## 未平倉量的 Put/Call Ratio

在未平倉量的 Put/Call Ratio 方面，若 Put/Call Ratio 越大，代表 Put 的未平倉量大於 Call 的未平倉量，市場氣氛偏空。

PCR = Put 全體市場未平倉量 / Call 全體市場未平倉量

但是未平倉 Put/Call Ratio 又被解讀為散戶指標。原因是選擇權多為散戶參與，因此 Put（賣權）/Call（買權）相除的比值（Ratio），可大致看出台指選擇權市場裡散戶與大戶的心態；所以 PCR 數值越高代表未來看多，反之 PCR 越低代表未來看空。

資料來源：台灣期交所

## Put/Call Ratio 交易策略範例 – MultiCharts

把相關資料從 QuoteManager 匯入，再交給 Multicharts 來運算，透過回測分析在什麼位置以上偏多，在什麼位置以下偏空。

把 data1 放台指期 data2 放未平倉 P/C ratio。

簡單範例測試：當 P/C ratio 大於某個數值就做多，當 P/C ratio 小於某個數值就做空。

加上 K 棒濾網重新回測。

---

## 關鍵字

- Put Call Ratio
- PCR
- 散戶指標
- 選擇權未平倉量
- 成交量PCR
- 未平倉PCR
- 反向指標
- MultiCharts回測