# PricePulse Analytics
### Indian Food Commodity Price Analysis (2015–2023)

**Tracking Trends. Discovering Insights.**

PricePulse Analytics is an interactive data analytics dashboard designed to explore and analyse historical food commodity prices across different states in India from 2015 to 2023.

The project uses Python-based data processing and interactive visualisations to identify price trends, compare commodities, examine regional price variations and understand fluctuations in food prices over time.

🌐 **Live Dashboard:** [Open PricePulse Analytics](ADD_LIVE_WEBSITE_LINK_HERE)

---

## 1. Project Overview

Food commodity prices fluctuate over time due to various market and regional factors. Understanding these changes can help identify pricing patterns and differences across commodities and geographical regions.

PricePulse Analytics transforms historical food price data into meaningful insights through an interactive dashboard. Users can explore commodity prices, analyse yearly and monthly trends, compare state-wise prices and investigate price volatility.

The analysis covers:

- **22 commodities**
- **34 states**
- **2015–2023**
- Approximately **1.83 million cleaned price records**

## 2. Key Features

### 📊 Overview
Provides a summary of the dataset, including important statistics and commodity price comparisons.

### 📈 Yearly Trends
Explores changes in commodity prices across different years and helps identify long-term pricing patterns.

### 🏆 Top 5 Commodities
Identifies and compares the five commodities with the highest average prices.

### 🗺️ State Comparison
Examines differences in commodity prices across Indian states to identify regional price variations.

### 💡 Price Insights
Highlights significant findings, including average commodity prices, major yearly price increases and state-wise price gaps.

### 🔍 Price Explorer
Allows users to explore individual price records using available dataset filters.

### 📅 Monthly Trends
Analyses monthly price movements to identify variations throughout the year.

### 📉 Price Volatility
Examines fluctuations in commodity prices to understand how stable or variable prices are over time.

## 3. Dataset Description

The project uses historical food commodity price data covering the period from 2015 to 2023.

The dataset is processed to handle missing price values, convert date information and derive additional time-based features such as year and month.

The cleaned dataset is used for further analysis and dashboard visualisations.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data cleaning, manipulation and analysis |
| Streamlit | Interactive dashboard development |
| Plotly | Interactive data visualisations |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| Git & GitHub | Version control and project hosting |

## 5. Project Structure

```text
PricePulse-Analytics/
│
├── website.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   ├── food_prices.csv
│   ├── cleaned_food_prices.csv.gz
│   ├── yearly_analysis.csv
│   └── commodity_state_analysis.csv
│
├── analysis/
│   ├── explore_data.py
│   ├── yearly_analysis.py
│   ├── price_insights.py
│   ├── state.py
│   ├── state_visualization.py
│   ├── visualizations.py
│   └── compress_dataset.py
│
└── .streamlit/
    └── config.toml
```

## 6. Installation and Setup

Follow these steps to run PricePulse Analytics locally.

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

**Step 2: Navigate to the project directory**

```bash
cd PricePulse-Analytics
```

**Step 3: Install the required dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Streamlit application**

```bash
streamlit run website.py
```

The dashboard will open in your default browser. If it does not, open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 7. Key Findings

Some notable findings from the analysis include:

- Tea Loose recorded the highest average commodity price, at approximately ₹240.44.
- Salt Pack (Iodised) recorded the lowest average price, at approximately ₹17.
- Potato experienced the highest yearly price increase in 2020, at approximately 64.17%.
- Tea Loose showed the largest difference in average prices across states, approximately ₹205.05.

These findings demonstrate how historical price data can be used to identify significant commodity and regional pricing patterns.

## 8. Dashboard Screenshots

Screenshots of the PricePulse Analytics dashboard will be added here to demonstrate its interface and visualisation features.

---

## 9. Project Objective

The objective of PricePulse Analytics is to demonstrate how data cleaning, exploratory data analysis and interactive visualisation can be combined to transform large datasets into meaningful and accessible insights.

**PricePulse Analytics — Tracking Trends. Discovering Insights.**