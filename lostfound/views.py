from flask import render_template, send_from_directory, request

from app import service
from flask_login import login_required
from . import lostfound
from .forms import LostForm, FoundForm
from config import *
from instance.config import *


@lostfound.route('/lost', methods=['GET', 'POST'])
@login_required
def register_lost():
    form = LostForm()
    #TODO: 폼데이터 분실 디비에 저장
    return render_template('bootstrap/register.html', form = form)

@lostfound.route('/found', methods=['GET', 'POST'])
@login_required
def register_found():
    form = FoundForm()
    #TODO: 폼에서 발견 디비에 저장
    #TODO: Register Service 랑 연동
    return render_template('bootstrap/register.html', form = form)

@lostfound.route('/my_page', methods=['GET','POST'])
@login_required
def my_page():
    pass
    return render_template('bootstrap/mypage.html')
