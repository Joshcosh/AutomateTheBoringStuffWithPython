# %%
# 1 | What does it take to recognize a phone number without regex

# 415-555-0000 - Phone number
# 415,550,0000 - Not a phone number

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not a phone number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[3] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber('hello'))

# Would be useless to recognize a phone number within a larger message

# message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
message = 'Call me 415-555-101 tomorrow, or at 415-555-a999 for my office line.'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any numbers.')

# This is too much code............
# %%
# 2 | Do the same thing with simple regex
import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
# message = 'Call me 415-555-101 tomorrow, or at 415-555-a999 for my office line.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message) # mo stands for Match Object
print('re.search = ' + mo.group())
mo = phoneNumRegex.findall(message) # mo stands for Match Object
print(mo)