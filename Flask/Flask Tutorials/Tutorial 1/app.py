from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello world!"

@app.route('/<name>')
def print_name(name):
  return f"<h1>Hello {name}!<h1/>"

@app.route('/sayhello')
def say_hello():
  return f"<h1>Hello<h1/>"

if __name__ == "__main__":
  app.run()