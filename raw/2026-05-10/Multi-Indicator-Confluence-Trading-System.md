# Multi-Indicator Confluence Trading System

**來源**：https://medium.com/@FMZQuant/multi-indicator-confluence-trading-system-886f15b18ae5
**日期**：2026-05-10
**主題**：技術分析

---

# Multi-Indicator Confluence Trading System

## Introduction

In financial markets, no single indicator is perfect. Every indicator has its strengths and weaknesses. The key to building a robust trading system is combining multiple indicators so that their signals **confluence** — that is, they align together to produce a high-probability entry or exit.

## What is Confluence?

Confluence in trading means multiple technical signals agree on the same direction at the same time. When 3 or more independent signals point to the same trade, the probability of success increases significantly.

### The Confluence Principle

- **Single indicator**: ~40-50% win rate
- **Two indicators confluence**: ~55-60% win rate  
- **Three indicators confluence**: ~65-70% win rate
- **Four+ indicators confluence**: ~70-75% win rate

The improvement follows diminishing returns — going from 1 to 2 indicators is more impactful than going from 3 to 4.

## Core Indicator Categories

### 1. Trend Indicators (Direction)
- **Moving Averages** (SMA, EMA): Price above/below MA determines trend direction
- **MACD**: Histogram above/below zero line confirms trend
- **ADX**: Above 25 = trending, below 20 = ranging

### 2. Momentum Indicators (Strength)
- **RSI**: Overbought (>70) / Oversold (<30), divergences
- **Stochastic (KD)**: %K and %D crossovers, overbought/oversold zones
- **CCI**: Extreme readings indicate momentum exhaustion

### 3. Volume Indicators (Confirmation)
- **OBV**: Rising OBV confirms uptrend
- **Volume MA**: Current volume vs 20-day average
- **Money Flow Index (MFI)**: Volume-weighted RSI

### 4. Volatility Indicators (Range)
- **Bollinger Bands**: Squeeze = low volatility, expansion = breakout imminent
- **ATR**: Measures typical daily range for stop-loss sizing
- **Keltner Channel**: EMA-based channel, narrower than Bollinger

## Building a Confluence System

### Step 1: Select Independent Indicators

Choose indicators from **different categories** to avoid redundancy:

| Combination | Redundant? | Reason |
|---|---|---|
| RSI + Stochastic | Yes | Both are momentum oscillators |
| RSI + MACD | No | Momentum + Trend |
| MACD + EMA | Partially | Both trend-following |
| Bollinger + ATR | Partially | Both volatility-based |
| OBV + MFI | Yes | Both volume-based |

**Rule**: Pick at most one from each category for maximum information gain.

### Step 2: Define Entry Conditions

A confluence entry requires ALL selected indicators to signal the same direction:

**Example: Bullish Confluence Entry**
1. Price above 20 EMA (Trend = Up)
2. MACD histogram positive and rising (Momentum = Up)
3. RSI crosses above 30 from oversold (Momentum = Recovering)
4. Volume above 20-day average (Confirmation = Strong)
5. Bollinger Band squeeze followed by expansion (Volatility = Breakout)

**Example: Bearish Confluence Entry**
1. Price below 20 EMA (Trend = Down)
2. MACD histogram negative and falling (Momentum = Down)
3. RSI crosses below 70 from overbought (Momentum = Weakening)
4. Volume above 20-day average (Confirmation = Strong)
5. Bollinger Band squeeze followed by downward expansion (Volatility = Breakout)

### Step 3: Define Exit Conditions

Exits can be based on:
- **Fixed R:R ratio**: Target 2:1 or 3:1 reward-to-risk
- **Indicator reversal**: Opposite confluence signal
- **Trailing stop**: ATR-based trailing stop (e.g., 2× ATR)
- **Time-based**: Exit after N bars if target not reached

### Step 4: Backtesting Framework

```python
def confluence_check(data):
    signals = []
    
    # Trend: EMA
    if data['close'] > data['ema_20']:
        signals.append(('trend', 'bullish'))
    else:
        signals.append(('trend', 'bearish'))
    
    # Momentum: MACD
    if data['macd_hist'] > 0 and data['macd_hist'] > data['macd_hist_prev']:
        signals.append(('momentum', 'bullish'))
    else:
        signals.append(('momentum', 'bearish'))
    
    # Momentum: RSI
    if data['rsi'] > 50:
        signals.append(('rsi', 'bullish'))
    else:
        signals.append(('rsi', 'bearish'))
    
    # Volume confirmation
    if data['volume'] > data['volume_ma_20']:
        signals.append(('volume', 'confirmed'))
    
    # Count confluence
    bullish = sum(1 for cat, sig in signals if sig == 'bullish')
    bearish = sum(1 for cat, sig in signals if sig == 'bearish')
    
    if bullish >= 3:
        return 'BUY'
    elif bearish >= 3:
        return 'SELL'
    else:
        return 'WAIT'
```

## Practical Confluence Strategies

### Strategy 1: EMA + MACD + RSI (Trend-Momentum Combo)

**Timeframe**: 4H or Daily
**Rules**:
- Long: EMA20 > EMA50, MACD > 0, RSI > 50 and < 70
- Short: EMA20 < EMA50, MACD < 0, RSI < 50 and > 30
- Stop: 2× ATR from entry
- Target: 3× ATR from entry

### Strategy 2: Bollinger + OBV + MACD (Squeeze Breakout)

**Timeframe**: Daily
**Rules**:
- Squeeze identified: Bollinger bandwidth < 10th percentile
- Breakout confirmed: Close outside band + OBV trending + MACD signal
- Stop: Middle Bollinger band
- Target: Opposite band or 2× ATR

### Strategy 3: Multi-Timeframe Confluence

**Timeframes**: Weekly (trend) + Daily (entry) + 4H (confirmation)
**Rules**:
- Weekly: Trend direction determined by EMA alignment
- Daily: Entry signal from MACD + RSI
- 4H: Fine-tune entry with candlestick pattern
- This adds 10-15% win rate over single-timeframe

## Common Mistakes

1. **Indicator redundancy**: Using RSI + Stochastic + CCI together provides almost no additional information
2. **Over-optimization**: Fitting too many parameters to historical data
3. **Ignoring context**: Confluence works better in trending markets; in ranges, signals conflict
4. **Confirmation bias**: Only seeing signals that match your desired direction
5. **Paralysis by analysis**: Too many indicators = never trading = missed opportunities

## Key Takeaways

- Confluence = multiple independent signals agree
- Choose indicators from different categories (trend, momentum, volume, volatility)
- 3-4 confluencing indicators is the sweet spot
- Always use volume as confirmation
- Multi-timeframe analysis adds significant edge
- Backtest before live trading
- Keep it simple — more indicators ≠ better results

---

## 關鍵字

- 多指標共振
- Confluence Trading
- 技術指標組合
- 趨勢指標
- 動量指標
- 成交量確認
- 波動率指標
- 多時間框架