import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Business Dashboard", layout="wide")

st.title("📊 Executive Business Dashboard")

# Sample data (azo soloina data-nao)
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [12000, 15000, 17000, 14000, 19000, 22000],
    "Orders": [120, 135, 160, 140, 180, 210]
}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)

with col1:
    fig1 = px.line(df, x="Month", y="Revenue", title="Monthly Revenue")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(df, x="Month", y="Orders", title="Monthly Orders")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("✅ Live interactive dashboard built with **Plotly & Streamlit**")
