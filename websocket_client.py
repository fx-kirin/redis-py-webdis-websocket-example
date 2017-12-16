#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 zenbook <zenbook@zenbook-XPS>
#
# Distributed under terms of the MIT license.

"""

"""
import websocket
import json

def on_open(ws):
    print("on open")
    ws.send(json.dumps(["SUBSCRIBE", "channel"]))
    
def on_message(ws, message):
    print("on message", message)
    
def on_error(ws, error):
    print("error", error)

if __name__ == '__main__':
    ws = websocket.WebSocketApp("ws://127.0.0.1:7379/.json",
                              on_open=on_open,
                              on_message = on_message,
                              on_error = on_error
                              )
    ws.run_forever()
