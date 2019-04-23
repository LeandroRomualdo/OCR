#!/usr/bin/env python
# -*- coding: utf-8 -*-

from call_ocr_aws import ocr

# Extrai os dados do documento e salva em uma lista.
def ocr_extract(arquivo):

    #arquivo = 'comp-pgto-2019-02-12T102940.jpg'
    res = ocr(arquivo)
    res2 = res.return_ocr()
    return res2

# Função para data e valores.
def get_data(value):
    if value.strip().replace('/','-').isdigit():
        return value.asDateTime()
    else:
        try:
            print(float(value))
        except ValueError:
            return False
    return True

# Valida se temos alguma data de pagamento menor que três dias, valores pagos e identificação SKY.
def ocr_rules(dados_ocr):
    
    filtered_data = []
    for text in dados_ocr:
        filtered_data.append =  get_data(text)
    return filtered_data

