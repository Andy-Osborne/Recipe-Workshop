from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class UserRegistration(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=3, max=20),
                                       Regexp('^[a-zA-Z0-9]*$',
                                              message="Please use only \
                                                   lowercase, uppercase or \
                                                        numbers")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     Length(min=8)])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(),
                                                 EqualTo("password")])
    submit = SubmitField("Sign Up")


class UserLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
