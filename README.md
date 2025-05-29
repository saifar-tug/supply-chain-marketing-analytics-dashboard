# Marketing Analytics Dashboard — ETL Project
This project simulates a real-world marketing analytics pipeline for a SaaS or product-based company. It uses the **Marketing Campaign Dataset** to build a complete **ETL (Extract-Transform-Load)** workflow using Python and pandas.

## Goal
To extract insights from marketing campaign data to inform customer segmentation, product targeting, and business decisions — similar to tasks expected in data engineering roles at companies like **Canonical**.

## Features
- ETL pipeline in modular Python scripts
- Smart missing value imputation (group-level based on Education & Marital Status)
- Feature engineering: customer lifetime, total kids, total spend
- Correlation analysis between income, spend, and engagement
- Clean dataset ready for dashboarding or machine learning

## Dashboard: Marketing Analytics Overview
Built using Apache Superset  
This dashboard includes:

- Total spending segmented by education level
- Customer acquisition trend over time
- Campaign response rate (conversion percentage)

![Dashboard](dashboards/screenshots/marketing_dashboard.png)