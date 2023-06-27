from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url).json()
    spis = []
    for i in response["Valute"]:
        spis.append(response["Valute"][i]["Name"])
        spis.append(response["Valute"][i]["Value"])
    return render_template("main.html", res=spis)







app.run("0.0.0.0")