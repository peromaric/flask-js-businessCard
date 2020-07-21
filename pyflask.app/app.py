import json
import re
from datetime import datetime

from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        in_file = open("pyflask.app/static/data.json", "w")
        form_data = request.form
        json.dump(form_data, in_file, sort_keys=True)
        in_file.close()
        return render_template("home.html", home = home)
    return render_template("home.html", home = home)

@app.route("/data.json", methods = ["POST", "GET"])
def return_data():
    if request.method == "GET":
        out_file = open("pyflask.app/static/data.json", "r")
        form_data = json.load(out_file)
        data_object = json.dumps(form_data)
        out_file.close()
        return  data_object
    return render_template("home.html", home = home)