# ML-Algorithms

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Notebooks](https://img.shields.io/badge/notebooks-18-orange.svg)](#curriculum)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/niravpatidar37/ML-Algorithms?style=social)](https://github.com/niravpatidar37/ML-Algorithms/stargazers)

> **18 core machine-learning algorithms — explained, derived, and built from scratch.**
> One notebook per topic: the intuition, the maths, and a fully worked example on a real
> dataset, side-by-side with the scikit-learn version. **Run any of them in your browser
> with one click — zero setup.**

![Gallery of plots produced across the notebooks](assets/banner.png)

## Why this repo?

- 🧠 **Theory *and* practice** — every algorithm covers the intuition, the underlying
  mathematics (cost functions, optimisation, key formulas), *and* a real worked example.
- 🛠️ **From scratch + scikit-learn** — see the algorithm implemented from first principles,
  then how you'd actually use it in practice.
- 📊 **Real datasets & proper evaluation** — the right metrics and plots for each problem,
  not just `.fit()` / `.score()`.
- ▶️ **Zero setup** — one-click **Open in Colab** on every notebook, or `pip install -r
  requirements.txt` to run locally.
- 🎯 **Great for** self-taught learners, students, and interview prep — a single, consistent
  path from linear regression to anomaly detection.

## Curriculum

Work through the topics in order — each builds on the previous ones. Click **Colab** to run
a notebook in the browser with zero setup.

### Supervised Learning
| # | Topic | Notebook | Run | Status |
|---|-------|----------|-----|--------|
| 1 | Linear Regression | [01_linear_regression.ipynb](01-linear-regression/01_linear_regression.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/01-linear-regression/01_linear_regression.ipynb) | ✅ Done |
| 2 | Ridge, Lasso & ElasticNet | [02_ridge_lasso_elasticnet.ipynb](02-ridge-lasso-elasticnet/02_ridge_lasso_elasticnet.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/02-ridge-lasso-elasticnet/02_ridge_lasso_elasticnet.ipynb) | ✅ Done |
| 3 | Logistic Regression | [03_logistic_regression.ipynb](03-logistic-regression/03_logistic_regression.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/03-logistic-regression/03_logistic_regression.ipynb) | ✅ Done |
| 4 | Support Vector Machines (SVM) | [04_svm.ipynb](04-svm/04_svm.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/04-svm/04_svm.ipynb) | ✅ Done |
| 5 | Naive Bayes | [05_naive_bayes.ipynb](05-naive-bayes/05_naive_bayes.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/05-naive-bayes/05_naive_bayes.ipynb) | ✅ Done |
| 6 | K-Nearest Neighbor (KNN) | [06_knn.ipynb](06-k-nearest-neighbor/06_knn.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/06-k-nearest-neighbor/06_knn.ipynb) | ✅ Done |
| 7 | Decision Tree | [07_decision_tree.ipynb](07-decision-tree/07_decision_tree.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/07-decision-tree/07_decision_tree.ipynb) | ✅ Done |

### Ensemble Methods
| # | Topic | Notebook | Run | Status |
|---|-------|----------|-----|--------|
| 8 | Random Forest | [08_random_forest.ipynb](08-random-forest/08_random_forest.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/08-random-forest/08_random_forest.ipynb) | ✅ Done |
| 9 | AdaBoost | [09_adaboost.ipynb](09-adaboost/09_adaboost.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/09-adaboost/09_adaboost.ipynb) | ✅ Done |
| 10 | Gradient Boosting | [10_gradient_boosting.ipynb](10-gradient-boosting/10_gradient_boosting.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/10-gradient-boosting/10_gradient_boosting.ipynb) | ✅ Done |
| 11 | XGBoost | [11_xgboost.ipynb](11-xgboost/11_xgboost.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/11-xgboost/11_xgboost.ipynb) | ✅ Done |

### Unsupervised Learning
| # | Topic | Notebook | Run | Status |
|---|-------|----------|-----|--------|
| 12 | Unsupervised ML (overview) | [12_unsupervised_overview.ipynb](12-unsupervised-ml/12_unsupervised_overview.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/12-unsupervised-ml/12_unsupervised_overview.ipynb) | ✅ Done |
| 13 | Principal Component Analysis (PCA) | [13_pca.ipynb](13-pca/13_pca.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/13-pca/13_pca.ipynb) | ✅ Done |
| 14 | K-Means Clustering | [14_kmeans.ipynb](14-k-means-clustering/14_kmeans.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/14-k-means-clustering/14_kmeans.ipynb) | ✅ Done |
| 15 | Hierarchical Clustering | [15_hierarchical_clustering.ipynb](15-hierarchical-clustering/15_hierarchical_clustering.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/15-hierarchical-clustering/15_hierarchical_clustering.ipynb) | ✅ Done |
| 16 | DBSCAN Clustering | [16_dbscan.ipynb](16-dbscan-clustering/16_dbscan.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/16-dbscan-clustering/16_dbscan.ipynb) | ✅ Done |
| 17 | Silhouette Analysis | [17_silhouette_analysis.ipynb](17-silhouette-analysis/17_silhouette_analysis.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/17-silhouette-analysis/17_silhouette_analysis.ipynb) | ✅ Done |
| 18 | Anomaly Detection | [18_anomaly_detection.ipynb](18-anomaly-detection/18_anomaly_detection.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niravpatidar37/ML-Algorithms/blob/main/18-anomaly-detection/18_anomaly_detection.ipynb) | ✅ Done |

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
datasets where they make a more compelling example. Local data files live in [data/](data/).

## Project structure

```
ML-Algorithms/
├── 01-linear-regression/
│   └── 01_linear_regression.ipynb
├── 02-ridge-lasso-elasticnet/
├── 03-logistic-regression/
├── ...                          # one folder per topic, 01 … 18
├── 18-anomaly-detection/
├── data/                        # local datasets (most come from sklearn/seaborn)
├── assets/                      # shared images + generate_gallery.py (README banner)
├── requirements.txt
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Roadmap

Done: all 18 classical algorithms above. Planned / ideas (contributions welcome — see below):

- [ ] Time-series forecasting (ARIMA, Prophet)
- [ ] Neural networks from scratch (MLP, backprop)
- [ ] Model selection & cross-validation deep-dive
- [ ] Feature engineering & pipelines
- [ ] A shared "datasets" cheatsheet

⭐ **Star the repo to follow along** as new topics land.

## Contributing

Found a typo, a clearer explanation, or want to add a topic from the roadmap? PRs and
issues are very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE).
