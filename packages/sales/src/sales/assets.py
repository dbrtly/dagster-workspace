import json
import os
import platform

from dagster import asset
import cowsay


@asset(group_name="sales")
def sales_python_version_check():
    """The Python version here should be different to the Inventory module/package."""
    os.makedirs("data/sales", exist_ok=True)
    python_version = platform.python_version()
    with open("data/sales/python_version_check.json", "w") as f:
        json.dump([python_version], f)


@asset(group_name="sales")
def sales_cowsay_version():
    """Logic to fetch inventory levels."""
    os.makedirs("data/sales", exist_ok=True)
    with open("data/sales/cowsay.txt", "w") as f:
        f.write(cowsay.__version__)
