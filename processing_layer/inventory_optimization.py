import pandas as pd

def calculate_inventory_metrics(avg_demand, lead_time=5):

    # safety stock
    avg_demand["safety_stock"] = avg_demand["avg_daily_demand"] * 2

    # reorder point
    avg_demand["reorder_point"] = (
        avg_demand["avg_daily_demand"] * lead_time
        + avg_demand["safety_stock"]
    )

    return avg_demand