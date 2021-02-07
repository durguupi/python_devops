import csv
# csv.Reader() allows you to access CSV data using indexes and is ideal for simple CSV files.
with open('/mnt/g/newyear_2021/python-devops/CSV_works/sample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('/mnt/g/newyear_2021/python-devops/CSV_works/new_sample.csv', 'w') as new_file:
        # All got printed in one col
        # csv_writer = csv.writer(new_file, delimiter='\t')
        # If we dont give any delimiter means it uses default delimiter which is ", " and it gives copy of same file format
        csv_writer = csv.writer(new_file)

# This loop deletes the last list(last col) in this sample.csv and prints the new file
        for line in csv_reader:
            del line[-1]
            csv_writer.writerow(line)
