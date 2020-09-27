import os
from flask_script import Manager, Server
from app import create_app
import ssl

if __name__ == "__main__":
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    #
    # twisted = Twisted(app)
    # log.startLogging(sys.stdout)
    # app.logger.info("Running the app")

    manager = Manager(app)
    manager.add_command("runserver", Server(host='0.0.0.0',port=5000,ssl_crt='certificate.crt', ssl_key='private.key'))
    #manager.add_command("runserver", Server(host=os.getenv('FLASK_RUN_HOST'), port=os.getenv('FLASK_RUN_PORT')))
    manager.run()
