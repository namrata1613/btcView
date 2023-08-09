from flask import Flask, render_template, request,flash,redirect,jsonify
import config, csv, datetime
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

#client = Client(config.API_KEY, config.API_SECRET, tld='us')
client = Client()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/buy")
def buy():
    return "<p>buy</p>"

@app.route("/sell")
def sell():
    return "<p>sell</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"

@app.route("/history")
def history() :
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Aug, 2023", "10 Aug, 2023")
    
    processed_candlesticks = []
    for data in candlesticks :
        candlestick = { 
            "time": data[0]/1000, 
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4] 
            }
        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)