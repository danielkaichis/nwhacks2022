from flask import Flask, render_template, request, redirect, url_for
from notification import SMS

app = Flask(__name__)

# home
@app.route('/')
def homePage():
    name = "home"
    return render_template('home.html', page=name)

# stretch
@app.route("/stretch")
def stretchPage():
    name = "stretch"
    return render_template('stretch.html', page=name)

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

''' 
   ===================================================
    # Will be delete at the end 
    # Example how to pass data from flask to HTML, how to get data from HTML to flask
   ===================================================
'''
@app.route('/form', methods=['GET', 'POST'])
def form():
    request_method = request.method
    # res from server
    if request_method == "POST":
        user = request.form['first_name']
        return redirect(url_for("greet", name=user))
    return render_template('form.html', request_method=request_method)

@app.route("/greet/<string:name>")
def greet(name):
    return f"Hello {name}"

# Dont delete this
if __name__ == '__main__':
    app.run(debug=True)
