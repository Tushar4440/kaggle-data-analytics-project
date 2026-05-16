# Shipment Order Data analysis project

## Project Overview
This project performs an end-to-end data analysis on a shipment orders dataset sourced from Kaggle. The project includes data extraction using the Kaggle API, data cleaning and transformation using Python (Pandas), in-depth data analysis using SQL, and an interactive data visualization dashboard built with Streamlit.

## Tech Stack
- **Python:** Data extraction, manipulation, and feature engineering.
- **Pandas:** Loading the data, handling missing values, and creating calculated columns (like Selling Price and Profit).
- **SQL Server:** Advanced querying using window functions, Common Table Expressions (CTEs), and aggregations to uncover business insights.
- **Streamlit & Plotly:** Building an interactive web dashboard to visualize key metrics.

## Project Structure
- `project.ipynb`: A Jupyter Notebook that demonstrates the data pipeline:
  - Downloading the dataset directly from Kaggle (`akshatagrawal9431/shipment-orders-dataset`) using the Kaggle CLI.
  - Unzipping and loading the data into a Pandas DataFrame.
  - Performing data cleaning (handling null values like 'Not Available' or 'unknown').
  - Calculating new fields like `Selling Price` (considering discounts) and `Profit`.
- `SQLQuery1.sql`: A comprehensive SQL script containing 11 queries answering specific business problems using the transformed data.
- `dashboard.py`: An interactive Streamlit application that provides a visual overview of the dataset.
- `orders_data.csv`: The raw dataset extracted from the Kaggle zip file.
- `.streamlit/config.toml`: Configuration file to ensure smooth local networking for the Streamlit dashboard (resolves WebSocket/IPv6 connection issues).

## Dashboard Features
The Streamlit dashboard (`dashboard.py`) visualizes:
- **Core KPIs:** Total Sales, Total Profit, Quantity Sold, and Average Order Value.
- **Sales by Region:** A donut chart breaking down revenue by geographic region.
- **Top 10 Profitable Products:** A horizontal bar chart identifying the best-performing products.
- **Sales Trend Over Time:** A line chart displaying month-over-month sales progression.
- **Category & City Insights:** Bar charts analyzing sales by product category and top cities by volume.

## Key Business Questions Answered (SQL Analysis)
The SQL queries in this project uncover various insights from the data, such as:
1. Distinct cities where orders have been shipped.
2. Total selling price and total profits of all orders.
3. Filtering specific orders (e.g., 'Technology' category shipped via 'Second Class').
4. Average Order Value (AOV).
5. The city with the highest total quantity of products ordered.
6. Ranking orders in each region by quantity using Window Functions.
7. Total cost for orders placed in the first quarter of any year.
8. Identifying the top 10 highest profit-generating products.
9. Discovering the top 3 highest selling products in each region.
10. Month-over-month sales growth comparison for 2022 and 2023.
11. Identifying the most profitable month for each product category.

## How to Run the Project

### 1. Data Pipeline (Python/Jupyter)
- Ensure you have Jupyter Notebook or JupyterLab installed.
- Configure your Kaggle API key (`kaggle.json`) to download the dataset.
- Run `project.ipynb` to generate a cleaned and transformed version of the dataset.

### 2. SQL Analysis
- Import the final dataset (`orders_data.csv`) into your SQL Server database.
- Execute the queries in `SQLQuery1.sql` against the database to view the analytical results.

### 3. Running the Dashboard (Streamlit)
To view the interactive dashboard locally, follow these steps:
1. Ensure the required Python libraries are installed:
   ```bash
   pip install streamlit pandas plotly
   ```
2. Start the Streamlit server from your terminal. If you are using a specific Python version (like 3.12), run:
   ```bash
   py -3.12 -m streamlit run dashboard.py
   ```
   *(Alternatively, just run `streamlit run dashboard.py`)*
3. The dashboard should automatically open in your browser. If it doesn't, or if you see a blank page, manually open your browser and navigate to:
   **`http://127.0.0.1:8501`**
