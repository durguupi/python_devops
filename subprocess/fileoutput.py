import subprocess

# Here we are printing the outptut of the command to a file
with open('python-devops/subprocess/output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-ltrha'], stdout=f, text=True)
