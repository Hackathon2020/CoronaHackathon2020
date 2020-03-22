# TODO: Import  muss noch angepasst werden, wenn von Konsole gestartet wird
import pathlib
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from project.flaskr import static_folder, template_folder
from project.flaskr.routes.questionaire import get_questionaire_blueprint
from project.questions_from_json import read




def create_app():
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    Bootstrap(app)

    #@app.route('/', methods=["GET", "POST"])
    #@app.route('/index')
    @app.route('/information')
    def index():
        return render_template("app/informations.html")

    @app.route("/")
    @app.route("/language")
    def language_selection():
        return render_template("app/language.html")
        pass

    @app.route("/crossing")
    def border_selection():
        return render_template("app/crossing.html")

    @app.route('/answer')
    def answer():
        return render_template("app/answer.html", title="Formula1")

    path_context = pathlib.Path(pathlib.Path(__file__).parent.parent.parent,
                                "json_schemas/questionaire_schema.json")
    path_to_json_example_file = pathlib.Path(pathlib.Path(__file__).parent.parent.parent,
                                             "json_schemas/questionaire_example.json")
    questionaire = read(path_to_json_example_file, path_context)
    localized_questions = questionaire.localized_questions("german")
    # TODO: Hier json einfügen die für Frage ids benötigt
    with open(pathlib.Path(pathlib.Path(__file__).parent.parent.parent, "json_schemas/questionaire_example.json")) as f:
        json_f = f.read()
    app.register_blueprint(get_questionaire_blueprint(localized_questions, json_f))
    return app

def main():
    app = create_app()
    print(app.url_map)
    app.run(debug=True)

if __name__ == "__main__":
    main()
