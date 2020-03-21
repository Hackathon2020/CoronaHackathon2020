
class Questionaire:
    """ holds all relevant data of a questionaire
    """
    global_questionaire_id = ""
    language_map = {}
    questions = []

    """ initialization

    Keyword arguments:
    gloabl_id(string) -- the globally unique identifier of this questionaire. This is needed to connect questionaires with anwsers.
    language_map(dict of str: (str: str)) -- containes the text-snippets used in this questionaire in every supported language.
                                             The mapping is "language" -> "id" -> "text
    questions(array of Question) -- the actual questions in the questionaire
    """

    def __init__(self, global_id, language_map, questions):
        self.global_id = global_id
        self.language_map = language_map
        self.questions = questions


class Question:
    """ hold the description of a question
    """
    question_id = ""
    anwser_type = ""
    options = []

    """ initialization

    Keyword arguments:
    question_id(string): the identifier of the question. This is needed to idenitify the corresponing question test stored in the Questionaire'S language_map and associate questions with anwsers
    anwser_type(string): which kind of anwser is expected (string, date, PLZ,...)

    Optional Keyword arguments:
    options(array of strings): specifies all possible anwsers
    """

    def __init__(self, question_id, anwser_type, options=[]):
        self.question_id = question_id
        self.anwser_type = anwser_type
        self.options = options
