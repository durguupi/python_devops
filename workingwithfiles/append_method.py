# # You can also append/add a new text to the already existing file or a new file.
# Once again if you could see a plus sign in the code, it indicates that it will create a new file
# if it does not exist. But in our case we already have the file,
# so we are not required to create a new file.

file_path = "/mnt/g/newyear_2021/python-devops/workingwithfiles/sample.txt"
# This will write data into the file in append mode.
with open(file_path, 'a+') as file_append:
    for i in range(2):
        file_append.write("Appended line %d\r\n" % (i+1))
print(file_append.closed)
