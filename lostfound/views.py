from flask import render_template, send_from_directory, request

from app import service
from . import lostfound
from .forms import LostForm, FoundForm
from config import *
from instance.config import *


@lostfound.route('/lost', methods=['GET', 'POST'])
def register_lost():
    form = LostForm()
    #TODO: 폼데이터 분실 디비에 저장
    return render_template('bootstrap/register.html', form = form)

@lostfound.route('/found', methods=['GET', 'POST'])
def register_found():
    form = FoundForm()
    #TODO: 폼에서 발견 디비에 저장
    #TODO: Register Service 랑 연동
    return render_template('bootstrap/register.html', form = form)

@lostfound.route('/show_lost', methods=['GET', 'POST'])
def show_lost():
    #TODO: MongoDB load data
    l_tems = ['item1','item2','item3']
    return render_template('bootstrap/lost.html', lostitem = l_tems)

@lostfound.route('/show_found', methods=['GET', 'POST'])
def show_found():
    #TODO: MongoDB load data
    #TODO: Search 기능 ( search_service 연동)
    f_item = ['founditem1','founditem2','founditem3']
    return render_template('bootstrap/found.html', founditem= f_item)

@lostfound.route('/my_page', methods=['GET','POST'])
def my_page():
    pass
    return render_template('bootstrap/mypage.html')
