# A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is
# separated by a symbol "#". Write a function definition for hash_display() in Python that would display
# the entire content of the file matter.txt in the desired format.

def hash_display(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        words = data.split()
        for word in words:
            word = '#' + word
            print(word, end='')


hash_display(
    'python-devops/workingwithfiles/practise_exercises/basics/story.txt')

# Easy method


def hash_display1(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        for letter in data:
            print(letter, end='#')


hash_display1(
    'python-devops/workingwithfiles/practise_exercises/basics/story.txt')
