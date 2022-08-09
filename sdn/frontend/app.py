from flask import Flask, render_template, request, send_file, redirect, url_for, session
import psutil
import requests
import json
import time
import subprocess
import sys
import os,socket

app = Flask(__name__)

@app.route("/")
def func():
    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", ", Hi Kurt and Roman from VM13"), hostname=socket.gethostname())

@app.route("/load")
def load():
    load = str(psutil.cpu_percent())
    return load
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=4000)
