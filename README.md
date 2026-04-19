# Workforce Demand Analysis & Scheduling

A data analysis project exploring customer demand, sales trends, and staffing
patterns to support smarter scheduling and operational decisions.

Built with Python · Pandas · Matplotlib

---

## Overview

This project analyzes hourly business activity to identify peak demand periods
and evaluate how well staffing aligns with actual customer volume. The goal is
to use historical data as a foundation for simple demand forecasting and
resource planning.

---

## Dataset

A structured dataset representing hourly business activity with the following features:

| Column | Description |
|---|---|
| `date` | Date of recorded activity |
| `hour` | Hour of the day (0–23) |
| `customers` | Number of customers during that hour |
| `sales` | Total sales amount |
| `staff_scheduled` | Number of staff on shift |

---

## Project Files

| File | Description |
|---|---|
| `analysis.py` | EDA, visualizations, and baseline demand forecast |
| `scheduling_tool.py` | Hourly reporting tool with labour costs and forecasting |

---

## Project Workflow

### 1. Data Setup
Constructed and loaded a structured hourly dataset into a Pandas DataFrame for
analysis and visualization.

### 2. Exploratory Data Analysis (EDA)
- Inspected data types, column structure, and summary statistics
- Examined relationships between customers, sales, and staffing levels
- Pearson correlation between customers & sales: **0.999**
- Identified general demand patterns across the day

### 3. Data Visualization
- Line chart of customer volume by hour to identify peak periods
- Comparative visuals of sales and staffing relative to demand
- Highlights operational gaps between scheduled staff and actual activity

### 4. Demand Forecasting (Baseline)
Grouped data by hour and calculated average sales per hour to produce a
simple hourly demand baseline. This serves as a starting forecast for
estimating busy periods and informing scheduling decisions.

### 5. Workforce Reporting Tool
Standalone script that generates a formatted report including:
- Sales revenue per hour
- Labour cost (staff × $15/hr wage rate)
- Customers per hour
- Day subtotals and grand totals
- Understaffed hour alerts
- Hourly averages forecast table

---

## Key Insights

- **Evening hours (6PM)** show the highest average sales — strongest peak demand window
- **Midday hours** show lower but more consistent activity
- Staffing allocation should be weighted toward peak evening hours
- Labour costs don't scale proportionally with demand — gap identified at peak hours
- Historical averages provide a reasonable baseline for near-term planning

---

## Sample Report Output

```
  HOURLY SALES · LABOUR COST · CUSTOMERS PER HOUR REPORT
═════════════════════════════════════════════════════════════════
  Assumed hourly wage rate: $15.00 per staff member

  📅  2025-12-01
  ───────────────────────────────────────────────────────
  12:00       620.00            75.00            45
  13:00       710.00            90.00            52
  18:00     1,200.00           120.00            80
  ───────────────────────────────────────────────────────
  DAY TOTAL 2,530.00           285.00           177

═════════════════════════════════════════════════════════════════
  GRAND TOTAL 4,530.00          570.00           315
═════════════════════════════════════════════════════════════════
```

---

## Limitations

- Forecast relies on historical averages and assumes demand patterns repeat
- Small dataset (5 rows) — larger dataset across more days would improve reliability

---

## Roadmap

- [ ] Expand dataset with more historical records
- [ ] Explore advanced forecasting models (moving average, regression, Prophet)
- [ ] Build comparison layer: forecasted vs. actual sales
- [ ] Add staffing optimization recommendations based on forecast output
- [ ] Visualize labour cost vs. sales by hour

---

## Status

🟡 In Progress — actively expanding analysis and forecasting methods
