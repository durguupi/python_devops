import requests

payload = {'Page': '23', 'Content': 'Textformat'}
# This site helps us in testing the different web requests methods
req = requests.get("https://httpbin.org/get", params=payload)

# Here we will get the output of get request with the args paramter passed
# print(req.text)
# JSON has created python dictionary for us to access the variables
print(req.json())
# This will print the updates URL with payload we passed
# https://httpbin.org/get?Page=23&Content=Textformat

print(req.url)
json_out = req.json()
print(json_out['args'])
print(json_out['args']['Content'])
