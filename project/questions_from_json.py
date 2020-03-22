import json
import jsonschema
import project.questionaire as questionaire


def read(filename, context):
    """
    Reads questionaire from file

    :param filename -- path to file containing questionaire
    :param context -- filepath to the schema files
    :rtype questionaire.Questionaire
    :return a questionaire
    """
    with open(filename) as file:
        json_string = file.read()

        decoded = json.loads(json_string)

        with open(context) as schema_file:
            schema = schema_file.read()
            jsonschema.validate(instance=decoded, schema=json.loads(schema))

        global_id = decoded["global_questionaire_id"]
        languages = decoded["language_map"]

        question_list = []
        questions = decoded["question_map"]
        for question in questions:
            try:
                options = question["options"]
            except KeyError:
                options = []

            question_list.append(questionaire.Question(
                question["question_id"], question["answer_type"], options))

        return questionaire.Questionaire(global_id, languages, question_list)
