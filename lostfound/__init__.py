from flask import Blueprint

lostfound = Blueprint('lostfound', __name__)

from . import views



