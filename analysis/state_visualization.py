import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load state analysis
state_data = pd.read_csv(
    "dataset/commodity_state_analysis.csv"
)

# Display available commodities
commodities = state_data["commodity"].unique()

print("Available commodities:")
for i, commodity in enumerate(commodities, start=1):
    print(f"{i}. {commodity}")

# Select commodity
selected = input("\nEnter commodity: ").strip()

# Filter data
commodity_state = state_data[
    state_data["commodity"] == selected
]

if commodity_state.empty:
    print("Invalid commodity name!")
else:
    # Sort states by average price
    commodity_state = commodity_state.sort_values(
        by="mean",
        ascending=False
    )

    # Plot
    plt.figure(figsize=(12, 7))

    sns.barplot(
        data=commodity_state,
        x="mean",
        y="state_name",
        errorbar=None
    )

    plt.title(f"Average Price of {selected} Across States")
    plt.xlabel("Average Price (₹)")
    plt.ylabel("State")
    plt.tight_layout()
    plt.show()