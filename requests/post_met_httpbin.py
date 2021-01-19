import requests

payload = {'username': 'James', 'password': 'Testing'}
# Since we are post we are posting some data so we use data here.
req = requests.post('https://httpbin.org/post', data=payload)
print(req.json())
# JSON has created python dictionary for us to access the variables
json_out = req.json()
print(json_out['form'])
