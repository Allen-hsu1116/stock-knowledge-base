# Monte Carlo Simulation | Complete Guide and Simulator

**來源**：https://www.buildalpha.com/monte-carlo-simulation/
**日期**：2026-05-01
**主題**：風險管理

---

## What is Monte Carlo Simulation?

Monte Carlo Simulation is a statistical technique that injects randomness into a dataset to create probability distributions for better risk analysis and quantitative decision-making.

In trading, Monte Carlo simulation is most commonly used to randomize or resample the order of historical trades to estimate a strategy's potential drawdowns, streaks, and equity curve variability in alternate "possible histories."

The purpose of Monte Carlo Simulation is to detect lucky backtests and misleading performance metrics before risking real capital.

## Why are Monte Carlo Simulations Used?

Monte Carlo Simulations help better simulate the unknown and are typically applied to problems that have uncertainty such as: trading, insurance, options pricing, games of chance, etc. The goal is to gain a better understanding of all the possible outcomes and potential minimum and maximum values.

## Benefits of Monte Carlo Simulation

### Better Understanding of Drawdown
Reshuffling the order of your trades can lead to different profit and loss sequences which can result in a greater drawdown. A trader may believe the backtest's drawdown is the worst it can get, but Monte Carlo analysis may show a much larger drawdown for most trading systems.

### Properly Fund Your Trading Strategy
Noticing a larger maximum drawdown from a Monte Carlo simulation can help a trader better capitalize a trading strategy. This can make a live drawdown more bearable and allow the trader to stick to the original plan.

### Understanding Possible Win and Loss Streaks
The backtest may show a maximum of 5 or 6 losing trades in a row but a Monte Carlo test may show that 8 or 9 losing trades in a row is possible.

### Set Better Expectations with Quantitative Analysis
This data analysis can help a trader remain calm enough to stick to the strategy when luck becomes favorable or unfavorable.

## How to Use Monte Carlo Results

- Compare the backtest drawdown to the 90th or 95th percentile Monte Carlo Drawdown
- Size the strategy so you can survive a statistically likely drawdown (not just the backtest's max drawdown)
- Use streak distributions (max loss streak) to set expectations and avoid turning a good strategy off at the worst time
- If Monte Carlo shows extreme sensitivity, revisit constraints (trade frequency, exits, filters) before going live

## Monte Carlo Methods: Different Types and Uses

### Reshuffle
Reshuffles historical trade order 1,000 times creating 1,000 new equity curves. All curves end at the same total P&L — but the paths change dramatically, revealing alternate drawdown scenarios.

### Resample
Randomly selects historical trades with replacement until reaching trade count. The same trade can appear multiple times. Creates broader distribution — curves don't end at the same spot.

### Randomized
Re-trades original entries while randomizing each trade's exit. If results remain profitable, your entry likely contains true edge. Catches overfit exits — a key lying backtest detector.

### Permutation
Reshuffles log inter/intrabar price changes and exponentiates to create synthetic data with same statistical properties but destroyed patterns. Re-trade on 1,000 new price series.

## Advanced Uses

### Monte Carlo Equity Curve Bands
Is my trading strategy broken? Randomly select 100 historical trades and add them to the end of the backtest's equity curve. Repeat 1,000 times and keep the 5th and 95th percentile equity curves. If future trading falls outside these bands, it's an early warning sign the strategy is broken.

### Monte Carlo Drawdown Technique
Answers: "How confident am I in this strategy's drawdown?" Uses the resample method to create 1,000 new equity curves and 1,000 new drawdown values. The blue cumulative distribution line shows what percentage of drawdowns fall below each value.

The red X indicates where 95% of all Monte Carlo drawdowns were less than the corresponding value. "We are 95% confident that drawdowns from this system will not exceed 30%."

## How Many Simulations are Needed?

The ideal number is 1,000 or more. To truly leverage the law of large numbers and get reliable results, one should strive for 1,000+ simulations; however, results are generally acceptable with 100 or more.

---

## 關鍵字

- Monte Carlo Simulation
- Reshuffle
- Resample
- Randomized
- Permutation
- Drawdown confidence
- Equity curve bands
- Position sizing