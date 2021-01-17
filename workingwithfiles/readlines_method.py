# This method reads the file and splits its contents on newline characters. It returns a list of strings.
# Each string is one line of the original text

file_path = "python-devops/workingwithfiles/bookofdreams.txt"
open_file = open(file_path, 'r')
text = open_file.readlines()
# This length reprsents the number of lines in the file starting from 0
print(len(text))
print(text[3])
print(text[2])
open_file.close()
# Returns True of false based on whether a file is opened or closed
print(open_file.closed)
