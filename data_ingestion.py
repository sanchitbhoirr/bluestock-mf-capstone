import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

for csv_file in DATA_DIR.glob("*.csv"):
    df = pd.read_csv(csv_file)
    print("="*80)
    print(csv_file.name)
    print("Shape:", df.shape)
    print(df.dtypes)
    print(df.head())
    print("Missing Values:")
    print(df.isnull().sum())

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("Fund Master Columns:")
print(fund_master.columns.tolist())

print("\nNAV History Columns:")
print(nav_history.columns.tolist())

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("Fund Master Columns:")
print(fund_master.columns.tolist())

print("\nNAV History Columns:")
print(nav_history.columns.tolist())

print("\\nUnique Fund Houses:", fund_master["fund_house"].nunique())
print("Categories:", fund_master["category"].unique())
