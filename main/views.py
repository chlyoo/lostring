from flask import url_for, render_template, flash
from werkzeug.utils import redirect

from app import service
from . import main
from .forms import SearchForm
from config import *
from instance.config import *

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('bootstrap/index.html', KAKAO=KAKAO_APP_KEY)

