# when running this program i have not created any files as copy_books.txt .
# It gets automatically created when we run this program with contents of bookofdreams.txt file

with open('/mnt/g/newyear_2021/python-devops/workingwithfiles/bookofdreams.txt', 'r') as rf:
    with open('/mnt/g/newyear_2021/python-devops/workingwithfiles/copy_books.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
