# Parsing Names From a CSV to an HTML List
import csv

html_output = ''
names = []

with open('python-devops/CSV_works/patexample.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    # # This prints reader object which behaves as generators so to get the output we have to loop over each line
    # print(csv_data)
    # # This prints the data in list format
    # print(list(csv_data))
# # we dont want headers and first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['seq'] == 'No Reward':
            for line in csv_data:
                names.append(f"{line['firstname']} {line['lastname']}")

# # print(names)
# for name in names:
#     print(name)

html_output += f"<p>Printing the names after no reward {len(names)} in excel. Thank you!</p>"
html_output += '\n<ul>'

for name in names:
    html_output += f"\n\t<li>{name}</li>"

html_output += '\n</ul>'
print(html_output)
