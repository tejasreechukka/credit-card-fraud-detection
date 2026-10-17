from pathlib import Path
import pandas as pd
PROJECT_ROOT= Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT /"data"/"raw"/"creditcard.csv"

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Datset not found at: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    #shape of the dataset
    print(df.shape)
    #Column names
    print(df.columns.tolist())
    #First five row
    print(df.head())
    #data types
    print(df.dtypes)
    #missing or null values
    print(df.isnull().sum())
    #duplicate rows
    print(df.duplicated().sum())
    #target counts
    if "Class" in df.columns:
        print(df["Class"].value_counts(normalize=True,dropna=False))

if __name__ =="__main__":
    main()
