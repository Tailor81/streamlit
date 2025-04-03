import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Data Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
    }
    .card {
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1 class='main-header'>Data Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("An interactive dashboard for exploring and visualizing data.")

# Sidebar
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=200)
    st.markdown("## Dashboard Settings")
    
    # Date range selector
    st.markdown("### Date Range")
    current_date = datetime.now()
    start_date = st.date_input("Start Date", current_date - timedelta(days=30))
    end_date = st.date_input("End Date", current_date)
    
    # Data filter options
    st.markdown("### Filters")
    data_category = st.selectbox("Data Category", ["Sales", "Marketing", "Operations", "Finance"])
    region = st.multiselect("Region", ["North America", "Europe", "Asia", "South America", "Africa", "Oceania"], default=["North America", "Europe"])
    
    # Display options
    st.markdown("### Display Options")
    chart_type = st.radio("Primary Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart"])
    show_raw_data = st.checkbox("Show Raw Data", value=False)
    dark_mode = st.checkbox("Dark Mode", value=False)
    
    st.markdown("---")
    st.markdown("Made with ❤️ by Streamlit")

# Generate sample data
@st.cache_data
def generate_sample_data(start_date, end_date, category, regions):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    data = []
    
    metrics = {
        "Sales": ["Revenue", "Units Sold", "Profit Margin", "Customer Count"],
        "Marketing": ["Ad Spend", "Impressions", "Clicks", "Conversions"],
        "Operations": ["Inventory", "Production", "Shipping Time", "Defect Rate"],
        "Finance": ["Cash Flow", "Expenses", "Investment", "ROI"]
    }
    
    selected_metrics = metrics[category]
    
    for date in date_range:
        for region in regions:
            for product in ["Product A", "Product B", "Product C"]:
                data.append({
                    "Date": date,
                    "Region": region,
                    "Product": product,
                    "Metric": selected_metrics[0],
                    "Value": np.random.randint(1000, 10000) * (1 + (date.day / 31)),
                    "Secondary Value": np.random.randint(500, 5000),
                    "Target": np.random.randint(8000, 12000),
                    "Status": np.random.choice(["Above Target", "On Target", "Below Target"]),
                })
                
                # Add other metrics
                for metric in selected_metrics[1:]:
                    data.append({
                        "Date": date,
                        "Region": region,
                        "Product": product,
                        "Metric": metric,
                        "Value": np.random.randint(100, 1000) * (1 + (date.day / 31)),
                        "Secondary Value": np.random.randint(50, 500),
                        "Target": np.random.randint(800, 1200),
                        "Status": np.random.choice(["Above Target", "On Target", "Below Target"]),
                    })
    
    return pd.DataFrame(data)

df = generate_sample_data(start_date, end_date, data_category, region)

# Create tabs for different views
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Trends Analysis", "Regional Breakdown", "Detailed Analysis"])

