# Write a function display_words() in python to read lines from a text file "story.txt",
# and display those words, which are less than 4 characters


def display_words(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        words = data.split()
        for word in words:
            if len(word) <= 4:
                print(word)


display_words(
    'python-devops/workingwithfiles/practise_exercises/basics/story.txt')
