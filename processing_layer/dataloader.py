import pandas as pd

def load_data():
    products = pd.read_csv(r"data_layer\product_table.csv")
    sales = pd.read_csv(r"data_layer/sales_transactions.csv")
    purchases = pd.read_csv(r"data_layer/purchase_table.csv")
    inventory = pd.read_csv(r"data_layer/inventory_table.csv")

    return products, sales, purchases, inventory