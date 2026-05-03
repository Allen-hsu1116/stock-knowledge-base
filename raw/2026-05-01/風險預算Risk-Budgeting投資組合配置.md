# 風險預算 Risk Budgeting 投資組合配置

**來源**：https://analystprep.com/study-notes/cfa-level-iii/absolute-and-relative-risk-budgets/
**日期**：2026-05-01
**主題**：風險管理

---

## Risk Budgeting: Absolute and Relative Risk Budgets

### Introduction

Risk budgeting is a portfolio allocation method that uses risk measures, such as Value at Risk (VaR), to determine the allocation of assets in a portfolio. Unlike traditional mean-variance optimization, which focuses on expected returns and variances, risk budgeting focuses on how risk is distributed across portfolio components. The key insight is that each asset class or strategy should receive a risk allocation proportional to its expected risk-adjusted return, not simply a capital allocation.

### Absolute Risk Budgets

An absolute risk budget specifies the maximum amount of risk the portfolio can assume. This is typically expressed as a VaR limit, tracking error limit, or standard deviation target.

For example, a portfolio might have an absolute risk budget of:
- VaR(95%) ≤ 10% of portfolio value
- Annual volatility ≤ 15%
- Maximum drawdown ≤ 20%

The absolute risk budget acts as a hard constraint. All positions must collectively satisfy this constraint.

### Relative Risk Budgets

A relative risk budget specifies the risk contribution of each component relative to the total portfolio risk. The most common framework is the Marginal Contribution to Risk (MCTR) and the Absolute Contribution to Total Risk (ACTR).

**MCTR (Marginal Contribution to Total Risk)**: The change in portfolio risk resulting from a small increase in the weight of an asset. Mathematically:

MCTR_i = (∂σ_p / ∂w_i) = (Cov(R_i, R_p)) / σ_p

**ACTR (Absolute Contribution to Total Risk)**: The total risk contribution of asset i:

ACTR_i = w_i × MCTR_i = w_i × Cov(R_i, R_p) / σ_p

The sum of all ACTR values equals the portfolio standard deviation:

Σ ACTR_i = σ_p

### Risk Budgeting vs Traditional Allocation

| Feature | Traditional (Capital Budgeting) | Risk Budgeting |
|---------|--------------------------------|----------------|
| Allocation basis | Capital weights | Risk contributions |
| Focus | Return optimization | Risk distribution |
| Diversification | By asset class | By risk source |
| Drawback | Concentration risk | May underweight low-risk assets |

### Practical Implementation Steps

1. **Define total risk budget**: Set absolute risk limits (VaR, volatility, drawdown)
2. **Estimate risk contributions**: Calculate MCTR and ACTR for each position
3. **Allocate risk**: Distribute risk budget across strategies/asset classes based on risk-adjusted returns
4. **Monitor and rebalance**: When ACTR drifts beyond thresholds, rebalance

### Risk Budgeting in Multi-Strategy Portfolios

For a multi-strategy portfolio (e.g., momentum, mean reversion, carry, volatility):
- Each strategy gets a risk allocation, not a capital allocation
- A strategy with Sharpe ratio 1.5 and low correlation might get 40% risk budget but only 20% capital
- A strategy with Sharpe ratio 0.5 and high correlation might get 10% risk budget but 15% capital

This ensures the portfolio's risk is efficiently distributed to strategies with the best risk-adjusted returns.

### Factor Risk Budgeting

Instead of budgeting by asset class, budget by risk factor:
- Equity beta risk: 40%
- Interest rate risk: 25%
- Credit risk: 20%
- Currency risk: 10%
- Volatility risk: 5%

This approach is more granular and captures hidden risk concentrations (e.g., equity and credit may both load on the same economic factor).

### Advantages of Risk Budgeting

1. Better diversification of risk sources
2. Explicit risk limits prevent concentration
3. More intuitive for risk-aware investors
4. Naturally leads to risk parity-like allocations
5. Can incorporate tail risk measures (CVaR budgeting)

### Limitations

1. Requires accurate risk estimates (correlation instability)
2. May produce unintuitive capital weights
3. Backward-looking risk estimates may miss regime changes
4. Does not directly maximize returns
5. Complex implementation for retail investors

---

## 關鍵字

- 風險預算 Risk Budgeting
- MCTR 邊際風險貢獻
- ACTR 絕對風險貢獻
- VaR風險值
- 風險平價 Risk Parity
- 因子風險預算 Factor Risk Budgeting
- 多策略組合配置