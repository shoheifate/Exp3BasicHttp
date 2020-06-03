import requests

req = requests.get('http://localhost:8080/hi')
print(req.text)
