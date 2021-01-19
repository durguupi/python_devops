import requests

# To set timeout to some seconds so it will return timeout error if the website doesnt respond within the time
# otherwise it will wait indefnitely for response


req = requests.get('https://httpbin.org/delay/6', timeout=3)
# This will return timeout error since we have set to timeout to 3 if we dont have any
print(req)
