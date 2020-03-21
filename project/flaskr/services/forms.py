from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from project.flaskr.config import LANGUAGE_MAP

class ReusableForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    handynr = StringField('HandyNr', validators=[DataRequired()])
    submit = SubmitField('Finish')

    def change_language(self, language):
        self.firstname.label.text = LANGUAGE_MAP[language].get('FirstName', 'First Name')
        self.lastname.label.text = LANGUAGE_MAP[language].get('LastName', 'Last Name')
        self.handynr.text = LANGUAGE_MAP[language].get('HandyNr', 'HandyNr')
        self.submit.text = LANGUAGE_MAP[language].get('SubmitText', 'Finish')


