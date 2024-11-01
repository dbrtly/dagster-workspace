from dagster import Definitions 
from . import assets

inventory_defs = Definitions(assets=[assets.inventory_levels, assets.reorder_alerts])