"""
Week 3 - Advanced Data Analysis and Visualization in Logistics
Student: Aditya Kumar Yadav

This script simulates a hypothetical logistics dataset, performs EDA,
calculates descriptive statistics/correlations, and creates seven
business-oriented visualizations.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "logistics_week3_dataset.csv"
OUTPUT_DIR = ROOT / "visualizations"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    return pd.read_csv(DATA_FILE)


def run_eda(df):
    numeric = [
        "Shipment_Volume_kg",
        "Distance_km",
        "Delivery_Time_days",
        "Delay_days",
        "Transport_Cost",
        "Fuel_Cost",
        "Orders",
    ]

    print("\n--- SHAPE ---")
    print(df.shape)

    print("\n--- DESCRIPTIVE STATISTICS ---")
    print(df[numeric].describe().T)

    print("\n--- CORRELATION MATRIX ---")
    print(df[numeric].corr().round(2))

    print("\n--- MODE SUMMARY ---")
    mode_summary = df.groupby("Transport_Mode").agg(
        Shipments=("Shipment_ID", "count"),
        Avg_Delivery_Days=("Delivery_Time_days", "mean"),
        Avg_Transport_Cost=("Transport_Cost", "mean"),
        On_Time_Rate=("On_Time", "mean"),
    )
    mode_summary["On_Time_Rate"] *= 100
    print(mode_summary.round(2))

    print("\n--- REGION SUMMARY ---")
    region_summary = df.groupby("Region").agg(
        Shipments=("Shipment_ID", "count"),
        Avg_Delivery_Days=("Delivery_Time_days", "mean"),
        Avg_Cost=("Transport_Cost", "mean"),
        On_Time_Rate=("On_Time", "mean"),
    )
    region_summary["On_Time_Rate"] *= 100
    print(region_summary.round(2))


def create_visualizations(df):
    # 1. Distribution
    plt.figure()
    plt.hist(df["Delivery_Time_days"], bins=18)
    plt.title("Distribution of Delivery Times")
    plt.xlabel("Delivery Time (days)")
    plt.ylabel("Number of Shipments")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "01_delivery_time_distribution.png", dpi=160)
    plt.close()

    # 2. Mode comparison
    mode = df.groupby("Transport_Mode")["Delivery_Time_days"].mean()
    plt.figure()
    plt.bar(mode.index, mode.values)
    plt.title("Average Delivery Time by Transport Mode")
    plt.xlabel("Transport Mode")
    plt.ylabel("Average Delivery Time (days)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "02_delivery_by_mode.png", dpi=160)
    plt.close()

    # 3. Volume vs cost
    plt.figure()
    for transport_mode in df["Transport_Mode"].unique():
        subset = df[df["Transport_Mode"] == transport_mode]
        plt.scatter(
            subset["Shipment_Volume_kg"],
            subset["Transport_Cost"],
            label=transport_mode,
            alpha=0.65,
        )
    plt.title("Shipment Volume vs Transport Cost")
    plt.xlabel("Shipment Volume (kg)")
    plt.ylabel("Transport Cost")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "03_volume_vs_cost.png", dpi=160)
    plt.close()

    # 4. Distance vs delivery
    plt.figure()
    plt.scatter(
        df["Distance_km"],
        df["Delivery_Time_days"],
        alpha=0.65,
    )
    z = np.polyfit(
        df["Distance_km"],
        df["Delivery_Time_days"],
        1,
    )
    p = np.poly1d(z)
    xs = np.linspace(
        df["Distance_km"].min(),
        df["Distance_km"].max(),
        100,
    )
    plt.plot(xs, p(xs))
    plt.title("Distance vs Delivery Time")
    plt.xlabel("Distance (km)")
    plt.ylabel("Delivery Time (days)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "04_distance_vs_delivery.png", dpi=160)
    plt.close()

    # 5. Region cost
    region = df.groupby("Region")["Transport_Cost"].mean()
    plt.figure()
    plt.bar(region.index, region.values)
    plt.title("Average Transport Cost by Region")
    plt.xlabel("Region")
    plt.ylabel("Average Transport Cost")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "05_cost_by_region.png", dpi=160)
    plt.close()

    # 6. Correlation matrix
    cols = [
        "Shipment_Volume_kg",
        "Distance_km",
        "Delivery_Time_days",
        "Transport_Cost",
        "Fuel_Cost",
        "Orders",
    ]
    corr = df[cols].corr()
    plt.figure(figsize=(8, 6))
    plt.imshow(corr.values, aspect="auto")
    plt.colorbar(label="Correlation")
    plt.xticks(
        range(len(cols)),
        cols,
        rotation=45,
        ha="right",
    )
    plt.yticks(range(len(cols)), cols)
    plt.title("Correlation Matrix of Key Logistics Variables")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "06_correlation_matrix.png", dpi=160)
    plt.close()

    # 7. On-time rate
    on_time = (
        df.groupby("Transport_Mode")["On_Time"]
        .mean()
        .mul(100)
    )
    plt.figure()
    plt.bar(on_time.index, on_time.values)
    plt.title("On-Time Delivery Rate by Transport Mode")
    plt.xlabel("Transport Mode")
    plt.ylabel("On-Time Rate (%)")
    plt.ylim(0, 100)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "07_on_time_by_mode.png", dpi=160)
    plt.close()


if __name__ == "__main__":
    data = load_data()
    run_eda(data)
    create_visualizations(data)
    print("\nAnalysis and visualizations completed.")
