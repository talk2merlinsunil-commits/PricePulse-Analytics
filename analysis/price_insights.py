import pandas as pd
#Load the datasets
data = pd.read_csv("dataset/cleaned_food_prices.csv.gz")
yearly = pd.read_csv("dataset/yearly_analysis.csv")
state_data = pd.read_csv("dataset/commodity_state_analysis.csv")
#Find the most expensive commodity
commodity_avg = data.groupby("commodity")["price"].mean()

most_expensive = commodity_avg.idxmax()
highest_avg_price = commodity_avg.max()

print("Most expensive commodity:", most_expensive)
print("Average price: ₹", round(highest_avg_price, 2))
#Find the commodity with the largest yearly increase
valid_changes = yearly.dropna(subset=["price_change_%"])

largest_increase = valid_changes.loc[
    valid_changes["price_change_%"].idxmax()
]

print("\nLargest yearly price increase:")
print(largest_increase[["commodity", "year", "price_change_%"]])
#Find the commodity with the biggest state-wise price gap
state_gaps = state_data.groupby("commodity")["mean"].agg(
    lambda x: x.max() - x.min()
)

biggest_gap = state_gaps.idxmax()

print("\nBiggest state-wise price gap:")
print(biggest_gap)
print("Price gap: ₹", round(state_gaps.max(), 2))