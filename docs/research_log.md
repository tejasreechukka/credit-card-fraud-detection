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

## Day 5 — AI Data Quality Review

### Tool
Claude [sonnet 5.5]

### Prompt
Data quality audit review.
[1. Identify potential data-quality issues.
2. Explain whether duplicate records should be investigated or removed.
3. Identify unusual numerical values that deserve further investigation.
4. Explain the impact of class imbalance.
5. Recommend appropriate next steps before exploratory data analysis.
6. Identify any checks missing from my audit.]

### Useful Recommendations
1. Potential data-quality issues
Possible duplication artefacts: 1,081 exact copies is not trivial (about 0.38% of rows).
Zero-amount transactions: 1,825 rows whose meaning is unknown. They could be a sentinel for missing or unknown, a non-monetary event, or a genuine value.
Extreme right tail in Amount: the maximum of 25,691.16 is far above what typical card transactions suggest, though I haven’t seen the distribution.
Severe class imbalance (a data characteristic that acts like a quality issue for modelling).
Limited temporal coverage: about 48 hours constrains generalisation and makes concept drift untestable.
Heterogeneous feature scales: Time and Amount are on very different scales from the (presumably) PCA-derived features.
Gaps in your audit itself: a placeholder [Actual value] for the Amount minimum, and a “Fraudulent percentage” that makes the two percentages sum to 99.99 (correctly rounded they are 99.83 and 0.17).

“0 missing values” does not mean “complete”. It means no NaN. Disguised missingness (sentinels such as 0 or -1, or inf) is a separate check.

2. Duplicates: investigate first, then decide

Investigate before removing. Whether to drop them depends on what they are and what you are using them for.

Reasons they may be artefacts: independent transactions are unlikely to match exactly across 30 continuous float columns including a 1-second-resolution Time, so identical rows suggest duplicated records.

Reasons they may be legitimate: if the underlying raw features are low-dimensional, two genuinely identical events (e.g. retries, split payments) could map to identical PCA values. Fraudsters also commonly repeat identical attempts, so duplicates in the fraud class could be real attack behaviour, and deleting them would remove signal from the scarcest class.

Why it matters for modelling: if duplicates are split across train and test, the model is evaluated on rows it has memorised, inflating performance. This is leakage. The effect is proportionally larger if duplicates concentrate in the minority class.

Investigate with:

python
dup_all   = df.duplicated(keep=False)          # every member of duplicate groups
dup_extra = df.duplicated(keep='first')        # the 1,081 "extra" copies
print(dup_all.sum(), dup_extra.sum())
print(df[dup_all].groupby('Class').size())      # distribution by class
# conflicting labels: same features, different Class
feat = [c for c in df.columns if c != 'Class']
print((df.groupby(feat)['Class'].nunique() > 1).sum())
# file-order adjacency and time clustering of duplicates
print(df[dup_all].sort_index().head(20))

Also check duplicates excluding Time (near-duplicates in feature space). Then document a decision rule, for example:

Conflicting labels: flag as label noise and examine individually.
Adjacent or same-Time copies: likely artefacts, so deduplicate with justification.
Fraud duplicates: decide separately and justify.

Finally, run a sensitivity analysis: report model results with and without duplicates. At minimum, deduplicate (or use group-aware splitting) before creating train/test sets.

