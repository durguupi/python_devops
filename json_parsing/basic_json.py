import json
# Load method loads file into python objects and loads method loads string into python objects
with open('python-devops/json_parsing/colors.json') as colors:
    data = json.load(colors)

# # print(data)
# print(type(data))
# print("=======================================================")
# print(data['colors'][0])

# # This will be list of values
# print((data['colors']))

# Using loops we will print the objects needed

for color in data['colors']:
    print(color)

# This loops through each object in colors and prints only the required color and catgory values
for color in data['colors']:
    print(color['color'], color['category'])

# Now lets loop through code and print only the first and last values of rgba

for colorrgba in data['colors']:
    print(
        f"RGBA VALUES: {color['code']['rgba'][0]}, {color['code']['rgba'][-1]}")
    print(f"HEX VALUES: {color['code']['hex']}")
