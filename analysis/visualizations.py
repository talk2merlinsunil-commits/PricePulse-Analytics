import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
yearly=pd.read_csv("dataset/yearly_analysis.csv")
i=0
commodities = yearly["commodity"].unique()

print("Available commodities:")
for i, commodity in enumerate(commodities, start=1):
    print(f"{i}. {commodity}")

selected = input(
    "\nEnter commodity names separated by commas: "
)

selected_commodities = [
    item.strip() for item in selected.split(",")
]
commodity_data = yearly[
    yearly["commodity"].isin(selected_commodities)
]
print(commodity_data)
plt.figure(figsize=(10,5))
sns.lineplot(data=commodity_data,
             x="year",
             y="price",
             marker="o",
             errorbar=None,
             hue="commodity"
             )
plt.legend(title="Commodity")
plt.title(f"Yearly Food Price Trend of {selected_commodities}")
plt.xlabel("Year")
plt.ylabel("Average Price (₹)")
plt.grid(True)
plt.show()
top_5 = (
    yearly.groupby("commodity")["price"]
    .mean()
    .nlargest(5)
)

print("Top 5 most expensive commodities:")
print(top_5)
top_5_data = yearly[
    yearly["commodity"].isin(top_5.index)
]
print(top_5_data.head())
plt.figure(figsize=(12, 6))

sns.lineplot(
    data=top_5_data,
    x="year",
    y="price",
    hue="commodity",
    marker="o",
    errorbar=None
)

plt.title("Yearly Price Trends of Top 5 Most Expensive Commodities")
plt.xlabel("Year")
plt.ylabel("Average Price (₹)")
plt.legend(title="Commodity")
plt.grid(True)
plt.show()
