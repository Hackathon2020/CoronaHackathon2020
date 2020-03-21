from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, abort
from project.flaskr import static_folder, template_folder
from project.questions_from_json import read


def get_questionaire_blueprint(formula_type="Formula1", language="English"):
    questionnaire_entry = Blueprint('questionaires', __name__, template_folder=template_folder, static_folder=static_folder)
    questionaire = read("/home/maximilianbeier/ws/CoronaHackathon2020/json_schemas/questionaire_example.json")
    print("DEBUG")

    @questionnaire_entry.route("/question")
    def questionnaire_begin():
        try:
            return render_template("questionnair.html")
        except TemplateNotFound:
            abort(404)




    return  questionnaire_entry
