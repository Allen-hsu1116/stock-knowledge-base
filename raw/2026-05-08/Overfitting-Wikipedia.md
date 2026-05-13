# Overfitting - 過度配適

**來源**：https://en.wikipedia.org/wiki/Overfitting
**日期**：2026-05-08
**主題**：風險管理

---

In mathematical modeling, overfitting is the production of an analysis that corresponds too closely or exactly to a particular set of data, and may therefore fail to fit to additional data or predict future observations reliably. An overfitted model is a mathematical model that contains more parameters than can be justified by the data.

The essence of overfitting is to unknowingly extract some of the residual variation (i.e., noise) as if that variation represents the underlying model structure.

Underfitting occurs when a mathematical model cannot adequately capture the underlying structure of the data. An under-fitted model is missing some parameters or terms that would appear in a correctly specified model.

## Overfitting in Trading Strategy Development

The possibility of over-fitting exists when the criterion used for selecting the model is not the same as the criterion used to judge the suitability of a model. For example, a model might be selected by maximizing its performance on some set of training data, yet its suitability might be determined by its ability to perform well on unseen data; overfitting occurs when a model begins to "memorize" training data rather than "learning" to generalize from a trend.

As an extreme example, if the number of parameters is the same as or greater than the number of observations, then a model can perfectly predict the training data simply by memorizing the data in its entirety. Such a model will typically fail severely when making predictions.

## Techniques to Prevent Overfitting

Several techniques are available:
1. Model comparison / cross-validation
2. Regularization
3. Early stopping
4. Pruning
5. Bayesian priors
6. Dropout

The basis of some techniques is to either:
(1) explicitly penalize overly complex models, or
(2) test the model's ability to generalize by evaluating its performance on a set of data not used for training.

## Bias-Variance Tradeoff

Overfitted models are often free of bias in the parameter estimators, but have estimated (and actual) sampling variances that are needlessly large. False treatment effects tend to be identified, and false variables are included with overfitted models. A best approximating model is achieved by properly balancing the errors of underfitting and overfitting.

Overfitting is more likely to be a serious concern when there is little theory available to guide the analysis, in part because then there tend to be a large number of models to select from.

## Negative Consequences of Overfitting

- Poor performance on the validation dataset
- A more complex, overfitted function is likely to be less portable than a simple one
- Overfitted models may reconstruct details of individual training instances (privacy concerns)
- Estimated sampling variances are needlessly large
- False treatment effects tend to be identified

## Freedman's Paradox

With a large set of explanatory variables that actually have no relation to the dependent variable being predicted, some variables will in general be falsely found to be statistically significant and the researcher may thus retain them in the model, thereby overfitting the model. This is known as Freedman's paradox.

## Key Insight for Traders

Generally, a learning algorithm is said to overfit relative to a simpler one if it is more accurate in fitting known data (hindsight) but less accurate in predicting new data (foresight). Information from all past experience can be divided into two groups: information that is relevant for the future, and irrelevant information ("noise"). The problem is determining which part to ignore.

---

## 關鍵字

- 過度配適 Overfitting
- 欠配適 Underfitting
- 交叉驗證 Cross-Validation
- 正則化 Regularization
- 偏差-變異權衡 Bias-Variance Tradeoff
- 弗里德曼悖論 Freedman's Paradox
- 回測過擬合 Backtest Overfitting