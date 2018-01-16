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
    queries = 0
    cmc_api = hook.CoinMarketCapApi(settings.API['cmc'])
    while True:
        coins = cmc_api.get()
        if coins != "[{}]":
            db = history.CoinPriceHistory(coins, "cmc_pricing")
            indicator = db.store("CoinMarketCap")
            print(str(indicator))
            queries+=1
        time.sleep(30)
