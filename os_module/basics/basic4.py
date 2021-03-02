import os

# Return information identifying the current operating system.
print(os.uname())

# Prints the systm Name
print(os.uname().sysname)

# Prints the release version
print(os.uname().release)

# Prints the machine name
print(os.uname().machine)
