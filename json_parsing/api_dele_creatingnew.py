import requests

import json

req = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

source = req.text

# print(data)

data = json.loads(source)
for todo in data:
    del todo['userId']

# print(data)
new_json = json.dumps(data, indent=2)

print(new_json)
