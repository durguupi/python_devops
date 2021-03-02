# Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified path.
import os
# To get various statistics of file then we can use stat command
filename = '/mnt/g/newyear_2021/python-devops/os_module/basics/basic.py'
print(os.stat(filename))

# Check for read access output returns true of false
read_access = os.access(filename, os.R_OK)
print(f"Read access for {filename}:{read_access}")

# Check for write access output returns true of false
write_access = os.access(filename, os.W_OK)
print(f"Write access for {filename}:{write_access}")

# Check for execution access output returns true of false
execution_access = os.access(filename, os.X_OK)
print(f"Execution access for {filename}:{execution_access}")

# Check for existence of file output returns true of false
file_exist = os.access(filename, os.F_OK)
print(f"Existence of file or not {filename}:{file_exist}")
