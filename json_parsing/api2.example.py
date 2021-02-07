import requests
import json

req = requests.get('https://jsonplaceholder.typicode.com/posts/')

source = req.text

# print(source)

data = json.loads(source)

# print(data)
new_data = {}
for useid in data:
    id_use = useid['id']
    title = useid['title']
    new_data[id_use] = title
# Ths prints the dictionary of items with id and title
# print(new_data)

new_json = json.dumps(new_data, indent=2)
print(new_json)
