# Write a Python program to count the frequency of particular word in a file
def frequency(filename, word_search):
    with open(filename, 'r') as reader:
        data = reader.read()
        words = data.split()
        count_fre = 0
        for word in words:
            if word == word_search:
                count_fre += 1
    print(f"The frequency of word {word_search} is : {count_fre}")


frequency(
    'python-devops/workingwithfiles/practise_exercises/Intermediate/input.txt', 'Hello')
