# Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.

def func1(filename):
    with open(filename, 'r') as file1:
        for line in file1:
            print(line, end='')


func1('python-devops/workingwithfiles/basics/bookofdreams.txt')
