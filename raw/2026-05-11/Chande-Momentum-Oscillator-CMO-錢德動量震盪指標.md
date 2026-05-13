# 錢德動量震盪指標 CMO (Chande Momentum Oscillator)

**來源**：https://deepvue.com/indicators/chande-momentum-oscillator-cmo/
**來源**：https://www.tradingview.com/support/solutions/43000589109-chande-momentum-oscillator-cmo/
**日期**：2026-05-11
**主題**：技術分析

---

## Deepvue 原文

The Chande Momentum Oscillator (CMO) is a technical momentum indicator developed by Tushar Chande, first introduced in his 1994 book, The New Technical Trader. The CMO helps traders identify overbought and oversold market conditions and spot potential entry and exit points. It is particularly useful because it accounts for both gains and losses over a defined period, providing a clear picture of market momentum.

### Calculation of the Oscillator

CMO = [(Sum of Gains - Sum of Losses) / (Sum of Gains + Sum of Losses)] * 100

Or alternatively:
CMO = 100 * ((Su - Sd) / (Su + Sd))

Where:
- Su = Sum of differences on up days over the specified period (commonly 14 or 20 days).
- Sd = Sum of absolute differences on down days over the same period.

The CMO value ranges from -100 to +100, providing a normalized scale of momentum.

### Interpretation

**Overbought and Oversold Levels:**
- Above +50 → Overbought condition (possible price correction)
- Below -50 → Oversold condition (possible price rebound)

**Trading Signals:**
- Buy Signal → CMO crosses above a lower threshold (e.g., -50 or -30), indicating upward momentum.
- Sell Signal → CMO crosses below an upper threshold (e.g., +50 or +30), indicating downward momentum.

Traders often add a 9-period moving average to the CMO as a signal line to confirm entries and exits.

### How This Indicator Works

- **Trend Strength**: The higher the absolute value of the CMO, the stronger the trend.
- **Sideways Trading**: Lower absolute values indicate a range-bound or consolidating market.
- **Divergences**: When price makes a new high or low not confirmed by the CMO, this divergence can signal a reversal.

### Combining with Other Indicators

To improve reliability, traders often combine the CMO with:
- Trend indicators (e.g., Moving Averages, ADX)
- Support and resistance levels
- Chart patterns (double tops, bottoms, trendlines on the CMO itself)

### Advantages
- Identifies overbought/oversold conditions.
- Generates clear trading signals.
- Applicable to multiple instruments (stocks, commodities, currencies) and timeframes.

### Limitations
- May produce false signals, especially in trending markets.
- Effectiveness varies with market conditions.
- Best used with additional tools to confirm signals.

### CMO vs. Stochastic Oscillator

| Aspect | CMO | Stochastic Oscillator |
|--------|-----|----------------------|
| Basis | Momentum, unsmoothed | Smoothed momentum |
| Range | -100 to +100 | 0 to 100 |
| Strength | More sensitive | Smoother signals |
| Crossover | Optional signal line | Built-in crossover signal line |

## TradingView 原文

The Chande Momentum Oscillator is a technical momentum indicator and was designed specifically to track the movement and momentum of a security. The oscillator calculates the difference between the sum of both recent gains and recent losses, then dividing the result by the sum of all price movement over the same period (usually defined as 20 periods).

The Chande Momentum Oscillator was invented by Tushar Chande and first introduced in 1994 in his book, "The New Technical Trader" written with the help of his colleague, Stanley Kroll. Chande and Kroll also worked together in developing the Chande Kroll Stop.

### Calculations

- Start by calculating the sum of the higher closes over "n" periods.
- Then, calculate the sum of the lower closes over "n" periods.
- Next, subtract the sum of the lower closes from the sum of the higher closes.
- Continue by adding the sum of the lower closes to the sum of the higher closes.
- Divide step 3 by step 4 and then multiply by 100.
- Plot the result on your chart and proceed with trading.

### Takeaways

From the start, traders should be aware of the time frame they choose when using the CMO. Signals are greatly affected by this decision.

When focusing on your chart settings and applying indicators and strategies to begin your trading, keep in mind that pattern recognition often generates more reliable signals when compared with absolute oscillator levels.

In strong trending markets, it's possible for overbought and oversold indicators to be considered less effective. When assessing your indicators, make sure to be aware of this point and proceed with your picks accordingly.

### What to look for

The Chande Momentum Oscillator measures momentum on up and down days and doesn't have the ability to smooth results, therefore triggering more frequent overbuys and oversells. This indicator oscillates between +100 and -100, but a security is not considered to be overbought until the oscillator is above +50. If the indicator oscillates below -50, then it is considered oversold.

It's common to initiate a moving average (i.e. 10-period) to this oscillator to act as a signal line - if the oscillator crosses above the moving average, it generates a bullish signal. Similarly, if the oscillator moves below the moving average, it generates a bearish signal.

The Chande Momentum Oscillator can also be used to determine trend strength by analyzing the strength or weakness of the present market trend.

---

## 關鍵字

- CMO
- 錢德動量震盪指標
- Chande Momentum Oscillator
- 動量指標
- 超買超賣
- 背離訊號
- Tushar Chande
- 均線訊號線
- 趨勢強度