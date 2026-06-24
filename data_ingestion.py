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

fund_master = pd.read_csv(DATA_DIR / "01_fund_master.csv")
nav_history = pd.read_csv(DATA_DIR / "02_nav_history.csv")

master_codes = set(fund_master["scheme_code"].astype(str))
nav_codes = set(nav_history["scheme_code"].astype(str))

missing_codes = master_codes - nav_codes

print("\\nAMFI VALIDATION")
print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

print("\\nUnique Fund Houses:", fund_master["fund_house"].nunique())
print("Categories:", fund_master["category"].unique())
