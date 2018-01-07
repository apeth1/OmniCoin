# ************************
# omni.py
# Author: Andrew Peth
# Date: 01/06/2018
# All Rights Reserved (c) 2018
# ************************

from omni_coin import hook, settings
from history import history
import time


if __name__ == "__main__":
    while True:
        cmc_api = hook.CoinMarketCapApi(settings.API['cmc'])
        coins = cmc_api.get()
        db = history.CoinHistory(coins, "cmc_pricing")
        indicator = db.store("CoinMarketCap")
        print(str(indicator))
        time.sleep(10)
