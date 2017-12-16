#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 zenbook <zenbook@zenbook-XPS>
#
# Distributed under terms of the MIT license.

"""

"""
import redis
import random
import time

if __name__ == '__main__':
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    price = 0
    while True:
        price += random.uniform(-10, 10)
        print("Sending Price", price)
        client.publish("channel", price)
        time.sleep(1)
