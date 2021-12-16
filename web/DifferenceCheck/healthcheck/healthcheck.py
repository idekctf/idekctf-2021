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

url1 = "http://localhost:1337/flag"
url2 = "http://localhost:1337/diff"

test_payload = {"url1": "http://google.com", "url2": "http://example.com"}

r = requests.get("http://localhost:1337/flag")
if 'idek' not in r.text:
    print("/flag failed")
    exit(1)

r = requests.post("http://localhost:1337/diff", data=test_payload)
if 'Difference Output' not in r.text:
    print("/diff failed")
    exit(1)

exit(0)
