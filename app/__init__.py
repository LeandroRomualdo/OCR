from flask import Flask

from app import configuration
from app.routes.apiv1 import api_v1
from app.extensions import cors



def create_app(config=configuration.PrdConfig):
    application = Flask(__name__)
    application.config.from_object(config)
    

    register_blueprint(application)
    register_extensions(application)
    application.config['UPLOAD_FOLDER'] = '/ocr/uploads'

    
    return application


def register_blueprint(application):
    application.register_blueprint(api_v1)


def register_extensions(application):
    cors.init_app(application)