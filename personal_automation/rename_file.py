import os
path_name = input("Please enter the path where you like to create files\n")
for filename in os.listdir(path_name):
    if filename.startswith("[ DevCourseWeb.com ]"):
        # os.rename(filename, filename[7:])
        print(os.listdir(filename))
