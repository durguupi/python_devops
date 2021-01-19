import requests

req = requests.get('https://tools.learningcontainer.com/sample-json.json')

print(req.status_code)

# To get the JSON Output and Parse it.
json_out = req.json()

print(json_out)
print(f"FirstName: {json_out['firstName']}")

print(f"Age: {json_out['age']}")

print(f"Address: {json_out['address']}")

# To get the items of dictionary inside dictionary
print(f"Street Address: {json_out['address']['streetAddress']}")

print(f"Postal Code: {json_out['address']['postalCode']}")

# To get the phonenumbers which is in list
print(f"PhoneNumbers: {json_out['phoneNumbers']}")

print(f"PhoneNumbers_type: {json_out['phoneNumbers'][0]['type']}")

print(f"Numbers: {json_out['phoneNumbers'][0]['number']}")
