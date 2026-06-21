# ML-Algorithms

An in-depth, hands-on course covering 18 core machine-learning algorithms — one notebook
per topic, organised into a folder per topic. Each notebook explains the **concept and
intuition**, works through the **mathematics**, and applies the algorithm **end-to-end on a
real dataset** with a fully worked example, evaluation, and a from-scratch implementation
where it helps understanding.

## Curriculum

Work through the topics in order — each builds on the previous ones.

### Supervised Learning
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 1 | Linear Regression | [01_linear_regression.ipynb](1-Linear%20Regression/01_linear_regression.ipynb) | ✅ Done |
| 2 | Ridge, Lasso & ElasticNet | [02_ridge_lasso_elasticnet.ipynb](2-Ridge%20Lasso%20Elasticnet/02_ridge_lasso_elasticnet.ipynb) | ✅ Done |
| 3 | Logistic Regression | [03_logistic_regression.ipynb](3-Logistic%20Regression/03_logistic_regression.ipynb) | ✅ Done |
| 4 | Support Vector Machines (SVM) | [04_svm.ipynb](4-SVM/04_svm.ipynb) | ✅ Done |
| 5 | Naive Bayes | [05_naive_bayes.ipynb](5-Naive%20Bayes/05_naive_bayes.ipynb) | ✅ Done |
| 6 | K-Nearest Neighbor (KNN) | [06_knn.ipynb](6-K%20Nearest%20Neighbor/06_knn.ipynb) | ✅ Done |
| 7 | Decision Tree | [07_decision_tree.ipynb](7-Decision%20Tree/07_decision_tree.ipynb) | ✅ Done |

### Ensemble Methods
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 8 | Random Forest | [08_random_forest.ipynb](8-Random%20Forest/08_random_forest.ipynb) | ✅ Done |
| 9 | AdaBoost | [09_adaboost.ipynb](9-Adaboost/09_adaboost.ipynb) | ✅ Done |
| 10 | Gradient Boosting | [10_gradient_boosting.ipynb](10-Gradient%20Boosting/10_gradient_boosting.ipynb) | ✅ Done |
| 11 | XGBoost | [11_xgboost.ipynb](11-XGBoost/11_xgboost.ipynb) | ✅ Done |

### Unsupervised Learning
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 12 | Unsupervised ML (overview) | [12_unsupervised_overview.ipynb](12-Unsupervised%20ML/12_unsupervised_overview.ipynb) | ✅ Done |
| 13 | Principal Component Analysis (PCA) | _coming soon_ | ⬜ |
| 14 | K-Means Clustering | _coming soon_ | ⬜ |
| 15 | Hierarchical Clustering | _coming soon_ | ⬜ |
| 16 | DBSCAN Clustering | _coming soon_ | ⬜ |
| 17 | Silhouette Analysis | _coming soon_ | ⬜ |
| 18 | Anomaly Detection | _coming soon_ | ⬜ |

## Each notebook follows the same structure

1. **Concept & intuition** — what the algorithm does and why
2. **The mathematics** — cost functions, optimisation, key formulas
3. **Assumptions / requirements**
4. **A real dataset** — chosen to showcase the algorithm
5. **EDA** — understanding the data first
6. **Training** with scikit-learn
7. **Evaluation** with the right metrics and plots
8. **From scratch** (where it deepens understanding)
9. **Pros, cons & when to use**
10. **Summary**

## Getting started

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter and open a notebook
jupyter notebook
```

Datasets are a mix of scikit-learn / seaborn built-ins (zero setup) and real-world
datasets where they make a more compelling example.

## Project structure

```
ML-Algorithms/
├── 1-Linear Regression/
│   └── 01_linear_regression.ipynb
├── 2-Ridge Lasso Elasticnet/
├── 3-Logistic Regression/
├── ...                          # one folder per topic, 1 … 18
├── 18-Anomaly Detection/
├── requirements.txt
└── README.md
```
