import os
import pathlib
from flask import Flask, render_template


app = Flask(__name__, instance_relative_config=True)

@app.route('/')
@app.route('/index')
#@app.route('/index')
def index():
    return render_template("app/index.html", title="Home")


@app.route('/answer')
def answer():
    return render_template("app/answer.html", title="Formula1")


@app.route('/question')
def question():
    return render_template("app/question.html", title="Formula2")
