import json
import jsonschema
import questionaire


def read(filename):
    """
    """
    with open(filename) as file:
        json_string = file.read()
        print(json_string)

        #with open("json_schemas/questionaire_schema.json") as schema_file:
            #schema = schema_file.read()
            #jsonschema.validate(json_string, json.load("json_schemas/questionaire_schema.json"))
            #jsonschema.validate(json_string, json.load(schema_file))

        decoded = json.loads(json_string)

        global_id = decoded["global_questionaire_id"]
        languages = decoded["language_map"]

        question_list = []
        questions = decoded["question_map"]
        for question in questions:
            try:
                options = question["options"]
            except KeyError:
                options = []

            question_list.append(questionaire.Question(question["question_id"], question["answer_type"], options))

        return questionaire.Questionaire(global_id, languages, question_list)

