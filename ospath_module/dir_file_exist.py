import os.path
import os
# Prints the current working directory
print(os.getcwd())
# Checks whether the file exist or not
file_exist = os.path.exists('notes_gcp.txt')
# Returns True if the file exists
print(file_exist)
file_notexist = os.path.exists('test.txt')
# Returns false since file does not exist
print(file_notexist)

# Checking for directories
pwd = os.getcwd()
print(
    f"Listing the dirctories in present working directory: {os.listdir(pwd)}")

# Directory esists
dir_exist = os.path.exists('python_programs')
print(dir_exist)

# Directory does not exist
dir_notexist = os.path.exists('python')
print(dir_notexist)
