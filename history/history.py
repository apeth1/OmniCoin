# ************************
# history.py
# Author: Andrew Peth
# Date: 01/06/2018
# All Rights Reserved (c) 2018
# ************************

import sqlite3
import json
import os

from omni_coin.log import LogManager


class CoinPriceHistory(object):
    def __init__(self, table):
        self.table = table
        self.db_path = os.path.join(os.getcwd(), "data", "price_history.db")
        self.log_path = os.path.join(os.getcwd(),"log","db.log")
        logger = LogManager("history_log", self.log_path)
        self.history_logger = logger.create_logger()

    def store(self, response, exchange):
        coins = json.loads(response)
        self._initialize_db()
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        i = 0
        try:
            for i in range(0, len(coins)):
                c.execute("INSERT INTO price_history VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (coins[i]['id'],
                          coins[i]['name'], coins[i]['symbol'], coins[i]['rank'],
                          coins[i]['price_usd'], coins[i]['price_btc'], coins[i]['24h_volume_usd'],
                          coins[i]['market_cap_usd'], coins[i]['available_supply'], coins[i]['total_supply'],
                          coins[i]['percent_change_1h'], coins[i]['percent_change_24h'],
                          coins[i]['percent_change_7d'], coins[i]['last_updated'], exchange))
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
            conn = sqlite3.connect(self.db_path)
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





