import json
from flask import Flask , render_template, url_for, request, send_file
import schedule as sc
import requests
import time

app = Flask(__name__)

@app.route('/')
def index() :
    with open("data.json", 'r') as file :
        data = json.load(file)
        return render_template("index.html", data = data[0:12])

@app.route('/<sub>')
def sub(sub) :
    arr = []
    with open("data.json", 'r') as file :
        data = json.load(file)
        for x in data : 
            if x["topic"] == sub :
                arr.append(x)
        return render_template("index.html", data = arr[0:20])



@app.route('/related/<topic>')
def related(topic) :
    with open("data.json", 'r') as file :
        data = json.load(file)
        rel = []
        for x in data :
            if topic == x["topic"] :
                rel.append(x)
    return render_template('partials/related.html', related = rel, topic = topic)


@app.route('/search/<query>')
def search(query) :
    with open("data.json", "r") as file :
        data = json.load(file)  
    related = []
    for x in data :
        if query in x["title"] :
            related.append(x)
    return render_template("search.html", related = related)

@app.route('/articles/<i>')
def articles(i) :
    return send_file(f"articles/{i}.html")

if __name__ == "__main__" :
    app.run()

