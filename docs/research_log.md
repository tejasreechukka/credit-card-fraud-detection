Research Log

12 October 2026 — Project Setup

Initial research question

How effectively can machine learning identify fraudulent transactions, and how does AI assistance affect the analytical workflow?

Initial source

- Kaggle Credit Card Fraud Detection dataset
- URL: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Status: Source identified; dataset not yet downloaded or inspected.

Research topics to investigate

- Class imbalance in fraud detection.
- Precision, recall, F1-score, and precision-recall curves.
- Data leakage and correct train/test splitting.
- Appropriate baseline models.
- Fair evaluation of AI-assisted data science.
- Ethical considerations and limitations of historical transaction data.

Next action

Download the dataset and verify its schema on Day 2.

Day 2 — 14 October 2026: Dataset Collection

Source

Kaggle Credit Card Fraud Detection dataset:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Work completed

- Downloaded the dataset.
- Stored the CSV in "data/raw/".
- Checked that the raw data is excluded from Git.
- Inspected the dataset using a Python script.
- Recorded the schema and initial data quality observations.

Initial findings

- Dataset dimensions: [Insert actual output]
- Number of columns: [Insert actual output]
- Target distribution: [Insert actual output]
- Missing values: [Insert actual output]
- Exact duplicate rows: [Insert actual output]

Interpretation

[Write 2–4 sentences explaining what you observed and why it matters.]

Limitations

The data represents historical transactions and does not contain all the original transaction information. The PCA-transformed features cannot be interpreted as named customer or merchant characteristics.

Next action

Conduct a more detailed data quality audit and begin exploratory data analysis.

Day -3 Conducted a basic methodology test using Claude 
   (missing link)

## Day 4 — Reproducibility

- Centralised project paths and experiment settings in src/config.py.
- Defined a fixed random seed of 42.
- Defined a planned test size of 20%.
- Tested repeatability using sklearn train_test_split.
- Confirmed that repeated splits produce identical results.
- Documented package dependencies in requirements.txt.

Note: The reproducibility test used synthetic data,
not the actual credit card dataset.