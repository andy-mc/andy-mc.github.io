import os
from flask import Flask, render_template, url_for, send_from_directory
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'airplane.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('index.html')
    