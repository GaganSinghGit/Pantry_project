from typing import ItemsView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import Length, Email, DataRequired
#from package.models import User

# class LoginForm(FlaskForm):
#     username = StringField(label='User Name', validators=[DataRequired()])
#     password = PasswordField(label='Password', validators=[DataRequired()])
#     submit = SubmitField(label='Sign in')

class RequestForm(FlaskForm):
    #my_choices = ["apples", "cheese", "nuclear weapons"]

    student_id = IntegerField(label='Student Id:', validators=[ DataRequired()])
    student_name = StringField(label='Student Name:', validators=[Length(min=2,max=50), DataRequired()])
    phone_number = StringField(label='Phone number:', validators=[DataRequired()])
    email_address = StringField(label='Student Email:', validators=[Email(), DataRequired()])
    group_number = StringField(label='Group number:', validators=[DataRequired()])
    item_id = StringField(label='Item ID:', validators=[DataRequired()])
    item_name = StringField(label='Item Name:', validators=[DataRequired()])
    item_quantity = StringField(label='quantity:', validators=[DataRequired()])
    delivery_date = StringField(label='Delivery Date:', validators=[DataRequired()])
    comments = StringField(label='Comments:')
    submit = SubmitField(label='Submit form')

class ShoppingListAddNewItem(FlaskForm):

    item_name = StringField(label='Item Name:', validators=[DataRequired()])
    individual_weight = StringField(label='Individual Weight:', validators=[DataRequired()])
    category = StringField(label='Category:', validators=[DataRequired()])
    expriry_date = StringField(label='Exprire Date:', validators=[DataRequired()])
    barcode = StringField(label='Barcode:', validators=[DataRequired()])
    container_id = StringField(label='Container ID:', validators=[DataRequired()])
    alert_at = StringField(label='Alert at:', validators=[DataRequired()])
    quantity = StringField(label='Quantity:', validators=[DataRequired()])
    submit = SubmitField(label='AddItem')