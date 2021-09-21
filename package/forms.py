from typing import ItemsView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Length, Email, DataRequired
#from package.models import User

# class LoginForm(FlaskForm):
#     username = StringField(label='User Name', validators=[DataRequired()])
#     password = PasswordField(label='Password', validators=[DataRequired()])
#     submit = SubmitField(label='Sign in')

class RequestForm(FlaskForm):
    my_choices = ["apples", "cheese", "nuclear weapons"]
    number_of_items = SelectField(label='Item:',choices=my_choices, validators=[DataRequired()])
    item = SelectField(label='Item:',choices=my_choices, validators=[DataRequired()])
    quantity = StringField(label='quantity:', validators=[DataRequired()])
    email_address = StringField(label='Student Email:', validators=[Email(), DataRequired()])
    student_id = StringField(label='Student Id:', validators=[Length(min=2,max=30), DataRequired()])

    submit = SubmitField(label='Submit form')
    