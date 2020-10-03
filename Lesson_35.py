# %% 
# 1 | Python raises an exeption whenever it tries to run invalid code
thisWillCauseAZeroDevisionError = 42/0
# The entire message that is printed is called a Traceback. 

# %%
# 2 | Raising your own Exceptions
# This is also an exception just like in example 1
raise Exception('This is the error message.')

# %%
# 3 | Raising an exception within a try and catch
"""

******************
*                *
*                *
*                *
******************

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a sgting of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or eqaule to 2.')
    
    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)
boxPrint('O', 5, 16)
boxPrint('**', 15, 5) # Bug! We raise an exception. 
boxPrint('$', 1, 1) # Another bug! We raise another exception. 

# %%
# 4 | How we can save the Traceback into a variable.
# This way we can avoid having an exception crash our 
# program, but rather handle it ourselves.
import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('Lesson_35_error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The tracebackinfo was written into error_log.txt')

# %%
import os

os.getcwd()

# %%
# 5 | Assertions are like exceptions but will always crash the program.
# They are meant only for developers.
# A bug that causes an assertion SHOULD make the code crash.
# This way we can pick up on our mistake sooner!
# assert → condition → error message
assert False, 'This is the error message.'

# %%
# 6 | A program that uses assert example 

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red! → ' + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd) # {'ns': 'yellow', 'ew': 'green'} → Car crash...

# Assertions are sanity checks :)