from . import api
from app import service
from flask import jsonify


@api.route("/ping", methods=['POST'])
def ping():
    return "pong"


@api.route('/<symbol>', methods=['POST'])
def search(symbol):
    result = service.get_maxprofit_highlow(symbol)
    if result is not None:
        return jsonify({'buy': result[0], 'sell': result[1]}), 200
    else:
        return "Couldn't find any stock data. Try Again!", 404
