import requests

req = requests.get('http://localhost:8080/')
print(req.text)
