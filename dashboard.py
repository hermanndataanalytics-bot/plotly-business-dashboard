import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# =========================================================
# 1. PROFESSIONAL EXECUTIVE COLOR PALETTE
# =========================================================
colors = {
    'bg': '#F8FAFC',
    'header_bg': '#1E3A8A',
    'bar_color': '#3B82F6',
    'line_color': '#10B981',
    'text_main': '#1E293B',
    'grid_color': '#E2E8F0'
}

# =========================================================
# 2. DASHBOARD STRUCTURE
# =========================================================
fig = make_subplots(
    rows=3,
    cols=1,
    vertical_spacing=0.08,
    row_heights=[0.22, 0.38, 0.40],
    specs=[
        [{"type": "table"}],
        [{"type": "scatter"}],
        [{"type": "bar"}]
    ]
)

# =========================================================
# A. EXECUTIVE KPI TABLE
# =========================================================
fig.add_trace(
    go.Table(
        header=dict(
            values=['Metric', 'Current Value', 'Trend (vs Last Month)'],
            fill_color=colors['header_bg'],
            align='center',
            font=dict(color='white', size=15, family="Arial Black")
        ),
        cells=dict(
            values=[
                ['Total Revenue', 'Total Orders', 'Avg Order Value'],
                ['$321,762', '1,973', '$163.08'],
                ['▲ +12.5%', '▲ +5.2%', '▲ +2.1%']
            ],
            fill_color=['#F1F5F9', 'white', 'white'],
            align='center',
            height=36,
            font=dict(
                size=16,
                color=[
                    colors['text_main'],
                    colors['text_main'],
                    colors['line_color']
                ]
            )
        )
    ),
    row=1, col=1
)

# =========================================================
# B. REVENUE TREND ANALYSIS
# =========================================================
months = ['Jan', 'Feb', 'Mar', 'Apr']
revenue = [75000, 72000, 92000, 88000]

fig.add_trace(
    go.Scatter(
        x=months,
        y=revenue,
        mode='lines+markers',
        line=dict(color=colors['line_color'], width=4),
        marker=dict(size=8),
        fill='tozeroy',
        fillcolor='rgba(16, 185, 129, 0.12)'
    ),
    row=2, col=1
)

# Peak Performance annotation
fig.add_annotation(
    x='Mar',
    y=92000,
    text='Peak Performance',
    showarrow=True,
    arrowhead=2,
    arrowcolor=colors['line_color'],
    font=dict(size=13, color=colors['text_main']),
    row=2,
    col=1
)

# =========================================================
# C. TOP PRODUCT PERFORMANCE
# =========================================================
products = [
    'Coffee Maker',
    'Office Chair',
    'Smartphone',
    'Headphones',
    'Laptop'
]

sales = [75000, 68000, 65000, 60000, 58000]

fig.add_trace(
    go.Bar(
        y=products,
        x=sales,
        orientation='h',
        marker_color=colors['bar_color'],
        text=[f"${v:,.0f}" for v in sales],
        textposition='outside'
    ),
    row=3, col=1
)

# =========================================================
# 3. FINAL LAYOUT & UI POLISH
# =========================================================
fig.update_layout(
    title=dict(
        text="BUSINESS INTELLIGENCE & REVENUE GROWTH ANALYSIS",
        x=0.5,
        y=0.97,
        font=dict(size=20, family="Arial Black")
    ),
    height=900,
    width=1200,
    paper_bgcolor=colors['bg'],
    plot_bgcolor='white',
    font=dict(
        family="Arial",
        size=13,
        color=colors['text_main']
    ),
    margin=dict(l=80, r=80, t=100, b=50),
    showlegend=False
)

fig.update_xaxes(showgrid=True, gridcolor=colors['grid_color'])
fig.update_yaxes(showgrid=True, gridcolor=colors['grid_color'], row=2, col=1)
fig.update_yaxes(showgrid=False, row=3, col=1)

# =========================================================
# 4. EXPORT HIGH-RES IMAGE (PORTFOLIO READY)
# =========================================================
if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image(
    "images/persuasive_dashboard_v2.png",
    scale=2
)

fig.show()

print("✅ Dashboard generated successfully → images/persuasive_dashboard_v2.png")
