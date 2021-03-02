# Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T".


def func1(filename):
    count = 0
    with open(filename, 'r') as file1:
        for line in file1:
            if not line.startswith("T"):
                count += 1
    print(count)


func1('python-devops/workingwithfiles/practise_exercises/basics/story.txt)
