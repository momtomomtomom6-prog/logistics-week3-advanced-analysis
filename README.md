# Week 3 - Advanced Data Analysis and Visualization in Logistics

**Student:** Aditya Kumar Yadav

## Project Overview

This project performs exploratory data analysis and visualization on a
hypothetical logistics dataset. The objective is to understand delivery
performance, shipment volume, transportation costs, route distance, fuel
cost, and on-time delivery.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib

## Dataset

The dataset is simulated specifically for this educational task. It
contains 180 shipment records and the following variables:

- Shipment ID
- Region
- Transport Mode
- Shipment Volume (kg)
- Distance (km)
- Delivery Time (days)
- Delay (days)
- Transport Cost
- Fuel Cost
- Orders
- On-Time status

## EDA Performed

The analysis includes:

- Dataset structure inspection
- Mean and median calculations
- Distribution analysis
- Grouped transport-mode analysis
- Regional analysis
- Correlation analysis
- Operational KPI analysis

## Visualizations

Seven visualizations are included in the `visualizations/` folder:

1. Delivery Time Distribution
2. Average Delivery Time by Transport Mode
3. Shipment Volume vs Transport Cost
4. Distance vs Delivery Time
5. Average Transport Cost by Region
6. Correlation Matrix
7. On-Time Delivery Rate by Transport Mode

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/week3_analysis.py
```

## Key Results From the Simulated Dataset

- Average delivery time: 5.16 days
- Average transport cost: 18528.66
- Total transport cost: 3335158.75
- Average shipment volume: 272.97 kg
- Overall on-time delivery rate: 43.89%

These values are based on the simulated dataset and are intended for
educational analysis rather than real-world operational decisions.

## Business Insights

1. Delivery time differs across transportation modes, so service-level
   requirements should be considered along with cost.
2. Shipment volume and transport cost can be examined together to support
   capacity and cost planning.
3. Route distance is an important factor when evaluating delivery time.
4. Regional cost comparisons can highlight areas for operational review.
5. On-time delivery is an important KPI for monitoring customer service.

## Recommendations

- Monitor slow transport modes and investigate operational bottlenecks.
- Compare cost and delivery performance before selecting transport modes.
- Review long-distance routes for better scheduling and capacity planning.
- Investigate high-cost regions.
- Use data dashboards to monitor delivery time, cost, volume, and on-time rate.

## Author

Aditya Kumar Yadav
