from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ReusableForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    handynr = StringField('HandyNr', validators=[DataRequired()])
    submit = SubmitField('Finish')