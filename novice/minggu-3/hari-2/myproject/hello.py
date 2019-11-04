from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ini adalah halaman awal browser'

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__=="main":
    app.run(debug.true)

