# Financial Performance and Forecasting Analysis (2015–2024)
I analyzed a decade of financial data from Norwegian non-financial companies to evaluate profitability, liquidity, and financial structure across industries—and built predictive models to measure COVID-19 impact and forecast future performance.

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Objectives](#2-objectives)
3. [Executive Summary](#3-executive-Summary)
4. [Tools & Technologies](#4-tools--technologies)
5. [Repository Structure](#5-repository-structure)
6. [Data Workflow](#6-data-workflow)
7. [Key Metrics](#7-key-metrics)
8. [Key Insights](#8-key-insights)
9. [Recommendations](#9-recommendations)
10. [Assumptions & Limitations](#10-assumptions--limitations)
11. [Author](#11-author)

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
│
├── visuals/
│   └── dashboard screenshots/
│
│
├── pbix/
│   └── Industry Financials Dashboard.pbix
│   └── Predictive Financial Analysis.pbix
│
│
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

#### **Financial Performance**
<img width="2689" height="1475" alt="Skjermbilde 2026-02-25 002944" src="https://github.com/user-attachments/assets/9c3ee2fe-72b6-4e0a-91ed-86884110b39f" />

**Profit Recovery Driven by Structural Cost Efficiency**

**Pattern:** Revenue and operating expenses declined during COVID-19, but in the post-COVID period, profit grew at a faster rate than both, with a visibly widening gap between revenue and costs.

**Interpretation:** The divergence between revenue and operating expenses indicates that companies improved cost structures during the crisis reducing or optimizing expenses and maintained this efficiency during recovery.

**Impact:** Profit growth is being driven by structural efficiency rather than top-line expansion. This suggests more resilient and scalable operations, positioning companies to sustain profitability even under future economic pressure.

**Post-COVID Strengthening of Financial Structure**

**Pattern:** Assets, liabilities, and equity declined during the COVID-19 period, followed by a strong recovery, with equity growing at a more stable pace relative to liabilities.

**Interpretation:** During the crisis, companies adjusted balance sheets by limiting growth and preserving capital. In the recovery phase, equity accumulation outpaced reliance on debt, indicating a shift toward stronger internal financing.

**Impact:** The post-COVID period reflects a structurally stronger financial position, with improved balance sheet resilience and reduced dependence on leverage, lowering overall financial risk.

---
#### **COVID-19 Shock and Fast Recovery**
<img width="2648" height="1492" alt="Skjermbilde 2026-02-25 003228" src="https://github.com/user-attachments/assets/c31d4c87-3d94-4082-9819-90a18f70d993" />

**Pattern:** Revenue, EBIT, and Net Profit dropped clearly in 2020, then bounced back quickly and even exceeded pre-COVID levels by 2021–2022.

**Interpretation:** All key metrics falling at the same time shows how widespread the impact was. But the quick rebound suggests companies adapted fast and were supported during the crisis.

**Impact:** The downturn didn’t last long. Most companies recovered quickly and returned to growth, which points to a strong and resilient business environment.

---
#### **Financial Stability Varies Significantly Across Industries**
<img width="2240" height="1275" alt="4" src="https://github.com/user-attachments/assets/f0ad9df4-c262-4b6b-8265-3f58a09e8106" />

**Pattern:** 
- **Revenue:** Wholesale trade (~17M) and mining (~13M) generate the highest revenues, followed by manufacturing (~8M). However, manufacturing also carries high liabilities relative to its size.
- **Profitability Efficiency:** Real estate and mining hold the largest asset bases, while sectors such as education and other services operate with low assets, equity, and margins.
- **Financial Stability:** Real estate achieves the highest net margins and holds strong equity levels (>15M), despite not being the top revenue generator. Smaller or niche categories also show disproportionately high margins.

**Interpretation:**
- High-revenue industries are often capital-intensive and require significant ongoing investment, leading to higher financial obligations and risk exposure.
- Profitability is driven more by business model efficiency than by revenue scale. Asset-based sectors like real estate benefit from stable income streams and lower operating costs.
- Capital-intensive industries build financial buffers through assets, while service-based sectors operate with limited reserves and higher vulnerability to shocks.
  
**Impact:**
- Revenue alone is not a reliable indicator of financial health. High-revenue sectors like manufacturing may face tighter margins and higher risk, requiring closer monitoring of leverage and cost structure.
- High-margin sectors represent more sustainable values. Investors and decision-makers should prioritize efficiency metrics (e.g., margins, returns) over revenue size when assessing performance.
- Financial resilience is uneven across industries. Asset-heavy sectors are better positioned to absorb economic shocks, while smaller service sectors may require external support during downturns.

---
#### **Uneven Industry Recovery Driven by Structural Differences**
<img width="2659" height="1492" alt="Skjermbilde 2026-02-25 005119" src="https://github.com/user-attachments/assets/08819b5f-3a88-4fe3-9de8-6c031a2cc1e9" />

**Pattern:** While most industries recovered by 2021, recovery speed varied significantly. Real estate, mining, and agriculture exceeded expected performance (+17% to +34%), whereas education (-8.9%), administrative services (-5.6%), and hospitality-related sectors remained below baseline and recovered later (2022–2023).

**Interpretation:** Asset-heavy and capital-driven industries benefited from rising asset values and stable demand, while service-based sectors dependent on physical interaction faced prolonged disruption and slower demand recovery.

**Impact:** Recovery is structurally uneven across industries, indicating that financial resilience depends on sector characteristics. This suggests that risk assessment, investment decisions, and policy support should be industry-specific rather than broadly applied.

---
#### **Actual Performance vs Forecast**
<img width="2651" height="1370" alt="Skjermbilde 2026-02-25 003626" src="https://github.com/user-attachments/assets/e8efb729-5600-4d44-a933-62770c25b567" />

**Pattern:** Across most indicators, the actual 2024 values follow the same upward trend as the forecast, but stay slightly below the expected (no-crisis) levels especially for total assets, fixed assets, and equity.

**Interpretation:** The overall direction shows that companies recovered and continued to grow, but not fully at the pace predicted without COVID. The gap suggests that some long-term effects of the crisis are still present, particularly in capital growth.

**Impact:** While the recovery is strong, it is not fully complete. This indicates that businesses are on a solid growth path, but still have some ground to cover to reach their full expected potential.

---
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

