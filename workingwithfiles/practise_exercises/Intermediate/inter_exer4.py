# Write a python program to find the longest words
with open("python-devops/workingwithfiles/practise_exercises/Intermediate/input.txt", "r") as file2:
    data = file2.read()
    words = data.split()
    # print(words)
    largest_word = words[0]
    # print(len(largest_word))
    new_word = ''
    for word in words:
        if len(word) > len(largest_word):
            new_word = word
            largest_word = new_word
        else:
            new_word = largest_word
    print(f'The largest word in the {file2.name} is : {new_word}')
