import requests

req = requests.get('http://localhost:8081/hi')
print(req.text)
