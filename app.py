import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Executive Dashboard", layout="wide")

st.title("📊 Executive Business Dashboard")

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [12000, 15000, 17000, 14000, 19000, 22000],
    "Orders": [120, 135, 160, 140, 180, 210]
})

col1, col2 = st.columns(2)

with col1:
    fig1 = px.line(df, x="Month", y="Revenue", title="Monthly Revenue")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(df, x="Month", y="Orders", title="Monthly Orders")
    st.plotly_chart(fig2, use_container_width=True)

st.success("Live interactive dashboard — ready for clients 🚀")

# Professional background watermark
watermark_bg = """
<style>
.stApp {
    position: relative;
}

.watermark-bg {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-30deg);
    font-size: 60px;
    color: lightgrey;
    opacity: 0.1;
    pointer-events: none;
    z-index: 0;
    white-space: nowrap;
}
</style>
<div class="watermark-bg">
    Created by Hermann Ramostafy - 2026
</div>
"""
st.markdown(watermark_bg, unsafe_allow_html=True)
