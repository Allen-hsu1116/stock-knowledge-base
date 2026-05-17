# MFI資金流量指標 — XQ教學

**來源**：https://www.xq.com.tw/xstrader/money-flow-index-mfi%E6%8C%87%E6%A8%99/
**日期**：2026-05-17
**主題**：技術分析

---

在技術分析領域，Money Flow Index（MFI，資金流量指標） 常被稱為「價量結合的 RSI」。

與 RSI 僅考慮價格漲跌不同，MFI 將成交量 (Volume) 納入計算邏輯。其核心假設是：如果股價上漲且成交量放大，代表資金流入強勁；若價格上漲但成交量萎縮，則動能可能虛假。

MFI 的應用有如下幾個原則：

- 超買與超賣 (Extreme Overheating):

當 MFI > 80：代表資金過度擁擠，需留意獲利了結壓力。若達到 90 以上，則是極度過熱。

- 當 MFI < 20：代表資金嚴重外流，可能出現反彈機會。

- 背離訊號 (The Divergence) —— 最強大的領先特徵:

看跌背離： 股價創下新高，但 MFI 卻走低。這代表股價上漲缺乏資金後援，趨勢即將反轉。

- 看漲背離： 股價創新低，但 MFI 底部墊高。代表聰明錢正在低檔默默吸貨（Accumulation）。

- 趨勢確認:

MFI 突破 50 分界線：代表資金流入占優勢，多頭趨勢確立。

MFI的計算方法如下

Input: Length(6);
variable: tp(0), tv(0), utv(0), dtv(0), pmf(0), nmf(0), mfivalue(0);

SetInputName(1, "天數");

tp = TypicalPrice;
tv = tp * Volume;

if tp > tp[1] then
 begin
 utv = tv;
 dtv = 0;
 end
else
 begin
 utv = 0;
 dtv = tv;
 end;

pmf = Average(utv, MinList(CurrentBar, length));
nmf = Average(dtv, MinList(CurrentBar, length));

if CurrentBar < Length or (pmf + nmf) = 0 then
 mfivalue = 50
else
 mfivalue = 100 * pmf /(pmf + nmf);

Plot1(mfivalue, "MFI");

---

## 關鍵字

- MFI
- 資金流量指標
- 價量結合RSI
- 超買超賣
- 背離訊號
- 成交量加權