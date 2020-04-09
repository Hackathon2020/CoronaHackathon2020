# TODO: Import  muss noch angepasst werden, wenn von Konsole gestartet wird
import pathlib
from flask import Flask, render_template, redirect, request
from project.flaskr import static_folder, template_folder
from project.flaskr.routes.questionaire import get_questionaire_blueprint
from project.questions_from_json import read




def create_app():
    """
    Create the Flask app for Grenz-er-fahrung: An easy to use Web Service to cross borders fast and efficient.
    Returns: Flask App

    """
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

    LOCAL_MAP = {'german' :  {'which_border': 'Welche Grenze möchten sie überqueren?',
                              'overview': 'Überblick',
                              'accept' : 'Forumlar Akzeptieren?',
                              'error_occured': 'Ein Fehler ist aufgetreten! Bitte gehen Sie eine Seite zurück!'},
                 'english' : {'which_border': 'Which Border do you want to cross?',
                              'overview': 'Overview',
                              'accept' : 'Accept form?',
                              'error_occured': 'An occured! Please step one site back!'}}

    questionaires = {}
    jsons = {}

    def add_border(border, json_path):
        path_context = pathlib.Path(pathlib.Path(__file__).parent.parent.parent,
                                "json_schemas/questionaire_schema.json")
        path_to_json = pathlib.Path(pathlib.Path(__file__).parent.parent.parent, json_path)
        with open(path_to_json) as f:
            json_f = f.read()
        questionaires[border] = read(path_to_json, path_context)
        jsons[border] = json_f

    add_border(('germany', 'switzerland'), "json_schemas/questionaire_example.json")


    #@app.route('/', methods=["GET", "POST"])
    #@app.route('/index')
    @app.route('/information')
    def index():
        """
        Page for the information -> General Information about the Crossing
        Returns: Template for Information

        """
        return render_template("app/informations.html")

    @app.route("/")
    @app.route("/language")
    def language_selection():
        """
        Page for language Selection -> Language for the questionnaire
        Returns: HTML Page

        """
        return render_template("app/language.html")
        pass

    @app.route("/crossing")
    def border_selection():
        """
        Page for which border to cross
        Returns: HTML Page

        """
        language = request.cookies.get('language')
        return render_template("app/crossing.html", localization=LOCAL_MAP[language])

    @app.route('/answer')
    def answer():
        return render_template("app/answer.html", title="Formula1")

    
    app.register_blueprint(get_questionaire_blueprint(questionaires, jsons, LOCAL_MAP))
    return app

def main():
    app = create_app()
    print(app.url_map)
    app.run(debug=True)

if __name__ == "__main__":
    main()
