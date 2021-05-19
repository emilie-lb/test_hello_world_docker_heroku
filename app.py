from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello, ceci est un test pour voir si le workflow fonctionne"

@app.route('/hello_world')
def hello_world():
  return 'Hello World'


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug = True, host = '0.0.0.0')