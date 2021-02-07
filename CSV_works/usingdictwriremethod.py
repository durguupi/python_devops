import csv
# csv.DictReader() on the other hand is friendlier and easy to use, especially when working with large CSV files
# The csv.DictReader class operates like a regular reader but maps the information read into a dictionary.
# The keys for the dictionary can be passed in with the fieldnames parameter or inferred from the first row of the CSV fil


with open('/mnt/g/newyear_2021/python-devops/CSV_works/sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
    #     print(line['date'])

    with open('/mnt/g/newyear_2021/python-devops/CSV_works/withdictsample.csv', 'w') as new_file:
        fieldnames = ['seq', 'firstname', 'lastname',
                      'age', 'city', 'state', 'zip']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            del line['dollar']
            del line['street']
            del line['pick']
            del line['date']
            csv_writer.writerow(line)
