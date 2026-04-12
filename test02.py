import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")

# -----------------------
# Fake Data (เปลี่ยนเป็น CSV จริงได้)
# -----------------------
df = pd.DataFrame({
    "Product": ["P-1001","P-1002","P-2001","P-3003","P-4500","P-5501"]*10,
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"]*10,
    "Defect": [5,7,3,6,8,4]*10,
    "Process": ["A","B","C","A","B","C"]*10
})

# -----------------------   
# Sidebar (เมนูซ้าย)
# -----------------------
st.sidebar.title("Menu")
menu = st.sidebar.radio("", ["Overview","Man","Machine","Method","Material","Details"])

# -----------------------
# Title
# -----------------------
st.markdown("<h1 style='text-align:center;color:#6A1B9A;'>Production Defect Investigation Dashboard</h1>", unsafe_allow_html=True)

# -----------------------
# Filters
# -----------------------
col1, col2, col3 = st.columns(3)

with col1:
    product_filter = st.selectbox("Product", ["All"] + list(df["Product"].unique()))

with col2:
    process_filter = st.selectbox("Process", ["All"] + list(df["Process"].unique()))

with col3:
    month_filter = st.selectbox("Month", ["All"] + list(df["Month"].unique()))

# Filter logic
filtered_df = df.copy()

if product_filter != "All":
    filtered_df = filtered_df[filtered_df["Product"] == product_filter]

if process_filter != "All":
    filtered_df = filtered_df[filtered_df["Process"] == process_filter]

if month_filter != "All":
    filtered_df = filtered_df[filtered_df["Month"] == month_filter]

# -----------------------
# KPI Cards
# -----------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Qty NG", filtered_df["Defect"].sum())
col2.metric("Qty Inspected", len(filtered_df)*100)
col3.metric("Occurrence Rate (%)", round(filtered_df["Defect"].mean(),2))
col4.metric("Count of Defect", filtered_df["Defect"].count())
col5.metric("Defect Days", filtered_df["Month"].nunique())

# -----------------------
# Charts
# -----------------------
col1, col2 = st.columns(2)

# Bar Chart
with col1:
    bar = px.bar(filtered_df,
                 x="Month",
                 y="Defect",
                 color="Product",
                 title="Defect by Month & Product")
    st.plotly_chart(bar, use_container_width=True)

# Pie Chart
with col2:
    pie = px.pie(filtered_df,
                 names="Product",
                 values="Defect",
                 title="Defect by Product",
                 hole=0.5)
    st.plotly_chart(pie, use_container_width=True)