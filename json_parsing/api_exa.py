import requests
import json

req = requests.get("https://anapioficeandfire.com/api/characters")

source = req.text

data = json.loads(source)
# print(data)

# print(len(data))  # This prints the number of items in data

# # This converts the string to JSON object so we can read better from it
# print(json.dumps(data, indent=2))

# # Loopin using for loop to get the values and print it

# for item in data:
#     print(f"URL: {item['url']}")
#     print(f"Culture: {item['culture']}")
#     print(f"Gender: {item['gender']}")
#     print(f"Books: {item['books']}")

new_dict = {}
for item in data:
    url = item['url']
    books = item['books']
    new_dict[url] = books

print(new_dict)
print("================================================================")
print(new_dict['https://anapioficeandfire.com/api/characters/4'])
# Getting the first list value of the values
print(new_dict['https://anapioficeandfire.com/api/characters/4'][0])
