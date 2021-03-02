# Write a Python program to read first n lines of a file

with open('python-devops/workingwithfiles/basics/bookofdreams.txt', 'r') as reader:
    data = [next(reader) for x in range(3)]
    print(data)
    for line in data:
        print(line, end='')

# One More method


def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head(
    'python-devops/workingwithfiles/basics/bookofdreams.txt', 2)
