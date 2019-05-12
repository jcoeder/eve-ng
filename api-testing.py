import requests
import json
import pprint

# Disable SSL Warnings
requests.urllib3.disable_warnings()

cookies = {}

data = '{"username":"admin","password":"eve"}'

try:
    response = requests.post('https://172.31.33.42/api/auth/login', cookies=cookies, data=data, verify=False)
    cookies = response.cookies
except:
    print('An error occured here')

headers = {'Content-type': 'application/json',}
try:
    response = requests.get('https://172.31.33.42/api/status', headers=headers, cookies=cookies, verify=False)
    pprint.pprint(response.json())
except:
    print('An error occured there')


try:
    response = requests.get('https://172.31.33.42/api/list/templates/', headers=headers, cookies=cookies, verify=False)
    pprint.pprint(response.json())
except:
    print('An error occured there')
