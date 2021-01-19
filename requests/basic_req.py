import requests

req = requests.get('https://xkcd.com/353/')
print(f"Response code:{req.status_code}")

#  Response of the contents of the page in html
print(req.text)

# print(help(requests))
print(req.content)
print(req.headers)
