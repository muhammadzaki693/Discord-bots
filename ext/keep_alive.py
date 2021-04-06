from flask import Flask
from threading import Thread
import sys

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = Flask('')

@app.route('/')
def home():
  return "idk"

def run1():
  app.run(host='0.0.0.0',port=8080)

def run():
  t = Thread(target=run1)
  t.start()