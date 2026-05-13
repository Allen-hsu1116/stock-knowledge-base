# Hull Moving Average (HMA) 赫爾移動平均線

**來源**：https://www.oanda.com/bvi-ft/lab-education/technical_analysis/moving_average-hull/
**來源**：https://www.taindicators.com/hma/
**來源**：https://alanhull.com/the-hull-moving-average/
**來源**：https://seekingalpha-tainan.blogspot.com/2017/07/hull-moving-averagehma.html
**日期**：2026-05-11
**主題**：技術分析

---

## OANDA Lab 原文

Hull移動平均線開發是為了降低多種移動平均線會延遲的弱點，同時還能減少假訊號。英文為「Hull Moving Average」，取其字母縮寫做HMA。這個方法是由澳洲的Allen Hull所開發，中文稱為赫爾移動平均線或船型移動平均線。

這個方法是組合了重視最近價格變動的加權移動平均（Weighted Moving Average：WMA），而且以一定的係數平均，因此降低了延遲與假訊號的多重移動平均線（移動平均線的移動平均線）。

例如n週期的Hull移動平均線是以「n÷2日WMA乘以2倍，然後減掉n日WMA，將所得結果以n的平方根日WMA平均」計算。

如果要看21日期間，則是10WMA，也就是乘以最近10日間的過度加權，然後以平方根參數平均來計算。由於計算的是過度移動平均，因此對價格變動的追隨性更好（參照圖1），有時可能超越價格變動，是其特徵之一。

在MT4/MT5不屬標準配備的功能，因此需取得製作的自定義指標。另外，有些類型的製作的自定義指標還會將上述的計算進一步平均，這時候形狀會與原來計算式的形狀大不相同，需多加注意。

Hull移動平均線與其他的移動平均線相比，即可一目瞭然看出其特徵。從圖2可看出期間20的Hull移動平均線（HMA）、簡單移動平均線（SMA）、指數平滑移動平均線（EMA）。HMA（綠・橙）貼著蠟燭線變動，相對地，SMA（藍）與EMA（紅）則位於較遠離的位置緩緩變動。

例如在圖中右端，HMA轉而向下變動，但是SMA與EMA仍然繼續往上變動。從這裡也可看出，HMA會追隨實際的蠟燭線的動態，和參數相同的SMA與EMA的走向完全不同。

使用Hull移動平均線時，只需1條線就足夠了。因為對蠟燭線的追隨性極為良好，透過傾斜角度就可以簡單的看出市場趨勢。Hull也能和其他類型的移動平均線同樣，組合短期線與長期線，但是建議先使用1條線，來清楚掌握當下趨勢。

## taindicators 原文

赫爾移動平均線 (HMA) 試圖最大限度地減少傳統移動平均線的滯後，同時保持移動平均線的平滑度。HMA指標由 Alan Hull 於 2005 年開發，利用加權移動平均線來優先考慮較新的價格,大大減少滯後。所得的平均值反應較靈敏，非常適合辨識買入點。

### 計算方法

WMA1 = WMA(n/2) 的價格
WMA2 = WMA(n) 的價格
RawHMA = (2 * WMA1) - WMA2
HMA = WMA(sqrt(n)) of RawHMA

### HMA如何降低滯後

- 加權移動平均數 (WMA) 本身就具有降低滯後的特性，原理是賦予較近期數據更高的權重。
- 為了進一步減少滯後，我們可以使用兩種 WMA 互相抵消。 其中一個 WMA 只涵蓋指定時間框架最近一半的區間，從而更加聚焦於近期價格。
- 最終的平滑處理會使用另一個週期更少的 WMA（週期數為指定時間框架週期數的平方根），這樣就能使計算結果更傾向於近期數據。
- 最終的結果將會得到一條貼近價格曲線的平滑移動平均線。

### 應用例子

由於 HMA 的平滑特性和對價格變化的反應能力，它在趨勢識別中可能特別有用。用HMA 確認趨勢，您可以觀察 HMA 線的斜率:

- 向上傾斜的 HMA 表示看漲趨勢，
- 而向下傾斜的 HMA 表示看跌趨勢。

儘管交叉訊號（例如，短期MA 與長期MA 交叉）在多種類型的移動平均線中都很常用，但HMA 創建者Alan Hull 不建議使用HMA 交叉訊號，因為該技術依賴於查看不同移動平均線之間的滯後差異。兩條移動平均線，HMA移動平均線的滯後已大大減少。 相反，他建議尋找轉折點來確定買入和賣出。當整體趨勢向上且HMA轉向向上時，這是買入的訊號。 反之，當整體趨勢向下且HMA轉向向下時，這是賣出的訊號。

