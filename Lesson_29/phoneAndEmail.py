#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# When there are groups within a regex the findall() method returns a list of tuples
# So to resolve this we put everything within one big group.
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345 
( # To simplify findall() result
((\d\d\d) | (\(\d\d\d\)))?      # area code (optinal)
(\s|-)              # first separator
\d\d\d              # first 3 digits
-                   # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)    # extention word-part (optional)
  (\d{2,5}))?          # extention number-part (optional)
) # To simplify findall() result
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@someth.+_ing.com

[a-zA-Z0-9_.+]+ # name part, we don't need to escape .+ within the square brackets
@              # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(extractedPhone)
# print(allPhoneNumbers)
# print(extractedEmail)

# TODO: Copy the extracted email/phone to the clipvoard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)