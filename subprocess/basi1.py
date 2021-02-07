import subprocess

subprocess.run('ls')

subprocess.run('ls -ltrh', shell=True)

# Printing the command without shell , we have to pass it as list of commands
subprocess.run(['ls', '-la'])
