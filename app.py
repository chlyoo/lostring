from flask import Flask, url_for
from flask_bootstrap import Bootstrap
from model import LostFound
from service import SearchService
from config import config
import pymongo


conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('LostnFound')
bootstrap = Bootstrap()

lostdata = LostFound(db)
service = SearchService(lostdata)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py')
    config[config_name].init_app(app)
    bootstrap.init_app(app)

    from main import main as index_blueprint
    app.register_blueprint(index_blueprint)

    from api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
    #app.run(host='localhost', port=80)
