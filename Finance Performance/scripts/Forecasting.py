import pandas as pd
import numpy as np

path = "Modeling Table.csv"
df = pd.read_csv(path)
print(df.head())

df.columns = df.columns.str.strip()
if 'years' in df.columns:
    df.rename(columns={'years': 'Years'}, inplace=True)

PRE_YEARS = [2015, 2016, 2017, 2018, 2019]
COVID_YEARS = [2020, 2021, 2022, 2023, 2024]
POST_YEARS = [2022, 2023, 2024]
FORECAST_YEARS = [2025, 2026, 2027, 2028, 2029]

INDICATORS = [
    "Revenue",
    "Operating expences",
    "Raw materials and consumables used",
    "Payroll expence",
    "Depreciation and write down of tangible and intangible fixed assets",
    "Operating profit",
    "Financial items, net",
    "Net profit",
    "Fixed assets",
    "Current assets",
    "Cash and bank deposits etc",
    "Total assets",
    "Equity",
    "Liabilities",
    "Short-term liabilities",
    "Number of enterprises"
]

macro_df = df.groupby("Years")[INDICATORS].sum().reset_index()

# TABLE 3: Forecast 2025–2029

baseline_years = [2022, 2023, 2024]
forecast_year = 2029
uncertainty_margin = 0.15

table_3_data = []

for col in INDICATORS:
    # A) 2024 actual
    val_2024 = macro_df.loc[macro_df["Years"] == 2024, col].values[0]

    # B) Fit a simple line using 2022–2024
    baseline_data = macro_df[macro_df["Years"].isin(baseline_years)]

    # slope (m) and intercept (b)
    m, b = np.polyfit(baseline_data["Years"], baseline_data[col], 1)

    # C) 2029 central
    val_2029_central = m * forecast_year + b

    # D) low/high
    val_2029_low = val_2029_central * (1 - uncertainty_margin)
    val_2029_high = val_2029_central * (1 + uncertainty_margin)

    # Baseline % per year
    baseline_pct = (m / val_2024) * 100 if val_2024 != 0 else np.nan

    table_3_data.append({
        "Indicator (all industries summed)": col,
        "2024 actual": round(val_2024, 0),
        "2029 central": round(val_2029_central, 0),
        "2029 low": round(val_2029_low, 0),
        "2029 high": round(val_2029_high, 0),
        "post-COVID baseline (%)": round(baseline_pct, 2)
    })

table_3 = pd.DataFrame(table_3_data)

table_3.to_csv("FORECASTS 2025–2029.csv", index=False)
print('\n[SUCCESS] Table 3 saved as "Forecasts 2025-2029.csv"')

print("\n" + "="*120)
print("TABLE 3: FORECASTS 2025–2029 (ALL INDUSTRIES SUMMED)")
print("Baseline: 2022-2024 Recovery Trend")
print("="*120)
print(table_3.to_string(index=False))