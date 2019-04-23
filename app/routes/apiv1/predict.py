#!/usr/bin/python3
import spacy
from flask import jsonify, request,flash,redirect
import logging
from flask_restplus import Namespace, Resource
from collections import defaultdict
from app.ocr.call_ocr_aws import ocr
from werkzeug.utils import secure_filename
from werkzeug import FileStorage
import os
import re
import datetime


predict = Namespace('predict')

upload_parser = predict.parser()
upload_parser.add_argument('file', location='files',
                  type=FileStorage, required=True)

@predict.route('/')
@predict.expect(upload_parser)
class OCRPredict(Resource):
    
    def post(self):
        
        if 'file' not in request.files:
            flash("Arquivo não encontrado!")
            return redirect(request.url)
            
        _file = request.files['file']
        if _file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        filename = secure_filename(_file.filename)
        _file.save(os.path.join('./app/ocr/uploads', filename))
        _ocr = ocr('./app/ocr/uploads/'+filename)
        text_in_list =  _ocr.return_ocr()
        text_in = ' '.join(text_in_list)
        all_payment_dates = re.findall(r'\d{2}/\d{2}/\d{4}',text_in)
        all_payment_value = re.findall(r'R\$\s\d+,?\.?\d{2}',text_in)
        all_payment_name = re.findall(r' SKY ',text_in)
        all_payment_type = re.findall(r' Comprovante ',text_in)

        # Pega data atual
        data_atual = datetime.datetime.now()
        data_atual_saida = time = data_atual.strftime("%d/%m/%y")

        # Trata erros
        payment_dates = '' if len(all_payment_dates) == 0 else all_payment_dates[0]
        payment_value = 0 if len(all_payment_value) == 0 else all_payment_value[0]
        payment_name = '' if len(all_payment_name) == 0 else all_payment_name[0]
        payment_type = '' if len(all_payment_type) == 0 else all_payment_type[0]

        diff = 0
        if(payment_dates):
            date_parts = payment_dates.split('/')
            payment_dates = datetime.datetime(int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))
            diff = abs((data_atual-payment_dates).days)
            
        try:
            return {'date' : payment_dates.strftime("%d/%m/%y"), 'value' : payment_value, 'Name' : payment_name,
            'type' : payment_type, 'current date' : data_atual_saida, 'days': diff}
        except:
            return 'Values not found!'