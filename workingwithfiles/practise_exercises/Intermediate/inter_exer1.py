# Write a Python program to append text to a file and display the text.

with open('python-devops/workingwithfiles/practise_exercises/Intermediate/input.txt', 'a+') as file1:
    data = file1.write('Hello How are you doing\t 45')
    data = file1.write(
        '\nThis is one more new line\nPython is aswesome programming language')

with open('python-devops/workingwithfiles/practise_exercises/Intermediate/input.txt', 'r') as reader:
    # data = reader.readlines()
    data = reader.read()
    print(data)
