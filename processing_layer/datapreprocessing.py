import pandas as pd

def convert_dates(sales, purchases):
    sales["date"] = pd.to_datetime(sales["date"], format="%Y-%m-%d")
    purchases["date"] = pd.to_datetime(purchases["date"], format="%d-%m-%Y")

    return sales, purchases

def aggregate_daily_sales(sales):
    daily_sales = sales.groupby(
        ["item_id", "date"]
    )["quantity_sold"].sum().reset_index()

    return daily_sales

def compute_average_demand(daily_sales):
    avg_demand = daily_sales.groupby("item_id")[
        "quantity_sold"
    ].mean().reset_index()

    avg_demand.rename(
        columns={"quantity_sold": "avg_daily_demand"},
        inplace=True
    )

    return avg_demand



def preprocess_data(sales, purchases):

    sales["date"] = pd.to_datetime(sales["date"])
    purchases["date"] = pd.to_datetime(purchases["date"])

    # daily sales
    daily_sales = sales.groupby(["item_id","date"])["quantity_sold"].sum().reset_index()

    # average demand
    avg_demand = daily_sales.groupby("item_id")["quantity_sold"].mean().reset_index()
    avg_demand.rename(columns={"quantity_sold":"avg_daily_demand"}, inplace=True)

    return daily_sales, avg_demand