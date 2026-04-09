#<<<<<<< HEAD
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 My First Data Dashboard")

# โหลดข้อมูล (ตัวอย่างสร้างเอง)
data = {
    "customer": ["A", "B", "C", "D", "E"],
    "total_spent": [1000, 2500, 1800, 3000, 2200],
    "orders": [5, 10, 7, 12, 9]
}
df = pd.DataFrame(data)

# แสดงตาราง
st.subheader("📋 Data Table")
st.dataframe(df)

# KPI
st.subheader("📌 Key Metrics")
col1, col2 = st.columns(2)

col1.metric("Total Revenue", df["total_spent"].sum())
col2.metric("Average Orders", df["orders"].mean())

# กราฟ
st.subheader("📈 Spending by Customer")

fig, ax = plt.subplots()
ax.bar(df["customer"], df["total_spent"])
ax.set_xlabel("Customer")
ax.set_ylabel("Total Spent")

st.pyplot(fig)

# Filter
st.subheader("🔍 Filter Data")
min_spent = st.slider("Minimum Spending", 0, 5000, 1000)

filtered_df = df[df["total_spent"] >= min_spent]

st.dataframe(filtered_df)
#=======
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 My First Data Dashboard")

# โหลดข้อมูล (ตัวอย่างสร้างเอง)
data = {
    "customer": ["A", "B", "C", "D", "E"],
    "total_spent": [1000, 2500, 1800, 3000, 2200],
    "orders": [5, 10, 7, 12, 9]
}
df = pd.DataFrame(data)

# แสดงตาราง
st.subheader("📋 Data Table")
st.dataframe(df)

# KPI
st.subheader("📌 Key Metrics")
col1, col2 = st.columns(2)

col1.metric("Total Revenue", df["total_spent"].sum())
col2.metric("Average Orders", df["orders"].mean())

# กราฟ
st.subheader("📈 Spending by Customer")

fig, ax = plt.subplots()
ax.bar(df["customer"], df["total_spent"])
ax.set_xlabel("Customer")
ax.set_ylabel("Total Spent")

st.pyplot(fig)

# Filter
st.subheader("🔍 Filter Data")
min_spent = st.slider("Minimum Spending", 0, 5000, 1000)

filtered_df = df[df["total_spent"] >= min_spent]

st.dataframe(filtered_df)   
#>>>>>>> 4e3c25f (add requirements.txt)
