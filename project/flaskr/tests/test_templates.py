import unittest
import pathlib
import json
from jinja2 import Template
from project.questionaire import  Question, Questionaire
from project.questions_from_json import read

class Jinja2TemplatesTest(unittest.TestCase):

    def test_get_result_questionair(self):
        path_context = pathlib.Path(pathlib.Path(__file__).parent.parent.parent.parent,
                                    "json_schemas/questionaire_schema.json")
        path_to_json_example_file = pathlib.Path(pathlib.Path(__file__).parent.parent.parent.parent,
                                                 "json_schemas/questionaire_example.json")
        questionaire = read(path_to_json_example_file, path_context)
        localized_questions = questionaire.localized_questions("german")
        path_template = pathlib.Path(pathlib.Path(__file__).parent.parent, "templates/questionnair/questionnair_all_in_one.html")
        s = Template(str(path_template))
        abc = s.render(localized_questions)
        print("DEBUG")

