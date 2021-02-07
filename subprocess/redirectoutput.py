import subprocess

p1 = subprocess.run(
    ['cat', 'python-devops/subprocess/output.txt'], capture_output=True, text=True)
# This prints the contents of the output.txt file
# print(p1.stdout)

# This is helpful when we want the outpout of one command to be passed as input to other command we use like below
p2 = subprocess.run(['grep', '-n', 'bash_scitping'],
                    capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

# for simple use case we can use with shell command as well

p3 = subprocess.run('cat python-devops/subprocess/output.txt | grep -n bash',
                    shell=True, capture_output=True, text=True)

print(p3.stdout)
