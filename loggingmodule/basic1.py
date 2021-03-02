import logging

# After adding this and setting the logging level to DEBUG it starts working
logging.basicConfig(level=logging.DEBUG)

# Simple Adding functions


def add(x, y):
    return x + y

# Simple subtraction function


def sub(x, y):
    return x - y


num1 = 10
num2 = 5
# Calling the functions
result_add = add(num1, num2)
# Printing the value
# print(f"ADD: {num1} + {num2} = {result_add}")

result_sub = sub(num1, num2)
# Printing the value
# print(f"SUB: {num1} - {num2} = {result_sub}")

# By default logging level is set to warning so it displays warning and critical messages
logging.warning(f"ADD: {num1} + {num2} = {result_add}")

logging.warning(f"SUB: {num1} - {num2} = {result_sub}")
# # This doesnt return any output since we have set defaut logging. only warning and critical messages will be printed
# logging.debug(f"ADD: {num1} + {num2} = {result_add}")

# This will return the output once we have changed the basicconfig setting in logging to Debug
logging.debug(f"ADD: {num1} + {num2} = {result_add}")
