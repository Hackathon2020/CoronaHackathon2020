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
                              'accept' : 'Forumlar Akzeptieren?'},
                 'english' : {'which_border': 'Which Border do you want to cross?',
                              'overview': 'Overview',
                              'accept' : 'Accept form?'}}

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

    @app.route("/crossing_<language>")
    def border_selection(language):
        """
        Page for which border to cross
        Args:
           language: the chosen language
        Returns: HTML Page

        """
        return render_template("app/crossing.html", localization=LOCAL_MAP[language])

    @app.route('/answer')
    def answer():
        return render_template("app/answer.html", title="Formula1")

    path_context = pathlib.Path(pathlib.Path(__file__).parent.parent.parent,
                                "json_schemas/questionaire_schema.json")
    path_to_json_example_file = pathlib.Path(pathlib.Path(__file__).parent.parent.parent,
                                             "json_schemas/questionaire_example.json")
    questionaire = read(path_to_json_example_file, path_context)
    # TODO: Hier json einfügen die für Frage ids benötigt
    with open(pathlib.Path(pathlib.Path(__file__).parent.parent.parent, "json_schemas/questionaire_example.json")) as f:
        json_f = f.read()
    app.register_blueprint(get_questionaire_blueprint(questionaire, json_f, LOCAL_MAP))
    return app

def main():
    app = create_app()
    print(app.url_map)
    app.run(debug=True)

if __name__ == "__main__":
    main()
