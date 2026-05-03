# 資金曲線管理 Equity Curve Management

**來源**：
- https://bullrush.com/what-is-equity-curve-management-in-prop-trading/
- https://www.mql5.com/en/blogs/post/765252
- https://www.fastercapital.com/content/Equity-Curve--Smoothing-the-Equity-Curve--Tactics-to-Reduce-Maximum-Drawdown.html
- https://arongroups.co/forex-articles/equity-curve-trading-strategy/

**日期**：2026-05-01
**主題**：風險管理

---

## BullRush: What Is Equity Curve Management in Prop Trading?

Most traders obsess over entries. Professionals obsess over survival.

An equity curve is the story of your trading account over time: every win, every loss, every emotional decision etched into a single line. Equity curve management is the skill of shaping that story so it grows steadily instead of violently. In prop trading, this skill often matters more than your strategy itself.

### Understanding the Equity Curve

Your equity curve tracks the rise and fall of your account balance. Smooth curves signal control. Jagged curves signal chaos. Prop firms don't just glance at your P&L; they study the shape of your curve.

A steady upward slope tells them you manage risk, size positions intelligently, and adapt after losses. Sharp spikes followed by crashes tell a different story.

- Equity curve shows account growth over time
- Smooth curves indicate discipline
- Jagged curves reveal emotional trading

### Why Equity Curve Management Matters

Prop firms operate at scale. They care about predictable and stable performance, not heroic wins. Equity curve management proves you can trade within limits without emotional breakdowns.

Many traders experience prop firm challenge failures not because they lack edge, but because they allow one bad session to erase all the good ones. Equity curve control protects your account from self-sabotage.

- Consistency matters more than peak profits
- Drawdown control protects evaluations
- Survival keeps you in the game

### Position Sizing: The Curve Shaper

Nothing impacts your equity curve more than position size. Oversized trades create sharp spikes and deeper drops. Controlled sizing smooths the curve.

Professional traders think in sequences, not just individual trades. They size so losses feel routine, not traumatic. That calm allows better decision-making over time.

- Position size defines curve volatility
- Smaller size equals smoother growth
- Emotional stability follows proper sizing

### Managing Losing Streaks Without Derailing the Curve

Losses are unavoidable. What matters is how you respond. Traders who chase after losses bend their equity curve downward fast.

Equity curve management means reducing size after drawdowns, tightening execution, and regaining rhythm before scaling back up. The goal is stability, not revenge.

Tip: After two consecutive losses, pause and reassess before placing the next trade.

- Losses are normal
- Reaction determines curve damage
- Pausing preserves capital and confidence

### Consistency Over Time Beats Short-Term Surges

Big winning days look impressive but often hide risk-taking behavior. Prop firms want to see controlled progress over many sessions.

A trader who makes small, steady gains is more fundable than one who swings wildly between extremes. Equity curve management is proof of long-term viability.

- Steady progress builds trust
- Volatility scares evaluators
- Repeatability drives funding

---

## MQL5: Equity Curve Control — How Pros Manage Drawdowns

### The Lesson

Anyone can grow an account in good times. But what separates pros from amateurs is how they behave when the equity curve dips. Drawdowns are inevitable — controlling them is a skill.

### Step 1: Know Your Maximum Drawdown Limit

MDD is the largest loss from a peak to a valley. A professional sets this limit before trading.

- Peak balance: $10,000
- Lowest point: $9,200 → MDD = $800 or 8%

Most consistent traders keep their MDD below 10–12%. Anything beyond that means risk control is broken.

### Step 2: The Recovery Math

The deeper the drawdown, the harder the recovery:

| Drawdown | Needed Gain to Recover |
|----------|----------------------|
| 10%      | 11%                  |
| 25%      | 33%                  |
| 50%      | 100%                 |
| 70%      | 233%                 |

This is why capital protection > profit chasing. You can always make money later — but you can't trade without money now.

### Step 3: Cut Risk During Losing Streaks

