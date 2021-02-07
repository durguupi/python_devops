import json

people_string = '''
{
   "people":[
      {
         "name":"Joe done",
         "company":"JJJ technologies",
         "type":"sales",
         "emails": null,
         "has_license":true,
         "code":{
            "pincode":[
               255,
               255,
               255,
               1
            ],
            "addr":"8989"
         }
      },

    {
         "name":"Lucas James",
         "company":"RK technologies",
         "type":"Marketing",
         "emails":"lucasss@example.com",
         "has_license":false,
         "code":{
            "pincode":[
               5,
               1
            ],
            "addr":"US"
         }
      }
   ]
}
'''

# Load method loads file into python objects and loads method loads string into python objects
data = json.loads(people_string)
# # Notes: true value converts to True in python and null converts to None.
print(data)
# Here the type of data will be dictionary
print(f"Type of Json data after parsing in python: {type(data)}")
print(data['people'])
# And the people type will be in list
print(f"Type of people data: {type(data['people'])}")

# looping to print each of the person

for person in data['people']:
    print(person['name'])
    print(person['company'])

# Converting json back to string after deleting few records

for pers in data['people']:
    del pers['code']

# This prints the new string with indent space of 2 and with sorted values in alphabetical order
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
