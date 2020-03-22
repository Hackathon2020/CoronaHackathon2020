
class Questionaire:
    """ holds all relevant data of a questionaire
    """
    global_questionaire_id = ""
    language_map = {}
    questions = []

    """ initialization

    :paran str global_id -- the globally unique identifier of this questionaire. This is needed to connect questionaires with anwsers.
    :param dict language_map -- (dict of str: (str: str)) -- containes the text-snippets used in this questionaire in every supported language. \
                                                             The mapping is "language" -> "id" -> "text
    :param list questions -- (list of Question)the actual questions in the questionaire
    """
    def __init__(self, global_id, language_map, questions):
        assert type(global_id) is str
        assert type(language_map) is dict
        assert type(questions) is list
        self.global_id = global_id
        self.language_map = language_map
        self.questions = questions

    """
    Creteas a localized list of the questions for the given language

    :param str language -- the language to localize to
    :rtype list of LocalizedQuestion
    :return a list of localized questions
    """
    def localized_questions(self, language):
        assert type(language) is str
        m = self.language_map[language]
        return list([LocalizedQuestion(q, m[q.question_id], list([m[opt] for opt in q.options])) for q in self.questions])

class Question:
    """ hold the description of a question
    """
    question_id = ""
    anwser_type = ""
    options = []

    """ initialization

    :param str question_id -- the identifier of the question. This is needed to idenitify the corresponing question test stored in the Questionaire'S language_map and associate questions with anwsers
    :param str anwser_type -- which kind of anwser is expected (string, date, PLZ,...)
    :param list options -- optional (array of strings) specifies all possible anwsers
    """
    def __init__(self, question_id, anwser_type, options=[]):
        assert type(question_id ) is str
        assert type(anwser_type) is str
        assert type(options) is list
        self.question_id = question_id
        self.anwser_type = anwser_type
        self.options = options

class LocalizedQuestion(Question):
   """ hols a localized question
   """
   question_text = ""
   options_texts = []

   """ initialization

   :param Question question -- the question
   :param str question_text -- the text of the question
   :param options_texts -- (list of str) the texts of the options
   """
   def __init__(self, question, question_text, options_texts):
       super().__init__(question.question_id, question.anwser_type, question.options)
       assert type(question_text) is str
       assert type(options_texts) is list
       self.question_text = question_text
       self.options_texts = options_texts

