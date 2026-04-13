import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# CONFIG
# -----------------------
st.set_page_config(layout="wide")
st.title("🛒 E-Commerce Customer Dashboard")

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data
def load_data():
    return pd.read_csv("ecommerce_customers_dataset.csv")

df = load_data()

# -----------------------
# CLEAN COLUMN NAME
# -----------------------
df.columns = df.columns.str.lower().str.strip()

# -----------------------
# AUTO DETECT COLUMNS
# -----------------------
def find_column(possible_names):
    for col in df.columns:
        for name in possible_names:
            if name in col:
                return col
    return None

col_spent = find_column(["spent", "revenue", "total"])
col_orders = find_column(["order", "purchase"])
col_customer = find_column(["customer", "id"])
col_gender = find_column(["gender", "sex"])
col_age = find_column(["age"])

# -----------------------
# SIDEBAR FILTER
# -----------------------
st.sidebar.header("🔍 Filters")

filtered_df = df.copy()

if col_gender:
    gender = st.sidebar.selectbox("Gender", ["All"] + list(df[col_gender].dropna().unique()))
    if gender != "All":
        filtered_df = filtered_df[filtered_df[col_gender] == gender]

if col_age:
    min_age = int(filtered_df[col_age].min())
    max_age = int(filtered_df[col_age].max())
    age_range = st.sidebar.slider("Age Range", min_age, max_age, (min_age, max_age))
    filtered_df = filtered_df[
        (filtered_df[col_age] >= age_range[0]) &
        (filtered_df[col_age] <= age_range[1])
    ]

# -----------------------
# KPI
# -----------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

if col_spent:
    col1.metric("💰 Total Revenue", f"{filtered_df[col_spent].sum():,.0f}")

if col_orders:
    col2.metric("📦 Total Orders", f"{filtered_df[col_orders].sum():,.0f}")

col3.metric("👥 Customers", filtered_df.shape[0])

# -----------------------
# CUSTOMER SEGMENT
# -----------------------
if col_spent:
    filtered_df["segment"] = pd.qcut(
        filtered_df[col_spent],
        3,
        labels=["Low", "Mid", "High"]
    )

# -----------------------
# CHARTS
# -----------------------
st.subheader("📊 Analytics")

colA, colB = st.columns(2)

# 🔥 Top Customers
if col_customer and col_spent:
    top_df = filtered_df.sort_values(by=col_spent, ascending=False).head(10)
    fig1 = px.bar(
        top_df,
        x=col_customer,
        y=col_spent,
        title="Top 10 Customers"
    )
    colA.plotly_chart(fig1, use_container_width=True)

# 🔥 Spending Distribution
if col_spent:
    fig2 = px.histogram(
        filtered_df,
        x=col_spent,
        nbins=30,
        title="Spending Distribution"
    )
    colB.plotly_chart(fig2, use_container_width=True)

# -----------------------
# SCATTER
# -----------------------
if col_orders and col_spent:
    st.subheader("📈 Orders vs Spending")

    fig3 = px.scatter(
        filtered_df,
        x=col_orders,
        y=col_spent,
        color="segment" if "segment" in filtered_df else None,
        title="Orders vs Spending"
    )

    st.plotly_chart(fig3, use_container_width=True)

# -----------------------
# PIE CHART
# -----------------------
if "segment" in filtered_df:
    st.subheader("🥧 Customer Segments")

    fig4 = px.pie(
        filtered_df,
        names="segment",
        title="Customer Segmentation"
    )

    st.plotly_chart(fig4, use_container_width=True)

# -----------------------
# DATA TABLE
# -----------------------
st.subheader("📋 Data Table")
st.dataframe(filtered_df.head(100))

# -----------------------
# INSIGHT
# -----------------------
st.subheader("🧠 Insights")

if col_spent:
    avg_spent = filtered_df[col_spent].mean()
    total_spent = filtered_df[col_spent].sum()

    st.write(f"""
    - 💰 Total Revenue: {total_spent:,.0f}
    - 📊 Average Spending: {avg_spent:,.0f}
    - 👥 Customers: {filtered_df.shape[0]}
    """)

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.caption("🚀 Built with Streamlit | Portfolio Ready Dashboard")