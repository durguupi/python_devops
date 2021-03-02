# Write a function in Python to count and display the total number of words in a text file
def func1(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        words = data.split()

    print(data)
    print(words)
    print(f"Total No of Words: {len(words)}")


func1('python-devops/workingwithfiles/practise_exercises/basics/story.txt')
