from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, abort
from project.flaskr import static_folder, template_folder
from project.questionaire import Question, Questionaire
from project.questions_from_json import read


def get_questionaire_blueprint(language="English"):
    questionnair = Blueprint('questionnair', __name__, template_folder=template_folder, static_folder=static_folder)
    language_map = {"English": {"1": "test question?", "2": "Another Question!"}}
    questions = [Question("1", "string"), Question("2", "String")]
    questionaire = Questionaire("global_id", language_map, questions)
    localized_questions = questionaire.localized_questions(language)
    localized_questions[0].options_text = ["A", "B", "C"]
    localized_questions[1].options_text = ["A", "B", "C"]
    #questionaire = read("/home/maximilianbeier/ws/CoronaHackathon2020/json_schemas/questionaire_example.json")
    @questionnair.route("/questionnair")
    def questionnaire_begin():
            return render_template("questionnair.html", questions=localized_questions)



    return  questionnair
