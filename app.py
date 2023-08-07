from flask import Flask, render_template

app = Flask(__name__)

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