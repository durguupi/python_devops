import requests

req = requests.get('https://imgs.xkcd.com/comics/tech_support_cheat_sheet.png')

# Request.content returns the output in bytes .
# We are getting the image file and storing it with comic as name
# with open('/mnt/g/newyear_2021/python-devops/requests/comic.png', 'wb') as f:
#     f.write(req.content)

# It returns True of false based on response code of less than 400
print(req.ok)
# It returns the output in the form of key-value pairs (like dictionary)
print(req.headers)
# From the headers output I am gettin the value of only server key
print(req.headers['server'])

print(f"Connection Type: {req.headers['connection']}")
print(f"Image Type: {req.headers['content-Type']}")
