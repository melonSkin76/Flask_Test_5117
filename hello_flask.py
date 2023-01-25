from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hi', methods=['GET'])
def hi_world():
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name) 