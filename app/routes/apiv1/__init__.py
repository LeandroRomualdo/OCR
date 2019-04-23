#!/usr/bin/python3
from flask import Blueprint
from flask_restplus import Api

from .predict import predict


api_v1 = Blueprint('api', __name__, url_prefix='/v1')

api = Api(api_v1,
          title='Ocr Model',
          version='1.0',
          description='It is an api to OCR Model',
          )

api.add_namespace(predict)