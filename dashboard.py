import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Shipment Orders Dashboard", page_icon="📦", layout="wide")

st.title("📦 Shipment Orders Dashboard")
st.markdown("This dashboard visualizes the key business metrics from the Shipment Orders Data Analytics project.")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("orders_data.csv", na_values=['Not Available', 'unknown'])
    # Data transformations based on the project notebook
    df['Selling Price'] = df['List Price'] - df['List Price'] * (df['Discount Percent'] / 100)
    df['Profit'] = df['Selling Price'] - df['cost price']
    df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d-%m-%Y", errors='coerce')
    df['Order Year-Month'] = df['Order Date'].dt.to_period('M').astype(str)
    return df

df = load_data()

# --- KPIs ---
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

total_sales = df['Selling Price'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()
aov = (df['Quantity'] * df['Selling Price']).mean()

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Quantity Sold", f"{total_quantity:,}")
col4.metric("Avg Order Value (AOV)", f"${aov:,.2f}")

st.divider()

# --- Visualizations ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Sales by Region")
    region_sales = df.groupby("Region")['Selling Price'].sum().reset_index()
    fig_region = px.pie(region_sales, values='Selling Price', names='Region', hole=0.4, 
                        color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_region, width='stretch')

with col_right:
    st.subheader("Top 10 Profitable Products")
    product_profit = df.groupby("Product Id")['Profit'].sum().reset_index().sort_values(by="Profit", ascending=False).head(10)
    fig_prod = px.bar(product_profit, x='Profit', y='Product Id', orientation='h', 
                      color='Profit', color_continuous_scale='Greens')
    fig_prod.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_prod, width='stretch')


st.divider()
st.subheader("Sales Trend Over Time")
trend = df.groupby("Order Year-Month")['Selling Price'].sum().reset_index()
# Sort by date
trend['Order Year-Month'] = pd.to_datetime(trend['Order Year-Month'])
trend = trend.sort_values(by="Order Year-Month")

fig_trend = px.line(trend, x='Order Year-Month', y='Selling Price', markers=True, 
                    line_shape="spline", color_discrete_sequence=['#ff7f0e'])
st.plotly_chart(fig_trend, width='stretch')


st.divider()
col_left2, col_right2 = st.columns(2)

with col_left2:
    st.subheader("Sales by Category")
    cat_sales = df.groupby("Category")['Selling Price'].sum().reset_index().sort_values(by="Selling Price", ascending=False)
    fig_cat = px.bar(cat_sales, x='Category', y='Selling Price', text_auto='.2s', color='Category')
    st.plotly_chart(fig_cat, width='stretch')

with col_right2:
    st.subheader("Top 5 Cities by Quantity Sold")
    city_qty = df.groupby("City")['Quantity'].sum().reset_index().sort_values(by="Quantity", ascending=False).head(5)
    fig_city = px.bar(city_qty, x='City', y='Quantity', text_auto=True, color='Quantity', color_continuous_scale='Blues')
    st.plotly_chart(fig_city, width='stretch')

st.markdown("---")
st.markdown("Dashboard created with ❤️ by Tushar Tewari")
