# Write a function in Python to count uppercase character in a text file.

def func_uppercase(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        words = data.split()
        count_upper = 0
        count_lower = 0
        for word in words:
            if word[0].isupper():
                count_upper += 1
                print(word)
            count_lower += 1
        print(f"Upper case letter: {count_upper}")
        print(f"Lower case letter: {count_lower}")


func_uppercase(
    'python-devops/workingwithfiles/practise_exercises/basics/story.txt')

# Easy Method


def count_letter():
    file = open(
        'python-devops/workingwithfiles/practise_exercises/basics/story.txt', "r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count += 1
    print(count)


count_letter()
