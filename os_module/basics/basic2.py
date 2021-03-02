import os

# To get the environment variables

print(os.environ)

print("Home:", os.environ.get('HOME'))

print("SHELLPATH:", os.environ.get('SHELL'))
