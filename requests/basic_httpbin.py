import requests

req = requests.get('https://httpbin.org/get')
# Gets the html reponse of that page
# print(req.text)
print(req.status_code)

# Returns the output in Json format
# JSON has created python dictionary for us to access the variables
print(req.json())

# For getting the response and getting values from the output we will store it in some variable and
# from it we will request data
json_out = req.json()
print(json_out['origin'])
print(json_out['url'])
