# ML-Algorithms

An in-depth, hands-on course covering 18 core machine-learning algorithms — one notebook
per topic. Each notebook explains the **concept and intuition**, works through the
**mathematics**, and applies the algorithm **end-to-end on a real dataset** with a fully
worked example, evaluation, and a from-scratch implementation where it helps understanding.

## Curriculum

Work through the topics in order — each builds on the previous ones.

### Supervised Learning — Regression
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 1 | Linear Regression | [01_linear_regression.ipynb](notebooks/01_linear_regression.ipynb) | ✅ Done |
| 2 | Ridge & Lasso (Regularization) | _coming soon_ | ⬜ |

### Supervised Learning — Classification
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 3 | Logistic Regression | _coming soon_ | ⬜ |
| 4 | K-Nearest Neighbors (KNN) | _coming soon_ | ⬜ |
| 5 | Naive Bayes | _coming soon_ | ⬜ |
| 6 | Support Vector Machines (SVM) | _coming soon_ | ⬜ |
| 7 | Decision Trees | _coming soon_ | ⬜ |

### Ensemble Methods
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 8 | Random Forest | _coming soon_ | ⬜ |
| 9 | AdaBoost | _coming soon_ | ⬜ |
| 10 | Gradient Boosting | _coming soon_ | ⬜ |
| 11 | XGBoost | _coming soon_ | ⬜ |

### Unsupervised Learning — Clustering
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 12 | K-Means Clustering | _coming soon_ | ⬜ |
| 13 | Hierarchical Clustering | _coming soon_ | ⬜ |
| 14 | DBSCAN | _coming soon_ | ⬜ |

### Dimensionality Reduction & Pattern Mining
| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 15 | Principal Component Analysis (PCA) | _coming soon_ | ⬜ |
| 16 | t-SNE / UMAP (Visualization) | _coming soon_ | ⬜ |
| 17 | Anomaly Detection (Isolation Forest) | _coming soon_ | ⬜ |
| 18 | Association Rule Mining (Apriori) | _coming soon_ | ⬜ |

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
├── notebooks/                  # One notebook per topic (01 … 18)
│   └── 01_linear_regression.ipynb
├── requirements.txt
└── README.md
```
