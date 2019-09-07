from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# class RegistrationForm(FlaskForm):
#
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password',
#                                      validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')
#
#
# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

class ReusableForm(Form):

    # name = TextField('From:', validators=[validators.required()])
    source = TextField('source:', validators=[validators.required()])
    destination = TextField('destination:', validators=[validators.required()])
    # source = StringField('source', validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
    # destination = StringField('destination', validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
