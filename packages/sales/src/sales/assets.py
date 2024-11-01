import json
import os
import platform

from dagster import asset

@asset
def sales_python_version_check():
    """The Python version here should be different to the Inventory module/package."""
    os.makedirs("data", exist_ok=True)
    python_version = platform.python_version()
    with open("data/sales_python_version_check.json", "w") as f:
        json.dump([python_version], f)

@asset
def sales_data():
    # Logic to ingest sales data
    pass

@asset
def sales_metrics(sales_data):
    # Logic to calculate sales performance metrics
    pass
