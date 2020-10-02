# %% 
# 1 | ^ is not only for negation, it also states the beggining of the string.
import re
beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello there!')
beginsWithHelloRegex.search('He said "Hello!"') == None

# %%
# 2 | $ signifies end of the string.
import re
endsWithWorldRegex = re.compile(r'world!$')
endsWithWorldRegex.search('Hello world!')
endsWithWorldRegex.search('Hello world!abc')

# %%
# 3 | pattern is the entire text
import re 

allDigitsRegex = re.compile(r'^\d+$')
allDigitsRegex.search('2985418456245212')
allDigitsRegex.search('2985418x456245212')
allDigitsRegex = re.compile(r'^\d+')
allDigitsRegex.search('2985418x456245212')
allDigitsRegex = re.compile(r'\d+$')
allDigitsRegex.search('2985418x456245212')

# %%
# 4 | The . character means anything but the newline.
import re

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat')

atRegex = re.compile(r'.{1,2}at')
atRegex.findall('The cat in the hat sat on the flat mat')

# %%
# 5 | .* to match anything
# .* creates a Greedy match
# .*? creates a Non-Greedy match

import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall('First Name: Uri Last Name: Shilo')

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
nongreedy.findall(serve)

greedy = re.compile(r'<(.*)>')
greedy.findall(serve)

# %%
# 6 | Emphasis on the . character not including newline.
import re

prime = 'Serve the public\nProtect the innocent\nUphold the law.'
print(prime)

dotStar = re.compile(r'.*')
dotStar.search(prime) # greedy match will only include 'Serve the public'

dotAllStar = re.compile(r'.*', re.DOTALL)
dotAllStar.search(prime) # greedy match will match everything

# %%
# 7 | How to be case insensitive
import re

vowelRegex = re.compile(r'[aeiou]')
vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')

allVowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
allVowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')

allVowelRegex2 = re.compile(r'[aeiou]', re.I) # Same thing as writing IGNORECASE
allVowelRegex2.findall('Al, why does your programming book talk about RoboCop so much?')
