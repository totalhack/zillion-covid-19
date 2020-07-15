import os

from zillion.warehouse import Warehouse

FILEDIR = os.path.dirname(os.path.abspath(__file__))

wh = Warehouse(config=FILEDIR + "/covid_warehouse.json")

if __name__ == "__main__":
    wh.print_info()
