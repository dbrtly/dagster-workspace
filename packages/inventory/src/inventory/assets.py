import json
import os
import platform

from dagster import asset
import cowsay


@asset(group_name="inventory")
def inventory_python_version_check():
    """The Python version here should be different to the Sales module/package."""
    os.makedirs("data/inventory", exist_ok=True)
    python_version = platform.python_version()
    with open("data/inventory/python_version_check.json", "w") as f:
        json.dump([python_version], f)


@asset(group_name="inventory")
def inventory_cowsay_version():
    """Logic to fetch inventory levels."""
    os.makedirs("data/inventory", exist_ok=True)
    with open("data/inventory/cowsay_version.txt", "w") as f:
        f.write(cowsay.__version__)
