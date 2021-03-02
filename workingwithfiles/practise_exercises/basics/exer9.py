# Write a function AMCount() in Python, which should read each character of a text file STORY.TXT,
# should count and display the occurance of alphabets A and M (including small cases a and m too).

def AMCount(filename):
    with open(filename, 'r') as file1:
        data = file1.read()
        count_a = 0
        count_m = 0
        for letter in data:
            if letter == 'A' or letter == 'a':
                count_a += 1
            if letter == 'M' or letter == 'm':
                count_m += 1
        print(f"A or a: {count_a}")
        print(f"M or m: {count_m}")


AMCount('python-devops/workingwithfiles/practise_exercises/basics/story.txt')
