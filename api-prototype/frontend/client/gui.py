from flask import render_template
from client import app


@app.route('/index')
def index():
    return render_template('index.html')