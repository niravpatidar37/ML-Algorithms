# Contributing

Thanks for your interest in improving **ML-Algorithms**! This is a learning resource, so
contributions that make a topic *clearer* or *more correct* are just as valuable as new
content.

## Ways to contribute

- **Fix** a typo, a broken link, or a mathematical/code error.
- **Clarify** an explanation, add intuition, or improve a plot.
- **Add a topic** from the [roadmap](README.md#roadmap) (or propose a new one in an issue first).

## Notebook conventions

To keep the course consistent, each notebook follows the same structure:

1. Concept & intuition
2. The mathematics
3. Assumptions / requirements
4. A real dataset
5. EDA
6. Training with scikit-learn
7. Evaluation (right metrics + plots)
8. From scratch (where it deepens understanding)
9. Pros, cons & when to use
10. Summary

A few practical notes:

- Place a new topic in its own zero-padded, kebab-case folder: `NN-topic-name/`,
  with the notebook named `NN_topic_name.ipynb`.
- **Clear notebook outputs before committing** (`Kernel → Restart & Clear Output`) to keep
  diffs small and the repo light.
- Prefer scikit-learn / seaborn built-in datasets where they work; put any local data in
  [`data/`](data/).
- If you add a new dependency, pin it in [`requirements.txt`](requirements.txt).

## Submitting changes

1. Fork the repo and create a branch: `git checkout -b improve-topic-x`.
2. Make your change and check the notebook runs top-to-bottom without errors.
3. Open a pull request describing what you changed and why.

By contributing, you agree that your contributions are licensed under the
[MIT License](LICENSE).
