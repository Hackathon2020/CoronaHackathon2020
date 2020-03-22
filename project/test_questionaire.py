import unittest

from project.questionaire import Questionaire, Question

class TestStringMethods(unittest.TestCase):

    def test_localized_questions_string_question(self):
        language_map = {"german" : {"1": "test question?"}};
        questions = [Question("1", "string")]
        questionaire = Questionaire("global_id", language_map, questions)
        localized_questions = questionaire.localized_questions("german")
        self.assertEqual(localized_questions[0].question_id, questions[0].question_id)
        self.assertEqual(localized_questions[0].anwser_type, questions[0].anwser_type)
        self.assertEqual(localized_questions[0].question_text, 'test question?')

    def test_localized_questions_with_options(self):
        language_map = {"german" : {"1": "test question?","2": "option a","3": "option b"}};
        options = ["2", "3"]
        questions = [Question("1", "string", options)]
        questionaire = Questionaire("global_id", language_map, questions)
        localized_questions = questionaire.localized_questions("german")
        self.assertEqual(localized_questions[0].question_id, questions[0].question_id)
        self.assertEqual(localized_questions[0].anwser_type, questions[0].anwser_type)
        self.assertEqual(localized_questions[0].options_texts[0], 'option a')
        self.assertEqual(localized_questions[0].options_texts[1], 'option b')


if __name__ == '__main__':
    unittest.main()
