import os


def main():
    i = 0
    path = '/mnt/g/newyear_2021/python-devops/personal_automation/tests/'
    for filename in os.listdir(path):
        print(filename)
        my_dest = "textfile" + str(i) + ".txt"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


main()
