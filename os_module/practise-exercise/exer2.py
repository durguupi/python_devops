# Write a Python program to scan a specified directory and identify the sub directories and files.
import os


def subdir(pathname):
    for dirpath, dirnames, filenames in os.walk(pathname):
        print("Current Working Directory: ", dirpath)
        print('Directories: ', dirnames)
        print('Files', filenames)
        print()


subdir('/mnt/g/newyear_2021/python-devops/os_module')
