import requests

# req_ip = requests.get('https://httpbin.org/ip')

# print(req_ip.text)

# req_base = requests.get(
#     'https://httpbin.org/base64/bGlmZWlzYXdlc29tZQ%20%3D%3D')
# print(req_base.text)

payload = {'undefined': 'undefined', 'name': 'beeb'}
req_cookies = requests.get(
    "https://httpbin.org/cookies/set/name/beeb", params=payload)
print(req_cookies.text)
