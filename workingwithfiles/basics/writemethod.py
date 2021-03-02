# we used "w" letter in our argument, which indicates write and will create a file if it does not exist in library
# Plus sign indicates both read and write.
file_path = "/mnt/g/newyear_2021/python-devops/workingwithfiles/sample.txt"
file_open = open(file_path, 'w+')
for i in range(10):
    file_open.write("This is line %d\r\n" % (i+1))
file_open.close()
