# exapmle 1 | importing and using a random library

# import random
# random.randint(1,10)

# exmaple 2 | it's fine importing multiple libraries in the same line

# import radom, sys, os, math 

# example 3 | more specific imports
#           | not recommended

# from random import *
# randint(1, 10) # no need to speficy random. like we did in exaple 1

# example 4 | importing the sys module to correctly exit a program

# import sys
# print('Hello')
# sys.exit()
# print('Goodbye') # this will not be called

# example 5 | we can also import 3rd party modules 

import pyperclip
# copy and paste text to the clipboard
pyperclip.copy('Hello world!')
pyperclip.paste()