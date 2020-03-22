# TODO: Import  muss noch angepasst werden, wenn von Konsole gestartet wird
import os
import pathlib
import json
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from project.questionaire import Questionaire, Question
from project.flaskr import static_folder, template_folder
#from project.questions_from_json import read


def create_app():
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    Bootstrap(app)


    @app.route('/', methods=["GET", "POST"])
    @app.route('/index')
    def index():
        return render_template("app/informations.html")


    @app.route('/answer')
    def answer():
        return render_template("app/answer.html", title="Formula1")


    @app.route('/question')
    def question():
        path_to_repo = "/home/kevin/Documents/hackathon" # subpath to CoronaHackthon2020 repo, for example /home/user/code/
        path_to_json_example_file = path_to_repo + "/CoronaHackathon2020/json_schemas/questionaire_example.json"
        with open( path_to_json_example_file, 'r') as j:
            contents = json.loads(j.read())
        language_map = contents["language_map"]
        options = ["2", "3", "4"]
        questions = [Question("1", "string", options)]
        questionaire = Questionaire("global_id", language_map, questions)
        localized_questions = questionaire.localized_questions("german")
        return render_template('app/questionaire.html', questions=localized_questions)
        #render_template("app/question.html", title="Formula2")


    @app.route('/question/example_form/<question_id>/<language>', methods=["GET", "POST"])
    def example_form(language, question_id):
        with open("/home/kevin/Dokumente/hackathon/CoronaHackathon2020/json_schemas/questionaire_example.json", 'r') as j:
            contents = json.loads(j.read())
        language_map = contents["language_map"]
        options = ["2", "3", "4"]
        options1 = ["10", "11", "12"]
        questions = [Question("1", "string", options), Question("9", "string", options1)]
        questionaire = Questionaire("global_id", language_map, questions)
        localized_questions = questionaire.localized_questions(language)
        #form = forms.ReusableForm()
        #form.change_language(language)
        return render_template('app/questionaire.html', questions=localized_questions[int(question_id)])


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)