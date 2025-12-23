# Workforce Demand Analysis

This project explores customer demand and staffing patterns using basic data analysis and visualization.

Status: In progress.

# Workforce Demand Analysis & Scheduling

## Overview
This project explores customer demand, sales trends, and staffing patterns using basic data analysis and visualization techniques. The goal is to better understand when demand is highest and how historical data can support scheduling and operational decisions.

---

## Step 1: Data Setup

In this step, I created a structured dataset representing hourly business activity.  
The dataset includes:
- Date
- Hour of the day
- Number of customers
- Total sales
- Staff scheduled

The data was loaded into a Pandas DataFrame to allow for analysis and visualization.

---

## Step 2: Exploratory Data Analysis

I explored the dataset to understand its structure and basic characteristics.  
This included:
- Inspecting column names and data types
- Reviewing summary statistics such as averages and ranges
- Examining relationships between customers, sales, and staffing levels

This step helped identify general demand patterns and confirmed that the data was suitable for further analysis.

---

## Step 3: Data Visualization

In this step, I visualized customer demand across different hours of the day.  
Using a line chart, I plotted customer volume by hour to identify peak demand periods.

Additional visualization techniques were used to compare sales and staffing levels relative to demand.  
These charts make it easier to see trends and understand how workload changes throughout the day.

---

## Step 4: Simple Demand Forecasting

In this step, I created a basic demand forecast using historical data.  
I grouped the dataset by hour and calculated the average sales for each hour.  
This produces a summarized view of typical sales patterns throughout the day.

The resulting averages can be used as a simple forecast, assuming future days follow similar demand trends.  
This approach provides a clear baseline for understanding when higher sales are likely to occur and can support staffing and scheduling decisions.

---

## Project Status
This project is currently in progress and may be expanded with additional analysis or forecasting techniques in the future.
