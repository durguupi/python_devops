# This will print all the lines as list
with open('python-devops/workingwithfiles/bookofdreams.txt', 'r') as file1:
    contents = file1.readlines()
    print(contents)
    print('\n=======================================================================')


print('\n=======================================================================')
# TO print lines in perfect order we can use the below way
# Now this prints in neat way
with open('python-devops/workingwithfiles/bookofdreams.txt', 'r') as file2:
    for line in file2:
        print(line, end="")

print('\n==========================================================================')
with open('python-devops/workingwithfiles/bookofdreams.txt', 'r') as file3:
    # This will print the first 100 characters of the content
    contents_read = file3.read(100)
    print(contents_read, end="")
