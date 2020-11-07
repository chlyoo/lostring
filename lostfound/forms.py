from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, BooleanField, RadioField, Label
from wtforms.validators import DataRequired
import json


class LostForm(FlaskForm):
    itemname = StringField('분실물')
    with open('lostfound/category.json', 'r') as f:
        cate = list(json.load(f).items())
    category = SelectField('분류', choices=cate)
    place = StringField('분실장소')  # 이부분은 지도에서 핀을 설정해서 좌표를 가져와야 함
    lost_date = DateTimeField('분실일시')
    detail = StringField('물건의 특징')
    submit = SubmitField('등록')
    #사진 필드 #TODO:사진필드 추가


class FoundForm(FlaskForm):
    itemname = StringField('습득품')
    with open('lostfound/category.json', 'r') as f:
        cate = list(json.load(f).items())
    category = SelectField('분류', choices=cate)
    place = StringField('습득장소')  # 이부분은 지도에서 핀을 설정해서 좌표를 가져와야 함
    found_date = DateTimeField('발견일시')
    detail = StringField('물건의 특징')
    text = Label('ownership',text='소유권 주장')
    claim_ownership = RadioField(label='ownership', choices=[(True, '네'), (False, '아니오')], default=False)
    submit = SubmitField('등록')
    #TODO: 사진필드 추
