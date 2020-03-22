from flask import Blueprint, render_template
from project.flaskr import static_folder, template_folder


def get_questionaire_blueprint(questions, json_schema):
    questionnair = Blueprint('questionnair', __name__, template_folder=template_folder, static_folder=static_folder)
    @questionnair.route('/', methods=["GET", "POST"])
    @questionnair.route('/index')
    @questionnair.route("/questionnair")
    def questionnaire_begin():
            return render_template("questionnair/page.html", questions=questions, json_schema=json_schema)



    return  questionnair
