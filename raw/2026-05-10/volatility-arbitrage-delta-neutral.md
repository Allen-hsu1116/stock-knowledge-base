# Volatility Arbitrage & Delta Neutral

**來源**：https://en.wikipedia.org/wiki/Volatility_arbitrage, https://en.wikipedia.org/wiki/Delta_neutral, https://en.wikipedia.org/wiki/Greeks_(finance)
**日期**：2026-05-10
**主題**：操作策略

---

## Volatility Arbitrage

Volatility arbitrage (vol arb) is a type of statistical arbitrage implemented by trading a delta neutral portfolio of an option and its underlying. The objective is to take advantage of differences between the implied volatility of the option and a forecast of future realized volatility of the underlying.

To an option trader engaging in volatility arbitrage, an option contract is a way to speculate in the volatility of the underlying rather than a directional bet on the underlying's price. If a trader buys options as part of a delta-neutral portfolio, he is said to be long volatility. If he sells options, he is said to be short volatility.

Key concepts:
- When IV < forecast realized volatility → buy options (long vol), delta hedge
- When IV > forecast realized volatility → sell options (short vol), delta hedge
- Vol arb is NOT risk-free: it relies on predicting future realized volatility
- Put-call parity means delta-hedged calls and puts produce the same returns
- Long Term Capital Management used volatility arbitrage and famously collapsed

### Forecast Volatility

Traders must forecast the underlying's future realized volatility. Methods:
1. Historical volatility (252-day daily returns is standard)
2. Realized variance from high-frequency intraday returns (more precise)
3. Adjustments for known upcoming events (earnings, legal decisions, etc.)
4. Econometric models (GARCH family)
5. Machine learning and deep learning models (Leushuis & Petkov 2026 survey)

### Market (Implied) Volatility

The theoretical price of an option can be expressed as V = f(S, σ), where S is the underlying price and σ is the estimated future volatility. Since V is a monotonically increasing function of σ, there exists a corresponding inverse function σ = g(V, S).

This means:
- Implied volatility is the volatility level implied by the market price
- IV is used as a measure of relative value rather than the option's absolute price
- A call trading at $1.90 with IV 17.5% is actually MORE EXPENSIVE than the same call later trading at $2.50 with IV 16.5%, because the higher underlying price justifies a higher absolute price

## Delta Neutral

Delta neutral describes a portfolio where the portfolio value remains unchanged when small changes occur in the value of the underlying security (having zero delta). The portfolio typically contains options and their corresponding underlying securities such that positive and negative delta components offset.

### Mathematical Interpretation

Delta = ∂V/∂S (partial derivative of option value with respect to spot price)

For a portfolio to be delta neutral: Δ_portfolio = 0

Since delta is a function of S, strike, and time to expiry, a delta neutral position is only instantaneously hedged. For non-infinitesimal moves, the second-order term (gamma) must be considered:

ΔV ≈ Δ × ΔS + ½ × Γ × (ΔS)²

### Maintaining Delta Neutrality

- Requires continuous recalculation of Greeks and rebalancing
- Typically rebalanced daily or weekly
- Research indicates portfolios tend to have lower cash flows if re-hedged too frequently
- Large underlying moves create gamma risk that delta hedging alone cannot address

## Greeks Key Points

### Delta (Δ)
- Rate of change of option value with respect to underlying price
- Long call: 0 to +1; Long put: 0 to -1
- |Delta| ≈ probability of expiring in-the-money
- Call Delta - Put Delta = 1 (put-call parity)

### Gamma (Γ)
- Rate of change of delta with respect to underlying price
- Second derivative of option value
- Most long options have positive gamma, most short options have negative gamma
- Greatest at-the-money, diminishes ITM and OTM
- Important for delta-hedging effectiveness over wider price ranges

### Vega (ν)
- Sensitivity to volatility (1 percentage point change)
- All options (calls and puts) gain value with rising volatility
- At-the-money straddle is extremely dependent on volatility changes
- Not actually a Greek letter (derived from nu ν)

### Theta (Θ)
- Time decay sensitivity
- Long options typically have negative theta (lose value over time)
- Deep ITM options may have positive theta (discount factor effect)

### Vanna
- DvegaDspot = DdeltaDvol
- Sensitivity of delta to volatility change, or vega to underlying price change
- Important for maintaining delta- or vega-hedged portfolios

### Vomma (Volga)
- DvegaDvol = second derivative of option value w.r.t. volatility
- Vega convexity
- Positive vomma: position becomes more long vega as IV increases
- Can be scalped analogously to long gamma

---

## 關鍵字

- 波動率套利
- Delta Neutral
- 隱含波動率
- 歷史波動率
- Gamma
- Vega
- Theta
- Vanna
- Vomma
- 選擇權避險
- 選擇權 Greeks