import requests

endpoint = 'http://127.0.0.1:5000'

response = requests.get(endpoint).json()

print(response['hello'])
