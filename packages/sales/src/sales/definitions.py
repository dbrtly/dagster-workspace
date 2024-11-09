from dagster import Definitions
from packages.sales.src.sales import assets

sales_defs = Definitions(
    assets=[assets.sales_python_version_check, assets.sales_cowsay_version]
)
