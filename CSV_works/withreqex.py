import requests
import csv
import json

req = requests.get('https://jsonplaceholder.typicode.com/posts/')

source = req.text
data = json.loads(source)
# print(source)
with open('python-devops/CSV_works/apiposts.csv', 'w') as csv_file:
    fieldnames = ['userId', 'id', 'title', 'body']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    for line in data:
        csv_writer.writerow(line)
