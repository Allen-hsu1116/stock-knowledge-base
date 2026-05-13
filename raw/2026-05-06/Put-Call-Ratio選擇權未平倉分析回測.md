# Put/Call Ratio 選擇權的未平倉分析

**來源**：https://futuresinvest90223.com/put-call-ratio-選擇權的未平倉分析/
**日期**：2026-05-06
**主題**：籌碼面分析

---

期交所每天盤後有公布選擇權買權和賣權的數據。Put/Call Ratio分為成交量和未平倉量。若是「成交量的Put/Call Ratio」，就是用Put的成交量除以Call的成交量，若是「未平倉量的Put/Call Ratio」，即「用Put的未平倉量除以Call的未平倉量之比例」的意思。

在成交量的Put/Call Ratio方面，若Put/Call Ratio值越大，代表Put的交易越較Call的交易活絡；在未平倉量的Put/Call Ratio方面，若Put/Call Ratio值越大，代表Put的未平倉量大於Call的未平倉量，但不代表未來看跌。

Put Call Ratio(簡稱PCR) = Put 全市場未平倉量 / Call 全市場未平倉量

未平倉Put/Call Ratio又被解讀為散戶指標。原因是選擇權多為散戶參與，因此PUT(賣權)/CALL(買權)相除的比值(Ratio)，可大致看出台指選擇權市場裡散戶與大戶的心態；反而PCR數值越高代表未來看多，PCR越低代表未來看空。

## 回測結果

交易策略範例：當P/C ratio大於某個數值就買進多單，小於某個數值就買進空單。

改進版：PCR連續大於一定的值超過3天則做多，連續小於一定的數值3天做空，過了3天如果仍未獲利創新高則平倉出場。

結論：PCR適合判斷大盤方向多空，利用選擇權未平倉比當濾網長期得到不錯的效果。搭配K棒的型態判斷更能提升策略的品質穩定度。

---

## 關鍵字

- Put/Call Ratio
- PCR
- 未平倉量
- 散戶指標
- 逆向指標
- 回測