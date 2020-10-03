# %%
# 1 | How to log easily with custom messages using the 
# logging module.
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(messages)s')
# We should add the code above each time we want to use the logging mechanism.
logging.disable(logging.CRITICAL)
# This is how to disable the logging for production code.

# There are 5 Log Levels:
# =======================
# debug (lowest)
# info
# warning
# error
# critical (highest)


# %%
# 2 | The logging.debug() method.
import logging 

# Log into the terminal:
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Log into a file:
logging.basicConfig(filename='Lesson_36_Log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disable logging:
# logging.disable(logging.CRITICAL) # Will disable all logging because critical is the highest
# logging.disable(logging.INFO) # Will only disable info and debug


logging.debug('Start of program')
logging.info('Start of program')
# logging.info('Start of program')
# logging.warning('Start of program')
# logging.error('Start of program')
# logging.critical('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    # for i in range(n + 1): # Bug
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))
# Example with factorial
# print(1*2*3*4)
# print(1*2*3*4*5*6*7)

logging.debug('Start of program')

