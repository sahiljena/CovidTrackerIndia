from flask import Flask, flash, request, redirect, url_for ,render_template
import json
import requests


app = Flask(__name__)

def get_data():
    url = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
    r = requests.get(url)
    y = json.loads(r.text)
    return y["activeCases"],y["recovered"],y["deaths"]

@app.route('/')
def index():
    h = get_data()
    total_positive = h[0]
    total_deaths = h[2]
    total_recv = h[1]
    return render_template("base.html", total_positive = total_positive,total_deaths = total_deaths,total_recv = total_recv)
