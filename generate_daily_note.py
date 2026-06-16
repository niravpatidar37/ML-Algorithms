import os
import json
from datetime import date

today = str(date.today())

# Rotate through topics daily
topics = [
    "Linear Regression", "Ridge & Lasso", "Logistic Regression",
    "SVM", "Naive Bayes", "KNN", "Decision Tree", "Random Forest",
    "Adaboost", "Gradient Boosting", "XGBoost", "K-Means",
    "PCA", "DBSCAN", "Hierarchical Clustering", "Anomaly Detection"
]

day_of_year = date.today().timetuple().tm_yday
topic = topics[day_of_year % len(topics)]

notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.10.0"}
    },
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"# Daily ML Note: {topic}\n**Date:** {today}"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [f"# Auto-generated revision note for {topic}\nprint('Reviewing: {topic}')"]
        }
    ]
}

folder = "daily-notes"
os.makedirs(folder, exist_ok=True)
filepath = os.path.join(folder, f"{today}-{topic.replace(' ', '-')}.ipynb")

with open(filepath, "w") as f:
    json.dump(notebook, f, indent=2)

print(f"Created: {filepath}")