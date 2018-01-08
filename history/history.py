# ************************
# history.py
# Author: Andrew Peth
# Date: 01/06/2018
# All Rights Reserved (c) 2018
# ************************

import sqlite3
import json
import time
from omni_coin.log import LogManager


class CoinHistory(object):
    def __init__(self, response, table):
        self.response = json.loads(response)
        self.table = table
        logger = LogManager("history_log", "history.log")
        self.history_logger = logger.create_logger()

    def store(self, exchange) -> int:
        coins = self.response
        self._initialize_db()
        conn = sqlite3.connect('price_history.db')
        c = conn.cursor()
        i = 0
        try:
            for i in range(1, len(coins)):
                c.execute("INSERT INTO price_history VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (coins[i]['id'],
                          coins[i]['name'], coins[i]['symbol'], coins[i]['rank'],
                          coins[i]['price_usd'], coins[i]['price_btc'], coins[i]['24h_volume_usd'],
                          coins[i]['market_cap_usd'], coins[i]['available_supply'], coins[i]['total_supply'],
                          coins[i]['percent_change_1h'], coins[i]['percent_change_24h'],
                          coins[i]['percent_change_7d'], coins[i]['last_updated'], exchange))
                print(coins[i]) #Remove this for faster inserts
                time.sleep(0.2) #And remove this
            conn.commit()
            c.close()
            conn.close()
            self.history_logger.info("Database Updated, Inserted %s Records" % str(len(coins)))
            print("Database has been updated successfully using %s" % exchange)
            return 0
        except sqlite3.Error as e:
            self.history_logger.info("Database Insert Error: %s" % str(e))
            return 1

    def _initialize_db(self):
        try:
            conn = sqlite3.connect('price_history.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS price_history 
                    (id text, name text, symbol text, rank text,
                    price_usd text, price_btc text, "24h_volume_usd" text, market_cap_usd text, available_supply text,
                    total_supply text, percent_change_1h text, percent_change_24h text, 
                    percent_change_7d text, last_updated text, exchange text)
                    ''')
            conn.commit()
            c.close()
            conn.close()
            self.history_logger.info("Database Table Created")
        except sqlite3.Error as e:
            self.history_logger.info("Database Table Creation Error: %s" % str(e))





