import pandas as pd

data = pd.read_csv("dataset/cleaned_food_prices.csv.gz")

# 1. Calculate yearly average prices
yearly_analysis = data.groupby(
    ["year", "commodity"]
)["price"].mean().reset_index()

# 2. Sort by commodity and year
yearly_analysis = yearly_analysis.sort_values(
    ["commodity", "year"]
)

# 3. Calculate yearly percentage change
yearly_analysis["price_change_%"] = (
    yearly_analysis.groupby("commodity")["price"]
    .pct_change() * 100
)

# 4. Reset row numbering
yearly_analysis = yearly_analysis.reset_index(drop=True)

# 5. Display results
pd.set_option("display.max_rows", None)
#print(yearly_analysis)

# 6. Save results
yearly_analysis.to_csv(
    "dataset/yearly_analysis.csv",
    index=False
)
valid_changes=yearly_analysis.dropna(
    subset=["price_change_%"]
)
highest_increase = valid_changes.loc[
    valid_changes.groupby("commodity")["price_change_%"].idxmax()
]
highest_decrease = valid_changes.loc[
    valid_changes.groupby("commodity")["price_change_%"].idxmin()
]
print("Highest increases:")
print(highest_increase[["commodity", "year", "price_change_%"]])
print("Highest decreases:")
print(highest_decrease[["commodity", "year", "price_change_%"]])
print(
    yearly_analysis.groupby("commodity")["year"].nunique()
)