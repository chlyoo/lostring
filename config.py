import os
# PUBLIC_DATA_SERVICE_KEY
PUBLIC_DATA_SERVICE_KEY = "Your-Public-Data-Service-Key"
PUBLIC_DATA_REQUEST_URL = "Your-data-request-url"
KAKAO_APP_KEY = 'Your-Kakao-API-Key'
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
