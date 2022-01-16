from flask import Flask, render_template, request, redirect, url_for
from notification import SMS
import json

app = Flask(__name__)

# home
@app.route('/')
def homePage():
    name = "home"
    return render_template('home.html', page=name)

#loading
@app.route('/loading')
def loadingPage():
    name = "loading"
    return render_template('loading.html', page=name)

# stretch
@app.route("/stretch")
def stretchPage():
    details = []
    name = []
    with open('./static/stretches.json') as json_file:
        data = json.load(json_file)
        for ele in data:
            for key, value in ele.items():
                name.append(value[0])
                details.append(value[1])
        return render_template('stretch.html', name=json.dumps(name), details=json.dumps(details))

# games
@app.route("/games")
def rabbitPage():
    name = "rabbit"
    return render_template('games.html', page=name)

# about page to add info regarding our webapp
@app.route('/about')
def about():
    list = ["I", "love", "pizza"]
    return render_template('about.html', listName=list)

@app.route('/api', methods = ['POST'])
def api():
  print("sent SMS")
  # do not uncomment this until demo
  #SMS()
  return request.values.get('input', '')

# Dont delete this
if __name__ == '__main__':
    app.run(debug=True)
