# Write a function in Python to count the words "this" and "these" present in a text file "story.txt"

def func_count(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        count_this = 0
        count_these = 0
        words = data.split()
        for word in words:
            if word == "This":
                count_this += 1
            if word == "These":
                count_this += 1
        total = count_these + count_this
        print(total)


func_count('python-devops/workingwithfiles/practise_exercises/story.txt')

# Simplified version of above code


def func_count1(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        count_data = 0
        words = data.split()
        for word in words:
            if word == "This" or word == "These":
                count_data += 1
        print(count_data)


func_count1('python-devops/workingwithfiles/practise_exercises/basics/story.txt)