with tab1:
    st.markdown("<h2 class='sub-header'>Key Performance Indicators</h2>", unsafe_allow_html=True)
    
    # KPI metrics
    col1, col2, col3, col4 = st.columns(4)
    
    metrics_data = df.groupby("Metric")["Value"].sum().reset_index()
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        metric_name = metrics_data.iloc[0]["Metric"]
        metric_value = int(metrics_data.iloc[0]["Value"])
        st.metric(
            label=metric_name,
            value=f"${metric_value:,}" if "Revenue" in metric_name or "Spend" in metric_name else f"{metric_value:,}",
            delta=f"{np.random.randint(5, 15)}%" if np.random.random() > 0.5 else f"-{np.random.randint(1, 10)}%"
        )
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        metric_name = metrics_data.iloc[1]["Metric"]
        metric_value = int(metrics_data.iloc[1]["Value"])
        st.metric(
            label=metric_name,
            value=f"${metric_value:,}" if "Revenue" in metric_name or "Spend" in metric_name else f"{metric_value:,}",
            delta=f"{np.random.randint(5, 15)}%" if np.random.random() > 0.5 else f"-{np.random.randint(1, 10)}%"
        )
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        metric_name = metrics_data.iloc[2]["Metric"]
        metric_value = int(metrics_data.iloc[2]["Value"])
        st.metric(
            label=metric_name,
            value=f"${metric_value:,}" if "Revenue" in metric_name or "Spend" in metric_name else f"{metric_value:,}",
            delta=f"{np.random.randint(5, 15)}%" if np.random.random() > 0.5 else f"-{np.random.randint(1, 10)}%"
        )
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        metric_name = metrics_data.iloc[3]["Metric"]
        metric_value = int(metrics_data.iloc[3]["Value"])
        st.metric(
            label=metric_name,
            value=f"${metric_value:,}" if "Revenue" in metric_name or "Spend" in metric_name else f"{metric_value:,}",
            delta=f"{np.random.randint(5, 15)}%" if np.random.random() > 0.5 else f"-{np.random.randint(1, 10)}%"
        )
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main chart
    st.markdown("<h2 class='sub-header'>Performance Overview</h2>", unsafe_allow_html=True)
    
    # Prepare data for chart
    daily_data = df.groupby(["Date", "Metric"])["Value"].sum().reset_index()
    pivot_data = daily_data.pivot(index="Date", columns="Metric", values="Value").reset_index()
    
    # Create chart based on selected type
    if chart_type == "Bar Chart":
        fig = px.bar(
            pivot_data,
            x="Date",
            y=pivot_data.columns[1:],
            title=f"{data_category} Metrics Over Time",
            labels={"value": "Value", "variable": "Metric"},
            height=500
        )
    elif chart_type == "Line Chart":
        fig = px.line(
            pivot_data,
            x="Date",
            y=pivot_data.columns[1:],
            title=f"{data_category} Metrics Over Time",
            labels={"value": "Value", "variable": "Metric"},
            height=500
        )
    elif chart_type == "Scatter Plot":
        # For scatter plot, we'll use the first two metrics
        fig = px.scatter(
            df,
            x=df[df["Metric"] == pivot_data.columns[1]]["Value"],
            y=df[df["Metric"] == pivot_data.columns[2]]["Value"],
            color="Region",
            size="Secondary Value",
            hover_name="Product",
            title=f"Relationship between {pivot_data.columns[1]} and {pivot_data.columns[2]}",
            height=500
        )
    else:  # Pie Chart
        region_data = df.groupby("Region")["Value"].sum().reset_index()
        fig = px.pie(
            region_data,
            values="Value",
            names="Region",
            title=f"{data_category} Distribution by Region",
            height=500
        )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display raw data if checked
    if show_raw_data:
        st.markdown("<h3>Raw Data</h3>", unsafe_allow_html=True)
        st.dataframe(df)

with tab2:
    st.markdown("<h2 class='sub-header'>Trends Analysis</h2>", unsafe_allow_html=True)
    
    # Time series analysis
    st.markdown("### Time Series Analysis")
    
    # Create time series for first metric
    primary_metric = df["Metric"].unique()[0]
    time_series = df[df["Metric"] == primary_metric].groupby("Date")["Value"].sum().reset_index()
    
    # Add rolling average
    time_series["7-Day Rolling Avg"] = time_series["Value"].rolling(7, min_periods=1).mean()
    
    # Plot time series
    fig_time = px.line(
        time_series,
        x="Date",
        y=["Value", "7-Day Rolling Avg"],
        title=f"{primary_metric} Time Series with 7-Day Rolling Average",
        labels={"value": "Value", "variable": "Metric"},
        height=400
    )
    st.plotly_chart(fig_time, use_container_width=True)
    
    # Product comparison
    st.markdown("### Product Comparison")
    
    product_data = df[df["Metric"] == primary_metric].groupby(["Date", "Product"])["Value"].sum().reset_index()
    product_pivot = product_data.pivot(index="Date", columns="Product", values="Value").reset_index()
    
    fig_product = px.line(
        product_pivot,
        x="Date",
        y=product_pivot.columns[1:],
        title=f"{primary_metric} by Product",
        labels={"value": "Value", "variable": "Product"},
        height=400
    )
    st.plotly_chart(fig_product, use_container_width=True)
    
    # Seasonal patterns
    st.markdown("### Day of Week Analysis")
    
    # Add day of week
    df["Day of Week"] = pd.to_datetime(df["Date"]).dt.day_name()
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    day_data = df[df["Metric"] == primary_metric].groupby("Day of Week")["Value"].mean().reindex(day_order).reset_index()
    
    fig_day = px.bar(
        day_data,
        x="Day of Week",
        y="Value",
        title=f"Average {primary_metric} by Day of Week",
        height=400
    )
    st.plotly_chart(fig_day, use_container_width=True)

