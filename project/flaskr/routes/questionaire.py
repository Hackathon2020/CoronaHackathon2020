from flask import Blueprint, render_template, request, redirect
from project.flaskr import static_folder, template_folder


def get_questionaire_blueprint(questionaires, jsons, local_map):
    """
    Flask routing for the questionnaire
    Args:
        questionaires: map form (str, str) to questionaire
        jsons: The json files-map
        local_map: map of localizations. Hold for a language a map of localizations

    Returns: the blueprint for routing of the questionaire

    """
    questionnair = Blueprint('questionnair', __name__, template_folder=template_folder, static_folder=static_folder)
    @questionnair.route("/questionnair")
    def questionnaire_begin():
        language = request.cookies.get('language')
        if not isinstance(language, str):
            return redirect("/language?from=" + request.args['from'] + "&to=" + request.args['to'] + "&global_id=" + request.args['global_id'] + "&data=" + request.args['data'])
        try:
            FROM = request.args['from']
            TO = request.args['to']
            BORDER = (FROM, TO)
            if BORDER in questionaires:
                localized_questions = questionaires[(FROM, TO)].localized_questions(language)
                json = jsons[(FROM, TO)]
                return render_template("questionnair/page.html", questions=localized_questions, json_schema=json, localization=local_map[language])
            else:
               print("Border " + str(BORDER) + " could not be found")
        except:
            pass
        return render_template("app/error.html", localization=local_map[language])

    return  questionnair
