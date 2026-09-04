# 🇮🇳 Indian E-Commerce Customer, Sales & Profitability Analytics Case Study
*An End-to-End Commercial Data Analytics & Customer Intelligence Portfolio Project (INR ₹)*

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy)
![Seaborn](https://img.shields.io/badge/Seaborn-Visuals-3776AB?style=for-the-badge)
![Market](https://img.shields.io/badge/Market-India_INR-orange?style=for-the-badge)

---

## 🎯 Executive Business Question
> **“What drives revenue, customer retention, and profitability in an Indian e-commerce business?”**

Rather than executing a generic "Load CSV → Clean → Plot charts" pipeline, this project approaches Indian retail operations as a **Senior Commercial Analytics Specialist**. It evaluates a multi-table relational dataset of **5,000 customers**, **14,200 orders**, and **22,100+ order line items** over a two-year operating timeline (2023–2024), diagnosing revenue growth, margin leakages, product velocity, state-wise demand, and customer lifetime value in **Indian Rupees (₹ Lakhs and ₹ Crores)**.

---

## 📸 Executive Visual Dashboard

### 1. Monthly Revenue & Profitability Trajectory (Diwali Festive Peaks)
![Monthly Revenue Trend in INR]01_monthly_revenue_trend_inr.png

### 2. ⭐ Indian RFM Customer Segmentation (Pareto Skew)
![RFM Segmentation Breakdown in INR](images/03_rfm_segmentation_breakdown_inr.png)

### 3. Category Revenue vs. Return-to-Origin (RTO) Friction
![Category Revenue vs Returns in INR](images/02_category_revenue_returns_inr.png)

### 4. Discount Elasticity: Margin Compression vs. Return Friction
![Discount vs Profit & Returns in INR](images/04_discount_vs_profit_returns_inr.png)

### 5. Top 10 Flagship Products Across India
![Top Products Sales & Profit](images/05_top_products_sales_profit_inr.png)

### 6. Geographic Concentration: Top 8 States & Zone-Wise AOV
![Geography State & AOV](images/06_geography_state_aov_inr.png)

---

## 📊 Key Executive Findings & Answers (INR ₹)

| Business Dimension | Core Metric / Finding | Strategic Commercial Insight |
| :--- | :--- | :--- |
| **Gross Merchandise Value (GMV)** | **₹5.05 Crore** (₹5,05,35,672) | Pre-discount transaction volume across all delivered lines. |
| **Net Top-Line Revenue** | **₹4.69 Crore** (₹4,68,88,185) | Realized revenue before accounting for return refunds. |
| **Realized Sales (Excl. Returns)** | **₹4.25 Crore** (₹4,24,61,149) | **₹44.27 Lakhs (9.4%)** is lost to customer return refunds and logistics leakage. |
| **Gross Operating Profit** | **₹2.71 Crore (57.9% Margin)** | Robust unit economics led by Ayurveda/Beauty (70.5%) and compressed by Apparel (52.2%). |
| **Customer Retention** | **65.1% Repeat Buyers** | 1,961 out of 3,010 transacting customers purchased 2 or more times. |
| **Average Order Value (AOV)** | **₹3,506.97** | Healthy basket size averaging 1.6 products per delivered order. |
| **⭐ RFM "Champions"** | **21.2% users → 59.1% revenue** | Intense Pareto distribution: 638 VIP accounts drive nearly 60% of total revenue. |
| **Return-to-Origin (RTO)** | **Apparel & Ethnic (18.1% return rate)** | Sizing inconsistencies and COD impulse orders drive 4x higher returns than Skincare (3.9%). |
| **Discount Threshold** | **>15% discount degrades margins** | Discounts above 15% drop gross margins below 50% and raise returns above 11%. |

---

## 🏆 Detailed Question-by-Question Breakdown

### 1. Revenue Dynamics
* **Monthly Trajectory**: Monthly sales scaled from **~₹2.5 Lakhs/month** in early 2023 to a peak of **₹74.5 Lakhs** during Diwali/Festive season in October/November 2024.
* **Top Category by Volume & Sales**:
  1. **Electronics & Gadgets**: **₹1.28 Crore** (56.2% margin, 8.9% returns)
  2. **Fitness, Sports & Yoga**: **₹1.19 Crore** (60.7% margin, 5.8% returns)
  3. **Home, Kitchen & Living**: **₹1.08 Crore** (60.4% margin, 6.6% returns)
  4. **Apparel & Ethnic Wear**: **₹1.00 Crore** (52.2% margin, **18.1% returns**)
  5. **Beauty, Skincare & Ayurveda**: **₹14.19 Lakhs** (**70.5% margin**, 3.9% returns)
* **Flagship Products**:
  1. *Cast Iron Hex Dumbbells Set with Rack 20kg* (Fitness): **₹59.27 Lakhs** (1,036 units)
  2. *4K Ultra HD Android Streaming Stick* (Electronics): **₹36.27 Lakhs** (1,003 units)
  3. *Hard Anodized 5-Piece Non-Stick Cookware Set* (Home): **₹31.25 Lakhs** (578 units)

### 2. Customer Health & Retention
* **Repeat Customer Percentage**: **65.1%** of active buyers placed 2 or more orders.
* **Average Order Value (AOV)**: **₹3,506.97** per delivered order.
* **Highest-Value Accounts**: The top customer (`IND_CUST_02877`) placed 380 orders totaling **₹13.67 Lakhs** in net spend and **₹7.87 Lakhs** in gross operating profit.

### 3. Product Catalog Diagnostics
* **High Return Liabilities**: Apparel SKUs like the *Waterproof Breathable Trail Running Jacket* (21.4% return rate) and *100% Pure Organic Cotton Printed Kurti* (20.5% return rate) suffer from sizing disputes and Cash-on-Delivery buyer remorse.
* **High-Margin Anchors**: Ayurvedic products (e.g., *Kumkumadi Face Oil*, *Rose Water*) deliver **70.5% gross profit** with minimal return friction (<4%).

### 4. Geographic Concentration Across Indian States
* **Top Revenue States**:
  1. **Maharashtra**: **₹1.13 Crore** (3,179 orders, ₹3,548 AOV)
  2. **Karnataka**: **₹81.49 Lakhs** (2,351 orders, ₹3,466 AOV)
  3. **Delhi NCR**: **₹54.93 Lakhs** (1,630 orders, ₹3,370 AOV)
  4. **Tamil Nadu**: **₹54.59 Lakhs** (1,521 orders, ₹3,589 AOV)
  5. **Telangana**: **₹46.55 Lakhs** (1,272 orders, ₹3,660 AOV)
  6. **Uttar Pradesh**: **₹33.05 Lakhs** (945 orders, ₹3,497 AOV)
* **Zone-Wise AOV**: Consistently strong across all zones: South (₹3,552), West (₹3,521), East (₹3,479), North (₹3,407).

### 5. Payment Methods & Cash on Delivery (COD) Impact
* **UPI Dominance**: UPI (GooglePay / PhonePe / Paytm) represents **52.3%** of all orders.
* **The COD Penalty**: Cash-on-Delivery orders represent **16.1%** of total volume but have a **4% higher return-to-origin (RTO)** rate compared to prepaid orders.

---

## ⭐ Advanced Portfolio Module: RFM Customer Segmentation (INR ₹)

Using five-tier quantile scoring for **Recency**, **Frequency**, and **Monetary Value**:

| Customer Segment | Customer Count | % of Base | % of Revenue | Avg. Recency | Avg. Orders | Strategic Recommendation |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 🥇 **Champions** | 638 | 21.2% | **59.1%** | 14.5 days | 12.1 | VIP loyalty rewards, exclusive early festive access, zero-fee fast shipping |
| 🥈 **Loyal Customers** | 715 | 23.8% | **19.2%** | 37.6 days | 3.9 | Cross-sell complementary high-margin categories (Ayurveda/Home) |
| ⚠️ **Need Attention / At Risk**| 293 | 9.7% | **7.9%** | 132.8 days | 3.5 | Win-back WhatsApp / SMS sequences with personalized replenishment alerts |
| 📉 **At Risk** | 479 | 15.9% | **5.3%** | 280.9 days | 1.4 | Re-engagement discounts and surveys targeting product/delivery friction |
| 💤 **Lost Customers** | 379 | 12.6% | **3.1%** | 270.4 days | 1.0 | Low-cost automated email drip; sunset inactive profiles |
| 🚀 **New & Promising** | 256 | 8.5% | **2.3%** | 19.8 days | 1.2 | Welcome onboarding sequence with instant second-purchase cashback |
| 🌱 **Potential Loyalists** | 200 | 6.6% | **1.7%** | 55.4 days | 1.1 | Nudge for second purchase within 30-day post-delivery window |
| 🚨 **Can't Lose Them** | 50 | 1.7% | **1.5%** | 287.1 days | 4.0 | High prior spenders who lapsed; personalized relationship outreach |

---

## 📂 Repository Architecture

```text
ecommerce_analytics_india_case_study/
│
├── data/
│   ├── customers.csv                    # 5,000 Indian customer demographic profiles
│   ├── products.csv                     # 50 products across 5 retail categories in INR (₹)
│   ├── orders.csv                       # 14,200 orders with UPI, COD, Card payment tags
│   ├── order_items.csv                  # 22,100+ line items with discounts & returns in ₹
│   └── ecommerce_india_master_transactions.csv # Merged denormalized master analytical view
│
├── notebooks/
│   └── ecommerce_analytics_india_case_study.ipynb # Interactive Jupyter Notebook with full code & EDA
│
├── scripts/
│   └── run_analysis_india.py            # Standalone CLI analysis script
│
├── images/                              # High-resolution portfolio visualizations
│   ├── 01_monthly_revenue_trend_inr.png
│   ├── 02_category_revenue_returns_inr.png
│   ├── 03_rfm_segmentation_breakdown_inr.png
│   ├── 04_discount_vs_profit_returns_inr.png
│   ├── 05_top_products_sales_profit_inr.png
│   └── 06_geography_state_aov_inr.png
│
├── requirements.txt                     # Reproducible package dependencies
├── .gitignore                           # Git hygiene
└── README.md                            # Comprehensive case study documentation
```

---

## 🛠️ Installation & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/shrutithacker14/ecommerce-customer-sales-analytics.git
cd ecommerce-customer-sales-analytics
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Complete Analysis Script
```bash
python scripts/run_analysis_india.py
```

### 4. Or Explore the Interactive Jupyter Notebook
```bash
jupyter notebook notebooks/ecommerce_analytics_india_case_study.ipynb
```

---

## 💡 Strategic Recommendations for Indian E-Commerce Leadership
1. **Nurture the 21.2% Champions**: This group generates **59.1% of total revenue**. Investing in a dedicated VIP loyalty tier with early festive access yields significantly higher ROI than broad customer acquisition.
2. **Incentivize Prepaid UPI over COD**: Offering a 3–5% instant discount for prepaid UPI payments will compress Cash-on-Delivery orders, directly mitigating ~₹44 Lakhs in return-to-origin (RTO) reverse logistics waste.
3. **Apparel Sizing Optimization**: Implement localized sizing charts and verified customer fit images to reduce the 18.1% Apparel return bottleneck.
4. **Cap Promotional Markdowns at 15%**: Discounts exceeding 15% compress gross margins below 50% without generating proportional unit volume.
