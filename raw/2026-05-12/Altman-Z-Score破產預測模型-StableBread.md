# How to Assess Bankruptcy Risk With the Altman Z-Score Models

**來源**：https://stablebread.com/altman-z-score/
**日期**：2026-05-12
**主題**：基本面分析

---

This article will cover the Altman Z-Score and its variations, a set of financial models developed by Professor Edward Altman to predict the likelihood of a company going bankrupt. The original Z-Score model, introduced in 1968, combines five key financial ratios to assess a company's financial health and provide investors with an indicator of potential bankruptcy risk. Subsequent adaptations, such as the Z'-Score for private companies (1998) and the Z"-Score for non-manufacturing and emerging firms (1995), have extended the model's applicability.

This article will also highlight two proprietary models, the ZETA Credit Risk Model (1977) and the Altman Z-Score Plus (2012), which incorporate additional variables and industry-specific factors to improve predictive accuracy. While these models are only available to subscribers and are not fully disclosed to the public, they represent important advancements in bankruptcy prediction.

## Altman Z-Score Explained

The Altman Z-Score is a financial model created in 1968 by Edward I. Altman, a professor at New York University's (NYU) Stern School of Business. The model aims to evaluate a company's creditworthiness and predict the likelihood of bankruptcy within two years. By combining five key financial ratios, each with different weights, the Z-Score generates a single score that reflects a company's financial health, including its operational strength, liquidity, solvency, profit margins, and leverage.

Since its introduction in 1968, the Altman Z-Score has undergone several revisions:
- Z-Score (1968): U.S. public manufacturing companies.
- Z'-Score (1983): U.S. private manufacturing companies.
- Z"-Score (1995): U.S. non-manufacturing and emerging firms (both public and private).
- ZETA Credit Risk Model (1977) and Altman Z-Score Plus (2012): Proprietary risk models.

## Altman Z-Score Formula

Z-Score [Modified; Public U.S. Manufacturing] = (1.2 × X1) + (1.4 × X2) + (3.3 × X3) + (0.6 × X4) + (1.0 × X5)

where:
- X1 = Working Capital / Total Assets
- X2 = Retained Earnings / Total Assets
- X3 = Earnings Before Interest and Taxes (EBIT) / Total Assets
- X4 = Market Value of Equity / Total Liabilities
- X5 = Sales / Total Assets

### Five X-Variables Explained

#### X1: Working Capital / Total Assets (WC/TA)
Provides insight into a company's short-term financial health and liquidity.
- Higher WC/TA: Better liquidity and greater ability to meet short-term obligations.
- Lower WC/TA: May indicate struggling to pay bills, though negative working capital isn't always bad (e.g., companies with high inventory turnover).
- Most valuable among the three liquidity ratios Altman evaluated.

#### X2: Retained Earnings / Total Assets (RE/TA)
Measures the proportion of a company's assets financed through retained earnings rather than debt.
- Higher RE/TA: History of profitability, less reliance on borrowing.
- Lower RE/TA: More dependent on debt financing or dilution.
- Indirectly considers the age of a firm — younger firms tend to have lower RE/TA ratios.
- Can be affected by quasi-reorganizations and stock dividend declarations.

#### X3: EBIT / Total Assets (EBIT/TA)
Assesses a company's ability to generate operating profits from its assets.
- Higher EBIT/TA: Greater profitability and more efficient asset utilization.
- Lower EBIT/TA: Lower profitability, may signal potential financial distress.
- Similar to ROA but uses EBIT instead of net income.
- Consistently outperforms other profitability measures, including cash flow.

#### X4: Market Value of Equity / Total Liabilities (MVE/TL)
Assesses how much a company's market value can decline before its liabilities exceed its assets.
- Higher MVE/TL: Stronger investor confidence.
- Lower MVE/TL: Weak investor confidence.
- Incorporates market value perspective.
- Can be influenced by stock price fluctuations — a high stock price can inflate this ratio.

#### X5: Sales / Total Assets (S/TA)
Evaluates a company's efficiency in using its assets to generate sales.
- Higher S/TA: Better management of competition, more effective asset utilization.
- Lower S/TA: Failure to maintain or grow market share.
- Least significant ratio individually but ranks second in contribution to the model's overall discriminating ability.

### Altman Z-Score Findings
- One Year Before Bankruptcy: 95% accurate in predicting bankruptcy.
- Two Years Before Bankruptcy: 83% accurate.

### Z'-Score for Private Manufacturing Companies
Z' = 0.717 × X1 + 0.847 × X2 + 3.107 × X3 + 0.420 × X4 + 0.998 × X5
(Where X4 uses Book Value of Equity instead of Market Value)

### Z"-Score for Non-Manufacturing and Emerging Firms
Z" = 6.56 × X1 + 3.26 × X2 + 6.72 × X3 + 1.05 × X4
(No X5/Sales variable; X4 uses Book Value of Equity)

### Emerging Market Companies
Z" = 3.25 + 6.56 × X1 + 3.26 × X2 + 6.72 × X3 + 1.05 × X4

### Interpretation Zones
**Public Manufacturing:**
- Z > 2.99: Safe Zone
- 1.81 ≤ Z ≤ 2.99: Grey Zone
- Z < 1.81: Distress Zone

**Private Non-Manufacturing:**
- Z > 2.60: Safe Zone
- 1.10 ≤ Z ≤ 2.60: Grey Zone
- Z < 1.10: Distress Zone

### Limitations
- Less accurate for financial firms, startups, or companies with atypical capital structures.
- Based on historical accounting data; may lag rapidly deteriorating conditions.
- Scores can be manipulated by aggressive accounting or one-off transactions.
- Not a substitute for full due diligence or qualitative analysis.

---

## 關鍵字

- Altman Z-Score
- 破產預測
- Z-Score公式
- 五大財務比率
- Z'-Score私有企業
- Z"-Score非製造業
- 灰色地帶
- 破產風險