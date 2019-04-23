#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
'''
export AWS_ACCESS_KEY_ID="ASIA2QGPBJYY5TL4MAKO"
export AWS_SECRET_ACCESS_KEY="W0Q4/nQ6ViuhDL7GiLPcsCD1aSj4sU8CkVo+UqXf"
export AWS_SESSION_TOKEN="FQoGZXIvYXdzEDUaDByvRVJz8UvwndWICSKmAu9WmtuwCKgTZmr79PDamjOqtxkb9jKZr14WqtyjbOQADsQ8MX8qpgxuJvUDyQZJxmzIi70g/LIXzJw19cQO3Ce7euVNs1VXb6Nt0BhMDrwOZ3kwFrT9r7dpzxlOswXqC1sqGPcgKvDcAjMDpsKiBthtF4S7wImU2kxnBFQyq+Vgn7x56fQWPMTxRBrWXheSL4ASdcQCDRVtaYCPHzszIt3vOjS5z2A0PDhUUNKcd97yLLUByKaKnyS9wXGxPmXnJCPWSE2/RxHH0zhvKhOLMNiGD1nJYviDATKErOcYB6aXLRyBu3B7ym64tlkAeDWzExipbizP/CjOTTETl1wehOH9RBATvXqmTN5kYcL52m7jgr2mTs7VuSXysY3kfouoIIZVH9CjVCiy4dHlBQ=="
'''

class ocr:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def return_ocr(self):

        client=boto3.client('rekognition')
        with open(self.arquivo, 'rb') as image:
            response = client.detect_text(Image={'Bytes': image.read()})

        textDetections=response['TextDetections']

        df =[]
        for text in textDetections:
            df.append(text['DetectedText'])

        print(df)
        return df