from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Question:
    """hold the description of a question

    Attributes:
        question_id (str): The identifier of the question. This is needed to idenitify
            the corresponing question test stored in the Questionnaire's language_map
            and associate questions with anwsers
        anwser_type (str): which kind of anwser is expected (string, date, PLZ,...)
        options (List[str]) = None: specifies all possible anwsers
    """

    question_id: str
    anwser_type: str
    options: List[str] = field(default_factory=lambda: [])


@dataclass
class LocalizedQuestion(Question):
    """ holds a question in a specified language.

    Attributes:
        question (Question): the question
        question_text (str): the text of the question
        options_texts (List[str]): the texts of the options
    """

    question_text: str = ""
    options_texts: List[str] = field(default_factory=lambda: [])


@dataclass
class Questionaire:
    """Holds all relevant data of a questionnaire.

    Attributes:
        global_id (str): Globally unique identifier of this questionnaire.
            This is needed to connect questionnaires to anwsers.
        language_map (Dict[str,Dict[str,str]]): Contains the text-snippets used
            in this questionnaire in every supported language.
            The mapping is "language" -> "id" -> "text
        questions (List[str]): Actual questions in the questionaire
    """

    global_id: str
    language_map: Dict[str, Dict[str, str]]
    questions: List[Question]

    def localized_questions(self, language: str) -> List[LocalizedQuestion]:
        """Create a list of the questions in the given language."""
        m: Dict[str, str] = self.language_map[language]

        return [
            LocalizedQuestion(
                q.question_id,
                q.anwser_type,
                q.options,
                m[q.question_id],
                list([m[opt] for opt in q.options]),
            )
            for q in self.questions
        ]
