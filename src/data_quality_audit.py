from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT /"data"/"raw"/"creditcard.csv"


def main():

    print("=" * 55)
    print("CREDIT CARD FRAUD DETECTION - DATA QUALITY AUDIT")
    print("=" * 55)

    # 1. Load dataset
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    # 2. Dataset structure
    print("\n1. DATASET STRUCTURE")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # 3. Missing values
    print("\n2. MISSING VALUES")
    missing = df.isnull().sum()
    print(missing[missing > 0])

    print("Total missing values:", df.isnull().sum().sum())

    # 4. Duplicate records
    print("\n3. DUPLICATE RECORDS")
    duplicates = df.duplicated().sum()
    print("Exact duplicate rows:", duplicates)

    # 5. Data types
    print("\n4. DATA TYPES")
    print(df.dtypes)

    # 6. Numerical summary
    print("\n5. NUMERICAL SUMMARY")
    print(df.describe().T)

    # 7. Target validation
    print("\n6. TARGET DISTRIBUTION")

    if "Class" in df.columns:
        print(df["Class"].value_counts(dropna=False))
        print("\nPercentages:")
        print(
            df["Class"].value_counts(
                normalize=True, dropna=False
            ) * 100
        )

        print("\nUnexpected target values:")
        print(df.loc[~df["Class"].isin([0, 1]), "Class"].unique())

    # 8. Negative transaction amounts
    print("\n7. AMOUNT VALIDATION")

    if "Amount" in df.columns:
        print("Negative amounts:", (df["Amount"] < 0).sum())
        print("Zero amounts:", (df["Amount"] == 0).sum())
        print("Maximum amount:", df["Amount"].max())

    # 9. Time validation
    print("\n8. TIME VALIDATION")

    if "Time" in df.columns:
        print("Minimum time:", df["Time"].min())
        print("Maximum time:", df["Time"].max())
        print("Negative time values:", (df["Time"] < 0).sum())

    # 10. Final summary
    print("\n9. AUDIT SUMMARY")
    print("Dataset shape:", df.shape)
    print("Missing values:", df.isnull().sum().sum())
    print("Duplicate rows:", duplicates)

    print("\nAudit completed successfully.")


if __name__ == "__main__":
    main()