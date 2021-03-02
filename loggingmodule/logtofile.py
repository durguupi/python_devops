# https://docs.python.org/3/library/logging.html#logrecord-attributes
# To refer the attributes used to log in file use the above link
import logging

# We define the filename where logs need to stored. It gets updated each time when we run the program
logging.basicConfig(
    filename='python-devops/loggingmodule/test.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s:%(funcName)s:%(lineno)d')


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


num1 = 20
num2 = 10

result_add = add(num1, num2)
result_sub = sub(num1, num2)
# This debug should be in small letter or else you will get error
logging.debug(f"ADD: {num1} + {num2} = {result_add}")
logging.debug(f"SUB: {num1} - {num2} = {result_sub}")
