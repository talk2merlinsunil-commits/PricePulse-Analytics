import pandas as pd
data=pd.read_csv("dataset/food_prices.csv")
data=data.dropna(subset=["price"])
data["date"]=pd.to_datetime(data["date"])
data["year"]=data["date"].dt.year
data["month"]=data["date"].dt.month
# # print(data.info())
# # print(data[["date", "year", "month"]].head())
# # print(data.shape)
# # print("Lowest 10 prices:")
# # print(data["price"].nsmallest(10))
# # print("Highest 10 prices:")
# # print(data["price"].nlargest(10))
# # print("Price statistics:")
# # print(data["price"].describe())
# commodity_analysis = data.groupby("commodity")["price"].agg(
#     ["mean", "min", "max", "median","std"]
# )

# # print(commodity_analysis.sort_values("std",ascending=False))
# # data.to_csv(
# #     "dataset/cleaned_food_prices.csv",
# #     index=False
# # )
# # commodity_analysis["cv"]=(commodity_analysis["std"]/commodity_analysis["mean"])*100
# # print(commodity_analysis.sort_values("cv",ascending=False))
# # state_analysis=data.groupby("state_name")["price"].agg(
# #     ["mean","min","max","median","std"]
# # )
# # print(state_analysis.sort_values("mean",ascending=False))
# # print("Highes average price state:")
# # print(state_analysis["mean"].idxmax())
# # print(state_analysis["mean"].idxmin())
# print(data["commodity"].unique())
print(data.info())
print(data.isnull().sum())
print("Duplicate rows:", data.duplicated().sum())
print("Negative prices:", (data["price"] < 0).sum())
print("Zero prices:", (data["price"] == 0).sum())