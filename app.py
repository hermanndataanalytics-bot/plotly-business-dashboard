import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Business Intelligence Dashboard",
    layout="wide"
)

st.title("📊 Business Intelligence & Revenue Growth Analysis")

# -------------------------------------------------
# COLORS
# -------------------------------------------------
colors = {
    'bg': '#F8FAFC',
    'header_bg': '#1E3A8A',
    'bar_color': '#3B82F6',
    'line_color': '#10B981',
    'text_main': '#1E293B',
    'grid_color': '#E2E8F0'
}

# -------------------------------------------------
# SUBPLOTS
# -------------------------------------------------
fig = make_subplots(
    rows=3, cols=1,
    row_heights=[0.2, 0.4, 0.4],
    vertical_spacing=0.08,
    specs=[
        [{"type": "table"}],
        [{"type": "scatter"}],
        [{"type": "bar"}]
    ]
)

# -------------------------------------------------
# KPI TABLE
# -------------------------------------------------
fig.add_trace(
    go.Table(
        header=dict(
            values=['Metric', 'Current Value', 'Trend'],
            fill_color=colors['header_bg'],
            font=dict(color='white', size=15),
            align='center'
        ),
        cells=dict(
            values=[
                ['Total Revenue', 'Total Orders', 'Avg Order Value'],
                ['$321,762', '1,973', '$163.08'],
                ['▲ +12.5%', '▲ +5.2%', '▲ +2.1%']
            ],
            align='center',
            font=dict(size=14)
        )
    ),
    row=1, col=1
)

# -------------------------------------------------
# LINE CHART
# -------------------------------------------------
months = ['Jan', 'Feb', 'Mar', 'Apr']
revenue = [75000, 72000, 92000, 88000]

fig.add_trace(
    go.Scatter(
        x=months,
        y=revenue,
        mode='lines+markers',
        line=dict(color=colors['line_color'], width=4),
        fill='tozeroy'
    ),
    row=2, col=1
)

# -------------------------------------------------
# BAR CHART
# -------------------------------------------------
fig.add_trace(
    go.Bar(
        y=['Laptop', 'Headphones', 'Smartphone', 'Office Chair', 'Coffee Maker'],
        x=[58000, 60000, 65000, 68000, 75000],
        orientation='h',
        marker_color=colors['bar_color']
    ),
    row=3, col=1
)

fig.update_layout(
    height=900,
    showlegend=False,
    paper_bgcolor=colors['bg']
)

# -------------------------------------------------
# DISPLAY
# -------------------------------------------------
st.plotly_chart(fig, use_container_width=True)
