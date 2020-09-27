# %%
# 1 | upper and lower methods 
spam = 'Hello world'
print(spam.upper())
print(spam.lower())
print(spam.isupper())
print(spam.islower())
print(spam)

blankstring = ''
print(blankstring.isupper())
print(blankstring.islower())
print(blankstring)

# answer = input()
# if answer == 'yes':
#     print('Playing again')

# answer = input()
# if answer.lower() == 'yes':
#     print('Playing again')

print('Hello'.upper().isupper())
print('Hello'.upper().islower())
# %%
# 2 | is methods for strings
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print('       '.isspace())
print('Hello world!'.isspace())
print('Hello world!'[5].isspace())
print('This Is Title Case'.istitle())
print('hello world!'.title())
# %%
# 3 | startswith() and endswith() methods
print('Hello world!'.startswith('Hello'))
print('Hello world!'.startswith('H'))
print('Hello world!'.startswith('ello'))
print('Hello world!'.endswith('world!'))
print('Hello world!'.endswith('world'))
# %%
# 4 | the join() method
','.join(['cats', 'bats', 'rats'])
''.join(['cats', 'bats', 'rats'])
' '.join(['cats', 'bats', 'rats'])
spam = '\n\n'.join(['cats', 'bats', 'rats'])
print(spam)
# %%
# 5 | the split() method
'My name is Simon'.split()
'My name is Simon'.split('m') # can split on anything
# %%
# 6 | the strip(), ljust() and rjust() methods
print('Hello'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.rjust(20,'*'))
print('Hello'.ljust(25,'-'))
print('Hello'.center(20,'~'))

spam = 'Hello'.rjust(10) 
print(spam.strip())
print(spam)
spam = spam.strip()
print(spam)
# %%
# 7 | lstrip() and rstrip() methods also exist!
spam = '     x      '
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')
# %%
# 8 | the replace() method
spam = 'Hello there!'
spam.replace('e', 'XYZ')
print(spam)
spam = spam.replace('e', 'XYZ')
print(spam)
# %%
# 9 | some more pyperclip shenanigans
import pyperclip
import time

pyperclip.copy('Hello!!!!!!!!!!!!!!!')
pyperclip.paste()

while(spam != 'Oosh'):
    spam = pyperclip.paste()
    print(spam)
    time.sleep(1)
print('Done.')