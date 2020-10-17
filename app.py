from flask import Flask, url_for
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from model import LostFound
from service import SearchService
from config import config
from flask_moment import Moment
import pymongo


from flask_login import LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()

conn = pymongo.MongoClient('mongodb://db:27017')
db = conn.get_database('LostnFound')
lostdata = LostFound(db)
service = SearchService(lostdata)

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True, static_folder='static', static_url_path='')
	app.config.from_object(config[config_name])
	app.config.from_pyfile('config.py')
	config[config_name].init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	moment.init_app(app)

	from main import main as index_blueprint
	app.register_blueprint(index_blueprint)

	from api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix="/api")

	from auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix="/auth")

	return app
	#app.run(host='localhost', port=80)
