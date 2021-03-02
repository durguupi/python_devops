import os

# This will show us all the atributes and methods within this modules
# print(dir(os))

# Gets the current working directory
print(os.getcwd())

# Changing the directory
os.chdir('/mnt/g/newyear_2021/python-devops/json_parsing/')

print(os.getcwd())
# It prints the items files or directories present in that directory
print(os.listdir())

os.chdir('/mnt/g/newyear_2021/python-devops/os_module/')

# This creates sub directories make dirs
# os.makedirs('new_os/sub-mod-os1')

# print(os.listdir())

# To delete the directories and ist sub directories
os.removedirs('new_os/sub-mod-os1')
print(os.listdir())
