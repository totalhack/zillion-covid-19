import os

from zillion.configs import load_warehouse_config
from zillion.warehouse import Warehouse

FILEDIR = os.path.dirname(os.path.abspath(__file__))
SQLITE_DB_FILE = FILEDIR + "/sqlite.db"
SQLITE_URL = "sqlite:///" + SQLITE_DB_FILE

wh_config = load_warehouse_config(FILEDIR + "/covid_warehouse.json")
wh_config["datasources"]["glide_covid_19"]["connect"] = SQLITE_URL

wh = Warehouse(config=wh_config)

if __name__ == "__main__":
    wh.print_info()
