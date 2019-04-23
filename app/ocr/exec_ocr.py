#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from rules_of_ocr import ocr_extract

arquivo = 'comp-pgto-2019-02-12T102940.jpg'
df = ocr_extract(arquivo)
'''
# Regex para capturar data
data_padrao = "\d{2}\/(?P<mes>\d{2})\/2019"
valor_padrao = "[-+]?\d*\,\d+|\d+"
nome_padrao = "SKY"

data_pagto = []
marca = []
valor = []
for d in df:
    print("Start a process")
    data_pagto = re.findall(data_padrao, d)
    marca = re.findall(nome_padrao,d)
    valor = re.findall(valor_padrao,d)
    try:
        valor = float(valor)
    except:
        valor = 0
    print("End process")
    print(data_pagto, marca, valor)
data_pagto, marca, valor
#res = ocr(arquivo)
#res2 = res.return_ocr()
#rint(res2)
'''