# Write a Python program to scan a specified directory and identify the sub directories and files using scan method.

import os
root = '/mnt/g/newyear_2021/'
for entry in os.scandir(root):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print(f'{entry.name} {typ}')
