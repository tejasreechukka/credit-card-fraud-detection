Day 5 — Credit Card Fraud Detection Data Quality Report

1. Dataset Overview

- Dataset: Credit Card Fraud Detection
- Source: Kaggle — (https://www.kaggle.com/datasets/rehanliaqat17/creidct-card?resource=download)
- Rows: 284807
- Columns: 31

2. Missing Values

- Total missing values: 0
- Columns affected: 0
- Decision: 0 missing values found.Need tp be investigated further

3. Duplicate Records

- Exact duplicate rows: 1081
- Investigation performed: there are 1081 duplicate records needs further investigation. Need to check where they are legitimate.
- Decision: [further investigation required]

4. Data Types

- Numerical columns: 30 colomns float, 1 coloumn int
- Target column type: int64
- Unexpected data types: No findings

5. Numerical Validation

Amount

- Minimum: [Actual value]
- Maximum: [25691.16]
- Negative values: [0]
- Zero values: [1825]

Time

- Minimum: [0.0]
- Maximum: [172792.0]
- Negative values: [0]

6. Target Distribution

- Class 0 legitimate transactions: 284315
- Class 1 fraudulent transactions: 492
- Legitimate percentage: 99.82
- Fraudulent percentage: 0.17

7. Data Quality Decisions

Issue| Finding| Action
Missing values| 0 missing values| Need to check once again for any missing or null values
Duplicates| 1081| validate the duplicate rows again
Data types| Float and int| All the coloumn data type sare float and int
Amount values|Negative amounts: 0
Zero amounts: 1825
Maximum amount: 25691.16 | Validate the zero amount and maximum amount values to find whether they are true
Time values| Minimum time: 0.0
Maximum time: 172792.0
Negative time values: 0| Time lapse recorded between two tranactions
Class imbalance| [Finding]| [Decision]

8. Conclusion

As far as the above findings there are no data quality issues that are to be taken care of. The data has no missing values, 1081 duplicate values and 492(0.17%) fradulent transactions. Further Explorartory data analysis can be done to identify any more fradulent cases or any genuine cases that are mistakenly taken as fradulent. 

9. Limitations

This audit identifies issues detectable through the available dataset fields. It cannot establish whether every transaction is genuine, correctly labelled, or representative of current fraud behaviour.