from flask import Flask
import os

app = Flask(__name__)

@app.route('/', )
def index():
  return "Hello, ceci est un test pour voir si le workflow fonctionne. nouveau test pour checker les lignes necessaires... est'ce que ça marche?? Ok et manitenant, ça marche ou bien?"

@app.route('/hello_world')
def hello_world():
  return 'Hello World'


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host = '0.0.0.0', port = port, debug=True)