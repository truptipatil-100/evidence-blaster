# build 434ad29a30
# (auto) 5d3c12
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
