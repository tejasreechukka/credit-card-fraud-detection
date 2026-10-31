Credit Card Fraud Detection — Experimental Methodology

1. Project Aim

The aim of this project is to investigate credit card fraud detection using data analysis and machine learning. The project will compare a manually designed analytical workflow with an AI-assisted workflow.

The comparison will consider correctness, reproducibility, analytical quality, evaluation metrics, time required, and limitations.

2. Research Questions

1. How can exploratory data analysis reveal patterns and data-quality issues in credit card transactions?
2. How does class imbalance affect the evaluation of fraud detection models?
3. Which evaluation metrics are most appropriate for this imbalanced classification problem?
4. Does AI assistance improve the efficiency and quality of the analytical workflow?
5. What errors, assumptions, or limitations can occur when AI-generated code and explanations are used?

3. Dataset

The project uses the Credit Card Fraud Detection dataset published by MLG-ULB on Kaggle.

Source: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset contains transaction features, an Amount column, and a Class target. Class 1 represents fraudulent transactions and Class 0 represents legitimate transactions.

The dataset's dimensions, missing values, duplicates, data types, and class distribution will be verified programmatically before analysis.

4. Experimental Workflows

Workflow A: Manual Analysis

1. Inspect the dataset and validate data quality.
2. Explore feature distributions and class imbalance.
3. Create visualisations and document observations.
4. Prepare the features and target variable.
5. Split the data into training and test sets.
6. Train baseline classification models.
7. Evaluate the models using suitable metrics.
8. Record decisions, results, and limitations.

Workflow B: AI-Assisted Analysis

1. Give an AI assistant the same verified dataset information.
2. Request suggestions for data-quality checks and exploratory analysis.
3. Ask for explanations and candidate code for selected tasks.
4. Review and execute the generated code.
5. Verify results independently rather than accepting AI output without checking.
6. Record useful suggestions, mistakes, corrections, and time spent.
7. Evaluate the final results using the same rules as the manual workflow.

5. Fair Comparison Rules

- Use the same dataset and target definition for both workflows.
- Apply the same train/test split wherever models are compared directly.
- Use the same evaluation metrics and test data for comparable models.
- Keep preprocessing and feature selection decisions documented.
- Fit learned preprocessing steps on training data only.
- Do not use test-set results to repeatedly tune the model.
- Record AI-generated suggestions separately from verified findings.
- Report actual results, including unsuccessful experiments.

6. Data Leakage Prevention

Data leakage occurs when information unavailable at prediction time influences model training or evaluation.

To reduce leakage:

- Separate training and test data before fitting learned preprocessing steps.
- Fit scalers, imputers, and other learned transformations on training data only.
- Do not use the target variable as an input feature.
- Keep the test set separate from model selection and tuning.
- Document any data preparation that occurs before splitting and justify it.

7. Evaluation Metrics

The primary evaluation measures will include:

- Precision: Of transactions predicted as fraud, how many were actually fraud?
- Recall: Of all actual fraudulent transactions, how many were detected?
- F1-score: The harmonic mean of precision and recall.
- Confusion matrix: Counts of true positives, true negatives, false positives, and false negatives.
- Precision-recall curve and average precision: Useful for evaluating fraud detection under severe class imbalance.

Accuracy will also be reported where useful, but it will not be used alone to judge model quality.

8. AI Usage and Verification

For each AI-assisted task, record:

- Tool and model used, when known
- Prompt provided
- Output or recommendation received
- Code or claims independently checked
- Errors or unsupported assumptions identified
- Corrections made
- Time spent

AI output will be treated as a proposal, not as verified evidence.

9. Reproducibility

The project will maintain documented dependencies, scripts, research notes, and Git history. Random seeds and split settings will be recorded where applicable.

The raw dataset will remain outside version control.

10. Limitations

The dataset is historical and anonymised. Its patterns may not represent current fraud behaviour or every real-world payment system. Model performance on this dataset does not guarantee performance in a live credit card or UPI payment environment.

The manual-versus-AI comparison will also be affected by the prompts used, the user's experience, and the amount of time spent reviewing outputs.

11. Planned Outcome

The final report will compare analytical decisions, code quality, efficiency, evaluation results, and limitations. Conclusions will be based on recorded experiments rather than assumed improvements from AI assistance.

