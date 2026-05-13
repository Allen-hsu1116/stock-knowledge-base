# How to Assess Financial Health with Z-Score and Bankruptcy Prediction Models

**來源**：https://www.datastudios.org/post/how-to-assess-financial-health-with-z-score-and-bankruptcy-prediction-models-practical-approaches
**日期**：2026-05-12
**主題**：基本面分析

---

## Bankruptcy Prediction Models Overview

Corporate failures rarely happen without warning—financial stress accumulates, often visible in the numbers before crisis hits. Bankruptcy prediction models, especially the Z-score model, give investors, lenders, auditors, and managers early signals of distress, allowing for timely intervention and improved risk management.

## Altman Z-Score: Structure, Formulas, and Theoretical Foundation

Developed by Edward Altman in 1968, the Z-score is the most widely known bankruptcy prediction model. It uses a weighted linear combination of several financial ratios, each capturing a dimension of corporate health.

Classic Z-score formula (for public manufacturing companies):
Z = 1.2 × X₁ + 1.4 × X₂ + 3.3 × X₃ + 0.6 × X₄ + 1.0 × X₅

Where:
- X₁: Working Capital / Total Assets (Liquidity)
- X₂: Retained Earnings / Total Assets (Cumulative Profitability)
- X₃: EBIT / Total Assets (Profitability)
- X₄: Market Value of Equity / Total Liabilities (Leverage/Market Confidence)
- X₅: Sales / Total Assets (Asset Efficiency)

## Z-Score Interpretation: Risk Zones

- Z > 2.99: "Safe zone" — Very low probability of bankruptcy
- 1.81 – 2.99: "Grey zone" — Indeterminate risk; close monitoring needed
- Z < 1.81: "Distress zone" — High probability of bankruptcy

Scores are not static—trends over time offer better signals than a single reading. A deteriorating Z-score often signals rising financial risk even before other warning signs emerge.

## Variations and Extensions

- Z'-score (for private firms): Substitutes book values for market values and adjusts coefficients.
- Z"-score (for non-manufacturers): Removes the sales/total assets variable and further adjusts weights.
- Country- or region-specific versions: Adapt weights and ratios to reflect local financial norms and regulatory environments.

Example: Z'-score for private manufacturing firms:
Z' = 0.717 × X₁ + 0.847 × X₂ + 3.107 × X₃ + 0.420 × X₄ + 0.998 × X₅
(Where X₄ is Book Value of Equity / Total Liabilities)

## Other Bankruptcy Prediction Models

- Ohlson O-score: Uses logistic regression on a broader set of variables, applicable to all industries.
- Springate S-score and Fulmer H-score: Variants tailored to specific sectors.
- Moody's KMV and CreditEdge: Proprietary models incorporating market-based measures (e.g., equity volatility).

## Practical Calculation Example

A mid-size manufacturing firm:
- Working capital: 8, Total assets: 40, Retained earnings: 7
- EBIT: 4, Market value of equity: 16, Total liabilities: 18, Sales: 60

X₁: 8/40 = 0.20, X₂: 7/40 = 0.175, X₃: 4/40 = 0.10, X₄: 16/18 = 0.89, X₅: 60/40 = 1.5
Z = 0.24 + 0.245 + 0.33 + 0.534 + 1.5 = 2.85

Interpretation: Grey zone — close monitoring and further analysis recommended.

## Strategic Applications

- Credit risk assessment: Banks and suppliers use Z-scores in loan origination, credit lines.
- Early warning system: Boards and executives monitor trends to detect emerging distress.
- Investment analysis: Equity and bond investors screen for red flags.
- Performance benchmarking: Internal teams compare units for proactive risk management.
- Restructuring triggers: Distress zone scores can prompt turnaround plans.

## Strengths and Limitations

Strengths:
- Empirically proven predictive value, especially for manufacturing and mature companies.
- Simple calculation from widely available data.
- Transparent, easy to benchmark and communicate.

Limitations:
- Less accurate for financial firms, startups, or companies with atypical capital structures.
- Based on historical accounting data; may lag rapidly deteriorating conditions.
- Scores can be manipulated by aggressive accounting or one-off transactions.
- Models are less predictive in highly volatile or interventionist regulatory environments.
- Not a substitute for full due diligence or qualitative analysis.

## Best Practices

- Use as an early warning — not a final verdict.
- Track trends, not just point-in-time results.
- Regularly update models: Adapt formulas or weights if local GAAP evolves.
- Communicate results transparently with stakeholders.

---

## 關鍵字

- Altman Z-Score
- 破產預測模型
- Ohlson O-score
- Springate S-score
- 信用風險評估
- 趨勢追蹤
- 灰色地帶判讀