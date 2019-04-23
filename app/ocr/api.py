#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eve import Eve
from rules_of_ocr import ocr_extract

app = Eve()

class CallApiOcr():
    def check_auth(self, firstname, method):
        if firstname == "Leandro" and method == "GET":
            arquivo = 'comp-pgto-2019-02-12T102940.jpg'
            df = ocr_extract(arquivo)
        return df

if __name__ == '__main__':
    app = Eve(auth=CallApiOcr())
    app.run()