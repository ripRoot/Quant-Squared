import pandas as pd
from pathlib import Path
## Requires file prices.csv in the same folder as this script, with a Date column and one column per stock.""

# 1. Load the data: a Date column plus one closing-price column per stock.
#    The file must be in the same folder as this script.
data = pd.read_csv(Path(__file__).parent / "prices.csv")

stocks = ["BABA", "GOOGL", "JD", "NTES", "NVDA"]
prices = data[stocks].dropna()   # keep only rows where all five stocks have a price

# 2. Daily percentage returns: (today - yesterday) / yesterday
returns = prices.pct_change().dropna()

# 3. Covariance and correlation of the daily returns
cov = returns.cov()
corr = returns.corr()

print("Covariance matrix")
print(cov.to_string(float_format="{:.8f}".format))
print()
print("Correlation matrix")
print(corr.to_string(float_format="{:.4f}".format))
