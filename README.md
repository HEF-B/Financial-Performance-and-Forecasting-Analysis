# Financial Performance and Forecasting Analysis (2015–2024)
I analyzed a decade of financial data from Norwegian non-financial companies to evaluate profitability, liquidity, and financial structure across industries—and built predictive models to measure COVID-19 impact and forecast future performance.

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Objectives](#3-objectives)
3. [Executive Summary](#2-executive-Summary)
4. [Tools & Technologies](#4-tools-&-technologies)
5. [Repository Structure](#5-repository-structure)
6. [Data Workflow](#6-data-workflow)
7. [ERD - Entity Relationship Diagram](#7-erd--entity-relationship-diagram)
8. [Analysis & Metrics](#8-analysis--metrics)
19. [Key Insights](#9-key-insights)
10. [Recommendations](#10-recommendations)
11. [Assumptions & Limitations](#11-assumptions--limitations)
12. [Author](#12-author)

1. [Project Overview](#1-project-overview)
2. [Objectives](#2-objectives)
3. [Executive Summary](#3-executive-Summary)
4. [Tools & Technologies](#tools & technologies)
5. [Repository Structure](#repository structure)
6. [Data Workflow](#data workflow)
7. [Key Metrics](#key metrics)
8. [Key Insights](#key insights)
9. [Recommendations](#recommendations)
10. [Assumptions & Limitations](#assumptions & limitations)
11. [Author](#author)

## 1. Project Overview

Understanding the long-term financial stability of the Norwegian private sector requires looking beyond surface-level financial reports. This project analyses non-financial companies over a 10-year period (2015–2024), covering major economic disruptions including COVID-19 and inflation shocks.
Norwegian businesses experienced significant volatility due to pandemic disruptions, oil price fluctuations, and rising inflation.
#### Problem Statement
Raw financial data alone does not clearly show how economic shocks affected profitability, liquidity, and leverage across industries.
#### Approach
I combined profit & loss and balance sheet data from Statistics Norway, transformed it using Power Query, and built interactive dashboards in Power BI. In addition, I developed Python-based forecasting models using pre-COVID data (2015–2019) to estimate expected “no-crisis” performance and compare it with actual outcomes.
#### Outcome
- Interactive Power BI dashboard for financial analysis 
- COVID impact analysis (actual vs expected performance) 
- Industry-level recovery insights 
- 5-year financial forecasts (2025–2029) with uncertainty range

## 2. Objectives
- Analyze trends in revenue, operating profit, and net profit (2015–2024)
- Examine changes in assets, equity, and liabilities over time
- Determine relationship between profitability and financial structure
- Quantify the impact of COVID-19 (pre, during, post periods)
- Build a predictive model to estimate no-crisis baseline performance
- Compare actual vs expected results to measure economic shock impact
- Forecast key financial indicators for 2025–2029

## 3. Executive Summary

<img width="2615" height="1487" alt="1" src="https://github.com/user-attachments/assets/f5028df6-ac35-4b2c-9170-681a2d30508f" />

---
The analysis reveals a definitive financial shock during the COVID-19 pandemic, followed by a structurally sound recovery across Norwegian industries. While profitability dipped sharply in covid, the subsequent rebound was driven by operational efficiency rather than simple revenue growth.
### Key Performance Indicators (2015–2024)
- **Resilient Profitability**, Net margins improved post-COVID as companies optimized cost structures to combat inflationary pressures.
- **Strengthened Solvency**, Equity ratios increased while leverage declined, signaling a strategic shift away from debt dependency.
- **Stable Liquidity**, Effective cash management ensured that liquidity remained stable during the crisis and improved slightly in the recovery phase.
  
Norwegian non-financial companies emerged from the pandemic period more financially resilient, characterized by improved profit retention and significantly lower financial risk profiles.


## 4. Tools & Technologies

| Category        | Tools used                              
| --------------- | ---------------------------------- |
| Data Storage    | CSV (SSB Statbank)                 |
| Data Processing | Excel, Power Query                 |
| Analysis        | Python (linear regression) |
| Visualization   | Power BI                           |
| Version Control | GitHub                             |
| Documentation   | Markdown                           |


## 5. Repository Structure

```
financial-performance-analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── scripts/
│   ├── global_impact_analysis.py
│   ├── industrial_impact.py
│   ├── forecasting.py
│
├── reports/
│   └── Project Report.pdf
│
├── visuals/
│   └── dashboard screenshots/
│
├── pbix/
│   └── Industry Financials Dashboard.pbix
│   └── Predictive Financial Analysis.pbix
└── README.md

```


## 6. Data Workflow

```
Source
Annual financial statement data (2015–2024) for Norwegian non-financial companies sourced from SSB Statbank:
- Profit & Loss (Table 08120)
- Balance Sheet (Table 08121)
        ↓
Ingestion
- Data exported from SSB and loaded into Excel  
- Imported into Power BI via Power Query  
- Final modeling dataset exported and used in Python (PyCharm)
        ↓
Cleaning
- Removed unnecessary and empty columns in balance sheet dataset  
- Handled missing values using fill-down techniques  
- Filtered dataset to relevant period (2015–2024)  
- Standardized structure across both datasets  
        ↓
Transformation
- Converted wide-format datasets into structured long format  
  (each row = Year × Industry × Indicator)  
- Unpivoted financial indicators into attribute–value pairs  
- Created:
  - Fact tables: `fact_pnl_long`, `fact_bs_long`  
  - Dimension tables: `dim_pnl`, `dim_bs`  
- Built a time table using distinct year values  
- Added grouped indicator categories using conditional columns  
        ↓
Data Integration
- Merged Profit & Loss and Balance Sheet datasets using:
  - Keys: Year + Industry  
- Created a unified Modeling Table for analysis and prediction  
- Selected key variables:
  - Revenue, OPEX, Payroll, Depreciation, EBIT, Net Profit  
  - Total Assets, Equity, Liabilities, Liquidity indicators  
        ↓
Analysis & Modeling
- Power BI:
  - Built DAX measures for KPIs and period comparisons (Pre, COVID, Post)  
- Python:
  - Applied linear regression on pre-COVID data (2015–2019)  
  - Generated “no-crisis” baseline predictions  
  - Calculated deviation between actual vs expected values  
  - Built 5-year forecasts (2025–2029) with uncertainty range  
        ↓
Output
- Interactive Power BI dashboard (financial KPIs & trends)  
- COVID impact analysis (Actual vs Expected)  
- Industry-level recovery insights  
- Forecasting outputs (central, low, high scenarios)  
- Final PDF report documenting methodology and findings  

```

## 7. Key Metrics

| Metric | Definition | Why It Matters |
|--------|--------------------------|----------------|
| Net Profit Margin | Net profit as % of revenue | Measures profitability efficiency |
| Equity Ratio | Equity / Total Assets| Indicates financial stability |
| Leverage Ratio | Liabilities / Equity | Measures financial risk|
| Liquidity Ratio | Current assets vs liabilities| Indicates short-term solvency |
| Deviation % | (Actual - Expected) | Expected	Quantifies crisis impact|

### Methods Used
- Time-series trend analysis (2015–2024)
- Pre vs During vs Post COVID comparison
- Industry segmentation analysis
- Linear regression (baseline modeling)
- Forecasting with uncertainty bands (±15%)

## 8. Key Insights

<!--
  c

Revenue and profitability dropped sharply in 2020, followed by a rapid recovery that exceeded pre-COVID levels by 2021. This pattern indicates strong resilience across Norwegian industries, supported by effective cost control and external support measures. The trend suggests that the crisis impact was temporary rather than structural, with most sectors recovering quickly.
-->

#### **COVID-19 Shock and Recovery**
<img width="2689" height="1475" alt="Skjermbilde 2026-02-25 002944" src="https://github.com/user-attachments/assets/9c3ee2fe-72b6-4e0a-91ed-86884110b39f" />

Revenue and profitability dropped sharply in 2020, followed by a rapid recovery that exceeded pre-COVID levels by 2021. This pattern indicates strong resilience across Norwegian industries, supported by effective cost control and external support measures. The trend suggests that the crisis impact was temporary rather than structural, with most sectors recovering quickly.


#### **COVID-19 Shock and Recovery**
<img width="2648" height="1492" alt="Skjermbilde 2026-02-25 003228" src="https://github.com/user-attachments/assets/c31d4c87-3d94-4082-9819-90a18f70d993" />



#### **COVID-19 Shock and Recovery**
<img width="2240" height="1275" alt="4" src="https://github.com/user-attachments/assets/f0ad9df4-c262-4b6b-8265-3f58a09e8106" />


#### **COVID-19 Shock and Recovery**
<img width="2659" height="1492" alt="Skjermbilde 2026-02-25 005119" src="https://github.com/user-attachments/assets/08819b5f-3a88-4fe3-9de8-6c031a2cc1e9" />


#### **COVID-19 Shock and Recovery**
<img width="2651" height="1370" alt="Skjermbilde 2026-02-25 003626" src="https://github.com/user-attachments/assets/e8efb729-5600-4d44-a933-62770c25b567" />



## 9. Recommendations

| Priority | Recommendation | Based On | Suggested Owner |
|----------|---------------|----------|-----------------|
| High | Monitor industries with slow recovery (e.g. education) | Uneven recovery trends | Policy makers |
| High | Use deviation analysis to identify financial risk sectors | Crisis impact analysis | Banks / Analysts |
| Medium | Benchmark company performance against industry trends | Industry comparison insights | Business managers |
| Low | Improve forecasting models with more advanced ML methods | Model limitations | Data teams |

## 10. Assumptions & Limitations

### Assumptions
- Pre-COVID period (2015–2019) represents a stable baseline
- Linear regression adequately captures trend direction
- Financial ratios reflect real economic performance
  
### Limitations
- Data is at an industry-aggregate level, which may mask individual company successes or failures.
- The forecasting model does not account for unforeseen "Black Swan" geopolitical events in 2025; it relies strictly on historical trends.
- Forecasts include uncertainty and are not guaranteed outcomes
- External factors (policy changes, global markets) not fully included


## 11. Author

**Florence Braut**
- 🔗 linkedin.com/in/Florence B
- 💼 Portfolio:https://hef-b.github.io/
- 📧 dainsights@proton.me

