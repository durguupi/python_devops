# Write a function in Python to count words in a text file those are ending with alphabet "e"

def count_e(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        words = data.split()
        count_e = 0
        for word in words:
            # print(word)
            if word[-1] == 'e':
                count_e += 1
                # print(word)
        print(count_e)


count_e('python-devops/workingwithfiles/practise_exercises/basics/story.txt')
