from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, abort
from project.flaskr import static_folder, template_folder
from project.questionaire import Question, Questionaire
from project.questions_from_json import read


def get_overview_blueprint(questions):
    overview = Blueprint('overview', __name__, template_folder=template_folder, static_folder=static_folder)
    @overview.route("/overview")
    def overview_begin():
            return render_template("app/overview.html", questions=questions)



    return overview
