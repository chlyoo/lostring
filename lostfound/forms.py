from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField, Label, HiddenField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired
import json


class LostForm(FlaskForm):
    itemname = StringField('분실물 이름')
    with open('lostfound/category.json', 'r') as f:
        cate = list(json.load(f).items())
    category = SelectField('분류', choices=cate)
    latitude = HiddenField('위도')
    longitude = HiddenField('경도')
    place = StringField('습득장소')
    lost_date = DateTimeLocalField('분실일시')
    detail = StringField('물건의 특징')
    submit = SubmitField('신고')
    # 사진 필드 #TODO:사진필드 추가


class FoundForm(FlaskForm):
    itemname = StringField('습득품')
    with open('lostfound/category.json', 'r') as f:
        cate = list(json.load(f).items())
    category = SelectField('분류', choices=cate)
    place = StringField('습득장소')
    latitude = HiddenField('위도')
    longitude = HiddenField('경도')
    found_date = DateTimeLocalField('발견일시')
    detail = StringField('물건의 특징')
    # ownership = Label(field_id='ownership', text='<span>소유권 주장하시겠습니까?</span>')
    claim_ownership = StringField(label='ownership', render_kw={'placeholder': '소유권을 주장합니다'})
    test_ownership = RadioField(label='ownership', render_kw={'placeholder': '소유권 주장합니다', 'description': '소유권 주장합니다',
                                                              'value': '소유권 주장합니다'},
                                choices=[(True, '네'), (False, '아니오')], default=False)
    # claim_ownership = StringField(label='ownership',coerce=str, )
    submit = SubmitField('신고')
    # TODO: 사진필드 추
