import subprocess

p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
# python normally wont throw error if external command fails. If you want to check whether that command executed sucessfully or not
# We can check using returncodes
print(p1.stderr)
# It will return 1 or 2 since the command failed Sucess means 0 (no errors)
print(p1.returncode)

# To have python code to throw error for external command when it fails use check=True
p2 = subprocess.run(['ls', '-la', 'dne'],
                    capture_output=True, text=True, check=True)
print(p2)

# # Redirecting the error to null value as in linux
p3 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)
# This retuns Null
print(p3.stderr)
