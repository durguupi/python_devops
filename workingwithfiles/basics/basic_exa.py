# The file object has a read method that returns the contents of the file as a string
# file_object  = open("filename", "mode")
# filename: gives name of the file that the file object has opened.
# mode: attribute of a file object tells you which mode a file was opened in.
file_path = 'python-devops/workingwithfiles/bookofdreams.txt'
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))
print(text[56])
print(open_file.name)
# Prints which mode we are working like r-->Read w--> write
print(open_file.mode)
# It is a good practice to close a file when you finish with it. Python closes a file when it is out of scope,
# but until then the file consumes resources and may prevent other processes from opening it.

open_file.close()
