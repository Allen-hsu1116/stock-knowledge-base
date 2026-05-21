# 相對活力指標 RVI (Relative Vigor Index)

**來源**：https://www.ifcmarkets.com/en/ntx-indicators/relative-vigor-index + https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/relative-vigor-index
**日期**：2026-05-18
**主題**：技術分析

---

## IFC Markets 原文

### What is Relative Vigor Index

Relative Vigor Index (RVI Indicator), developed by John Ehlers, is a technical indicator designed to determine price trend direction. The underlying logic is based on the assumption that close prices tend to be higher than open prices in a bullish environment and lower in a bearish environment.

### How to Use RVI Indicator

The Relative Vigor Index allows to identify the reinforcement of price changes (and therefore may be used within convergence/divergence patterns analysis):

- Generally the higher the indicator climbs, the stronger is the current relative price increase;
- Generally the lower the indicator falls, the stronger is the current relative price drop.

Together with its signal line (Red), a 4-period moving average of RVI, the indicator (Green) may help to identify changes in prevailing price developments:

- Crossing the signal line from above, the RVI signals a possible sell opportunity;
- Crossing the signal line from below, the RVI signals a possible buy opportunity.

### Relative Vigor Index Formula (RVI Calculation)

The Relative Vigor Index indicator is calculated as the actual price change for a certain period divided by the maximum range of price changes in that period. To reduce the dependence on strong price fluctuations, the averaging was applied according to the algorithm of Simple Moving Average with the period of 10.

The Relative Vigor Index formula is as follows:
Relative Vigor Index (1) = (Close - Open) / (High - Low)
Relative Vigor Index (10) = 10-period SMA of Relative Vigor Index (1)

### Divergence

An important additional sign of a price reversal using RVI is the divergence between local extremes of price movement and extremes of the indicator movement. Bearish divergence occurs when the price reaches a new low and the local low on the oscillator is higher than the previous one. Conversely, a bullish divergence occurs when price makes a new high and the oscillator high is lower than the previous one. This signal indicates that the price will soon reverse. In our example, we can see that in the vicinity of the date Jan 16, 2012, the price lows are still going down, but the RVI lows are already going up (bullish divergence), which is a signal to buy.

---

## Fidelity 原文

### Description

The Relative Vigor Index (RVI) is an oscillator based on the concept that prices tend to close higher than they open in up trends and close lower than they open in down trends. Basically, it is an oscillator that is in phase with the cycle of the underlying's price.

Divergence between the RVI and the price action may signal a change in trend.

In up trends potential buy opportunities occur when the RVI crosses above its signal line.

In down trends potential short sale opportunities occur when the RVI crosses below its signal line.

### RVI Calculation

bar a = Close – Open
bar b = Close – Open one bar prior to a
bar c = Close – Open one bar prior to b
bar d = Close – Open one bar prior to c

numerator = [ a + (2 * b) + (2 * c) + d ] / 6

e = High – Low of bar a
f = High – Low of bar b
g = High – Low of bar c
h = High – Low of bar d

denominator = [ e + (2 * f) + (2 * g) + h ] / 6

RVI = SMA of numerator for period selected / SMA of denominator for period selected

Signal Line Calculation:
i = RVI value one bar prior
j = RVI value one bar prior to i
k = RVI value one bar prior to j

Signal Line = [ RVI + (2 * i) + (2 * j) + k] / 6

---

## 關鍵字

- RVI
- 相對活力指標
- Relative Vigor Index
- John Ehlers
- 背離
- 信號線交叉
- 震盪指標