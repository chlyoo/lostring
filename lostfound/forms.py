from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField, HiddenField, ValidationError
from wtforms.fields.html5 import DateTimeLocalField, DateTimeField
from wtforms.validators import DataRequired, InputRequired, Required
import json
from datetime import datetime


class LostForm(FlaskForm):
    itemname = StringField('분실물 이름', [DataRequired()])
    with open('lostfound/category.json', 'r') as f:
        cate = list(json.load(f).items())
    category = SelectField('분류', choices=cate)
    latitude = HiddenField('위도', [InputRequired("지도에서 분실 위치를 지정해주세요")])
    longitude = HiddenField('경도')
    place = StringField('습득장소')
    lost_date = DateTimeLocalField('분실일시', validators=[InputRequired('시간을 입력해주세요')], format='%Y-%m-%dT%H:%M',default= datetime.utcnow)
    detail = StringField('물건의 특징')
    submit = SubmitField('등록')
    # 사진 필드 #TODO:사진필드 추가


class FoundForm(FlaskForm):
    itemname = StringField('습득품')
    with open('lostfound/category.json', 'r') as f:
        cate = list(json.load(f).items())
    category = SelectField('분류', choices=cate)
    place = StringField('습득장소')
    latitude = HiddenField('위도', [DataRequired("지도에서 습득 위치를 지정해주세요")])
    longitude = HiddenField('경도')
    lost_date = DateTimeLocalField('발견일시', validators=[InputRequired('시간을 입력해주세요')], format='%Y-%m-%dT%H:%M',default= datetime.utcnow)
    detail = StringField('물건의 특징')
    label = StringField(label = '소유권을 주장하시겠습니까?', render_kw={'type':'hidden'})
    check_ownership = RadioField(label='ownership', choices=[(True, '네'), (False, '아니오')], default=False)
    sign_owner = StringField(label="", render_kw={'placeholder':'소유권을 주장합니다', 'type':'hidden'})
    submit = SubmitField('등록')

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        print(self.check_ownership.data)
        if self.check_ownership.data:
            self.validate_sign_owner()
        return True

    def validate_sign_owner(self, field):
        if '소유권을 주장합니다' not in field.data:
            raise ValidationError('정확히 입력하세요')


# TODO: 사진필드 추가
