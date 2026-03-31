"""
Workforce Demand & Forecasting Tool
Tracks and compares hourly sales, labour costs, and customers per hour
across a given time period, broken down by day with totals.
"""

import pandas as pd

# ── 1. DATA SETUP ─────────────────────────────────────────────────────────────
# Source data: matches the structure from the original notebook.
# Each row = one hour of activity on a given day.
data = {
    "date": [
        "2025-12-01", "2025-12-01", "2025-12-01",
        "2025-12-02", "2025-12-02",
    ],
    "hour": [12, 13, 18, 12, 18],
    "customers": [45, 52, 80, 48, 90],
    "sales": [620, 710, 1200, 650, 1350],
    "staff_scheduled": [5, 6, 8, 5, 9],
}

df = pd.DataFrame(data)

# ── 2. CALCULATE MISSING METRICS ──────────────────────────────────────────────

# Labour cost: staff scheduled × hourly wage rate (assumed $15/hr per staff member).
# Each row already represents exactly one hour, so no further time multiplier needed.
HOURLY_RATE = 15.00  # $ per staff member per hour

df["labour_cost"] = df["staff_scheduled"] * HOURLY_RATE

# Customers per hour: the dataset is already at hourly granularity,
# so the 'customers' column IS customers per hour.
df["customers_per_hour"] = df["customers"]

# ── 3. BUILD THE HOURLY DETAIL TABLE ──────────────────────────────────────────
detail = df[["date", "hour", "sales", "labour_cost", "customers_per_hour"]].copy()
detail.columns = ["Date", "Hour", "Sales ($)", "Labour Cost ($)", "Customers/Hr"]
detail["Hour"] = detail["Hour"].apply(lambda h: f"{h:02d}:00")

# ── 4. ASSEMBLE REPORT: DETAIL ROWS + DAY TOTALS + GRAND TOTAL ───────────────
SEP = "─" * 65

report_lines = []
report_lines.append("\n" + "═" * 65)
report_lines.append("  HOURLY SALES · LABOUR COST · CUSTOMERS PER HOUR REPORT")
report_lines.append("═" * 65)
report_lines.append(f"  Assumed hourly wage rate: ${HOURLY_RATE:.2f} per staff member")
report_lines.append("═" * 65 + "\n")

# Column header
header = f"{'Hour':<8}{'Sales ($)':>12}{'Labour Cost ($)':>18}{'Customers/Hr':>14}"
report_lines.append(header)
report_lines.append(SEP)

grand_sales = 0
grand_labour = 0
grand_customers = 0

for date, group in detail.groupby("Date", sort=True):
    report_lines.append(f"\n  📅  {date}")
    report_lines.append("  " + "─" * 55)

    day_sales = 0
    day_labour = 0
    day_customers = 0

    for _, row in group.iterrows():
        line = (
            f"  {row['Hour']:<8}"
            f"{row['Sales ($)']:>10,.2f}"
            f"{row['Labour Cost ($)']:>16,.2f}"
            f"{row['Customers/Hr']:>14.0f}"
        )
        report_lines.append(line)
        day_sales += row["Sales ($)"]
        day_labour += row["Labour Cost ($)"]
        day_customers += row["Customers/Hr"]

    report_lines.append("  " + "─" * 55)
    day_total_line = (
        f"  {'DAY TOTAL':<8}"
        f"{day_sales:>10,.2f}"
        f"{day_labour:>16,.2f}"
        f"{day_customers:>14.0f}"
    )
    report_lines.append(day_total_line)

    grand_sales += day_sales
    grand_labour += day_labour
    grand_customers += day_customers

report_lines.append("\n" + "═" * 65)
grand_total_line = (
    f"  {'GRAND TOTAL':<8}"
    f"{grand_sales:>10,.2f}"
    f"{grand_labour:>16,.2f}"
    f"{grand_customers:>14.0f}"
)
report_lines.append(grand_total_line)
report_lines.append("═" * 65)

report_text = "\n".join(report_lines)
print(report_text)

# ── 5. HOURLY AVERAGES FORECAST (completing the original groupby logic) ────────
print("\n\n" + "═" * 65)
print("  HOURLY AVERAGES (Simple Demand Forecast Baseline)")
print("═" * 65)

forecast = df.groupby("hour").agg(
    avg_sales=("sales", "mean"),
    avg_labour_cost=("labour_cost", "mean"),
    avg_customers_per_hour=("customers_per_hour", "mean"),
).reset_index()

forecast["hour_label"] = forecast["hour"].apply(lambda h: f"{h:02d}:00")

print(f"\n{'Hour':<8}{'Avg Sales ($)':>15}{'Avg Labour ($)':>16}{'Avg Cust/Hr':>13}")
print("─" * 55)
for _, row in forecast.iterrows():
    print(
        f"  {row['hour_label']:<8}"
        f"{row['avg_sales']:>13,.2f}"
        f"{row['avg_labour_cost']:>14,.2f}"
        f"{row['avg_customers_per_hour']:>13.1f}"
    )
print("─" * 55)
print("\n✅  Script completed successfully.\n")
