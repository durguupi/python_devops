import subprocess

# We are assinging the output of the subprocess to variable but still the output prints
p1 = subprocess.run(['ls', '-la'])
# This returns CompletedProcess(args=['ls', '-la'], returncode=0)
print(p1)
print(f"Args: {p1.args}")
print(f"Return Code: {p1.returncode}")
print("============P2 output============")
# To capture the output in variable use capture_output
p2 = subprocess.run(['ls', '-la'], capture_output=True)
# output comes as bytes
print(p2.stdout)
# to convert the stdout into string we can use below ways
print(p2.stdout.decode())
print("============P3 output============")
# to get the output as string we use text = True value
p3 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(p3.stdout)
