import csv
# csv.Reader() allows you to access CSV data using indexes and is ideal for simple CSV files.
with open('/mnt/g/newyear_2021/python-devops/CSV_works/sample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# This prints out only the memory location of CSV object. To get the contents of CSV file we have to iterate over it
    # print(csv_reader)

# While iterating through the CSV file if we want to omit the first value of the file then we can use the below method to do that
# This method is from generators where it loops over the line one by one
    next(csv_reader)

    for line in csv_reader:
        # print(line)
        print(f"Firstname: {line[1]}, AGE: {line[3]}, CITY: {line[5]}")

    #print(f"LENGTH: {len(line)}")
