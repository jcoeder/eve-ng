import requests
import json
import pprint

# Disable SSL Warnings
requests.urllib3.disable_warnings()

cookies = {}

data = '{"username":"admin","password":"eve"}'

session = requests.Session()

response = session.post('https://172.31.33.42/api/auth/login', data=data, verify=False)

headers = {'Content-type': 'application/json',}
response = session.get('https://172.31.33.42/api/status', headers=headers, verify=False)
pprint.pprint(response.json())

headers = {'Content-type': 'application/json',}
response = session.get('https://172.31.33.42/api/list/templates/', headers=headers, verify=False)
pprint.pprint(response.json())
