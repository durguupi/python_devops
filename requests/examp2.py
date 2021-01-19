import requests

payload = {'int': '1'}
req_range = requests.get('https://httpbin.org/stream/1', params=payload)
# print(req_range.text)
print(req_range.headers)
print(f"URL: {req_range.url}")
json_out = req_range.json()
# JSON Out was available only for int value 1.Its because of the api problem in the URL
print(json_out)
print(
    f"ID: {json_out['id']}, ARGS: {json_out['args']}, ARGS_INT_VALUE: {json_out['args']['int']}")
