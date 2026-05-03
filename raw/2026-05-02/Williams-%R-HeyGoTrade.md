# Williams %R Indicator: Understanding Overbought and Oversold Signals - HeyGoTrade

**來源**：https://www.heygotrade.com/en/blog/williams-r-indicator-explained/
**日期**：2026-05-02
**主題**：技術分析

---

## What Is Williams %R

Williams Percent Range was developed by Larry Williams in 1973. It is a bounded momentum indicator that compares the current closing price to the high-low range over a set number of periods, typically 14. The indicator oscillates between 0 and -100. Readings near 0 mean the close is near the highest high of the lookback period. Readings near -100 mean the close is near the lowest low. Williams %R moves quickly because it uses raw data without smoothing, offering early signals at the cost of occasional false readings.

## Formula

%R = (Highest High - Current Close) / (Highest High - Lowest Low) x -100

Example: 14-day lookback. Highest high $55, lowest low $48, close $52:
(55 - 52) / (55 - 48) x -100 = -42.86 → close is in the upper half of the range, moderate bullish positioning.

## Reading the Scale

- 0 to -20: Overbought zone (close near top of range)
- -80 to -100: Oversold zone (close near bottom of range)
- -20 to -80: Neutral momentum zone

## Williams %R vs RSI

| Feature | Williams %R | RSI |
|---------|------------|-----|
| What it measures | Close position within high-low range | Ratio of average gains to average losses |
| Scale | 0 to -100 | 0 to 100 |
| Default period | 14 bars | 14 bars |
| Smoothing | None (raw calculation) | Internal smoothing via averages |
| Speed | Very fast, more volatile | Smoother, fewer whipsaws |
| Overbought threshold | 0 to -20 | Above 70 |
| Oversold threshold | -80 to -100 | Below 30 |

Williams %R reacts faster because it uses unsmoothed data, making it better for catching early momentum shifts but worse for avoiding false signals. Using both together creates a layered approach where %R provides the alert and RSI provides confirmation.

## Trading Signals

### Overbought and Oversold Crossings
A move from below -80 back above -80 signals easing selling pressure. A move from above -20 back below -20 signals fading buying pressure. More reliable in range-bound markets.

### Momentum Divergence
- Bearish divergence: price new high but %R lower high → weakening momentum
- Bullish divergence: price new low but %R higher low → fading downward pressure
- Divergence tends to precede reversals but can persist before price reacts

### Failure Swings
A failure swing occurs when Williams %R enters overbought territory, pulls back, attempts to re-enter but fails, then drops. This pattern signals weakening momentum without requiring price confirmation and is considered stronger than simple threshold crossings.

## Best Practices

1. Combine with trend context: Always identify the prevailing trend before acting on Williams %R signals. In an uptrend, oversold readings are potential buying opportunities. In a bear market, overbought readings may signal exits. Use MA or ADX to define direction.
2. Use confirmation before acting: Because Williams %R is unsmoothed, waiting for confirmation reduces whipsaws. Require a second bar to confirm the threshold crossing or wait for price to break a short-term level.
3. Adjust the lookback period: Default 14 suits daily charts. Shorter (10) for intraday. Longer (21) for swing trades.
4. Avoid isolation: Pair Williams %R with trend indicators, volume analysis, or price structure for a complete picture.

---

## 關鍵字

- Williams %R
- Failure swing
- Divergence
- Unsmoothed oscillator
- RSI comparison
- Trend confirmation