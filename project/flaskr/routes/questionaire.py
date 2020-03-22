from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, abort
from project.flaskr import static_folder, template_folder
from project.questionaire import Question, Questionaire
from project.questions_from_json import read


def get_questionaire_blueprint(questions):
    questionnair = Blueprint('questionnair', __name__, template_folder=template_folder, static_folder=static_folder)
    @questionnair.route("/questionnair")
    def questionnaire_begin():
            return render_template("questionnair/questionnair_all_in_one.html", questions=questions)



    return  questionnair
