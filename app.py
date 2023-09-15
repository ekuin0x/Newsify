import json
from flask import Flask , render_template, url_for, request, send_file
from jinja2 import Template
import time
import random

topics = [ "Global", "Sport","Politics", "India", "Latest", "Health", "Technology"]
#key = "pub_265336ee2696ca69ba98f092f4122499822c6"
key = "pub_277439a73bbbb0d3aa7c80b32ebc7e246d8d4"
app = Flask(__name__)

@app.route('/')
def index() :
    with open("data.json", 'r') as file :
        data = json.load(file)
    i = len(data) - 1
    return render_template("index.html", data = data[i:i-20:-1])

@app.route('/<sub>')
def sub(sub) :
    arr = []
    with open("data.json", 'r') as file :
        data = json.load(file)
    for x in data : 
        if x["topic"] == sub :
            arr.append(x)
            if len(arr) == 20 :
                break         
    return render_template("index.html", data = arr[::-1])


@app.route('/related/<topic>')
def related(topic) :
    with open("data.json", 'r') as file :
        data = json.load(file)
        arr = []
        for x in data :
            if topic == x["topic"] :
                arr.append(x)
                if len(arr) == 12 :
                    break
    return render_template('partials/related.html', related = arr, topic = topic)


@app.route('/search/<query>')
def search(query) :
    with open("data.json", "r") as file :
        data = json.load(file)  
    arr = []
    for x in data :
        if query in x["title"] :
            arr.append(x)
        if len(arr) == 12 :
            break    
    return render_template("search.html", related = arr)

@app.route('/articles/<i>')
def articles(i) :
    return send_file(f"articles/{i}.html")

if __name__ == "__main__" :
    app.run()