with tab3:
    st.markdown("<h2 class='sub-header'>Regional Breakdown</h2>", unsafe_allow_html=True)
    
    # Regional map
    st.markdown("### Regional Performance Map")
    
    # Create map data
    map_data = df.groupby("Region")["Value"].sum().reset_index()
    
    # Map region names to ISO codes for the choropleth
    region_to_iso = {
        "North America": "NAM",
        "Europe": "EUR",
        "Asia": "ASI",
        "South America": "SAM",
        "Africa": "AFR",
        "Oceania": "OCE"
    }
    
    map_data["ISO"] = map_data["Region"].map(region_to_iso)
    
    fig_map = px.choropleth(
        map_data,
        locations="ISO",
        color="Value",
        hover_name="Region",
        projection="natural earth",
        title=f"Total {data_category} Performance by Region",
        color_continuous_scale=px.colors.sequential.Blues,
        height=500
    )
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Regional comparison
    st.markdown("### Regional Metrics Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        regional_data = df.groupby(["Region", "Metric"])["Value"].sum().reset_index()
        regional_pivot = regional_data.pivot(index="Region", columns="Metric", values="Value").reset_index()
        
        selected_metric = st.selectbox("Select Metric for Comparison", df["Metric"].unique())
        
        fig_regional = px.bar(
            regional_data[regional_data["Metric"] == selected_metric],
            x="Region",
            y="Value",
            title=f"{selected_metric} by Region",
            height=400
        )
        st.plotly_chart(fig_regional, use_container_width=True)
    
    with col2:
        # Regional distribution pie chart
        regional_total = df.groupby("Region")["Value"].sum().reset_index()
        
        fig_pie = px.pie(
            regional_total,
            values="Value",
            names="Region",
            title=f"Regional Distribution of {data_category}",
            height=400
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Regional trends
    st.markdown("### Regional Trends Over Time")
    
    region_time = df[df["Metric"] == primary_metric].groupby(["Date", "Region"])["Value"].sum().reset_index()
    region_pivot = region_time.pivot(index="Date", columns="Region", values="Value").reset_index()
    
    fig_region_time = px.line(
        region_pivot,
        x="Date",
        y=region_pivot.columns[1:],
        title=f"{primary_metric} Trends by Region",
        labels={"value": "Value", "variable": "Region"},
        height=500
    )
    st.plotly_chart(fig_region_time, use_container_width=True)

with tab4:
    st.markdown("<h2 class='sub-header'>Detailed Analysis</h2>", unsafe_allow_html=True)
    
    # Custom analysis options
    st.markdown("### Custom Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_axis = st.selectbox("X-Axis", ["Date", "Region", "Product", "Metric", "Value", "Secondary Value"])
    
    with col2:
        y_axis = st.selectbox("Y-Axis", ["Value", "Secondary Value", "Target", "Region", "Product", "Metric"])
    
    # Create custom chart
    if x_axis != y_axis:
        if x_axis in ["Date", "Region", "Product", "Metric"] and y_axis in ["Value", "Secondary Value", "Target"]:
            custom_data = df.groupby(x_axis)[y_axis].sum().reset_index()
            
            fig_custom = px.bar(
                custom_data,
                x=x_axis,
                y=y_axis,
                title=f"{y_axis} by {x_axis}",
                height=500
            )
            st.plotly_chart(fig_custom, use_container_width=True)
        else:
            st.warning("Please select a categorical variable for X-Axis and a numerical variable for Y-Axis.")
    else:
        st.warning("Please select different variables for X and Y axes.")
    
    # Statistical analysis
    st.markdown("### Statistical Analysis")
    
    # Calculate statistics for the primary metric
    stats_data = df[df["Metric"] == primary_metric]["Value"]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Mean", f"{stats_data.mean():.2f}")
    
    with col2:
        st.metric("Median", f"{stats_data.median():.2f}")
    
    with col3:
        st.metric("Standard Deviation", f"{stats_data.std():.2f}")
    
    with col4:
        st.metric("Total Count", f"{stats_data.count():,}")
    
    # Distribution analysis
    st.markdown("### Distribution Analysis")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(stats_data, kde=True, ax=ax)
    ax.set_title(f"Distribution of {primary_metric} Values")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    
    # Correlation matrix
    st.markdown("### Correlation Analysis")
    
    # Create a correlation dataframe for numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    
    fig_corr = px.imshow(
        corr_matrix,
        text_auto=True,
        title="Correlation Matrix",
        color_continuous_scale="RdBu_r",
        height=500,
        aspect="auto"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='display: flex; justify-content: space-between; align-items: center;'>
    <p>Data Analytics Dashboard v1.0</p>
    <p>Created with Streamlit • Last updated: April 3, 2025</p>
</div>
""", unsafe_allow_html=True)