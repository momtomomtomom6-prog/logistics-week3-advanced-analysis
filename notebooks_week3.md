# Week 3 - Advanced Data Analysis and Visualization in Logistics

**Student:** Aditya Kumar Yadav

## Objective

Explore a hypothetical logistics dataset, calculate descriptive statistics
and correlations, create visualizations, and derive operational insights.

## Dataset Variables

- Shipment_ID
- Region
- Transport_Mode
- Shipment_Volume_kg
- Distance_km
- Delivery_Time_days
- Delay_days
- Transport_Cost
- Fuel_Cost
- Orders
- On_Time

## Load Data

```python
import pandas as pd

df = pd.read_csv("../data/logistics_week3_dataset.csv")
df.head()
```

## Exploratory Data Analysis

```python
print(df.shape)
print(df.info())
print(df.describe().T)
```

### Central Tendency

```python
numeric = [
    "Shipment_Volume_kg",
    "Distance_km",
    "Delivery_Time_days",
    "Transport_Cost",
    "Fuel_Cost",
    "Orders",
]

print(df[numeric].mean())
print(df[numeric].median())
```

### Correlation

```python
print(df[numeric].corr().round(2))
```

## Visualizations

The project creates:

1. Delivery-time distribution
2. Average delivery time by transport mode
3. Shipment volume vs transport cost
4. Distance vs delivery time
5. Average transport cost by region
6. Correlation matrix
7. On-time delivery rate by transport mode

Run the complete script:

```bash
python src/week3_analysis.py
```

## Interpretation

The delivery-time distribution shows the overall spread of operational
performance. Comparing transport modes helps identify which modes are
faster or slower. The volume-cost relationship helps evaluate whether
larger shipments are associated with higher transport spending. The
distance-delivery plot helps identify the effect of route length on delivery
time. Regional cost comparison can reveal locations that may need cost
optimization. The correlation matrix provides a quick view of relationships
among operational variables.

## Recommendations

- Monitor transport modes with slower delivery performance.
- Compare cost and service level before selecting a transport mode.
- Review long-distance routes for scheduling and capacity improvements.
- Investigate regions with higher average transportation costs.
- Use shipment-volume information for capacity planning.
- Track on-time delivery as a core logistics KPI.
