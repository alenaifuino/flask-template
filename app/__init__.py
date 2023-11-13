import logging
from flask import Flask
from config import Config
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config.from_object(Config)

# Configuration for media files
app.config['MEDIA_FOLDER'] = 'media'

# Configures the logging
def configure_logging(app):
    # Create a file handler which logs even debug messages
    handler = TimedRotatingFileHandler('flask-template.log', when='midnight', interval=1, backupCount=10)
    handler.setLevel(logging.INFO)  # Set the log level you want here
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

configure_logging(app)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)
