import os.path

is_fileexist = os.path.isfile('test.txt')
print(is_fileexist)

is_fileexist2 = os.path.isfile('notes_gcp.txt')
print(is_fileexist2)

is_direxist = os.path.isdir('python-devops')
print(is_direxist)

is_dirnotexist = os.path.isdir('python')
print(is_dirnotexist)
