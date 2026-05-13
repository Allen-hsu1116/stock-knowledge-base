# Risk Parity 風險平價策略

**來源**：https://en.wikipedia.org/wiki/Risk_parity
**日期**：2026-05-08
**主題**：風險管理

---

## 原文內容

Risk parity (or risk premia parity) is an approach to investment management which focuses on allocation of risk, usually defined as volatility, rather than allocation of capital. The risk parity approach asserts that when asset allocations are adjusted (leveraged or deleveraged) to the same risk level, the risk parity portfolio can achieve a higher Sharpe ratio and can be more resistant to market downturns than the traditional portfolio. Risk parity is vulnerable to significant shifts in correlation regimes, such as observed in Q1 2020, which led to the significant underperformance of risk-parity funds in the COVID-19 sell-off.

Roughly speaking, the approach of building a risk parity portfolio is similar to creating a minimum-variance portfolio subject to the constraint that each asset (or asset class, such as bonds, stocks, real estate, etc.) contributes equally to the portfolio's overall volatility.

### 歷史背景

The first risk parity fund, called the All Weather fund, was pioneered in 1996 by Bridgewater Associates. The term "risk parity" came into use in 2005, coined by Edward Qian of PanAgora Asset Management, and was then adopted by the asset management industry.

The theoretical seeds go back further:
- 1952: Harry Markowitz introduced the efficient frontier into modern portfolio theory
- 1958: James Tobin concluded that the efficient frontier model could be improved by adding risk-free investments and advocated leveraging a diversified portfolio
- 1961-1966: Treynor, Sharpe, Lintner, and Mossin further analyzed combining leverage and minimizing risk
- However, the concept was not put into practice due to difficulties of implementing leverage in the portfolio of a large institution

### 60/40 傳統組合的問題

Risk parity is a conceptual approach to investing which attempts to provide a lower risk and lower fee alternative to the "traditional" portfolio allocation of 60% in shares and 40% bonds. The critical observation: this 60/40 portfolio carries approximately 90% of its risk in the stock portion, because stocks are much more volatile than bonds.

The risk parity approach attempts to equalize risk by allocating funds to a wider range of categories such as stocks, government bonds, credit-related securities and inflation hedges (including real assets, commodities, real estate and inflation-protected bonds), while maximizing gains through financial leveraging.

According to Bob Prince, CIO at Bridgewater Associates, the defining parameters of a traditional risk parity portfolio are:
1. Uncorrelated assets
2. Low equity risk
3. Passive management

### Equally-Weighted Risk Contributions (ERC)

The best known version of risk parity is the equally-weighted risk contributions portfolio method.

Key distinction: ERC is NOT about "having the same volatility" — it is about having each asset contributing in the same way to the portfolio overall volatility.

Mathematical formulation:
- Consider portfolio of assets w₁, ..., wₙ
- Covariance matrix Σ
- Portfolio volatility σ(w) = √(w'Σw)
- Since σ(w) is homogeneous of degree 1 in w, by Euler's theorem:
  σ(w) = Σᵢ wᵢ × ∂σ/∂wᵢ
- Where ∂σ/∂wᵢ = (Σw)ᵢ / σ(w) is the marginal risk contribution
- wᵢ × (Σw)ᵢ / σ(w) is the risk contribution of asset i
- Equal risk contribution means: wᵢ(Σw)ᵢ = wⱼ(Σw)ⱼ for all i,j

Solution methods:
1. Convex optimization (provably convergent)
2. Fixed point iteration
3. Minimization problem with constraints

Constraints typically:
- Set overall portfolio volatility to target: σ(w) = σ_target
- Or set gross investment to 1: Σ|wᵢ| = 1

### 績效歷史

- 1990s: Levered Risk Parity would have significantly underperformed vs standard institutional portfolio
- 2000-2010: Would have significantly outperformed standard institutional portfolio
- 2008 Financial Crisis: AQR's risk parity fund declined 18-19% vs 22% decline in Vanguard Balanced Index fund
- Post-2008: Risk parity funds "soared in popularity" and "consistently outperformed traditional strategies"

By 2014: 46% of institutional investors surveyed were using risk parity and 8% were considering investing.

### 風險與批評

- Vulnerable to significant shifts in correlation regimes (Q1 2020 COVID-19 sell-off)
- Mutual funds using risk parity incurred losses of 6.75% during the first half of 2013
- Requires strong management and continuous oversight to reduce potential for negative consequences of leverage
- Some portfolio managers have expressed skepticism about practical application
- Moderate risks include: communicating value to boards, unforeseen events, market timing risks, use of leverage

### 主要基金公司

Aquila Capital (2004), AQR Capital Management (2006), Bridgewater Associates (1996), BlackRock (2009), Neuberger Berman (2009), AllianceBernstein (2010), Schroders (2012), Natixis (2013), Allianz Global Investors (2015)

---

## 關鍵字

- 風險平價
- Risk Parity
- 等風險貢獻
- Equal Risk Contribution
- ERC Portfolio
- All Weather Strategy
- Bridgewater
- 資產配置
- 風險分配
- 槓桿
- Sharpe Ratio
- 60/40 Portfolio
- 相關性制度轉變
- Correlation Regime Shift