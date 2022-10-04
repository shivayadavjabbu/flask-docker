from flask import Flask, render_template, request, send_file, redirect, url_for, session
import requests
import json
import time
import subprocess
import sys
import os

app = Flask(__name__)

ipAddressWebServer1 = "10.0.1.19"
ipAddressWebServer2 = "10.0.1.20"

# 0 - is RoundRobin, 1 - Weighted Round Robin
strategy = 1

# 0 - ipAddressWebServer1, 1 - ipAddressWebServer2
roundRobin = 0

loadWebServer1 = 0
loadWebServer2 = 0


@app.route('/', method=["GET"])
def func():
    response = loadBanacer(request)
    return response


@app.route("/changeStrategy", method = ["GET"])
def func():
    if strategy == 0:
        strategy = 1
    else:
        strategy = 0
    return 0

def loadBanacer():
    # Route for RoundRobin
    if strategy == 0:
        ipAddressWebServer = ""
        if roundRobin == 0:
            ipAddressWebServer = ipAddressWebServer1
            roundRobin = 1
        else:
            ipAddressWebServer = ipAddressWebServer2
            roundRobin = 0
        response = requests.get("http://" + ipAddressWebServer + "/")
        return response
    if strategy == 1:
        loadWebServer1 = requests.get("http://" + ipAddressWebServer1 + "/load")
        loadWebServer2 = requests.get("http://" + ipAddressWebServer2 + "/load")
        if loadWebServer1 > loadWebServer2:
            ipAddressWebServer = loadWebServer2
        else:
            ipAddressWebServer = loadWebServer1
        response = requests.get("http://" + ipAddressWebServer + "/")
        return response
