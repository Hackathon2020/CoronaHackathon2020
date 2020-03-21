
class Anwsers:
    """ holds a anwser
    """
    global_questionaire_id = ""
    anwsers = []

    """
    initilization

    Keyword arguments:
    global_questionatire_id(string) -- the globally unique id of the corresponding questionaire
    anwsers (array of Anwser) -- the given anwsers
    """
    def __init__(self, global_questionaire_id, anwsers):
        self.global_questionaire_id = questionaire_id
        self.anwsers = anwsers


class Anwser:
    """holds one specific anwser
    """
    question_id = ""
    anwser = []

    """ initialization

    Keyword arguments:
    question_id(string) -- the id of the question
    anwser -- the anwser. The type of this attribute depends on the anwser_type of the question.
    """
    def __init__(self, question_id, anwser):
        self.question_id = question_id
        self.anwser = anwser
