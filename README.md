# ML-Algorithms

A self-updating repository of daily machine-learning revision notes. Every day a
GitHub Actions workflow generates a fresh Jupyter notebook for one ML topic and
commits it automatically — keeping the repo active and building a growing study log.

## How it works

1. [`generate_daily_note.py`](generate_daily_note.py) picks an ML topic based on the
   day of the year and writes a notebook into [`daily-notes/`](daily-notes/).
2. The scheduled workflow in
   [`.github/workflows/daily-push.yml`](.github/workflows/daily-push.yml) runs once a
   day, executes the script, and commits + pushes the new notebook.

## Topics covered

Linear Regression · Ridge & Lasso · Logistic Regression · SVM · Naive Bayes · KNN ·
Decision Tree · Random Forest · Adaboost · Gradient Boosting · XGBoost · K-Means ·
PCA · DBSCAN · Hierarchical Clustering · Anomaly Detection

## Project structure

```
ML-Algorithms/
├── .github/workflows/
│   └── daily-push.yml        # Daily auto-commit GitHub Action
├── daily-notes/              # Auto-generated daily notebooks
│   └── YYYY-MM-DD-<Topic>.ipynb
├── generate_daily_note.py    # Notebook generator
└── README.md
```

## Run it manually

```bash
python generate_daily_note.py
```

This creates a new notebook in `daily-notes/` for today's topic.

## Automation

The workflow runs daily on a cron schedule and can also be triggered manually from the
**Actions** tab via **Run workflow**. It requires *Read and write* workflow permissions
(Settings → Actions → General → Workflow permissions).
