# Drawdown Analysis Advanced - 回撤分析進階

**來源**：https://en.wikipedia.org/wiki/Drawdown_(economics), https://en.wikipedia.org/wiki/Maximum_drawdown
**日期**：2026-05-09
**主題**：風險管理

---

Drawdown is the measure of the decline from a historical peak in some variable (typically the cumulative profit or total open equity of a financial trading strategy).

If X(t) is a stochastic process with X(0) = 0, the drawdown at time T, denoted D(T), is defined as:

D(T) = max(0, max_{0≤t≤T} X(t) - X(T))

The average drawdown (AvDD) up to time T is the time average of drawdowns that have occurred up to time T.

The maximum drawdown (MDD) up to time T is the maximum of the drawdown over the history of the variable:

MDD(T) = max_{0≤t≤T} D(t)

## Two Dimensions of Drawdown

### 1. Magnitude (How low it goes)
- The "pain" period between a peak and subsequent valley
- Maximum Drawdown (Max DD) is the worst peak-to-valley loss since inception
- Used in three performance measures: Calmar ratio, Sterling ratio, Burke ratio
- These modify the Sharpe ratio by replacing standard deviation with drawdown-based risk measures

### 2. Duration (How long it lasts)
- Drawdown duration: the length of any peak-to-peak period
- Max drawdown duration: the longest time between peaks
- Important distinction: Max DD duration ≠ duration of the Max DD magnitude event (though they often coincide)

## Mathematical Properties

When X(t) follows Brownian motion with drift μ and volatility σ:

X(t) = μt + σW(t)

Where W(t) is a standard Wiener process, three possible outcomes based on drift:

- μ > 0 (positive drift): MDD grows logarithmically with time — the best case, portfolio recovers
- μ = 0 (no drift): MDD grows as square root of time — random walk, slow recovery
- μ < 0 (negative drift): MDD grows linearly with time — the worst case, portfolio bleeds

This has profound implications: a strategy with positive expected return will have bounded MDD, while a negative expected return strategy has MDD that grows without bound.

## Conditional Drawdown-at-Risk (CDaR)

Chekhlov, Uryasev, and Zabarankin (2003, 2005) proposed an auxiliary function for drawdown optimization:

CDaR_α(x) = min_{ζ∈R} { ζ + (1/(1-α)) * (1/T) * Σ max(D(x,t) - ζ, 0) }

This is analogous to CVaR for drawdowns:
- When α = 0: CDaR is the average drawdown
- When α → 1: CDaR approaches maximum drawdown

Key insight: Drawdown optimization can be turned into a linear program, making it computationally tractable for portfolio optimization.

## Performance Measures Using Drawdown

1. **Calmar Ratio** = Annualized Return / Maximum Drawdown
   - Higher is better, penalizes strategies with large drawdowns
   - Typical threshold: >1.0 for decent strategies, >3.0 for excellent

2. **Sterling Ratio** = Annualized Return / (Average of worst K drawdowns)
   - More robust than Calmar as it considers multiple drawdown events
   - Reduces sensitivity to a single extreme event

3. **Burke Ratio** = Annualized Return / sqrt(Sum of squared drawdowns)
   - Penalizes both frequency and magnitude of drawdowns
   - Squared term gives more weight to larger drawdowns

4. **CDaR Ratio** (analogous to Sharpe ratio) = (Expected Return - Risk-free) / CDaR
   - Most general form, subsumes Calmar and Sterling as special cases

---

## 關鍵字

- 回撤分析
- 最大回撤
- MDD
- Calmar比率
- Sterling比率
- CDaR
- 條件回撤風險
- 回撤最佳化
- 布朗運動
- 風險調整報酬