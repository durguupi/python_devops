import os
from datetime import datetime
# To get various statistics of file then we can use stat command

print(os.stat('/mnt/g/newyear_2021/python-devops/os_module/basic.py'))

# This jus prints the size of the file in bytes
print(os.stat('/mnt/g/newyear_2021/python-devops/os_module/basic.py').st_size)

# Prints out the last modification time
print(os.stat('/mnt/g/newyear_2021/python-devops/os_module/basic.py').st_mtime)

# To get this timestamp in human readable format

mod_time = os.stat(
    '/mnt/g/newyear_2021/python-devops/os_module/basic.py').st_mtime

# This will print date and time in human readable format
print(datetime.fromtimestamp(mod_time))
