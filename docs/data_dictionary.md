Data Dictionary

Dataset Information

- Dataset: Credit Card Fraud Detection
- Source: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Observation unit: One transaction record
- Target variable: "Class"
- Inspection date: 14 October 2026

Variables

Variable| Meaning| Role
"Time"| Seconds elapsed since the first transaction in the dataset| Input feature
"V1"–"V28"| Anonymised principal components derived using PCA| Input features
"Amount"| Transaction amount| Input feature
"Class"| 0 = legitimate transaction; 1 = fraudulent transaction| Target

Verification Status

The expected schema is 30 input features and one target column, giving 31 columns in total. Verify this against the downloaded file.

Notes and Limitations

- The dataset represents historical transactions from September 2013 over two days.
- The original meanings of the PCA-transformed variables are not available.
- The dataset is highly imbalanced, with fraudulent transactions representing approximately 0.172% of records.
- The currency and original meaning of the anonymised variables should not be assumed beyond what the source documents.
- Missing values, duplicates, data types, and target counts must be confirmed using the local file.

Findings

Complete this section after running "src/inspect_dataset.py". Record actual results, not assumed values.