3. Unusual numerical values to investigate
Amount = 0 (1,825 rows): tabulate by Class. If they are disproportionately fraudulent, this could reflect “card testing” (a hypothesis, not a finding). If they are mostly legitimate, they may be auth checks. Either way, don’t impute or drop without evidence.
Amount maximum (25,691.16): inspect the top-N values, their Class, and their Time. A single high-value legitimate transaction is plausible. Don’t treat it as an error just because it is large. Compare it to the 99th and 99.9th percentiles.
Amount distribution shape: report mean, median, quantiles, skewness. Heavy skew often motivates a log transform, but that is a modelling decision for later.
Time: confirm monotonicity, look for gaps, and check the transaction rate per hour (daily cycles would be expected if it spans two days). Don’t assume a calendar start time.
V1–V28: check means near 0, variances, extreme tails, and whether they are approximately uncorrelated (expected for PCA, to be confirmed). Don’t remove “outliers” in these naively: in fraud detection the anomalies are often the signal.
4. Impact of class imbalance
Accuracy paradox: predicting “legitimate” for everything yields about 99.83% accuracy while detecting zero fraud. Accuracy is therefore uninformative.
Metrics: prefer precision-recall curves/AUPRC (the no-skill baseline equals prevalence, about 0.0017), recall at a fixed precision or alert budget, F-beta, and MCC. ROC-AUC can look deceptively strong because the huge negative class keeps the false-positive rate small even when precision is poor.
Estimator variance: with 492 positives, a 20% test set holds about 98 frauds, so metrics have wide confidence intervals. Use stratified splits, repeated stratified k-fold, and report intervals (e.g. bootstrap).
Training dynamics: unweighted loss is dominated by the majority class, giving biased decision boundaries and poorly calibrated probabilities.
Mitigation options: class weights/cost-sensitive learning, threshold tuning on validation data, and resampling (SMOTE, undersampling). Resampling must occur only inside training folds, never before splitting, or synthetic samples leak into validation. Resampling also distorts predicted probabilities, so recalibrate if you need them.
Business framing: false negatives and false positives have different costs, so the operating threshold should reflect that.
5. Recommended next steps before EDA
Preserve the raw data: keep an untouched copy, record the file hash, row count and source/version.
Complete and rewrite the audit: fill every placeholder, and make “Action” cells actual actions (e.g. “Tabulated zero-amount rows by class; decision: retain, flagged”).
Resolve the duplicates per section 2, and log the decision with its evidence.
Define the evaluation design first: stratified split, or a temporal split (train on earlier Time, test on later), with duplicates handled and held-out data untouched.
Perform EDA on the training partition only, so insights, scaling parameters and feature choices aren’t informed by test data.
Create a data-quality log linking each finding to evidence, hypothesis, decision and rationale. This is what examiners reward.
6. Checks missing from your audit
Shape, column names and schema against the documentation.
Class domain check: df['Class'].unique() should be exactly {0, 1}.
inf/-inf, constant or near-constant columns, and sentinel value scan.
Full descriptive statistics (the Amount min is missing), and per-class summaries.
Duplicate checks excluding Time, near-duplicates, and label conflicts.
Row ordering and Time monotonicity.
Fraud rate over time (is prevalence stable across the 48 hours?).
Feature correlation and PCA sanity check (are the V columns near-uncorrelated?).
Scale comparison across columns.
Provenance: confirm this Kaggle upload matches the original source, its licence/terms, and documented anonymisation.
Representativeness limits: short window, single institution/region (verify from documentation), label reliability (delayed or confirmed-only labels), and any ethical/data-protection considerations.

### Independently Verified
I have performed a basic data quality audit check on the given Kaggle data set. I have obtained the Numerical summary, missing values, null values , duplicate records, shape and coloumns of the dataset. I hav egiven my whole analysis to the AI and asked to verify the findings.

### Incorrect or Unsupported Suggestions
As far no record of incorrect or unsupported suggestions. Infact the AI has given more advanced suggestions and data analysis techniques to be performed with the data.

### Conclusion
I have given basic manual data quality analysis report and asked the AI to compare its findings and evaluate any missing audit. The AI has suggested many advanced Exploratory data analytics techniques. It has given the report of precise numbers and why those numbers need to be verified again. Suggested the missing numerical summary to be taken care of. Overall AI has compared the manual analysis to its own findings and the suggestions expected were little basic but turned out to be advanced to where still the manula analysis has not done. So the AI has the power of interpreting and improvising the prompt and also return the extra information besides the useful and required one.