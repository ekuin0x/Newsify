import json
from flask import Flask , render_template, url_for, request, send_file
from jinja2 import Template
import requests
import time
import random

topics = [ "Breaking", "Latest", "India", "Politics", "Health", "Technology"]
key = "pub_265336ee2696ca69ba98f092f4122499822c6"

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

@app.route('/insert/<psswrd>')
def insert(psswrd) :
    if psswrd != 'pizza69' :
        return 'Fuck You !'

    for topic in topics :
        res = requests.get(f'https://newsdata.io/api/1/news?apikey={key}&q={topic}&language=en')
        results = json.loads(res.text)["results"]
        for i in range(0, len(results) - 1) :
            if results[i]["image_url"] != None :
                title = results[i]["title"].encode("ascii", "ignore").decode() 
                content = results[i]["content"].encode("ascii", "ignore").decode() 
                img = results[i]["image_url"]
                source = results[i]["source_id"]
                date = results[i]["pubDate"]
                link = results[i]["link"] 
                id = random.randint(0, 10000000) 
                # Create html document
                with open("templates/template.html", 'r+') as t :
                    template = Template(t.read())
                    rendered = template.render(title = title, content = content, img =img, source = source, date = date, link = link, q = topic)
                    f = open(f"articles/{id}.html", 'w')
                    f.write(rendered)
                    f.close()
                # Insert data into json 
                new_data = {
                    "id" : id,
                    "topic" : topic, 
                    "title" : title,
                    "img" : img,
                }
                file = open("data.json",'r+')        
                f = json.load(file) 
                duplicate = 0   
                for x in f :
                    if title == x["title"] :
                        duplicate = 1;
                        break
                
                if duplicate == 0 :
                    f.append(new_data)
                    file.seek(0)
                    json.dump(f, file, indent = 4)
                    file.close()
    return "Success69"    



if __name__ == "__main__" :
    app.run()

