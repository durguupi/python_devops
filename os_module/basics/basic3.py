import os

# Executing a shell command
print(os.system('ls'))

# Get the users environment
print(os.environ.get('HOME'))

# Returns the current working directory.
print(os.getcwd())

# Return the real group id of the current process.
print(os.getgid())

# Return the current process’s user id.
print(os.getuid())

# Returns the real process ID of the current process.
print(os.getpid())
