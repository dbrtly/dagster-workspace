from dagster import Definitions
from . import assets

inventory_defs = Definitions(
    assets=[
        assets.inventory_python_version_check,
        assets.inventory_cowsay_version,
    ]
)
