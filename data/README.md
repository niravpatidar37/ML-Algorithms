# Data

Most notebooks load datasets directly from `scikit-learn` or `seaborn` built-ins,
so they need **zero setup**.

Use this folder for any **local datasets** a notebook reads from disk (CSV, etc.).
Reference them with a relative path from the notebook, e.g.:

```python
import pandas as pd
df = pd.read_csv("../data/my_dataset.csv")
```

Large or downloaded datasets are git-ignored (see [.gitignore](../.gitignore));
keep only small, redistributable files here, or add a script/cell that downloads
the data on demand.
