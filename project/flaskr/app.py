# TODO: Import  muss noch angepasst werden, wenn von Konsole gestartet wird
import os
import pathlib
from flask import Flask, render_template, redirect
from project.flaskr.services import forms
from project.questionaire import Questionaire, Question


project_dir = pathlib.Path(os.path.abspath(os.path.dirname(__file__)), "templates")

app = Flask(__name__, template_folder=project_dir)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

@app.route('/')
@app.route('/index')
#@app.route('/index')
def index():
    LANGUAGES = ["English", "German", "Spanish", "French"]
    BORDERS = ["England", "Germany", "Spain", "Poland", "France"]
    return render_template("app/index.html", title="Home", languages=LANGUAGES, borders=BORDERS)


@app.route('/answer')
def answer():

    return render_template("app/answer.html", title="Formula1")


@app.route('/question')
def question():
    return redirect('/question/example_form')
    #render_template("app/question.html", title="Formula2")

@app.route('/question/example_form/<language>', methods=["GET", "POST"])
def example_form(language):
    language_map = {"german": {"1": "test question?"}};
    questions = [Question("1", "string")]
    questionaire = Questionaire("global_id", language_map, questions)
    localized_questions = questionaire.localized_questions(language)
    #form = forms.ReusableForm()
    #form.change_language(language)
    return render_template('app/questionaire.html',  title="Answer Questions", questions=localized_questions)

if __name__ == "__main__":
    app.run()