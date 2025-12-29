# ev_sales_analysis.py
# Electric Vehicle Sales Analysis - India

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/ev_sales_india.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Create Year and Month columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# ------------------ KPIs ------------------

# Total EV Sales
total_ev_sales = df['EV_Sales_Quantity'].sum()
print("Total EV Sales:", total_ev_sales)

# Year-over-Year Growth
yearly_sales = df.groupby('Year')['EV_Sales_Quantity'].sum().reset_index()
yearly_sales['YoY_Growth_%'] = yearly_sales['EV_Sales_Quantity'].pct_change() * 100
print(yearly_sales)

# Active States
active_states = df[df['EV_Sales_Quantity'] > 0]['State'].nunique()
print("Active States:", active_states)

# Top State by Sales
top_state = (
    df.groupby('State')['EV_Sales_Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
print("Top State by EV Sales:")
print(top_state)

# ------------------ Charts ------------------

# EV Sales Trend
plt.figure()
plt.plot(yearly_sales['Year'], yearly_sales['EV_Sales_Quantity'])
plt.title("EV Sales Trend Over Time")
plt.xlabel("Year")
plt.ylabel("EV Sales")
plt.show()
