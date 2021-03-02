# Write a Python program to get the size, permissions, owner, device, created, last modified and l
# last accessed date time of a specified path.
import os
from datetime import datetime
path_name = '/mnt/g/newyear_2021/python-devops/os_module/basics/basic.py'

# To get various statistics of file then we can use stat command

print(os.stat(path_name))

# This jus prints the size of the file in bytes
print(f"Size :{os.stat(path_name).st_size}")

# Prints out the last modification time
print(f"Last modfication time: {os.stat(path_name).st_mtime}")

mod_time = os.stat(
    '/mnt/g/newyear_2021/python-devops/os_module/basics/basic.py').st_mtime

# This will print date and time in human readable format
print(datetime.fromtimestamp(mod_time))

print('Permissions:', oct(os.stat(path_name).st_mode))
print('Owner:', os.stat(path_name).st_uid)
print('Device:', os.stat(path_name).st_dev)
