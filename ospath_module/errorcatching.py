import os.path

# f1 = open('doesnotexist.txt')
# # This will return FileNotFoundError: [Errno 2] No such file or directory: 'doesnotexist.txt Error
# print(f1)

# We will use try and catch method to handle this exceptions like filenot found , permission error
# Generally all this errors are IOErrors


def func1(filename):

    try:
        f = open(filename)
        print("file exists")
        f.close()
    except IOError:
        print("File not found or not accessible")


func1('file2.txt')
func1('notes_gcp.txt')
func1('file1.txt')
