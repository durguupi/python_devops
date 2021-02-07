import json

with open('python-devops/json_parsing/colors.json') as colors:
    data = json.load(colors)

# print(data)

# Now using for loop we will delete some values

for color in data['colors']:
    del color['code']

# # Now we are convering it to new_color as JSON object dumps method converts data into JSON string
# new_color = json.dumps(data, indent=2, sort_keys=True)
# print(new_color)

# dump method converts data into JSON file
# what we want to dump is data and where it is file . new json file will be generated with code value deleted
with open('python-devops/json_parsing/new_colors.json', 'w') as file:
    json.dump(data, file, indent=2)
