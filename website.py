
import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PricePulse",
    page_icon="🥑",
    layout="wide"
)


st.markdown("""
<style>

/* =====================================
   GLOBAL BACKGROUND
===================================== */

.stApp {
    background: #E8E7DF;
    color: #24382E;
}

.block-container {
    max-width: 1450px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Main content text */
[data-testid="stMain"] {
    color: #24382E;
}

/* =====================================
   SIDEBAR
===================================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #10271F 0%,
        #18392B 100%
    );
    border-right: 1px solid #365746;
}

[data-testid="stSidebar"] * {
    color: #F0F0E8;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #B8C9BA;
    font-size: 14px;
}

/* Navigation spacing */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 9px;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    background: transparent;
    border-radius: 10px;
    padding: 11px 13px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: #315442;
}

[data-testid="stSidebar"] [role="radiogroup"] label p {
    color: #E7EEE7 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* =====================================
   HEADINGS
===================================== */

h1, h2, h3, h4 {
    color: #193B2D !important;
    font-weight: 750 !important;
    letter-spacing: -0.5px;
}

h1 {
    font-size: 2.35rem !important;
}

h2 {
    font-size: 1.6rem !important;
}

h3 {
    font-size: 1.25rem !important;
}

/* Body copy */
[data-testid="stMarkdownContainer"] p {
    color: #53665A;
    line-height: 1.65;
}

/* =====================================
   METRIC CARDS
===================================== */

[data-testid="stMetric"] {
    background: #F8F7F0;
    padding: 21px;
    border-radius: 15px;
    border: 1px solid #D5D7C9;
    border-bottom: 3px solid #55775C;
    box-shadow: 0 5px 15px rgba(25, 48, 35, 0.08);
    transition: all 0.2s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 9px 22px rgba(25, 48, 35, 0.13);
}

[data-testid="stMetricLabel"] p {
    color: #65776A !important;
    font-size: 13px !important;
    font-weight: 650 !important;
}

[data-testid="stMetricValue"] {
    color: #193B2D !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
}

/* =====================================
   CHART CONTAINERS
===================================== */

[data-testid="stPlotlyChart"] {
    background: #F8F7F0;
    padding: 12px;
    border-radius: 16px;
    border: 1px solid #D8D9CE;
    box-shadow: 0 5px 16px rgba(25, 48, 35, 0.06);
}

/* =====================================
   FILTERS AND INPUTS
===================================== */

[data-testid="stSelectbox"],
[data-testid="stMultiSelect"],
[data-testid="stTextInput"] {
    background: #F8F7F0;
    border-radius: 10px;
}

[data-baseweb="select"] > div {
    background: #F8F7F0 !important;
    border-radius: 10px !important;
    border-color: #BCC8B9 !important;
}

[data-baseweb="select"] * {
    color: #24382E !important;
}

[data-testid="stWidgetLabel"] p {
    color: #344D3D !important;
    font-weight: 650 !important;
}

/* =====================================
   CONTAINERS
===================================== */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: #F1F0E8;
    border-color: #D1D5C8 !important;
    border-radius: 15px;
}

/* =====================================
   TABLES
===================================== */

[data-testid="stDataFrame"] {
    background: #F8F7F0;
    border: 1px solid #D6D9CE;
    border-radius: 14px;
    overflow: hidden;
}

/* =====================================
   BUTTONS
===================================== */

.stButton button,
.stDownloadButton button {
    background: #214B36;
    color: #F7F5EA;
    border: 1px solid #315C43;
    border-radius: 10px;
    padding: 10px 19px;
    font-weight: 650;
    transition: all 0.2s ease;
}

.stButton button:hover,
.stDownloadButton button:hover {
    background: #142F23;
    color: #FFFFFF;
    border-color: #B89A58;
    transform: translateY(-2px);
}

/* =====================================
   CAPTIONS AND DIVIDERS
===================================== */

[data-testid="stCaptionContainer"] {
    color: #748075;
    font-size: 13px;
}

hr {
    border-color: #CFD3C7 !important;
    margin-top: 28px;
    margin-bottom: 28px;
}

/* =====================================
   HIDE STREAMLIT BRANDING
===================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
/* GLOBAL TEXT VISIBILITY FIX */

/* Main page text */
.stApp,
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    color: #24382E !important;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #183629 !important;
}

/* Paragraphs, labels and captions */
p, label, .stMarkdown,
[data-testid="stCaptionContainer"],
[data-testid="stWidgetLabel"] {
    color: #34483D !important;
}

/* Sidebar text */
[data-testid="stSidebar"] {
    background: #142A23 !important;
}

[data-testid="stSidebar"] * {
    color: #F4F1E8 !important;
}

/* Metric cards */
[data-testid="stMetricLabel"] {
    color: #52665A !important;
}

[data-testid="stMetricValue"] {
    color: #183629 !important;
}

[data-testid="stMetricDelta"] {
    color: #426B50 !important;
}

/* Input boxes and dropdowns */
.stSelectbox div,
.stMultiSelect div,
.stTextInput input,
.stNumberInput input {
    color: #24382E !important;
}

/* Dataframes and tables */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    color: #24382E !important;
}

/* Buttons */
.stButton button {
    color: #FFFFFF !important;
}

/* Expander headings */
[data-testid="stExpander"] summary {
    color: #24382E !important;
}
/* SIDEBAR — larger, brighter text */
[data-testid="stSidebar"] {
    background: #142A23 !important;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
    opacity: 1 !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    font-size: 14px !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] .stRadio label {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] .stRadio label p {
    font-size: 15px !important;
    color: #FFFFFF !important;
}
/* COLOURED HERO BANNERS */
div[style*="linear-gradient"] {
    color: #FFFFFF !important;
}

div[style*="linear-gradient"] h1,
div[style*="linear-gradient"] h2,
div[style*="linear-gradient"] h3,
div[style*="linear-gradient"] p,
div[style*="linear-gradient"] span,
div[style*="linear-gradient"] strong {
    color: #FFFFFF !important;
}
/* DOWNLOAD BUTTON TEXT VISIBILITY */
[data-testid="stDownloadButton"] button {
    background-color: #204B3B !important;
    color: #FFFFFF !important;
    border: 1px solid #B89A58 !important;
    font-weight: 700 !important;
    opacity: 1 !important;
}

[data-testid="stDownloadButton"] button p,
[data-testid="stDownloadButton"] button span,
[data-testid="stDownloadButton"] button div {
    color: #FFFFFF !important;
    opacity: 1 !important;
}

[data-testid="stDownloadButton"] button:hover {
    background-color: #326B53 !important;
    color: #FFFFFF !important;
    border-color: #D6B968 !important;
}
</style>
""", unsafe_allow_html=True)



# --------------------------------------------------
# 2. LOAD DATASETS
# --------------------------------------------------

@st.cache_data
def load_data():
    data = pd.read_csv("dataset/cleaned_food_prices.csv.gz")
    yearly = pd.read_csv("dataset/yearly_analysis.csv")
    state_data = pd.read_csv("dataset/commodity_state_analysis.csv")

    return data, yearly, state_data


data, yearly, state_data = load_data()


# --------------------------------------------------
# 3. CHART STYLING FUNCTION
# --------------------------------------------------

