import pandas as pd

def aggregate_daily_sales(sales):
    daily_sales = sales.groupby(["item_id", "date"])["quantity_sold"].sum().reset_index()
    return daily_sales


def compute_average_demand(daily_sales):
    avg_demand = daily_sales.groupby("item_id")["quantity_sold"].mean().reset_index()
    avg_demand.rename(columns={"quantity_sold": "avg_daily_demand"}, inplace=True)
    return avg_demand