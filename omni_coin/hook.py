# ************************
# hook.py
# Author: Andrew Peth
# Date: 01/06/2018
# All Rights Reserved (c) 2018
# ************************
import requests
import os
from omni_coin import log

"""
CoinMarketCap.com API interaction class
Supports:
1. Return all cryptocurrencies financial information
2. Return a user specified cryptocurrencies financial information
3. Cryptocurrency conversion to currencies that are not USD.
"""


class CoinMarketCapApi(object):
    def __init__(self, url):
        self.url= url
        log_path = os.path.join(os.getcwd(),"log","api.log")
        api_log = log.LogManager('api_hook', log_path)
        self.api_log = api_log.create_logger()

    def get(self, ticker: str = None, currency: str = None) -> str:
        if ticker is not None:
            self.url = self._url_builder(ticker, currency)
        try:
            response = requests.get(self.url)
            self.api_log.info("Request Made to %s with response %s." % (self.url, response.status_code))
            return response.text
        except requests.exceptions.HTTPError as e:
            self.api_log.info("HTTPError Occurred %s" % str(e))
            return '[{}]'
        except requests.exceptions.ConnectTimeout as e:
            self.api_log.info("Connection Timeout Occurred: %s" % str(e))
            return '[{}]'
        except requests.exceptions.ConnectionError as e:
            self.api_log.info("Connection Error Occurred: %s" % str(e))
            return '[{}]'
        except requests.exceptions.RequestException as e:
            self.api_log.info("Requests Exception Occurred: %s" % str(e))
            return '[{}]'

    def _url_builder(self, ticker: str = None, currency: str = None) -> str:
        url = self.url
        if ticker is not None:
            url = self.url + ticker + '/'
        if currency is not None:
            url = self.url + ticker + '/?convert=' + currency
        return url









