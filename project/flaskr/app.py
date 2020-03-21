# TODO: Import  muss noch angepasst werden, wenn von Konsole gestartet wird
import os
import pathlib
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from project.questionaire import Questionaire, Question
from project.flaskr import static_folder, template_folder
from project.flaskr.routes import questionaire
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


    app.register_blueprint(questionaire.get_questionaire_blueprint())
    return app


if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(debug=True)