def style_chart(fig, line_chart=False):

    fig.update_layout(
        template="plotly_white",
        font=dict(
            family="Arial",
            size=13
        ),
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    if line_chart:
        fig.update_layout(
            colorway=[
                "#267A58",
                "#5B9B78",
                "#91B9A0",
                "#B7D2BF",
                "#D0E2D5"
            ],
            xaxis_title="Year",
            yaxis_title="Average Price (₹)",
            hovermode="x unified"
        )

    return fig


# --------------------------------------------------
# 4. WEBSITE HEADER
# --------------------------------------------------

st.html("""
<div style="display:flex; justify-content:space-between; align-items:center; gap:24px; padding:10px 0 18px 0;">
  <div>
    <div style="color:#267A58; font-size:11px; font-weight:800; letter-spacing:2.4px; margin-bottom:7px;">INDIA FOOD MARKET INTELLIGENCE</div>
    <div style="font-size:50px; color:#173F32; font-weight:800; letter-spacing:-.5px;">📈 PricePulse</div>
    <div style="font-size:13px; color:#718076; margin-top:5px;">Historical prices. Regional patterns. Better market understanding.</div>
  </div>
  <div style="background:#173F32; color:#D9EF82; border-radius:999px; padding:9px 15px; font-size:11px; font-weight:800; letter-spacing:1px; white-space:nowrap;">INDIA&nbsp; · &nbsp;2015–2023</div>
</div>
""")

st.divider()


# --------------------------------------------------
# 5. SIDEBAR NAVIGATION
# --------------------------------------------------



st.sidebar.html("""
<div style="padding:12px 0 18px 0;">
  <div style="font-size:30px; font-weight:800; color:#173F32;">🥗 Food Insights</div>
  <div style="font-size:10px; letter-spacing:1.7px; font-weight:750; color:#718076; margin-top:5px;">ANALYTICS WORKSPACE</div>
</div>
""")
st.sidebar.caption("Indian Food Price Dashboard")
st.sidebar.divider()

page = st.sidebar.radio(
    "Choose a section",
    [
        "Overview",
        "Yearly Trends",
        "Top 5 Commodities",
        "State Comparison",
        "Price Insights",
        "Price Explorer",
        "Monthly Trends",
        "Price Volatility"
    ]
)


# --------------------------------------------------
# 6. OVERVIEW PAGE
# --------------------------------------------------

if page == "Overview":

    # HERO PANEL
    st.html("""
    <div style="background:linear-gradient(120deg,#173F32 0%,#245B43 68%,#347653 100%); border-radius:22px; padding:30px 32px; margin:4px 0 24px 0; position:relative; overflow:hidden;">
      <div style="color:#D9EF82; font-size:10px; font-weight:800; letter-spacing:2.5px; margin-bottom:12px;">FOOD MARKET INTELLIGENCE</div>
      <div style="color:#FFFFFF; font-size:34px; line-height:1.15; font-weight:800; letter-spacing:-1px; max-width:650px;">Understanding the prices of everyday essentials.</div>
      <div style="color:#D4E2D8; font-size:14px; line-height:1.7; margin-top:12px; max-width:700px;">From rice and atta to pulses, oils and vegetables — explore how food prices vary across Indian states and change over time.</div>
      <div style="margin-top:20px; display:inline-block; background:#D9EF82; color:#173F32; border-radius:999px; padding:7px 13px; font-size:10px; font-weight:800; letter-spacing:1px;">HISTORICAL DATA · 2015–2023</div>
    </div>
    """)

    # KPI CARDS
    st.markdown("### At a glance")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🌾 Commodities", data["commodity"].nunique())
    with col2:
        st.metric("📍 States", data["state_name"].nunique())
    with col3:
        st.metric("📅 Years covered", data["year"].nunique())
    with col4:
        st.metric("📊 Price records", f"{len(data):,}")

    # DATASET CONTEXT + DYNAMIC HIGHLIGHTS
    commodity_avg = (
        data.groupby("commodity")["price"]
        .mean()
        .sort_values(ascending=False)
    )
    highest_commodity = commodity_avg.index[0]
    highest_price = commodity_avg.iloc[0]
    lowest_commodity = commodity_avg.index[-1]
    lowest_price = commodity_avg.iloc[-1]

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    left, right = st.columns([1.15, 1])

    with left:
        st.html("""
        <div style="height:100%; background:#E7EDE4; border:1px solid #DCE5D9; border-radius:17px; padding:20px 22px;">
          <div style="font-size:10px; color:#267A58; font-weight:800; letter-spacing:1.8px;">ABOUT THE DATA</div>
          <div style="font-size:19px; color:#173F32; font-weight:800; margin:8px 0;">A closer look at India's food basket</div>
          <div style="font-size:13px; color:#5D7064; line-height:1.75;">This dashboard brings historical food-price observations together to help explore commodity-level trends, compare state averages and identify meaningful changes in the market.</div>
        </div>
        """)

    with right:
        st.html(f"""
        <div style="height:100%; background:#FFFFFF; border:1px solid #E3E8DF; border-radius:17px; padding:20px 22px;">
          <div style="font-size:10px; color:#267A58; font-weight:800; letter-spacing:1.8px;">QUICK DISCOVERY</div>
          <div style="font-size:13px; color:#718076; margin-top:10px;">Highest average-priced commodity</div>
          <div style="font-size:23px; color:#173F32; font-weight:800; margin-top:3px;">{highest_commodity}</div>
          <div style="font-size:14px; color:#267A58; font-weight:700;">₹{highest_price:,.2f} average</div>
          <div style="height:1px; background:#E8EDE6; margin:13px 0;"></div>
          <div style="font-size:12px; color:#718076;">Lowest average-priced commodity: <b style="color:#355447;">{lowest_commodity}</b> · ₹{lowest_price:,.2f}</div>
        </div>
        """)

    # ALL-COMMODITY CHART
    st.markdown("### Commodity price landscape")
    st.caption("Average recorded price for every commodity across all available states and years. Select or hover over a bar to inspect a value.")

    commodity_chart = commodity_avg.rename("average_price").reset_index()
    commodity_chart = commodity_chart.sort_values("average_price", ascending=True)

    fig = px.bar(
        commodity_chart,
        x="average_price",
        y="commodity",
        orientation="h",
        text="average_price",
        labels={"average_price": "Average price (₹)", "commodity": ""},
        color="average_price",
        color_continuous_scale=["#D6E8D6", "#78AD83", "#267A58", "#173F32"]
    )

    fig.update_traces(
        texttemplate="₹%{text:.1f}",
        textposition="outside",
        cliponaxis=False,
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Average price: ₹%{x:.2f}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        height=max(560, len(commodity_chart) * 34 + 100),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial", size=12, color="#355447"),
        margin=dict(l=10, r=85, t=20, b=35),
        xaxis=dict(title="Average price (₹)", showgrid=True, gridcolor="#E8EDE6", zeroline=False),
        yaxis=dict(title="", automargin=True),
        coloraxis_showscale=False,
        bargap=0.28,
        hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial")
    )

    st.plotly_chart(fig, use_container_width=True)

    st.html("""
    <div style="border-top:1px solid #DCE4DA; padding:18px 0 4px 0; text-align:center; color:#849188; font-size:10px; font-weight:700; letter-spacing:1.5px;">
      FOOD PRICE ANALYTICS &nbsp; · &nbsp; INDIA &nbsp; · &nbsp; HISTORICAL MARKET DATA
    </div>
    """)

# --------------------------------------------------
# 7. YEARLY TRENDS PAGE
# --------------------------------------------------


elif page == "Yearly Trends":

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.html("""
    <div style="
        background: linear-gradient(120deg, #173B30, #286B4E);
        padding: 30px;
        border-radius: 18px;
        margin-bottom: 25px;
    ">
        <div style="
            color: #D9EF82;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
        ">HISTORICAL MARKET ANALYSIS</div>

        <h1 style="
            color: white;
            font-size: 34px;
            margin: 10px 0;
        ">Yearly Price Trends</h1>

        <p style="
            color: #D5E2D9;
            font-size: 15px;
            margin: 0;
        ">
            Explore how food commodity prices have evolved
            across India from 2015 to 2023.
        </p>
    </div>
    """)

    # ==========================================
    # FILTER PANEL
    # ==========================================

    st.markdown("### Explore Commodities")

    st.caption(
        "Select one or more commodities to compare their "
        "historical average prices."
    )

    commodities = sorted(yearly["commodity"].unique())

    selected_commodities = st.multiselect(
        "Choose commodities",
        commodities,
        default=["Tomato"] if "Tomato" in commodities else [],
        key="yearly_commodities"
    )

    if selected_commodities:

        trend_data = yearly[
            yearly["commodity"].isin(selected_commodities)
        ].copy()

        # ==========================================
        # PRICE TREND CHART
        # ==========================================

        st.markdown("---")
        st.markdown("### Historical Price Movement")

        fig = px.line(
            trend_data,
            x="year",
            y="price",
            color="commodity",
            markers=True,
            labels={
                "year": "Year",
                "price": "Average Price (₹)",
                "commodity": "Commodity"
            },
            color_discrete_sequence=[
                "#267A58",
                "#D58A53",
                "#7771B5",
                "#D1AD45",
                "#4C91B5",
                "#C66C7A",
                "#80A65B",
                "#8B755D"
            ]
        )

        fig.update_traces(
            line=dict(width=3),
            marker=dict(size=8),
            hovertemplate=(
                "<b>%{fullData.name}</b><br>"
                "Year: %{x}<br>"
                "Average Price: ₹%{y:.2f}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=540,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family="Arial",
                size=13,
                color="#20352A"
            ),
            margin=dict(l=15, r=20, t=35, b=20),
            hovermode="x unified",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0
            ),
            xaxis=dict(
                title="Year",
                dtick=1,
                showgrid=False
            ),
            yaxis=dict(
                title="Average Price (₹)",
                showgrid=True,
                gridcolor="#E9EEE8"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================================
        # SELECTED COMMODITY STATISTICS
        # ==========================================

        st.markdown("---")
        st.markdown("### Price Statistics")

        selected_stats = (
            trend_data.groupby("commodity")["price"]
            .agg(["mean", "min", "max", "std"])
            .reset_index()
        )

        st.dataframe(
            selected_stats.rename(columns={
                "commodity": "Commodity",
                "mean": "Average Price (₹)",
                "min": "Minimum Price (₹)",
                "max": "Maximum Price (₹)",
                "std": "Standard Deviation"
            }).round(2),
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # AUTOMATIC YEARLY INSIGHTS
        # ==========================================

        st.markdown("---")
        st.markdown("### What does the trend reveal?")

        for commodity in selected_commodities:

            commodity_trend = (
                trend_data[
                    trend_data["commodity"] == commodity
                ]
                .sort_values("year")
            )

            first = commodity_trend.iloc[0]
            last = commodity_trend.iloc[-1]

            highest = commodity_trend.loc[
                commodity_trend["price"].idxmax()
            ]

            lowest = commodity_trend.loc[
                commodity_trend["price"].idxmin()
            ]

            change = (
                (last["price"] - first["price"])
                / first["price"]
            ) * 100

            st.html(f"""
            <div style="
                background: #E9EEE8;
                border-radius: 12px;
                padding: 18px 22px;
                margin: 10px 0;
                border-left: 4px solid #267A58;
            ">
                <h4 style="
                    color: #194D38;
                    margin: 0 0 10px 0;
                ">{commodity}</h4>

                <p style="
                    color: #52665A;
                    font-size: 14px;
                    line-height: 1.8;
                    margin: 0;
                ">
                    Between {int(first['year'])} and
                    {int(last['year'])}, its annual average price
                    changed by <b>{change:.2f}%</b>.

                    Its highest annual average was
                    <b>₹{highest['price']:.2f}</b> in
                    {int(highest['year'])}, while its lowest was
                    <b>₹{lowest['price']:.2f}</b> in
                    {int(lowest['year'])}.
                </p>
            </div>
            """)

    else:

        st.info("Select at least one commodity to view trends.")



# --------------------------------------------------
# TOP 5 COMMODITIES PAGE
# --------------------------------------------------

elif page == "Top 5 Commodities":

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.html("""
    <div style="
        background: linear-gradient(120deg, #243D32, #526B43);
        padding: 32px;
        border-radius: 18px;
        margin-bottom: 28px;
    ">
        <div style="
            color: #E4D99B;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
        ">COMMODITY RANKINGS / INDIA</div>

        <h1 style="
            color: white;
            font-size: 35px;
            margin: 12px 0;
        ">The Price Leaders</h1>

        <p style="
            color: #E3E9DE;
            font-size: 15px;
            margin: 0;
        ">
            Discover the five commodities with the highest
            average recorded prices and explore how their
            prices evolved over time.
        </p>
    </div>
    """)

    # ==========================================
    # CALCULATE TOP 5
    # ==========================================

    top_5 = (
        yearly.groupby("commodity")["price"]
        .mean()
        .nlargest(5)
        .reset_index()
        .sort_values("price", ascending=False)
        .reset_index(drop=True)
    )

    top_5["rank"] = top_5.index + 1

    # ==========================================
    # TOP 5 RANKING SHOWCASE
    # ==========================================

    st.markdown("## The Top Five")

    st.caption(
        "Ranked according to average yearly prices "
        "across the available historical period."
    )

    rank_colors = [
        ("#F1E3B5", "#725A20"),
        ("#E5E9E5", "#53665B"),
        ("#F0D9C8", "#86563B"),
        ("#E9EEE8", "#267A58"),
        ("#E9EEE8", "#267A58")
    ]

    cols = st.columns(5)

    for i, row in top_5.iterrows():

        bg, accent = rank_colors[i]

        with cols[i]:

            st.html(f"""
            <div style="
                background: {bg};
                padding: 17px 12px;
                border-radius: 14px;
                min-height: 160px;
                border-top: 4px solid {accent};
            ">
                <div style="
                    color: {accent};
                    font-size: 12px;
                    font-weight: 700;
                ">RANK #{int(row['rank'])}</div>

                <div style="
                    color: #243D32;
                    font-size: 15px;
                    font-weight: 700;
                    margin-top: 15px;
                    min-height: 48px;
                    overflow-wrap: anywhere;
                ">{row['commodity']}</div>

                <div style="
                    color: {accent};
                    font-size: 19px;
                    font-weight: 700;
                    margin-top: 10px;
                ">₹{row['price']:.2f}</div>

                <div style="
                    color: #718076;
                    font-size: 10px;
                ">Average price</div>
            </div>
            """)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # PRICE COMPARISON
    # ==========================================

    st.markdown("---")
    st.markdown("## 01 / Average Price Comparison")

    st.write(
        "Compare the average yearly prices of the five "
        "highest-priced commodities."
    )

    comparison = top_5.sort_values(
        "price",
        ascending=True
    )

    fig = px.bar(
        comparison,
        x="price",
        y="commodity",
        orientation="h",
        text="price",
        color="price",
        color_continuous_scale=[
            "#B9D9B7",
            "#267A58",
            "#173B30"
        ],
        labels={
            "price": "Average Price (₹)",
            "commodity": "Commodity"
        },
        hover_data={"price": ":.2f"}
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f}",
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Average Price: ₹%{x:.2f}"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        coloraxis_showscale=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=80, t=25, b=35),
        font=dict(
            family="Arial",
            size=13,
            color="#20352A"
        ),
        xaxis=dict(
            title="Average Price (₹)",
            gridcolor="#E9EEE8"
        ),
        yaxis=dict(
            title="",
            automargin=True
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================================
    # HISTORICAL PRICE TRENDS
    # ==========================================

    st.markdown("---")
    st.markdown("## 02 / Historical Price Trends")

    st.write(
        "Examine how the top five commodities performed "
        "across the entire nine-year period."
    )

    top_5_data = yearly[
        yearly["commodity"].isin(top_5["commodity"])
    ].copy()

    fig = px.line(
        top_5_data,
        x="year",
        y="price",
        color="commodity",
        markers=True,
        color_discrete_sequence=[
            "#267A58",
            "#D58A53",
            "#7771B5",
            "#C66C7A",
            "#4C91B5"
        ],
        labels={
            "year": "Year",
            "price": "Average Price (₹)",
            "commodity": "Commodity"
        }
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=7)
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        margin=dict(l=15, r=20, t=35, b=25),
        xaxis=dict(
            title="Year",
            dtick=1,
            showgrid=False
        ),
        yaxis=dict(
            title="Average Price (₹)",
            gridcolor="#E9EEE8"
        ),
        legend=dict(
            orientation="h",
            y=1.12,
            x=0
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================================
    # RANKING INSIGHTS
    # ==========================================

    st.markdown("---")
    st.markdown("## 03 / Ranking Insights")

    first = top_5.iloc[0]
    fifth = top_5.iloc[-1]

    price_difference = first["price"] - fifth["price"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Highest Average Price",
            first["commodity"],
            f"₹{first['price']:.2f}"
        )

    with col2:

        st.metric(
            "Difference Between Rank 1 and 5",
            f"₹{price_difference:.2f}"
        )

    st.markdown("### What stands out?")

    st.markdown(f"""
    - **Price leader:** {first['commodity']} has the highest
      average price among all commodities.

    - **Fifth position:** {fifth['commodity']} occupies
      the fifth position in this ranking.

    - **Price difference:** The gap between the first and
      fifth ranked commodities is ₹{price_difference:.2f}.

    - **Historical comparison:** The line chart shows how
      the relative prices of these five commodities changed
      between 2015 and 2023.
    """)

    # ==========================================
    # DETAILED RANKING TABLE
    # ==========================================

    st.markdown("---")
    st.markdown("## 04 / Complete Ranking")

    ranking_table = top_5[
        ["rank", "commodity", "price"]
    ].rename(columns={
        "rank": "Rank",
        "commodity": "Commodity",
        "price": "Average Yearly Price (₹)"
    })

    st.dataframe(
        ranking_table.round(2),
        use_container_width=True,
        hide_index=True
    )



# --------------------------------------------------
# STATE COMPARISON PAGE
# --------------------------------------------------

elif page == "State Comparison":

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.html("""
    <div style="
        background: linear-gradient(120deg, #252F49, #52658B);
        padding: 32px;
        border-radius: 18px;
        margin-bottom: 28px;
    ">
        <div style="
            color: #D9DDF5;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
        ">REGIONAL MARKET ANALYSIS / INDIA</div>

        <h1 style="
            color: white;
            font-size: 35px;
            margin: 12px 0;
        ">Food Prices Across States</h1>

        <p style="
            color: #E0E5F1;
            font-size: 15px;
            margin: 0;
        ">
            Explore regional price differences and discover
            how the cost of food commodities varies
            across Indian states.
        </p>
    </div>
    """)

    # ==========================================
    # COMMODITY SELECTION
    # ==========================================

    st.markdown("## 01 / Select a Commodity")

    st.caption(
        "Choose a food commodity to investigate its "
        "average price across different states."
    )

    commodities = sorted(state_data["commodity"].unique())

    selected_commodity = st.selectbox(
        "Choose commodity",
        commodities,
        key="state_comparison_commodity"
    )

    # ==========================================
    # FILTER AND SORT DATA
    # ==========================================

    commodity_state = state_data[
        state_data["commodity"] == selected_commodity
    ].copy()

    commodity_state = commodity_state.sort_values(
        "mean",
        ascending=False
    ).reset_index(drop=True)

    # ==========================================
    # REGIONAL SUMMARY
    # ==========================================

    st.markdown("---")
    st.markdown("## 02 / Regional Price Highlights")

    highest_state = commodity_state.iloc[0]
    lowest_state = commodity_state.iloc[-1]

    price_gap = (
        highest_state["mean"] - lowest_state["mean"]
    )

    average_state_price = commodity_state["mean"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Highest Average Price",
            highest_state["state_name"],
            f"₹{highest_state['mean']:.2f}"
        )

    with col2:
        st.metric(
            "Lowest Average Price",
            lowest_state["state_name"],
            f"₹{lowest_state['mean']:.2f}"
        )

    with col3:
        st.metric(
            "Difference Between States",
            f"₹{price_gap:.2f}"
        )

    st.caption(
        f"Average of state-level mean prices for "
        f"{selected_commodity}: ₹{average_state_price:.2f}"
    )

    # ==========================================
    # STATE RANKING CHART
    # ==========================================

    st.markdown("---")
    st.markdown("## 03 / State-wise Price Ranking")

    st.write(
        f"Compare the average price of {selected_commodity} "
        "across all states available in the dataset."
    )

    fig = px.bar(
        commodity_state,
        x="mean",
        y="state_name",
        orientation="h",
        color="mean",
        color_continuous_scale=[
            "#D8E9DC",
            "#6EAB83",
            "#194D38"
        ],
        labels={
            "mean": "Average Price (₹)",
            "state_name": "State"
        },
        hover_data={
            "min": ":.2f",
            "max": ":.2f",
            "median": ":.2f"
        }
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Average Price: ₹%{x:.2f}"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        template="plotly_white",
        height=max(480, len(commodity_state) * 32 + 100),
        coloraxis_showscale=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Arial",
            size=13,
            color="#20352A"
        ),
        margin=dict(l=10, r=20, t=30, b=35),
        xaxis=dict(
            title="Average Price (₹)",
            gridcolor="#E9EEE8"
        ),
        yaxis=dict(
            title="",
            autorange="reversed",
            automargin=True
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================================
    # DETAILED PRICE STATISTICS
    # ==========================================

    st.markdown("---")
    st.markdown("## 04 / Detailed State Statistics")

    st.write(
        "Examine the average, minimum, maximum and median "
        "prices recorded in each state."
    )

    stats_table = commodity_state[
        ["state_name", "mean", "min", "max", "median", "std"]
    ].rename(columns={
        "state_name": "State",
        "mean": "Average Price (₹)",
        "min": "Minimum Price (₹)",
        "max": "Maximum Price (₹)",
        "median": "Median Price (₹)",
        "std": "Standard Deviation"
    })

    st.dataframe(
        stats_table.round(2),
        use_container_width=True,
        hide_index=True
    )

    # ==========================================
    # AUTOMATIC REGIONAL INSIGHTS
    # ==========================================

    st.markdown("---")
    st.markdown("## 05 / Regional Discoveries")

    percentage_gap = (
        (price_gap / lowest_state["mean"]) * 100
        if lowest_state["mean"] != 0 else 0
    )

    most_variable_state = commodity_state.loc[
        commodity_state["std"].idxmax()
    ]

    least_variable_state = commodity_state.loc[
        commodity_state["std"].idxmin()
    ]

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:

        st.html(f"""
        <div style="
            background: #F5E8DD;
            padding: 22px;
            border-radius: 14px;
            border-left: 5px solid #C47A45;
            min-height: 155px;
        ">
            <div style="
                color: #A36338;
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 1px;
            ">HIGHEST-PRICED REGION</div>

            <h2 style="
                color: #68432B;
                font-size: 25px;
                margin: 12px 0;
            ">{highest_state['state_name']}</h2>

            <p style="color: #76543C; font-size: 14px;">
                Recorded the highest state average for
                {selected_commodity}: ₹{highest_state['mean']:.2f}.
            </p>
        </div>
        """)

    with insight_col2:

        st.html(f"""
        <div style="
            background: #E3F0E5;
            padding: 22px;
            border-radius: 14px;
            border-left: 5px solid #267A58;
            min-height: 155px;
        ">
            <div style="
                color: #267A58;
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 1px;
            ">LOWEST-PRICED REGION</div>

            <h2 style="
                color: #194D38;
                font-size: 25px;
                margin: 12px 0;
            ">{lowest_state['state_name']}</h2>

            <p style="color: #52665A; font-size: 14px;">
                Recorded the lowest state average for
                {selected_commodity}: ₹{lowest_state['mean']:.2f}.
            </p>
        </div>
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### What stands out?")

    st.markdown(f"""
    - **Regional price gap:** The difference between the
      highest and lowest state averages is ₹{price_gap:.2f}.

    - **Relative difference:** The highest state average is
      {percentage_gap:.2f}% higher than the lowest state average.

    - **Price variability:** {most_variable_state['state_name']}
      has the highest standard deviation among the states,
      while {least_variable_state['state_name']} has the lowest.
    """)


#############


elif page == "Price Insights":

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.html("""
    <div style="
        background: #173F32;
        padding: 34px;
        border-radius: 18px;
        margin-bottom: 28px;
    ">
        <p style="
            color: #D9EF82;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
            margin: 0;
        ">FOOD MARKET RESEARCH / INDIA</p>

        <h1 style="
            color: white;
            font-size: 36px;
            margin: 12px 0;
        ">Inside the Price Movement</h1>

        <p style="
            color: #D5E2D9;
            font-size: 15px;
            margin: 0;
            line-height: 1.7;
        ">
            An in-depth look at how food commodity prices
            have increased, decreased and evolved over time.
        </p>
    </div>
    """)

    # ==========================================
    # YEARLY PRICE MOVEMENT
    # ==========================================

    st.markdown("## 01 / Yearly Price Movements")

    st.write(
        "Which commodities experienced the largest "
        "year-on-year price changes?"
    )

    changes = yearly.dropna(
        subset=["price_change_%"]
    ).copy()

    increases = (
        changes[changes["price_change_%"] > 0]
        .sort_values("price_change_%", ascending=False)
        .head(10)
    )

    decreases = (
        changes[changes["price_change_%"] < 0]
        .sort_values("price_change_%", ascending=True)
        .head(10)
    )

    # Two contrasting charts
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Largest Increases")
        st.caption("Top 10 positive yearly price changes")

        fig_inc = px.bar(
            increases,
            x="price_change_%",
            y="commodity",
            orientation="h",
            color="price_change_%",
            color_continuous_scale=["#F4C9A8", "#C65D32"],
            hover_data=["year", "price"],
            labels={
                "price_change_%": "Price increase (%)",
                "commodity": "Commodity",
                "year": "Year",
                "price": "Yearly average price"
            }
        )

        fig_inc.update_layout(
            height=520,
            template="plotly_white",
            showlegend=False,
            coloraxis_showscale=False,
            yaxis=dict(autorange="reversed"),
            margin=dict(l=10, r=15, t=25, b=35)
        )

        st.plotly_chart(
            fig_inc,
            use_container_width=True
        )

    with col2:

        st.markdown("### Largest Decreases")
        st.caption("Top 10 negative yearly price changes")

        fig_dec = px.bar(
            decreases,
            x="price_change_%",
            y="commodity",
            orientation="h",
            color="price_change_%",
            color_continuous_scale=["#267A58", "#B9D9B7"],
            hover_data=["year", "price"],
            labels={
                "price_change_%": "Price decrease (%)",
                "commodity": "Commodity",
                "year": "Year",
                "price": "Yearly average price"
            }
        )

        fig_dec.update_layout(
            height=520,
            template="plotly_white",
            showlegend=False,
            coloraxis_showscale=False,
            yaxis=dict(autorange="reversed"),
            margin=dict(l=10, r=15, t=25, b=35)
        )

        st.plotly_chart(
            fig_dec,
            use_container_width=True
        )

    # ==========================================
    # LONG-TERM PRICE GROWTH
    # ==========================================

    st.markdown("---")
    st.markdown("## 02 / Long-Term Price Growth")

    st.write(
        "How much did average commodity prices change "
        "between the first and last years of the dataset?"
    )

    yearly_sorted = yearly.sort_values("year")

    first_year = yearly_sorted["year"].min()
    last_year = yearly_sorted["year"].max()

    first_prices = (
        yearly_sorted[yearly_sorted["year"] == first_year]
        [["commodity", "price"]]
        .rename(columns={"price": "starting_price"})
    )

    last_prices = (
        yearly_sorted[yearly_sorted["year"] == last_year]
        [["commodity", "price"]]
        .rename(columns={"price": "ending_price"})
    )

    growth = first_prices.merge(
        last_prices,
        on="commodity"
    )

    growth["growth_%"] = (
        (growth["ending_price"] - growth["starting_price"])
        / growth["starting_price"]
    ) * 100

    growth = growth.sort_values(
        "growth_%",
        ascending=False
    )

    growth_col1, growth_col2 = st.columns(2)

    with growth_col1:

        st.markdown("### Highest Long-Term Growth")

        top_growth = growth.head(10)

        fig_growth = px.bar(
            top_growth,
            x="growth_%",
            y="commodity",
            orientation="h",
            color_discrete_sequence=["#267A58"],
            labels={
                "growth_%": "Price growth (%)",
                "commodity": ""
            }
        )

        fig_growth.update_layout(
            height=480,
            template="plotly_white",
            yaxis=dict(autorange="reversed"),
            margin=dict(l=10, r=15, t=25, b=35)
        )

        st.plotly_chart(
            fig_growth,
            use_container_width=True
        )

    with growth_col2:

        st.markdown("### Growth Statistics")

        st.dataframe(
            growth.rename(columns={
                "commodity": "Commodity",
                "starting_price": f"Price in {int(first_year)}",
                "ending_price": f"Price in {int(last_year)}",
                "growth_%": "Growth (%)"
            }).round(2),
            use_container_width=True,
            hide_index=True,
            height=480
        )

    st.caption(
        "Long-term growth compares annual average prices in "
        f"{int(first_year)} and {int(last_year)}. It is not "
        "an annualised growth rate or an inflation measure."
    )

    # ==========================================
    # 03 / KEY MARKET TAKEAWAYS
    # ==========================================

    st.markdown("---")

    st.markdown("## 03 / Key Market Takeaways")

    st.write(
        "Important observations generated automatically "
        "from the historical food price data."
    )

    # Get important observations
    biggest_increase = increases.iloc[0]
    biggest_decrease = decreases.iloc[0]
    highest_growth = growth.iloc[0]
    lowest_growth = growth.iloc[-1]

    positive_changes = (changes["price_change_%"] > 0).sum()
    negative_changes = (changes["price_change_%"] < 0).sum()

    # Create takeaway cards
    takeaway_col1, takeaway_col2 = st.columns(2)

    with takeaway_col1:

        st.html(f"""
        <div style="
            background: #FCE9DE;
            padding: 22px;
            border-radius: 14px;
            border-left: 5px solid #C65D32;
            min-height: 145px;
        ">
            <div style="
                color: #A64C2C;
                font-size: 12px;
                font-weight: 700;
                letter-spacing: 1px;
            ">BIGGEST YEARLY INCREASE</div>

            <h2 style="
                color: #753B27;
                margin: 10px 0;
                font-size: 25px;
            ">{biggest_increase['commodity']}</h2>

            <p style="color: #704B3A; font-size: 14px;">
                Increased by
                <b>{biggest_increase['price_change_%']:.2f}%</b>
                in {int(biggest_increase['year'])}.
            </p>
        </div>
        """)

    with takeaway_col2:

        st.html(f"""
        <div style="
            background: #E3F0E5;
            padding: 22px;
            border-radius: 14px;
            border-left: 5px solid #267A58;
            min-height: 145px;
        ">
            <div style="
                color: #267A58;
                font-size: 12px;
                font-weight: 700;
                letter-spacing: 1px;
            ">BIGGEST YEARLY DECREASE</div>

            <h2 style="
                color: #194D38;
                margin: 10px 0;
                font-size: 25px;
            ">{biggest_decrease['commodity']}</h2>

            <p style="color: #52665A; font-size: 14px;">
                Decreased by
                <b>{abs(biggest_decrease['price_change_%']):.2f}%</b>
                in {int(biggest_decrease['year'])}.
            </p>
        </div>
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    takeaway_col3, takeaway_col4 = st.columns(2)

    with takeaway_col3:

        st.html(f"""
        <div style="
            background: #E9E8F5;
            padding: 22px;
            border-radius: 14px;
            border-left: 5px solid #7771B5;
            min-height: 145px;
        ">
            <div style="
                color: #625C9C;
                font-size: 12px;
                font-weight: 700;
                letter-spacing: 1px;
            ">HIGHEST LONG-TERM GROWTH</div>

            <h2 style="
                color: #393568;
                margin: 10px 0;
                font-size: 25px;
            ">{highest_growth['commodity']}</h2>

            <p style="color: #55517A; font-size: 14px;">
                Price changed by
                <b>{highest_growth['growth_%']:.2f}%</b>
                between {int(first_year)} and {int(last_year)}.
            </p>
        </div>
        """)

    with takeaway_col4:

        st.html(f"""
        <div style="
            background: #F2EEDC;
            padding: 22px;
            border-radius: 14px;
            border-left: 5px solid #B69A43;
            min-height: 145px;
        ">
            <div style="
                color: #90772F;
                font-size: 12px;
                font-weight: 700;
                letter-spacing: 1px;
            ">LOWEST LONG-TERM GROWTH</div>

            <h2 style="
                color: #685723;
                margin: 10px 0;
                font-size: 25px;
            ">{lowest_growth['commodity']}</h2>

            <p style="color: #766638; font-size: 14px;">
                Price changed by
                <b>{lowest_growth['growth_%']:.2f}%</b>
                between {int(first_year)} and {int(last_year)}.
            </p>
        </div>
        """)

    # ==========================================
    # OVERALL MARKET OBSERVATIONS
    # ==========================================

    st.markdown("### What the data reveals")

    st.markdown(f"""
    - **Price increases:** There were {positive_changes} positive
      year-on-year commodity price changes in the dataset.

    - **Price decreases:** There were {negative_changes} negative
      year-on-year commodity price changes.

    - **Long-term growth:** {highest_growth['commodity']} recorded
      the highest percentage change between {int(first_year)}
      and {int(last_year)}.

    - **Long-term decline or lowest growth:** {lowest_growth['commodity']}
      recorded the lowest percentage change over the same period.
    """)



# --------------------------------------------------
# PRICE EXPLORER PAGE
# --------------------------------------------------

elif page == "Price Explorer":

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.html("""
    <div style="
        background: linear-gradient(120deg, #263C46, #42717A);
        padding: 32px;
        border-radius: 18px;
        margin-bottom: 28px;
    ">
        <div style="
            color: #C9E8D8;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
        ">INTERACTIVE DATA EXPLORATION</div>

        <h1 style="
            color: white;
            font-size: 35px;
            margin: 12px 0;
        ">Explore Food Prices</h1>

        <p style="
            color: #E0ECEB;
            font-size: 15px;
            margin: 0;
        ">
            Investigate individual food commodities, compare
            regional prices and explore historical records.
        </p>
    </div>
    """)

    # ==========================================
    # FILTER PANEL
    # ==========================================

    st.markdown("## 01 / Build Your Search")

    st.caption(
        "Choose the commodity, state and year you want to investigate."
    )

    with st.container(border=True):

        col1, col2, col3 = st.columns(3)

        with col1:
            selected_commodity = st.selectbox(
                "Commodity",
                sorted(data["commodity"].unique()),
                key="explorer_commodity"
            )

        with col2:
            selected_state = st.selectbox(
                "State",
                sorted(data["state_name"].unique()),
                key="explorer_state"
            )

        with col3:
            selected_year = st.selectbox(
                "Year",
                sorted(data["year"].unique()),
                key="explorer_year"
            )

    # ==========================================
    # FILTER DATA
    # ==========================================

    filtered_data = data[
        (data["commodity"] == selected_commodity) &
        (data["state_name"] == selected_state) &
        (data["year"] == selected_year)
    ].copy()

    st.markdown("---")

    if not filtered_data.empty:

        # ==========================================
        # SUMMARY CARDS
        # ==========================================

        st.markdown("## 02 / Price Summary")

        average_price = filtered_data["price"].mean()
        minimum_price = filtered_data["price"].min()
        maximum_price = filtered_data["price"].max()
        median_price = filtered_data["price"].median()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Average Price",
            f"₹{average_price:.2f}"
        )

        col2.metric(
            "Minimum Price",
            f"₹{minimum_price:.2f}"
        )

        col3.metric(
            "Maximum Price",
            f"₹{maximum_price:.2f}"
        )

        col4.metric(
            "Median Price",
            f"₹{median_price:.2f}"
        )

        # ==========================================
        # PRICE DISTRIBUTION
        # ==========================================

        st.markdown("---")
        st.markdown("## 03 / Price Distribution")

        st.caption(
            f"How recorded prices of {selected_commodity} "
            f"were distributed in {selected_state} during "
            f"{selected_year}."
        )

        fig = px.histogram(
            filtered_data,
    x="price",
    nbins=15,
    title="Distribution of Recorded Food Prices",
    labels={
        "price": "Recorded Price (₹)",
        "count": "Number of Records"
    },
    color_discrete_sequence=["#28745F"]
        )

        fig.update_layout(
            height=480,
    bargap=0.08,
    plot_bgcolor="#F8F7F0",
    paper_bgcolor="#F8F7F0",
    font=dict(
        family="Arial",
        color="#24382E",
        size=13
    ),
    title=dict(
        font=dict(size=19, color="#183629"),
        x=0.02
    ),
    xaxis=dict(
        title="Recorded Price (₹)",
        showgrid=False,
        zeroline=False
    ),
    yaxis=dict(
        title="Number of Records",
        gridcolor="#E3E5DA",
        zeroline=False
    ),
    margin=dict(l=65, r=35, t=65, b=65)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        

        # ==========================================
        # AUTOMATIC OBSERVATIONS
        # ==========================================

        st.markdown("---")
        st.markdown("## 05 / What the Records Reveal")

        highest_record = filtered_data.loc[
            filtered_data["price"].idxmax()
        ]

        lowest_record = filtered_data.loc[
            filtered_data["price"].idxmin()
        ]

        price_range = maximum_price - minimum_price

        st.markdown(f"""
        - **Selected commodity:** {selected_commodity}

        - **Selected region:** {selected_state}

        - **Selected period:** {int(selected_year)}

        - **Price range:** ₹{price_range:.2f} between the
          highest and lowest recorded observations.

        - **Highest observation:** ₹{maximum_price:.2f}.

        - **Lowest observation:** ₹{minimum_price:.2f}.

        - **Number of records:** {len(filtered_data):,}.
        """)

        # ==========================================
        # DETAILED RECORDS
        # ==========================================

        st.markdown("---")
        st.markdown("## 06 / Detailed Price Records")

        st.caption(
            "Original observations matching your selected filters."
        )

        st.dataframe(
            filtered_data.sort_values("date"),
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # DOWNLOAD
        # ==========================================

        csv = filtered_data.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download These Records",
            data=csv,
            file_name="food_price_records.csv",
            mime="text/csv"
        )

    else:

        st.warning(
            "No records found for these filter selections."
        )

    st.subheader("Advanced Price Explorer")

    st.write(
        "Explore historical food prices using custom filters."
    )

    # Commodity filter
    commodities = sorted(data["commodity"].unique())

    selected_commodity = st.selectbox(
        "Select Commodity",
        commodities
    )

    # State filter
    states = sorted(data["state_name"].unique())

    selected_state = st.selectbox(
        "Select State",
        states
    )

    # Year filter
    years = sorted(data["year"].unique())

    selected_year = st.selectbox(
        "Select Year",
        years
    )

    # Filter dataset
    filtered_data = data[
        (data["commodity"] == selected_commodity) &
        (data["state_name"] == selected_state) &
        (data["year"] == selected_year)
    ]

    st.divider()

    if not filtered_data.empty:

        # Summary metrics
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Price",
            f'₹{filtered_data["price"].mean():.2f}'
        )

        col2.metric(
            "Minimum Price",
            f'₹{filtered_data["price"].min():.2f}'
        )

        col3.metric(
            "Maximum Price",
            f'₹{filtered_data["price"].max():.2f}'
        )

        # Display records
        st.subheader("Filtered Price Records")

        st.dataframe(
            filtered_data,
            use_container_width=True,
            hide_index=True
        )

        # Download button
        csv = filtered_data.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Filtered Data",
            data=csv,
            file_name="filtered_food_prices.csv",
            mime="text/csv"
        )

    else:
        st.warning("No records found for these filters.")


# --------------------------------------------------
# MONTHLY TRENDS PAGE
# --------------------------------------------------


elif page == "Monthly Trends":

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.html("""
    <div style="
        background: linear-gradient(120deg, #563D30, #A16D48);
        padding: 32px;
        border-radius: 18px;
        margin-bottom: 28px;
    ">
        <div style="
            color: #F5DDBB;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
        ">MONTHLY MARKET ANALYSIS</div>

        <h1 style="
            color: white;
            font-size: 35px;
            margin: 12px 0;
        ">The Year in Food Prices</h1>

        <p style="
            color: #F2E5D8;
            font-size: 15px;
            margin: 0;
        ">
            Explore monthly price movements and discover
            when food commodities recorded higher or
            lower average prices.
        </p>
    </div>
    """)

    # ==========================================
    # FILTER PANEL
    # ==========================================

    st.markdown("## 01 / Explore Monthly Prices")

    st.caption(
        "Select a commodity, region and year to investigate "
        "monthly average prices."
    )

    monthly_data = data.copy()

    monthly_data["date"] = pd.to_datetime(
        monthly_data["date"]
    )

    monthly_data["month"] = monthly_data["date"].dt.month

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_commodity = st.selectbox(
            "Commodity",
            sorted(data["commodity"].unique()),
            key="monthly_commodity"
        )

    with col2:
        selected_state = st.selectbox(
            "State",
            ["All States"] + sorted(data["state_name"].unique()),
            key="monthly_state"
        )

    with col3:
        selected_year = st.selectbox(
            "Year",
            sorted(monthly_data["year"].unique()),
            key="monthly_year"
        )

    # ==========================================
    # FILTER DATA
    # ==========================================

    filtered = monthly_data[
        (monthly_data["commodity"] == selected_commodity) &
        (monthly_data["year"] == selected_year)
    ].copy()

    if selected_state != "All States":
        filtered = filtered[
            filtered["state_name"] == selected_state
        ]

    # ==========================================
    # CALCULATE MONTHLY AVERAGES
    # ==========================================

    monthly_avg = (
        filtered.groupby("month")["price"]
        .agg(["mean", "min", "max", "count"])
        .reset_index()
    )

    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    monthly_avg["month_name"] = monthly_avg["month"].map(
        lambda month: month_names[month - 1]
    )

    monthly_avg = monthly_avg.sort_values("month")

    if not monthly_avg.empty:

        # ==========================================
        # MONTHLY PRICE MOVEMENT
        # ==========================================

        st.markdown("---")
        st.markdown("## 02 / Monthly Price Movement")

        st.caption(
            f"Average monthly prices for {selected_commodity} "
            f"during {int(selected_year)}."
        )

        fig = px.line(
            monthly_avg,
            x="month_name",
            y="mean",
            markers=True,
            color_discrete_sequence=["#B8794B"],
            labels={
                "month_name": "Month",
                "mean": "Average Price (₹)"
            }
        )

        fig.update_traces(
            line=dict(width=3),
            marker=dict(size=10),
            fill="tozeroy",
            fillcolor="rgba(184,121,75,0.10)",
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Average Price: ₹%{y:.2f}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=460,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            hovermode="x unified",
            margin=dict(l=15, r=15, t=30, b=35),
            font=dict(
                family="Arial",
                size=13,
                color="#20352A"
            ),
            xaxis=dict(
                title="Month",
                categoryorder="array",
                categoryarray=month_names,
                showgrid=False
            ),
            yaxis=dict(
                title="Average Price (₹)",
                gridcolor="#E9EEE8"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================================
        # MONTHLY HIGHLIGHTS
        # ==========================================

        st.markdown("---")
        st.markdown("## 03 / Monthly Highlights")

        highest_month = monthly_avg.loc[
            monthly_avg["mean"].idxmax()
        ]

        lowest_month = monthly_avg.loc[
            monthly_avg["mean"].idxmin()
        ]

        overall_monthly_avg = monthly_avg["mean"].mean()

        price_difference = (
            highest_month["mean"] - lowest_month["mean"]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Most Expensive Month",
            highest_month["month_name"],
            f"₹{highest_month['mean']:.2f}"
        )

        col2.metric(
            "Least Expensive Month",
            lowest_month["month_name"],
            f"₹{lowest_month['mean']:.2f}"
        )

        col3.metric(
            "Highest-Lowest Gap",
            f"₹{price_difference:.2f}"
        )

        # ==========================================
        # MONTHLY PRICE RANKING
        # ==========================================

        st.markdown("---")
        st.markdown("## 04 / Monthly Price Ranking")

        ranked_months = monthly_avg.sort_values(
            "mean",
            ascending=False
        ).copy()

        ranked_months.insert(
            0,
            "Rank",
            range(1, len(ranked_months) + 1)
        )

        st.dataframe(
            ranked_months[
                ["Rank", "month_name", "mean", "min", "max", "count"]
            ].rename(columns={
                "month_name": "Month",
                "mean": "Average Price (₹)",
                "min": "Minimum Price (₹)",
                "max": "Maximum Price (₹)",
                "count": "Number of Records"
            }).round(2),
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # AUTOMATIC MONTHLY OBSERVATIONS
        # ==========================================

        st.markdown("---")
        st.markdown("## 05 / What the Data Reveals")

        st.html(f"""
        <div style="
            background: #F3E9DE;
            padding: 22px;
            border-radius: 14px;
            border-left: 5px solid #B8794B;
            margin-bottom: 15px;
        ">
            <div style="
                color: #93613E;
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 1px;
            ">HIGHEST MONTHLY AVERAGE</div>

            <h2 style="
                color: #563D30;
                font-size: 25px;
                margin: 10px 0;
            ">{highest_month['month_name']}</h2>

            <p style="color: #765B48; font-size: 14px;">
                Recorded an average price of
                <b>₹{highest_month['mean']:.2f}</b>
                for {selected_commodity}.
            </p>
        </div>
        """)

        st.markdown(f"""
        - **Monthly price difference:** The gap between
          {highest_month['month_name']} and
          {lowest_month['month_name']} was ₹{price_difference:.2f}.

        - **Average across available months:** ₹{overall_monthly_avg:.2f}.

        - **Data coverage:** {len(monthly_avg)} months had
          available observations.

        - **Selected region:** {selected_state}.
        """)

        st.caption(
            "These findings describe the selected year only. "
            "They do not establish a recurring seasonal pattern."
        )

    else:

        st.warning(
            "No data available for the selected filters."
        )


# --------------------------------------------------
# PRICE VOLATILITY PAGE
# --------------------------------------------------

elif page == "Price Volatility":

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.html("""
    <div style="
        background: linear-gradient(120deg, #302C50, #625B91);
        padding: 32px;
        border-radius: 18px;
        margin-bottom: 28px;
    ">
        <div style="
            color: #DAD5FF;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
        ">PRICE STABILITY / MARKET RISK</div>

        <h1 style="
            color: white;
            font-size: 35px;
            margin: 12px 0;
        ">Understanding Price Volatility</h1>

        <p style="
            color: #E2DFF1;
            font-size: 15px;
            margin: 0;
        ">
            Discover which food commodities experience
            the greatest price fluctuations and which
            maintain relatively stable prices.
        </p>
    </div>
    """)

    # ==========================================
    # CALCULATE VOLATILITY
    # ==========================================

    st.markdown("## 01 / Commodity Volatility Overview")

    st.caption(
        "Volatility is calculated using the standard deviation "
        "of yearly average prices from 2015 to 2023."
    )

    volatility = (
        yearly.groupby("commodity")["price"]
        .agg(
            mean="mean",
            std="std",
            minimum="min",
            maximum="max"
        )
        .reset_index()
    )

    volatility["cv"] = (
        volatility["std"] / volatility["mean"]
    ) * 100

    volatility = volatility.dropna(
        subset=["cv"]
    )

    volatility = volatility.sort_values(
        "cv",
        ascending=False
    ).reset_index(drop=True)

    if not volatility.empty:

        most_volatile = volatility.iloc[0]
        most_stable = volatility.iloc[-1]

        # ==========================================
        # SUMMARY CARDS
        # ==========================================

        st.markdown("### Market Stability Highlights")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Most Volatile",
            most_volatile["commodity"],
            f'{most_volatile["cv"]:.2f}% CV'
        )

        col2.metric(
            "Most Stable",
            most_stable["commodity"],
            f'{most_stable["cv"]:.2f}% CV'
        )

        col3.metric(
            "Commodities Analysed",
            len(volatility)
        )

        # ==========================================
        # VOLATILITY RANKING CHART
        # ==========================================

        st.markdown("---")
        st.markdown("## 02 / Volatility Rankings")

        st.write(
            "Which commodities show the greatest relative "
            "variation in their yearly average prices?"
        )

        top_volatile = volatility.head(10).copy()

        fig = px.bar(
            top_volatile,
            x="cv",
            y="commodity",
            orientation="h",
            color="cv",
            color_continuous_scale=[
                "#D9D3F0",
                "#9589C7",
                "#51477F"
            ],
            labels={
                "cv": "Coefficient of Variation (%)",
                "commodity": "Commodity"
            },
            hover_data={
                "mean": ":.2f",
                "std": ":.2f"
            }
        )

        fig.update_traces(
            texttemplate="%{x:.1f}%",
            textposition="outside",
            cliponaxis=False,
            hovertemplate=(
                "<b>%{y}</b><br>"
                "CV: %{x:.2f}%"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=500,
            coloraxis_showscale=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family="Arial",
                size=13,
                color="#20352A"
            ),
            margin=dict(l=10, r=75, t=25, b=35),
            xaxis=dict(
                title="Coefficient of Variation (%)",
                gridcolor="#E9EEE8"
            ),
            yaxis=dict(
                title="",
                autorange="reversed",
                automargin=True
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================================
        # VOLATILITY EXPLANATION
        # ==========================================

        st.html("""
        <div style="
            background: #EEECF7;
            border-left: 5px solid #7165A6;
            padding: 20px 22px;
            border-radius: 12px;
            margin: 15px 0;
        ">
            <h4 style="color: #40396B; margin-top: 0;">
                What does volatility mean?
            </h4>

            <p style="
                color: #5C5879;
                font-size: 14px;
                line-height: 1.7;
            ">
                The Coefficient of Variation (CV) measures
                standard deviation relative to the mean.
                A higher CV indicates greater relative
                variation in yearly average prices.
                A lower CV indicates greater relative stability.
            </p>

            <p style="
                color: #5C5879;
                font-size: 14px;
                margin-bottom: 0;
            ">
                <b>Formula:</b> CV = (Standard Deviation / Mean) × 100
            </p>
        </div>
        """)

        # ==========================================
        # COMPLETE VOLATILITY TABLE
        # ==========================================

        st.markdown("---")
        st.markdown("## 03 / Detailed Volatility Analysis")

        volatility_table = volatility[
            [
                "commodity",
                "mean",
                "std",
                "minimum",
                "maximum",
                "cv"
            ]
        ].rename(columns={
            "commodity": "Commodity",
            "mean": "Average Yearly Price (₹)",
            "std": "Standard Deviation",
            "minimum": "Minimum Yearly Average (₹)",
            "maximum": "Maximum Yearly Average (₹)",
            "cv": "CV (%)"
        })

        st.dataframe(
            volatility_table.round(2),
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # INDIVIDUAL COMMODITY EXPLORER
        # ==========================================

        st.markdown("---")
        st.markdown("## 04 / Explore Individual Commodities")

        st.caption(
            "Select a commodity to investigate its yearly "
            "price fluctuations."
        )

        selected_commodity = st.selectbox(
            "Choose a commodity",
            sorted(yearly["commodity"].unique()),
            key="volatility_commodity"
        )

        selected_trend = (
            yearly[
                yearly["commodity"] == selected_commodity
            ]
            .sort_values("year")
            .copy()
        )

        selected_stats = volatility[
            volatility["commodity"] == selected_commodity
        ].iloc[0]

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Yearly Price",
            f"₹{selected_stats['mean']:.2f}"
        )

        col2.metric(
            "Standard Deviation",
            f"₹{selected_stats['std']:.2f}"
        )

        col3.metric(
            "Coefficient of Variation",
            f"{selected_stats['cv']:.2f}%"
        )

        fig = px.line(
            selected_trend,
            x="year",
            y="price",
            markers=True,
            color_discrete_sequence=["#7165A6"],
            labels={
                "year": "Year",
                "price": "Yearly Average Price (₹)"
            }
        )

        fig.update_traces(
            line=dict(width=3),
            marker=dict(size=9),
            hovertemplate=(
                "Year: %{x}<br>"
                "Average Price: ₹%{y:.2f}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=420,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=15, r=15, t=25, b=35),
            xaxis=dict(
                title="Year",
                dtick=1,
                showgrid=False
            ),
            yaxis=dict(
                title="Yearly Average Price (₹)",
                gridcolor="#E9EEE8"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================================
        # AUTOMATIC MARKET OBSERVATIONS
        # ==========================================

        st.markdown("---")
        st.markdown("## 05 / What the Data Reveals")

        difference = (
            most_volatile["cv"] - most_stable["cv"]
        )

        st.markdown(f"""
        - **Highest relative volatility:** {most_volatile['commodity']}
          has the highest CV at {most_volatile['cv']:.2f}%.

        - **Highest relative stability:** {most_stable['commodity']}
          has the lowest CV at {most_stable['cv']:.2f}%.

        - **Difference in CV:** The gap between the highest
          and lowest CV values is {difference:.2f} percentage points.

        - **Selected commodity:** {selected_commodity} has a CV
          of {selected_stats['cv']:.2f}% across the available
          yearly averages.
        """)

        st.caption(
            "Volatility describes variation in annual average prices. "
            "It does not identify the causes of price changes or "
            "measure daily price fluctuations."
        )

    else:

        st.warning(
            "Unable to calculate volatility. "
            "Check whether the yearly dataset contains sufficient "
            "price observations for each commodity."
        )

