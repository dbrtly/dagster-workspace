from dagster import Definitions 
from . import assets

sales_defs = Definitions(assets=[assets.sales_data, assets.sales_metrics])
