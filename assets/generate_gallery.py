"""Generate the README gallery / hero banner.

Produces a set of representative plots that showcase the algorithms covered in
this repo, plus a combined `banner.png` used at the top of the README. The plots
use synthetic / built-in datasets so the script is fully reproducible and needs
no downloads.

Usage:
    python assets/generate_gallery.py

Outputs (written next to this script, in assets/):
    banner.png                  # 2x3 grid used as the README hero
    01_linear_regression.png
    02_decision_boundary.png
    03_kmeans.png
    04_pca.png
    05_dendrogram.png
    06_confusion_matrix.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris, make_blobs, make_moons
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

ASSETS = Path(__file__).resolve().parent
RNG = 42
plt.style.use("seaborn-v0_8-darkgrid")
CMAP = "viridis"


def linear_regression(ax):
    rng = np.random.default_rng(RNG)
    x = np.linspace(0, 10, 60)
    y = 2.3 * x + 5 + rng.normal(0, 3, x.size)
    model = LinearRegression().fit(x.reshape(-1, 1), y)
    ax.scatter(x, y, s=20, alpha=0.7, color="#3b7dd8")
    ax.plot(x, model.predict(x.reshape(-1, 1)), color="#e4572e", lw=2.5)
    ax.set_title("Linear Regression")


def decision_boundary(ax):
    X, y = make_moons(n_samples=300, noise=0.25, random_state=RNG)
    clf = SVC(kernel="rbf", gamma=1.5, C=1.0).fit(X, y)
    xx, yy = np.meshgrid(
        np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 300),
        np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 300),
    )
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.25, cmap=CMAP)
    ax.scatter(X[:, 0], X[:, 1], c=y, s=15, cmap=CMAP, edgecolor="k", linewidth=0.3)
    ax.set_title("SVM Decision Boundary")


def kmeans(ax):
    X, _ = make_blobs(n_samples=400, centers=4, cluster_std=0.9, random_state=RNG)
    km = KMeans(n_clusters=4, n_init=10, random_state=RNG).fit(X)
    ax.scatter(X[:, 0], X[:, 1], c=km.labels_, s=15, cmap=CMAP, alpha=0.8)
    ax.scatter(
        km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
        marker="X", s=180, color="#e4572e", edgecolor="k",
    )
    ax.set_title("K-Means Clustering")


def pca(ax):
    iris = load_iris()
    proj = PCA(n_components=2, random_state=RNG).fit_transform(iris.data)
    ax.scatter(proj[:, 0], proj[:, 1], c=iris.target, s=25, cmap=CMAP, edgecolor="k", linewidth=0.3)
    ax.set_title("PCA Projection (Iris)")


def dendro(ax):
    X, _ = make_blobs(n_samples=30, centers=3, cluster_std=0.8, random_state=RNG)
    dendrogram(linkage(X, method="ward"), ax=ax, color_threshold=0, above_threshold_color="#3b7dd8")
    ax.set_title("Hierarchical Clustering")
    ax.set_xticks([])


def confusion(ax):
    iris = load_iris()
    Xtr, Xte, ytr, yte = train_test_split(iris.data, iris.target, test_size=0.3, random_state=RNG)
    clf = RandomForestClassifier(n_estimators=200, random_state=RNG).fit(Xtr, ytr)
    ConfusionMatrixDisplay.from_estimator(
        clf, Xte, yte, ax=ax, cmap=CMAP, colorbar=False, display_labels=iris.target_names
    )
    ax.set_title("Random Forest — Confusion Matrix")


PANELS = [
    ("01_linear_regression", linear_regression),
    ("02_decision_boundary", decision_boundary),
    ("03_kmeans", kmeans),
    ("04_pca", pca),
    ("05_dendrogram", dendro),
    ("06_confusion_matrix", confusion),
]


def main():
    # Combined hero banner (2 rows x 3 cols).
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    for (name, fn), ax in zip(PANELS, axes.ravel()):
        fn(ax)
    fig.suptitle("ML-Algorithms — 18 algorithms, explained, from scratch + scikit-learn", fontsize=15, y=1.0)
    fig.tight_layout()
    fig.savefig(ASSETS / "banner.png", dpi=130, bbox_inches="tight")
    plt.close(fig)

    # Individual panels (handy for slides / posts).
    for name, fn in PANELS:
        f, a = plt.subplots(figsize=(5, 4))
        fn(a)
        f.tight_layout()
        f.savefig(ASSETS / f"{name}.png", dpi=130, bbox_inches="tight")
        plt.close(f)

    print(f"Wrote banner.png + {len(PANELS)} panels to {ASSETS}")


if __name__ == "__main__":
    main()
