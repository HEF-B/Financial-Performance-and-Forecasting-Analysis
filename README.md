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

## 7. Analysis & Metrics

<!--
  Explain what you measured and how - before you share what you found.

  WHAT GOOD LOOKS LIKE:
  Metric: "Customer Return Rate"
  Definition: "Number of transactions flagged as returns divided by total
               transactions, calculated at product-category and regional grain."
  Why It Matters: "Return rate - not sales volume - was hypothesised to
                  explain regional revenue gaps. This metric tests that hypothesis."

  WHAT TO AVOID:
  ❌ Defining a metric only in code: SUM(returns) / COUNT(transaction_id)
     That's an implementation. Write the plain-language definition here.
     Both belong in your project - the definition in the README,
     the implementation in the code.
-->

### Analytical Approach

[Describe how you approached the analysis. Were you exploring patterns? Testing a hypothesis? Building and validating a pipeline? Be honest about your method - exploratory work is valid, just call it that.]

### Key Metrics Defined

| Metric | Plain-Language Definition | Why It Matters |
|--------|--------------------------|----------------|
| `[Metric 1]` | [What it measures, in one sentence] | [What decision or question it answers] |
| `[Metric 2]` | [What it measures, in one sentence] | [What decision or question it answers] |
| `[Metric 3]` | [What it measures, in one sentence] | [What decision or question it answers] |

### Methods Used

- [e.g., Descriptive statistics - distribution, central tendency, outlier detection]
- [e.g., Trend analysis across [time period]]
- [e.g., Segmentation / group comparison by [dimension]]
- [e.g., Correlation analysis between [variable A] and [variable B]]
- [e.g., SQL window functions for [specific aggregation]]
- [e.g., Custom aggregation or transformation logic in [tool]]

---

## 8. Key Insights

<!--
  Findings + implications. Not just what happened - what it means.

  WHAT GOOD LOOKS LIKE:
  ✅ "Return rates, not sales volume, explain Region A's underperformance.
      Region A's return rate on home goods was 34% - more than double the
      company average. Revenue was not lost at the point of sale; it was
      lost post-sale through refunds. This points to a fulfilment or
      product quality issue specific to that region, not a demand problem."

  WHAT TO AVOID:
  ❌ "Region A had lower revenue than other regions in Q4."
     (That's an observation. It describes what happened.
      An insight says what it means and where to look next.)

  Aim for 3–6 insights. Quality over quantity.
-->

**Insight 1: [Short descriptive headline]**
[What you found + what it suggests. One short paragraph.]

**Insight 2: [Short descriptive headline]**
[What you found + what it suggests.]

**Insight 3: [Short descriptive headline]**
[What you found + what it suggests.]

**Insight 4 (if applicable): [Short descriptive headline]**
[What you found + what it suggests.]

---

## 9. Recommendations

<!--
  Action-oriented. Addressed to a real audience.
  Tied explicitly to the insight that supports each one.

  WHAT GOOD LOOKS LIKE:
  Priority: High
  Recommendation: "Conduct a fulfilment audit for home goods deliveries
                   in Region A - specifically investigating whether returns
                   correlate with a particular warehouse, carrier, or SKU batch."
  Based On: Insight 1 - return rate anomaly in Region A
  Owner: Operations / Supply Chain team

  WHAT TO AVOID:
  ❌ "Improve the return rate."
     (Not actionable. Doesn't say who, how, or where to start.)
  ❌ "Further analysis is needed."
     (This is a placeholder, not a recommendation.)
-->

| Priority | Recommendation | Based On | Suggested Owner |
|----------|---------------|----------|-----------------|
| High | [Specific, actionable step] | [Insight it comes from] | [Who should act] |
| Medium | [Specific, actionable step] | [Insight it comes from] | [Who should act] |
| Low | [Exploratory or longer-term suggestion] | [Insight it comes from] | [Who should act] |

---

## 10. Assumptions & Limitations

<!--
  WHAT GOOD LOOKS LIKE:
  Assumption: "Transaction records were assumed to be complete for all five regions.
               No validation was performed against source system record counts."
  Limitation: "The analysis cannot distinguish between returns initiated by
               the customer vs. returns initiated by the business (e.g., recalls).
               If business-initiated returns are concentrated in Region A, the
               return rate finding may reflect a policy decision, not a quality issue."

  WHAT TO AVOID:
  ❌ Leaving this section blank or writing "None known."
     Every project has limitations. Documenting them is a sign of
     analytical maturity - not a confession of failure.
-->

### Assumptions
- [What did you treat as true without being able to verify?]
- [What simplifications did you make for scope or feasibility?]
- [What domain rules or definitions did you accept as given?]

### Limitations
- [What gaps exist in the data?]
- [What analysis was out of scope but could affect interpretation?]
- [What would a more rigorous version of this project include?]
- [Are there known biases in the data source or collection method?]

> *The goal here is pre-emptive Q&A. What would a thoughtful skeptic push back on? Document the answer here, before they ask.*

---

## 11. Author

**Florence Braut**
- 🔗 linkedin.com/in/Florence B
- 💼 Portfolio:https://hef-b.github.io/
- 📧 dainsights@proton.me

---

