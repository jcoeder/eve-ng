import requests

# Disable SSL Warnings
requests.urllib3.disable_warnings()

cookies = {}

data = '{"username":"admin","password":"eve"}'

response = requests.post('https://172.31.33.42/api/auth/login', cookies=cookies, data=data, verify=False)

print(response)
print(response.text)
print(cookies)
