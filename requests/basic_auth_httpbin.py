import requests

# To test the basic authentication in this site we can specify the username and pwd in
# URL and then test it against the auth param we provide and testing the basic authentication
# In Auth we have tp pass in tuple
req = requests.get(
    'https://httpbin.org/basic-auth/james/testing', auth=('james', 'testing'))


# This prints the response code
print(req)
print(req.text)

req_auth = req.json()
print(req_auth['authenticated'])
