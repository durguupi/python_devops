import os

path_name = input("Please enter the path where you like to create files\n")
file_prefix = float(input("Please enter a prefix number\n"))
keyword = input("Please enter the keyword\n")

ch_path = os.chdir(path_name)

file_name = [f"{file_prefix}_{keyword}_provider.tf",
             f"{file_prefix}_{keyword}_variable.tf", f"{file_prefix}_{keyword}_main.tf", f"{file_prefix}_{keyword}_output.tf",
             f"{file_prefix}_{keyword}_output.tf", f"{file_prefix}_{keyword}_networking.tf",
             f"{file_prefix}_{keyword}_SG.tf", f"{file_prefix}_{keyword}_ec2_instance.tf"]

for files in file_name:
    with open(files, mode='a'):
        pass

print(f"Following are the list of files created in {os.getcwd()}")
print("")
list_files = os.listdir(path_name)
for list_file in list_files:
    print(list_file)
