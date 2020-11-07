from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email

from wtforms import ValidationError
from app import db


class LoginForm(FlaskForm):
    email = StringField('이메일', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    remember_me = BooleanField('로그인 유지')
    submit = SubmitField('로그인')


class RegistrationForm(FlaskForm):
    email = StringField('이메일', validators=[DataRequired(), Length(1, 64), Email()])

    name = StringField('이름',
                       validators=[DataRequired(), Length(1, 64), Regexp('^[가-힣A-Za-z][가-힣A-Za-z0-9_.]*$', 0,
                                                                             'Usernames must have only letters, '
                                                                             'numbers, dots or underscores')])
    password = PasswordField('비밀번호', validators=[DataRequired(),
                                                     EqualTo('password2',
                                                             message='Passwords must match.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    submit = SubmitField('회원가입')

    def validate_email(self, field):
        collection = db.get_collection('users')
        results = collection.find_one({'id': field.data})
        if results is not None:
            raise ValidationError('이미 등록된 이메일 입니다.')
        pass

    # def validate_username(self, field):
    #     collection = db.get_collection('users')
    #     results = collection.find_one({'username': field.data})
    #     if results is not None:
    #         raise ValidationError('Username already registered.')
    #     pass
