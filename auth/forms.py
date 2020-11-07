from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email

from wtforms import ValidationError
from app import db


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])

    name = StringField('Username',
                       validators=[DataRequired(), Length(1, 64), Regexp('^[가-힣A-Za-z][가-힣A-Za-z0-9_.]*$', 0,
                                                                             'Usernames must have only letters, '
                                                                             'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password2',
                                                             message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        collection = db.get_collection('users')
        results = collection.find_one({'id': field.data})
        if results is not None:
            raise ValidationError('Email already registered.')
        pass

    # def validate_username(self, field):
    #     collection = db.get_collection('users')
    #     results = collection.find_one({'username': field.data})
    #     if results is not None:
    #         raise ValidationError('Username already registered.')
    #     pass
