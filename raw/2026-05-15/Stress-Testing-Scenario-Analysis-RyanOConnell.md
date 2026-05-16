# Stress Testing & Scenario Analysis

**來源**：https://ryanoconnellfinance.com/stress-testing-scenario-analysis/
**日期**：2026-05-15
**主題**：風險管理

---

Stress testing a portfolio means asking the question that standard risk models leave unanswered: what happens when markets break? Measures like Value at Risk and Expected Shortfall quantify potential losses under modeled conditions — but they rely on historical patterns and distributional assumptions that can fail during genuine crises. Stress testing fills this gap by evaluating portfolio performance under extreme, unlikely, but plausible scenarios that fall outside the statistical frame.

## What Is Portfolio Stress Testing?

Stress testing examines how a portfolio would perform under extreme market conditions that lie outside the range of normal statistical models. The term originates from engineering — testing whether a structure can survive forces far beyond its design load — and the principle applies directly to finance. A stress test identifies unusual circumstances that could lead to losses in excess of those typically expected, revealing vulnerabilities that day-to-day risk metrics miss.

VaR summarizes the loss at a chosen confidence level under a model or historical sample. Stress testing asks bespoke "what if" questions outside that statistical frame — specific adverse scenarios chosen for their relevance to the portfolio's actual risk exposures. Together, they cover both normal and abnormal market conditions.

Regulators reinforce this complementary relationship. The Basel Committee's Fundamental Review of the Trading Book (FRTB) replaced VaR with Expected Shortfall as the primary capital metric for market risk — but stress testing remains a separate supervisory expectation for banks.

For portfolio managers, stress testing serves three practical purposes:
1. Quantifying potential losses under extreme conditions before they occur
2. Identifying concentrated exposures and hidden correlations that only surface in crises
3. Informing risk limits, hedging decisions, and capital allocation

## Scenario Analysis: Three Approaches

### Stylized Scenarios
Stylized scenarios apply standardized, predefined shocks to key risk factors. The Derivatives Policy Group (DPG) established a widely referenced set of seven standard scenarios:

| Scenario | Shock |
|---|---|
| Parallel yield curve shift | ±100 basis points |
| Yield curve twist | ±25 basis points |
| Combined shift + twist | Four combinations of the above |
| Implied volatility change | ±20% from current levels |
| Equity index change | ±10% |
| Currency moves | ±6% (major) / ±20% (emerging) |
| Swap spread change | ±20 basis points |

Limitation: shocks are typically applied one factor at a time, while real crises involve simultaneous, correlated movements across multiple risk factors.

### Historical Extreme Events
Historical scenarios replay the market conditions of actual past crises through a current portfolio.

Major Market Stress Events:

| Event | Period | S&P 500 Loss | Event Window |
|---|---|---|---|
| Black Monday | Oct 1987 | -20.5% | 1 day |
| LTCM / Russian Crisis | Aug–Oct 1998 | -19.3% | ~3 months |
| Global Financial Crisis | Oct 2007–Mar 2009 | -56.8% | ~17 months |
| European Sovereign Debt | Apr–Oct 2011 | -19.4% | ~6 months |
| COVID Crash | Feb–Mar 2020 | -33.9% | 23 trading days |

The 1998 LTCM crisis illustrates why historical scenarios matter. Long-Term Capital Management held highly leveraged convergence trades — betting that bond yield spreads would narrow — with roughly $125 billion in assets on $4.7 billion in equity. When the Russian government defaulted on its debt in August 1998, correlations across global bond markets spiked simultaneously: spreads that LTCM expected to converge instead widened dramatically. The fund lost $4.6 billion in under four months.

Historical scenarios capture the full complexity of real crises — including correlation spikes, liquidity freezes, and contagion effects. However, they assume the next crisis will resemble a past one, which is rarely true in every detail.

### Hypothetical Scenarios
Hypothetical scenarios construct plausible events that have never actually occurred in markets. Examples include a simultaneous sovereign default and currency crisis in a major economy, a coordinated cyberattack on financial infrastructure, or a sudden 300-basis-point emergency rate hike. These scenarios are the most difficult to design — they require careful crafting to add analytical value rather than producing confusing or implausible results. The payoff is coverage of risks that no backward-looking approach can capture.

## Model-Based Stress Testing Methods

### Factor-Based Stress Loss (First-Order Approximation)

Portfolio Loss_stress ≈ Σ (ΔFactor_i × Dollar Sensitivity_i)

The stressed portfolio loss is approximately the sum of each risk factor's shock (ΔFactor) times the portfolio's dollar sensitivity to that factor — e.g., DV01 for interest rates, dollar beta exposure for equities, dollar delta for options. This is a first-order linear approximation; portfolios with options, convertible bonds, or other non-linear instruments require gamma, vega, convexity adjustments, or full repricing.

