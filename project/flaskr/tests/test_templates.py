import unittest
import pathlib
import json
from jinja2 import Template
from project.questionaire import  Question, Questionaire

class Jinja2TemplatesTest(unittest.TestCase):

    def test_get_result_questionair(self):
        path_to_json_example_file = pathlib.Path(pathlib.Path(__file__).parent.parent.parent.parent,
                                                 "json_schemas/questionaire_example.json")
        with open(path_to_json_example_file, 'r') as j:
            contents = json.loads(j.read())
            language_map = contents["language_map"]
            options = ["2", "3", "4"]
            options1 = ["10", "11", "12"]
            questions = [Question("1", "string", options), Question("9", "string", options1)]
            questionaire = Questionaire("global_id", language_map, questions)
            localized_questions = questionaire.localized_questions("german")
            path_template = pathlib.Path(pathlib.Path(__file__).parent.parent, "templates/questionnair/questionnair_all_in_one.html")
            s = Template(str(path_template))
            abc = s.render(localized_questions)
            print("DEBUG")
