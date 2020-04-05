from flask import Blueprint, render_template, request
from project.flaskr import static_folder, template_folder


def get_questionaire_blueprint(questionaire, json_schema, local_map):
    """
    Flask routing for the questionnaire
    Args:
        questions: List[localized_question, localized_question, ...]
        json_schema: The json schema for the questionnaire
        local_map: map of localizations. Hold for a language a map of localizations

    Returns: the blueprint for routing of the questionaire

    """
    questionnair = Blueprint('questionnair', __name__, template_folder=template_folder, static_folder=static_folder)
    @questionnair.route("/questionnair")
    def questionnaire_begin():
        language = request.cookies.get('language')
        localized_questions = questionaire.localized_questions(language)

        return render_template("questionnair/page.html", questions=localized_questions, json_schema=json_schema, localization=local_map[language])



    return  questionnair
