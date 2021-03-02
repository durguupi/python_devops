# Write a Python program to copy the contents of a file to another file

with open('python-devops/workingwithfiles/basics/bookofdreams.txt', 'r') as file1:
    with open("python-devops/workingwithfiles/practise_exercises/Intermediate/input.txt", "a+") as file2:
      # Move read cursor to the start of file.
        file2.seek(0)
        data = file2.read()
        # If file is not empty then append '\n'
        if len(data) > 0:
            file2.write("\n")
        # So now all the contents will be copied from the new line
        for line in file1:
            file2.write(line)
