import pandas as pd
import numpy as np

path = "Modeling Table.csv"
df = pd.read_csv(path)
print(df.head())

df.columns = df.columns.str.strip()
if 'years' in df.columns:
    df.rename(columns={'years': 'Years'}, inplace=True)


# TABLE 2: INDUSTRY-SPECIFIC IMPACT & FORECAST

industries = df['Industries'].unique()
table_2_data = []

for ind in industries:
    ind_df = df[df['Industries'] == ind].sort_values('Years')

    # A. Baseline (2015-2019)
    baseline_df = ind_df[ind_df['Years'] <= 2019]
    baseline_val = baseline_df['Revenue'].mean()

    # B. Actual Crisis (2020-2024)
    crisis_df = ind_df[(ind_df['Years'] >= 2020) & (ind_df['Years'] <= 2024)]
    actual_crisis_val = crisis_df['Revenue'].mean()

    # C. Expected Trend (Linear Regression based on 15-19)
    if len(baseline_df) >= 3:
        m, b = np.polyfit(baseline_df['Years'], baseline_df['Revenue'], 1)
        expected_20_24 = np.mean([m * yr + b for yr in range(2020, 2025)])
    else:
        expected_20_24 = baseline_val

    # D. Deviation
    deviation_val = actual_crisis_val - expected_20_24
    dev_pct = (deviation_val / expected_20_24 * 100) if expected_20_24 != 0 else 0

    # E. Recovery Year (First year >= 2021 where Revenue >= 2019 Revenue)
    rev_2019 = ind_df[ind_df['Years'] == 2019]['Revenue'].values
    rev_2019_val = rev_2019[0] if len(rev_2019) > 0 else 0

    recovery_year = "Not Yet"
    for yr in [2021, 2022, 2023, 2024]:
        yr_rev = ind_df[ind_df['Years'] == yr]['Revenue'].values
        if len(yr_rev) > 0 and yr_rev[0] >= rev_2019_val:
            recovery_year = str(yr)
            break

    # F. Forecast (2025-2029) - 5 Year Total
    recovery_period = ind_df[ind_df['Years'] >= 2021]
    if len(recovery_period) >= 2:
        m_f, b_f = np.polyfit(recovery_period['Years'], recovery_period['Revenue'], 1)
        forecast_total = sum([m_f * yr + b_f for yr in range(2025, 2030)])
    else:
        forecast_total = actual_crisis_val * 5  # Simple flat fallback

    table_2_data.append({
        'Industry': ind,
        'Baseline (2015-2019)': round(baseline_val, 0),
        'Actual Crisis (2020-2024)': round(actual_crisis_val, 0),
        'Expected (No Crisis)': round(expected_20_24, 0),
        'Deviation (Val)': round(deviation_val, 0),
        'Deviation (%)': f"{round(dev_pct, 1)}%",
        'Recovery Year': recovery_year,
        'Forecast 2025-2029 (Total)': round(max(0, forecast_total), 0)
    })

table_2 = pd.DataFrame(table_2_data)

table_2.to_csv("Industry_Impact_Analysis.csv", index=False)
print('\n[SUCCESS] Table 2 saved as "Industry_Impact_Analysis.csv"')

print("\n" + "=" * 130)
print("TABLE 2: INDUSTRY-SPECIFIC IMPACT & RECOVERY ANALYSIS")
print("=" * 130)
print(table_2.to_string(index=False))