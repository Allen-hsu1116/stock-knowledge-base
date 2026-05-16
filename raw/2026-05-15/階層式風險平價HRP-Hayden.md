# 【資產配置】第五代資產配置理論：階層式風險平價（Hayden海頓君）

**來源**：https://medium.com/data-driven-investment/%E8%B3%87%E7%94%A2%E9%85%8D%E7%BD%AE-%E7%AC%AC%E4%BA%94%E4%BB%A3%E8%B3%87%E7%94%A2%E9%85%8D%E7%BD%AE%E7%90%86%E8%AB%96-%E9%9A%8E%E5%B1%A4%E5%BC%8F%E9%A2%A8%E9%9A%AA%E5%B9%B3%E5%83%B9-ed606276b652
**日期**：2026-05-15
**主題**：風險管理

---

## Abstract

Lopez de Prado (2016) 結合了機器學習和圖論，想出了將相關係數矩陣降維後再放進MPT求解的方法，解決MPT對於參數太敏感的問題。

核心想法：將相關係數矩陣從 complete graph 轉換為 binary tree，透過機器學習中的 clustering 演算法，總共有3大步驟：

1. **Tree Clustering**：對 correlation matrix 執行 clustering
2. **Quasi-Diagonalization**：將 correlation matrix 依照 step1 排序
3. **Recursive Bisection**：依照 step2 的二叉樹迭代更新權重

## Warm up: MPT, IVP

根據馬可維茲的理論，long-only投資組合的封閉解：

在long-only約束下，馬可維茲解退化為反變異數組合（Inverse Variance Portfolio, IVP）：

w_i ∝ 1/σ_i²

## HRP 的三大步驟

### Step 1 & 2: Tree Clustering + Quasi-Diagonalization

核心問題：MPT對參數敏感，根本原因是相關係數矩陣的 condition number 過高。

相關係數矩陣在圖論上等價於 complete graph（完全圖），太多不必要的 edges 導致過多雜訊。我們只需要一個 Hierarchical Structure 即可——將 complete graph 剪枝降維成樹狀結構，減少不必要的雜訊達到優化目的。

Python 實作只需一行：
```python
import seaborn as sns
sns.clustermap(corr_matrix)
```

### Step 3: Recursive Bisection

在二叉樹結構下（N=2）重新推導 IVP 的權重，透過遞歸法從二叉樹 bottom-up 走訪迭代更新權重。

## Monte Carlo Simulation 驗證

在100萬次蒙地卡羅模擬中，HRP 表現證實優於原有方法。

修改版的 bottom-up 遞歸法比原作者提出的方法至少好 10%，且具有 robustness——不論如何修改 Linkage 方法（Daniel Müllner, 2011），bottom-up 方法都勝過原方法。

## 業界現況

目前業界還是傾向於透過 Barra Risk Model 進行風控，平衡各風險因子來穩定投資組合。

Lopez de Prado 本人進入 AQR 後短短不到一年就離職，或許暗示其理論離實際應用還有一段距離。

## Conclusion

- MPT 對參數敏感的問題是因為相關係數矩陣的 conditional number 過高
- 可以透過降維的方式將相關係數矩陣由 complete graph 剪枝成二叉樹
- 目前業界還是傾向於使用 Barra Risk Model 進行風控

---

## 關鍵字

- HRP
- 階層式風險平價
- Hierarchical Risk Parity
- Lopez de Prado
- MPT
- clustering
- condition number
- complete graph
- binary tree
- Barra Risk Model