- Risk per trade = 2%
- If you lose 3 trades in a row → reduce to 1%
- If you lose 5 trades in a row → stop trading for 24 hours

This simple rule creates an auto-brake system for your equity curve. You'll never spiral into deep losses by accident.

### Step 4: Track Your Equity Like a Pilot

Pilots monitor altitude — traders monitor equity. Log your daily balance and equity (open trades included). If your curve drops faster than expected, it's not "bad luck." It's bad management. Adjust before you crash.

---

## FasterCapital: Smoothing the Equity Curve — Tactics to Reduce Maximum Drawdown

### Introduction

The equity curve is a visual representation of a trader's account value over time. It's a crucial tool for assessing the performance and health of a trading strategy. The shape and slope of the equity curve can reveal much about the risk and consistency of a trading approach.

From the perspective of a risk manager, a smooth equity curve with fewer drawdowns is preferable as it suggests a more consistent strategy with well-managed risks. Extreme volatility in the equity curve can indicate overexposure to risk.

### Understanding Maximum Drawdown

Maximum drawdown (MDD) measures the largest single drop from peak to trough before a new peak is achieved. Key insights:

1. **Historical Significance**: Historical MDD gives investors a sense of what to expect during market downturns
2. **Recovery Period**: A 50% drawdown requires a 100% return to break even
3. **Risk Management**: Lower MDD suggests risk management techniques are working
4. **Benchmarking**: MDD serves as a benchmark to compare different portfolios
5. **Psychological Impact**: Fear of large MDD leads investors to choose more conservative strategies
6. **Portfolio Construction**: Understanding MDD influences portfolio construction

### Diversification and Asset Allocation

Diversification and asset allocation are primary strategies for smoothing the equity curve. By spreading investments across various asset classes, sectors, and geographies, investors can mitigate the volatility that any single investment may bring.

Key: Identify assets that do not move in tandem — when one zigs, the other zags.

### Drawdown Control Strategies

Implementing a strategy to reduce positions or switch to cash during significant drawdowns can help in preserving capital and smoothing the equity curve.

---

## AronGroups: Equity Curve Trading Strategy

### Moving Average Filters for Equity Curve Trading

An equity-curve moving average acts like a "trading permission" line. When the curve falls below it, you reduce or pause trading. When the curve rises above, you resume normal sizing.

Two implementation methods:
1. **Pause trading below the moving average and resume once equity crosses back above**
2. **Sizing modulation**: Keep trading, but reduce or increase position size on equity-curve crossovers

### Recovery Phases

A practical journal model uses four phases:
- **Expansion**: Equity curve prints new highs. Priority is consistency, not speed.
- **Pullback**: Controlled dip within tested limits. Treat as feedback, focus on execution quality.
- **Stress**: Drawdown deepens, losses cluster. Time-to-recover can widen. Equity curve drawdown analysis matters most here.
- **Repair**: Curve stops making new lows, variance reduces. Priority is rebuilding process discipline with smaller exposure.

### Risk Metrics

| Metric | What it measures | Why it matters |
|--------|-----------------|---------------|
| Max drawdown | Worst peak-to-trough decline | Worst-case stress test |
| Volatility of returns | Variability of outcomes | Flags unstable sizing |
| Sharpe / Sortino | Risk-adjusted return | Compares performance accounting for risk |
| Profit factor | Gross profit ÷ gross loss | Edge efficiency beyond win rate |
| Win rate + expectancy | Hit rate and average outcome quality | What drives the curve slope |

---

## 關鍵字

- 資金曲線 Equity Curve
- 最大回撤 MDD
- 回撤恢復 Recovery
- 資金曲線移動平均線
- 部位縮減 Drawdown Reduction
- 報復性交易 Revenge Trading
- 風險管理 Risk Management
- Prop Trading Evaluation
- 回撤控制 Drawdown Control
- 平滑資金曲線 Smoothing Equity Curve