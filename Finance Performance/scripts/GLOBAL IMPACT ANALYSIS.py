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

    RECOVERY_THRESHOLD = -0.05

    indicators = [
        'Revenue', 'Operating expences', 'Raw materials and consumables used',
        'Payroll expence', 'Depreciation and write down of tangible and intangible fixed assets',
        'Operating profit', 'Financial items, net', 'Net profit',
        'Fixed assets', 'Current assets', 'Cash and bank deposits etc',
        'Total assets', 'Equity', 'Liabilities', 'Short-term liabilities',
        'Number of enterprises'
    ]

    macro_df = df.groupby('Years')[indicators].sum().reset_index()

    # TABLE 1: GLOBAL IMPACT ANALYSIS (ALL INDUSTRIES)

    table_1_data = []

    for col in indicators:
        # 1. Baseline: 2015-2019 Mean
        baseline_data = macro_df[macro_df['Years'] <= 2019]
        baseline_val = baseline_data[col].mean()

        # 2. Actual COVID Crisis (2020-2024) Mean
        crisis_data = macro_df[(macro_df['Years'] >= 2020) & (macro_df['Years'] <= 2024)]
        actual_crisis_val = crisis_data[col].mean()

        # 3. Expected if no COVID crisis
        years_baseline = baseline_data['Years'].values
        vals_baseline = baseline_data[col].values

        slope, intercept = np.polyfit(years_baseline, vals_baseline, 1)

        crisis_years = np.array([2020, 2021, 2022, 2023, 2024])
        expected_vals = (slope * crisis_years) + intercept
        expected_mean_val = expected_vals.mean()

        # 4. Deviation
        deviation_val = actual_crisis_val - expected_mean_val
        deviation_pct = (deviation_val / expected_mean_val) * 100 if expected_mean_val != 0 else 0

        table_1_data.append({
            'Indicator': col,
            'Baseline (2015-2019)': round(baseline_val, 0),
            'Actual Crisis (2020-2024)': round(actual_crisis_val, 0),
            'Expected (No Crisis)': round(expected_mean_val, 0),
            'Deviation (Value)': round(deviation_val, 0),
            'Deviation (%)': f"{round(deviation_pct, 1)}%"
        })
        table_1 = pd.DataFrame(table_1_data)

        print("\n" + "=" * 110)
        print("TABLE 1: GLOBAL IMPACT ANALYSIS (ALL INDUSTRIES SUMMED)")
        print("=" * 110)
        print(table_1.to_string(index=False))


table_1.to_csv('Global_Impact_Analysis.csv', index=False)
print("\n[SUCCESS] Table 1 has been saved as 'Global_Impact_Analysis.csv'")
