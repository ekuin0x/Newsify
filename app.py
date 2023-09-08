import json
from flask import Flask , render_template, url_for, request, send_file

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template("index.html")

@app.route('/head')
def head() :
    f = open("templates/partials/head.html", 'r')
    head = f.read()
    f.close()
    return head

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