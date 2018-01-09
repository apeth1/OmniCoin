# ************************
# coin_price_producer.py
# Author: Andrew Peth
# Date: 01/08/2018
# All Rights Reserved (c) 2018
# ************************

#TO-DO Create a producer for each individual coins information.

from omni_coin import settings
from confluent_kafka import Producer


class Producer(object):
    def __init__(self, topic):
        self.topic = topic

    def send(self, message):
        p = Producer({'boostrap.server': settings.KAFKA['bootstrap.servers']})
        p.produce('CoinPrices', key='coin', value=message)
        p.flush(30)