import os

# To remove the extensions .txt
print(os.path.splitext("/path/to/some/file.txt")[0])
# Just to return the filename
print(
    f"Printing only the file name: {os.path.basename('/path/to/some/file.txt')}")

l_dir = os.listdir('python-devops/')
# print(l_dir)
print(
    f"Below are the directories present in {os.path.basename('/mnt/g/newyear_2021/python-devops')}")
print("\n".join(l_dir))
