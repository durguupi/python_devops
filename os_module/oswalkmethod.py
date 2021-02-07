import os

# for dirpath, dirnames, filenames in os.walk('/mnt/g/newyear_2021/python_programs'):
#     print("Current Working Directory: ", dirpath)
#     print('Directories: ', dirnames)
#     print('Files', filenames)
#     print()

# excluding some directories and files

# exclude = set(['.git', 'requests'])
# for root, dirs, files in os.walk('/mnt/g/newyear_2021/python-devops', topdown=True):
#     dirs[:] = [d for d in dirs if d not in exclude]
#     print(files)

# Not to print the hidden directories we can use this ways
for root, dirs, files in os.walk("/mnt/g/newyear_2021/python-devops"):
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    # use files and dirs
    print(dirs)
