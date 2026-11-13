import pandas as pd
data=pd.read_csv("dataset/cleaned_food_prices.csv.gz")
print(data.head())
commodity_state_analysis=data.groupby(
    ["commodity","state_name"]
)["price"].agg(
    ["mean","min","max","median","std"]
)
print(commodity_state_analysis)

commodity_state_analysis.to_csv("dataset/commodity_state_analysis.csv")
# to find total number of commodity combintion with state
print("Total commodity-state combinations:",len(commodity_state_analysis))
print("\nHighest and lowest priced state for each commodity:")
print("Total commodity-state combinations:", len(commodity_state_analysis))

print("\nHighest and lowest priced states for each commodity:")

for commodity in data["commodity"].unique():
    result = commodity_state_analysis.loc[commodity]

    highest_state = result["mean"].idxmax()
    lowest_state = result["mean"].idxmin()

    print(f"\n{commodity}")
    print(f"Highest: {highest_state} - ₹{result.loc[highest_state, 'mean']:.2f}")
    print(f"Lowest: {lowest_state} - ₹{result.loc[lowest_state, 'mean']:.2f}")

price_gap_analysis=[]
for commodity in data["commodity"].unique():
    result = commodity_state_analysis.loc[commodity]

    highest_state = result["mean"].idxmax()
    lowest_state = result["mean"].idxmin()

    highest_price=result.loc[highest_state,"mean"]
    lowest_price=result.loc[lowest_state,"mean"]
    price_gap=highest_price-lowest_price
    percentage_diff=(price_gap/lowest_price)*100
    price_gap_analysis.append({
    "commodity": commodity,
    "highest_state": highest_state,
    "highest_price": highest_price,
    "lowest_state": lowest_state,
    "lowest_price": lowest_price,
    "price_gap": price_gap,
    "percentage_difference": percentage_diff
    })
price_gap_analysis=pd.DataFrame(price_gap_analysis)
print(price_gap_analysis)
expensive_commodities = data.groupby("commodity")["price"].agg(
    ["mean", "min", "max", "median","std"]
)
expensive_commodities = expensive_commodities.sort_values(
    by="mean",
    ascending=False
)
print(expensive_commodities[["mean"]].head(10))