## Alan Hull 原始文章

Traditional moving averages lag the price activity. But with some clever mathematics the lag can be minimised. Here's how!

Back in 2005 when I was working on a new indicator I was temporarily sidetracked by trying to solve the problem of lag in moving averages, the outcome of which was the Hull Moving Average.

Since then the HMA has found its way into charting programs around the world and is regularly discussed on traders bulletin boards in different languages around the world. It was the result of an intellectual curiosity which I placed into the public domain by writing the following article.

The Hull Moving Average solves the age old dilemma of making a moving average more responsive to current price activity whilst maintaining curve smoothness. In fact the HMA almost eliminates lag altogether and manages to improve smoothing at the same time.

Consider a series of 10 numbers from '0' to '9' inclusive and imagine that they are successive price points on a chart with 9 being the most recent price point at the right hand leading edge.

If we take the 10 period simple average of these numbers then, not surprisingly, we will determine the midpoint of 4.5 which significantly lags behind the most recent price point of 9. Here's the clever bit, first let's halve the period of the average to 5 and apply it to the most recent numbers of 5, 6, 7, 8 and 9, the result being the midpoint of 7.

Finally, to remove the lag we take the midpoint of 7 and add the difference between the two averages which equals 2.5 (7 – 4.5). This gives a final answer of 9.5 (7 + 2.5) which is a slight overcompensation. But this overcompensation is very handy because it offsets the lagging effect of the nested averaging.

Hence the result of combining these 2 techniques is a near perfect balance between lag reduction and curve smoothing. The HMA manages to keep up with rapid changes in price activity whilst having superior smoothing over an SMA of the same period.

The HMA employs weighted moving averages and dampens the smoothing effect (and resulting lag) by using the square root of the period instead of the actual period itself.

Hull Moving Average (HMA) formula:
Integer(SquareRoot(Period)) WMA [2 x Integer(Period/2) WMA(Price) – Period WMA(Price)]

A simple application for the HMA, given its superior smoothing, would be to employ the turning points as entry/exit signals. However it shouldn't be used to generate crossover signals as this technique relies on lag.

## 程式交易快譯通原文

HMA基本上是從WMA(Weighted Moving Average)進化而來，WMA基本上就是給最近的收盤價最高權重，依序等量遞減(WMA與EMA的差別，就是權重遞減方是不同，前者等量遞減，後者以指數式遞減)。

PowerLanguage程式碼：

inputs:Length(20) ;
vars:MA(0),HMA(0);
MA=2*WAverage(close,IntPortion(Length*0.5))-WAverage(close,Length);
HMA=WAverage(MA,IntPortion(SquareRoot(Length)));
Plot1(HMA,"HMA") ;

IntPortion()函式是取整數之用。

跟上面解說範例的差異，實際HMA在計算MA_all及MA_w時是以WMA來計算(各位看官也可以採SMA甚至EMA取代看看有何不同效果)。此外，HMA在最後計算WMA時，取的期間再開一次根號，是何用意？如果不這麼做的話，在計算變數MA及變數HMA，前後做了兩次WAverage計算，其實等於已經把近20+20=40根K棒都抓進來運算，反而讓更多舊的價格來影響均線值，故以程式碼中Length=20，開根號取整數等於4，把權重還給近期價格。

HMA與其他均線比較：把HMA、AMA以及SMA放在一起比較，可以發現HMA(水藍色)最為敏感，最為貼著指數走，其次是AMA，最後也就是最鈍的SMA。在盤整時期，HMA也會跟著行情上上下下，顯然對抗雜訊震盪走勢能力不好。此外，在劇烈大行情時，HMA會算出比近日最高還高或是比近日最低還低的數值，這是HMA計算公式所致，可以解讀成最後的末升段或末跌段的強力動能遞延，如果是要開發以HMA為依據的進出策略，可特別留一下。

結論：HMA有短均線敏感度優點，面對盤整盤卻沒有忽上忽下的缺點，如果習慣採5日均線(5-SMA)操作的朋友，或許可以試試HMA。

---

## 關鍵字

- HMA
- 赫爾移動平均線
- Hull Moving Average
- 低延遲均線
- WMA加權移動平均
- 均線轉折點
- 均線斜率判趨勢
- 平方根平滑
- 移動平均線比較