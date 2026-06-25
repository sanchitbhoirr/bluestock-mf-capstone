<div align="center">

# 📈 Bluestock Mutual Fund Analytics
### End-to-End Mutual Fund Analytics & Business Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-purple?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge&logo=checkmarx&logoColor=white)

<br>
<a href=https://github.com/sanchitbhoirr/bluestock-mf-capstone" target="_blank">
  <img src="https://img.shields.io/badge/Live%20App-View%20Streamlit%20Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Streamlit Dashboard" />
</a>
<br>

---
</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🌐 Live Web Application (Bonus Task)](#-live-web-application-bonus-task)
- [🚀 Day 1: Data Ingestion, API Integration & Quality Validation](#-day-1-data-ingestion-api-integration--quality-validation)
- [🛠️ Day 2: Data Cleaning & SQL Database Design](#️-day-2-data-cleaning--sql-database-design)

---

## 🎯 Project Overview

This repository contains the completed Capstone Project for the **Bluestock Fintech Data Analytics Internship**.

The goal of this project is to build an end-to-end Mutual Fund Analytics Platform using real-world public data from AMFI India and `mfapi.in`.

This README documents the progressive completion of daily milestones, moving from raw data ingestion to structured data engineering, analytics, dynamic Power BI Dashboards, advanced Python recommender systems, and final production automation.

**Phases Completed:** `Day 1` • `Day 2` 

**Status:** `In progress`


## 🚀 Day 1: Data Ingestion, API Integration & Quality Validation

### 1. Project Architecture & Setup
- Initialized a standard data science folder structure (`data/raw`, `data/processed`, `notebooks`, `scripts`, `sql`, `dashboard`, `reports`).
- Set up a virtual environment and installed core dependencies listed in `requirements.txt` (Pandas, Requests, NumPy, etc.).

### 2. Static Data Ingestion
- Successfully loaded 10 extensive real-world CSV datasets provided by Bluestock (comprising 40 schemes, 4.5 years of NAV history, and 87K+ transaction rows).
- Evaluated dataset schemas, shapes, and data types to prepare for downstream transformation.

### 3. Live API Integration (Live NAV Fetcher)
- Developed an automated Python script (`scripts/live_nav_fetch.py`) to interact with the public `mfapi.in` REST API.
- Dynamically fetched live NAV data for 6 critical benchmark schemes:
  - *HDFC Top 100 Direct (125497)*
  - *SBI Bluechip (119551)*
  - *ICICI Bluechip (120503)*
  - *Nippon Large Cap (118632)*
  - *Axis Bluechip (119092)*
  - *Kotak Bluechip (120841)*

### 4. Initial Exploratory Data Analysis (EDA)
- Conducted preliminary exploration of the `01_fund_master.csv` dataset.
- Extracted and mapped unique Fund Houses, Categories, Sub-categories, and Risk Grades to understand the AMFI scheme code structure.

### 5. Data Quality & Validation
- Executed a strict validation protocol to ensure cross-dataset integrity.
- Confirmed a **100% match** by validating that every AMFI scheme code present in the `fund_master` dataset flawlessly aligns with the historical records in the `nav_history` dataset.

---

## 🛠️ Day 2: Data Cleaning & SQL Database Design

### 1. Data Cleaning Pipeline (Pandas)
- **NAV History:** Parsed dates, sorted records by scheme, removed duplicates, and implemented critical forward-filling (`ffill`) logic to handle missing NAV values during weekends and market holidays.
- **Transactions:** Standardized transaction types (SIP, Lumpsum, Redemption), validated positive investment amounts, fixed date formats, and filtered valid KYC statuses.
- **Scheme Performance:** Validated numeric return values, flagged risk anomalies (e.g., negative Sharpe ratios), and enforced acceptable expense ratio ranges.
- Exported all cleaned datasets to the `data/processed/` directory.

### 2. Database Schema Design
- Designed a professional analytical **Star Schema** with dimension tables (`dim_fund`, `dim_date`) and fact tables (`fact_nav`, `fact_transactions`, `fact_performance`, `fact_aum`).
- Authored strict DDL statements (`sql/schema.sql`) defining Primary Keys and Foreign Keys for data integrity.

### 3. Data Loading (SQLAlchemy)
- Created an automated Python pipeline using `SQLAlchemy` to generate a local SQLite database (`bluestock_mf.db`).
- Iteratively mapped, transformed, and loaded tens of thousands of processed records from Pandas DataFrames directly into the structured SQL tables.

### 4. Analytical SQL Queries
- Authored 10 business-critical SQL queries (`sql/queries.sql`) to extract insights such as:
  - Top 5 Fund Houses by AUM.
  - Average NAV trends per month.
  - Total SIP Amount by Year (YoY Growth).
  - Transaction volumes distributed by Fund Category.

### 5. Documentation
- Created a comprehensive Data Dictionary (`data_dictionary.md`) documenting all tables, columns, data types, and business logic to ensure project maintainability.

---

---

## 🛠️ Execution & Setup Guide

### 1. System Deployment & Virtual Environment Setup

Initialize a shell platform inside your target workstation path, fetch the production repository, and activate the Python dependency environment:

```bash
# Clone the repository
git clone https://github.com/sanchitbhoirr/bluestock-mf-capstone?utm

cd bluestock_mf_capstone

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Automation Master Pipeline

Execute the root orchestration file. This handles dynamic absolute directory discovery, ensures structural alignment, and triggers live REST API endpoints automatically:

```bash
python run_pipeline.py
```

### 3. Initialize the Interactive Financial Robo-Advisor App

Launch the interactive terminal-based tool to evaluate mutual fund schemes dynamically against individual risk parameters:

```bash
python scripts/recommender.py
```

### 4. Review Analytical Environments & Visual Dashboards

- Navigate into the `notebooks/` workspace and execute files `01` through `05` sequentially.
- Open `dashboard/bluestock_mf_dashboard.pbix` using Power BI Desktop to explore interactive visualizations and performance insights.

---

## 📑 Final Deliverables

### Project Deliverables

- 📄 `Bluestock_MF_Capstone_Project.pdf`
- 📊 `Bluestock_MF_Presentation.pptx`
- 📈 `bluestock_mf_dashboard.pbix`
- 📑 `Final_Report.pdf`
- 🗄️ `bluestock_mf.db`
- 📋 `fund_scorecard.csv`
- 📋 `alpha_beta.csv`
- 📋 `var_cvar_reports.csv`
- 📋 `sector_hhi.csv`
- 📋 `cohort_analysis.csv`

---

## 📜 License

This project was developed as part of the **Bluestock Fintech Data Analytics Internship Capstone Project** and is intended for educational and portfolio purposes.
