"""
=============================================================================
Indian E-Commerce Customer, Sales & Profitability Analytics Case Study (INR ₹)
=============================================================================
Core Business Question:
"What drives revenue, customer retention, and profitability in an Indian e-commerce business?"

Author: Data & Commercial Analytics Specialist
Tools: Python | Pandas | NumPy | Matplotlib | Seaborn | RFM Customer Segmentation
Currency: Indian Rupee (INR ₹) | Geography: 10 Key Indian States & 4 Zones
=============================================================================
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_india_case_study():
    print("--- 1. LOADING INDIAN E-COMMERCE RELATIONAL DATASETS ---")
    data_path = "../data/" if os.path.exists("../data/") else "data/"
    
    customers = pd.read_csv(os.path.join(data_path, "customers.csv"))
    products = pd.read_csv(os.path.join(data_path, "products.csv"))
    orders = pd.read_csv(os.path.join(data_path, "orders.csv"))
    order_items = pd.read_csv(os.path.join(data_path, "order_items.csv"))
    
    print(f"Loaded: {len(customers):,} Customers | {len(products)} Products | {len(orders):,} Orders | {len(order_items):,} Order Items")
    
    # Merge
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    customers['signup_date'] = pd.to_datetime(customers['signup_date'])
    
    master = order_items.merge(orders, on='order_id', how='inner')
    master = master.merge(products, on='product_id', how='inner')
    master = master.merge(customers, on='customer_id', how='inner')
    
    delivered = master[master['order_status'] == 'Delivered'].copy()
    delivered['order_month'] = delivered['order_date'].dt.to_period('M')
    
    # Financial KPI Summary
    gross_gmv = delivered['total_price_inr'].sum()
    discounts = delivered['discount_amount_inr'].sum()
    net_sales = delivered['net_revenue_inr'].sum()
    cogs = delivered['total_cogs_inr'].sum()
    profit = delivered['gross_profit_inr'].sum()
    returns = delivered[delivered['is_returned'] == 1]
    return_refunds = returns['net_revenue_inr'].sum()
    realized_sales = net_sales - return_refunds
    
    print(f"\n--- FINANCIAL KPI SUMMARY (INR ₹) ---")
    print(f"Gross Merchandise Value (GMV):  ₹{gross_gmv:,.2f} (₹{gross_gmv/10000000:.2f} Cr)")
    print(f"Total Customer Discounts:       ₹{discounts:,.2f} ({(discounts/gross_gmv)*100:.1f}% effective discount)")
    print(f"Net Top-Line Revenue:           ₹{net_sales:,.2f} (₹{net_sales/10000000:.2f} Cr)")
    print(f"Returns & Logistics Loss (RTO): ₹{return_refunds:,.2f} ({(len(returns)/len(delivered))*100:.1f}% return rate)")
    print(f"Realized Revenue:               ₹{realized_sales:,.2f} (₹{realized_sales/10000000:.2f} Cr)")
    print(f"Gross Operating Profit:         ₹{profit:,.2f} ({(profit/net_sales)*100:.1f}% margin)")
    
    # Category Breakdown
    print("\n--- CATEGORY INTELLIGENCE & RETURN BOTTLENECK ---")
    cat_summary = delivered.groupby('category').agg(
        revenue=('net_revenue_inr', 'sum'),
        units=('quantity', 'sum'),
        profit=('gross_profit_inr', 'sum'),
        returns=('is_returned', 'sum'),
        total_items=('order_item_id', 'count')
    ).reset_index()
    cat_summary['return_rate%'] = (cat_summary['returns'] / cat_summary['total_items']) * 100
    cat_summary['margin%'] = (cat_summary['profit'] / cat_summary['revenue']) * 100
    print(cat_summary.sort_values(by='revenue', ascending=False).to_string(index=False))
    
    # Customer Behavior & AOV
    print("\n--- CUSTOMER BEHAVIOR & AOV ---")
    cust_orders = delivered.groupby('customer_id').agg(
        orders=('order_id', 'nunique'),
        total_spent=('net_revenue_inr', 'sum')
    ).reset_index()
    
    repeat_rate = (len(cust_orders[cust_orders['orders'] > 1]) / len(cust_orders)) * 100
    order_aov = delivered.groupby('order_id')['net_revenue_inr'].sum().mean()
    print(f"Total Transacting Customers: {len(cust_orders):,}")
    print(f"Repeat Customer Share:       {repeat_rate:.1f}%")
    print(f"Average Order Value (AOV):   ₹{order_aov:,.2f}")
    
    # Payment Method Share
    print("\n--- PAYMENT METHOD DISTRIBUTION ---")
    pay_dist = orders.groupby('payment_method').agg(orders=('order_id', 'count')).reset_index()
    pay_dist['% share'] = (pay_dist['orders'] / len(orders)) * 100
    print(pay_dist.sort_values(by='orders', ascending=False).to_string(index=False))
    
    # RFM Segmentation
    print("\n--- RFM CUSTOMER SEGMENTATION ENGINE (INR ₹) ---")
    snapshot_date = pd.to_datetime('2025-01-01')
    rfm = delivered.groupby('customer_id').agg(
        Recency=('order_date', lambda x: (snapshot_date - x.max()).days),
        Frequency=('order_id', 'nunique'),
        Monetary=('net_revenue_inr', 'sum')
    ).reset_index()
    
    rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1]).astype(int)
    rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm['M_score'] = pd.qcut(rfm['Monetary'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    
    def assign_rfm(row):
        r, f, m = row['R_score'], row['F_score'], row['M_score']
        if r >= 4 and f >= 4 and m >= 4:
            return 'Champions'
        elif r >= 3 and f >= 3:
            return 'Loyal Customers'
        elif r >= 4 and f in [1, 2]:
            return 'New & Promising'
        elif r == 3 and f in [1, 2]:
            return 'Potential Loyalists'
        elif r in [2, 3] and f >= 3:
            return 'Need Attention / At Risk'
        elif r <= 2 and f >= 4:
            return "Can't Lose Them"
        elif r <= 2 and f in [2, 3]:
            return 'At Risk'
        else:
            return 'Lost Customers'

    rfm['Customer_Segment'] = rfm.apply(assign_rfm, axis=1)
    
    rfm_table = rfm.groupby('Customer_Segment').agg(
        Customers=('customer_id', 'count'),
        Avg_Recency_Days=('Recency', 'mean'),
        Avg_Orders=('Frequency', 'mean'),
        Total_Revenue_INR=('Monetary', 'sum'),
        Avg_Spend_INR=('Monetary', 'mean')
    ).reset_index()
    rfm_table['% Revenue'] = (rfm_table['Total_Revenue_INR'] / rfm['Monetary'].sum()) * 100
    rfm_table['% Customers'] = (rfm_table['Customers'] / len(rfm)) * 100
    print(rfm_table.sort_values(by='Total_Revenue_INR', ascending=False).to_string(index=False))
    
    print("\nIndian E-Commerce case study pipeline executed successfully.")

if __name__ == "__main__":
    run_india_case_study()
