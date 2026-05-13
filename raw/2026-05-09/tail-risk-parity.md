# Tail Risk Parity - 尾部風險平價

**來源**：https://en.wikipedia.org/wiki/Tail_risk_parity, https://en.wikipedia.org/wiki/Risk_parity, https://en.wikipedia.org/wiki/Tail_risk
**日期**：2026-05-09
**主題**：風險管理

---

Tail risk parity is an extension of the risk parity concept that takes into account the behavior of the portfolio components during tail risk events. The goal of the tail risk parity approach is to protect investment portfolios at the times of economic crises and reduce the cost of such protection during normal market conditions. In the tail risk parity framework risk is defined as expected tail loss.

Traditional portfolio diversification relies on the correlations among assets and among asset classes, but these correlations are not constant. Because correlations among assets and asset classes increase during tail risk events and can go to 100%, TRP divides asset classes into buckets that behave differently under market stress conditions, while assets in each bucket behave similarly. During tail risk events asset prices can fall significantly creating deep portfolio drawdowns. Asset classes in each tail risk bucket fall simultaneously during tail risk events and diversification of capital within buckets does not work because periods of negative performance of portfolio components are overlapped. Diversification across tail risk buckets can provide benefits in the form of smaller portfolio drawdowns and reduce the need for tail risk protection.

Some researchers propose an extension of the classical risk parity portfolio optimization approach which incorporates higher moments such as skewness and kurtosis. These higher moment risk parity methods tend to outperform classical risk parity approaches significantly when the underlying data exhibits high non-normality and co-dependencies, but may provide less value-add in other datasets.

## Risk Parity 基礎

Risk parity (or risk premia parity) is an approach to investment management which focuses on allocation of risk, usually defined as volatility, rather than allocation of capital. The risk parity approach asserts that when asset allocations are adjusted (leveraged or deleveraged) to the same risk level, the risk parity portfolio can achieve a higher Sharpe ratio and can be more resistant to market downturns than the traditional portfolio.

The best known version of risk parity is the equally-weighted risk contributions portfolio method. This means each asset contributes equally to the portfolio's overall volatility. Mathematically, for portfolio weights w and covariance matrix Σ:

σ_p = w'Σw^(1/2)

By Euler's theorem for homogeneous functions:
σ_p = Σ(w_i * ∂σ_p/∂w_i)

where ∂σ_p/∂w_i = (Σw)_i / σ_p can be interpreted as the marginal risk contribution of asset i.

Equal risk contribution means for all i,j: w_i * (Σw)_i = w_j * (Σw)_j

### Key Principles of Risk Parity

1. Traditional 60/40 portfolios carry ~90% risk in equities
2. Risk parity equalizes risk contributions across asset classes
3. Uses leverage on lower-risk assets (bonds) to equalize risk contributions
4. Four conditions for leverage to be risk-reducing: (i) enough unencumbered cash for margin calls (ii) leverage applied to well-diversified portfolio (iii) frequent rebalancing (iv) minimized counterparty risk

### Historical Performance

- 2008 Financial Crisis: AQR's risk parity fund declined 18-19% vs 22% decline in Vanguard Balanced Index
- 1990s bull market: Risk parity underperformed traditional portfolios
- 2000-2010 decade: Risk parity significantly outperformed traditional portfolios
- Q1 2020 COVID-19 sell-off: Risk parity funds underperformed due to correlation regime shift

## Tail Risk Characteristics

Tail risk (fat tail risk) is the financial risk of an asset or portfolio moving more than 3 standard deviations from its current price, above the risk of a normal distribution.

Key properties:
- Market returns exhibit fat tails - extreme events occur more frequently than normal distribution predicts
- During tail events, three things happen simultaneously: falling asset prices, increasing risk premia, increasing correlations between asset classes
- Traditional diversification fails during tail events because correlations converge to 1
- At least 7 tail events from late 1980s to early 2010s: 1987 crash, 1994 bond crisis, 1997 Asian crisis, 1998 Russian/LTCM crisis, dot-com bubble, 2008 subprime crisis, Lehman bankruptcy

### Active Tail Risk Management

1. Idea generation: identify possible epicenters of tail events and their repercussions
2. Hedge construction: build the actual hedging positions
3. Active management: constant effectiveness through position and risk level adjustment, maintaining convexity while minimizing negative carry

---

## 關鍵字

- 尾部風險平價
- 風險平價
- 等風險貢獻
- 全天候策略
- 尾部風險
- 肥尾分佈
- 相關性崩潰
- 避險
- CVaR
- Sharpe比率