### Factor Push Analysis
Push each risk factor individually to its most adverse plausible value, then aggregate the results. Applicable to option-pricing models (Black-Scholes-Merton), multifactor equity models, and term structure models. Limitation: evaluates one-factor-at-a-time shocks, which may miss interactions between risk factors.

### Maximum Loss Optimization
Mathematically searches for the combination of risk factor movements — within plausible bounds — that produces the worst portfolio outcome. More rigorous than factor push because it accounts for multi-factor interactions, but computationally demanding and sensitive to the bounds chosen.

### Worst-Case Scenario Analysis
Examines the worst outcome that is actually expected to occur — bounded by realistic expectations, not theoretical extremes. Bridges the gap between single-factor push tests and unconstrained worst-case thinking.

**Important Limitation**: All model-based stress tests carry model risk. The underlying pricing models were calibrated to normal market conditions. Under extreme stress, these models may produce unreliable outputs — precisely when accurate risk estimates matter most.

## How to Stress Test a Portfolio

1. **Map your portfolio's risk exposures** — Identify key risk factors: equity market risk, interest rate sensitivity, credit spreads, currency exposure, volatility, and liquidity.
2. **Choose your scenario horizon** — Define whether you are testing a sudden shock (1-day) or a prolonged crisis (months).
3. **Select a mix of scenarios** — Combine stylized shocks, historical replays, and at least one hypothetical event relevant to current risks.
4. **Decide on the revaluation method** — For linear instruments, first-order formula may suffice; full repricing is essential for options or convex instruments.
5. **Incorporate liquidity and funding constraints** — Model wider bid-ask spreads, reduced market depth, and potential margin calls.
6. **Compare results to risk limits** — Evaluate scenario losses against stated risk tolerance, capital buffers, and liquidity reserves.
7. **Run regularly and document** — At minimum quarterly; more frequently during volatile markets.

**Reverse Stress Testing**: Instead of asking "What happens if the market drops 30%?" ask "What combination of events would cause our portfolio to lose $X?" This backward approach often reveals hidden vulnerabilities.

## Stress Test in Practice: Pension Fund Response

Setup: A $500 million pension fund with 65% equity / 35% bond allocation runs a 2008-style GFC scenario.

Results: Estimated loss of $175 million (35% drawdown). Maximum acceptable drawdown is 25% ($125 million) — a $50 million gap.

Actions taken:
- Reduced equity allocation from 65% to 50%
- Purchased 6-month S&P 500 put options (5% OTM) as tail-risk insurance
- Established a liquidity reserve equal to 18 months of benefit payments
- Reported stress test results to the board with explicit risk-tolerance breach and remediation plan

## VaR vs Scenario Analysis vs Model-Based Stress Tests

| Method | Approach | Conditions | Output | Strengths | Weakness | Best for |
|---|---|---|---|---|---|---|
| VaR | Statistical | Normal conditions | Single number with probability | Objective, backtestable | Blind to tail severity | Daily monitoring |
| Scenario Analysis | Narrative | Extreme events | Estimated loss per scenario | Captures real crisis dynamics | Only as good as scenarios selected | Specific event exposure |
| Model-Based Stress | Computational | Adverse factor combinations | Range of worst-case outcomes | Discovers hidden tail risks | Inherits model risk | Finding portfolio weaknesses |

Best practice: use all three together.

## Common Mistakes

1. **Testing only historical scenarios** — The next crisis rarely resembles a past one.
2. **Ignoring correlation breakdown** — Correlations spike during crises; diversification relationships break down.
3. **Running stress tests but not acting on results** — Most common institutional failure.
4. **Applying shocks to one risk factor at a time** — Real crises involve simultaneous, correlated shocks.
5. **Treating stress test outputs as precise forecasts** — They produce order-of-magnitude estimates, not precise predictions.

## Limitations of Stress Testing

1. **Subjective scenario selection** — No objective way to determine the "right" set of scenarios.
2. **No probability attached** — Unlike VaR, stress tests don't tell you how likely a scenario is.
3. **Model risk in computational approaches** — Factor push, maximum loss optimization inherit assumptions of underlying pricing models.
4. **"Failure of imagination" problem** — Cannot protect against risks that no one has thought to test.

---

## 關鍵字

- 壓力測試
- 情境分析
- 風格化情境
- 歷史極端事件
- 假設情境
- 因子推壓
- 最大損失優化
- 反向壓力測試
- 相關性崩潰
- 流動性風險
- VaR
- Expected Shortfall