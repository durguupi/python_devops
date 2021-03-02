# Write a Python program to list only directories, files and all directories, files in a specified path
import os


def list_all(pathname):
    list_all = os.listdir(pathname)
    return list_all


def list_dir(pathname):
    return ([name for name in os.listdir(pathname)
             if os.path.isdir(os.path.join(pathname, name))])


pathname = '/mnt/g/newyear_2021/'
print(
    f"The files and directories present in the current path {pathname} is {list_all(pathname)}")
print(
    f"The directories present in the current path {pathname} is {list_dir(pathname)}")
