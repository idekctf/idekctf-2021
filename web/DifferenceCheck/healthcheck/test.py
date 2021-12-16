import requests

url = "http://localhost:1337/flag"

r = requests.get(url)

print(r.text)
