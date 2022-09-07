from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
  return f"Hello {name}"

@app.route('/showhello')  
def show_hello():
  return render_template("index.html")

@app.route('/showname/<name>')  
def show_name(name):
  return render_template("index.html", name=name)

@app.route('/showfriends')
def show_friends():
  return render_template("index.html", friend_list=["hazim", "fawzi", "sobhy", "khaled"])

if __name__ == "__main__":
  app.run(debug=True)