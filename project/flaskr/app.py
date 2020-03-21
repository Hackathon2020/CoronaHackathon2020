# TODO: Import  muss noch angepasst werden, wenn von Konsole gestartet wird
import os
import pathlib
from flask import Flask, render_template, redirect
from project.flaskr.services import forms

project_dir = pathlib.Path(os.path.abspath(os.path.dirname(__file__)), "templates")

app = Flask(__name__, template_folder=project_dir)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

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
    return redirect('/question/example_form')
    #render_template("app/question.html", title="Formula2")

@app.route('/question/example_form', methods=["GET", "POST"])
def example_form():
    form = forms.ReusableForm()
    return render_template('app/example_form.html', title="Answer Questions", form=form)

if __name__ == "__main__":
    app.run()