# Statistical arbitrage — 統計套利

**來源**：https://en.wikipedia.org/wiki/Statistical_arbitrage
**日期**：2026-05-07
**主題**：操作策略

---

In finance, statistical arbitrage (often abbreviated as Stat Arb or StatArb) is a class of short-term financial trading strategies that employ mean reversion models involving broadly diversified portfolios of securities (hundreds to thousands) held for short periods of time (generally seconds to days). These strategies are supported by substantial mathematical, computational, and trading platforms.

Broadly speaking, StatArb is actually any strategy that is bottom-up, beta-neutral in approach and uses statistical/econometric techniques in order to provide signals for execution. Signals are often generated through a contrarian mean reversion principle but can also be designed using such factors as lead/lag effects, corporate activity, short-term momentum, etc. This is usually referred to as a multi-factor approach to StatArb.

Because of the large number of stocks involved, the high portfolio turnover and the fairly small size of the effects one is trying to capture, the strategy is often implemented in an automated fashion and great attention is placed on reducing trading costs.

Statistical arbitrage has become a major force at both hedge funds and investment banks. Some bank proprietary operations now center to varying degrees around statistical arbitrage trading.

As a trading strategy, statistical arbitrage is a heavily quantitative and computational approach to securities trading. It involves data mining and statistical methods, as well as the use of automated trading systems.

Historically, StatArb evolved out of the simpler pairs trade strategy, in which stocks are put into pairs by fundamental or market-based similarities. When one stock in a pair outperforms the other, the underperforming stock is bought long and the outperforming stock is sold short with the expectation that underperforming stock will climb towards its outperforming partner.

Mathematically speaking, the strategy is to find a pair of stocks with high correlation, cointegration, or other common factor characteristics. Various statistical tools have been used in the context of pairs trading ranging from simple distance-based approaches to more complex tools such as cointegration and copula concepts.

StatArb considers not pairs of stocks but a portfolio of a hundred or more stocks—some long, some short—that are carefully matched by sector and region to eliminate exposure to beta and other risk factors. Portfolio construction is automated and consists of two phases:

1. **Scoring phase**: Each stock in the market is assigned a numeric score or rank that reflects its desirability; high scores indicate stocks that should be held long and low scores indicate stocks that are candidates for shorting. The details of the scoring formula vary and are highly proprietary, but, generally (as in pairs trading), they involve a short term mean reversion principle so that, e.g., stocks that have done unusually well in the past week receive low scores and stocks that have underperformed receive high scores.

2. **Risk reduction phase**: The stocks are combined into a portfolio in carefully matched proportions so as to eliminate, or at least greatly reduce, market and factor risk. This phase often uses commercially available risk models like MSCI/Barra, APT, Northfield, Risk Infotech, and Axioma to constrain or eliminate various risk factors.

## Risks

Over a finite period of time, a low probability market movement may impose heavy short-term losses. If such short-term losses are greater than the investor's funding to meet interim margin calls, its positions may need to be liquidated at a loss even when its strategy's modeled forecasts ultimately turn out to be correct. The 1998 default of Long-Term Capital Management was a widely publicized example of a fund that failed due to its inability to post collateral to cover adverse market fluctuations.

Statistical arbitrage is also subject to model weakness as well as stock- or security-specific risk. The statistical relationship on which the model is based may be spurious, or may break down due to changes in the distribution of returns on the underlying assets. Factors, which the model may not be aware of having exposure to, could become the significant drivers of price action in the markets.

On a stock-specific level, there is risk of M&A activity or even default for an individual name. Such an event would immediately invalidate the significance of any historical relationship assumed from empirical statistical analysis of the past data.

## 2007 Quant Quake

In July and August 2007, several StatArb (and other Quant type) hedge funds experienced significant losses at the same time. Several published accounts blame the emergency liquidation of a fund that experienced capital withdrawals or margin calls. By closing out its positions quickly, the fund put pressure on the prices of the stocks it was long and short. Because other StatArb funds had similar positions, due to the similarity of their alpha models and risk-reduction models, the other funds experienced adverse returns.

Simulations of simple StatArb strategies by Khandani and Lo show that the returns to such strategies have been reduced considerably from 1998 to 2007, presumably because of competition.

## China Market Constraints

In China, quantitative investment including statistical arbitrage is not the mainstream approach to investment. A set of market conditions restricts the trading behavior of funds and other financial institutions. The restriction on short selling as well as the market stabilization mechanisms (e.g. daily limit) set heavy obstacles.

The combination of the 10% daily limit and limited short selling means that the mean reversion component, the core signal for statistical arbitrage, cannot be reliably traded, as price limits often prevent convergence, turning a temporary mispricing into an intractable liquidity risk.

---

## 關鍵字

- 統計套利
- Statistical Arbitrage
- StatArb
- 配對交易
- Pairs Trading
- 均值回歸
- 共整合
- Beta中性
- 量化交易
- 長期資本管理LTCM