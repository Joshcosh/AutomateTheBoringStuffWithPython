# %%
# 1 | The findall regex function
import re
numberRegex = re.compile(r'((\d)+(,\d{3})+)')
story = '''
0,123,456,789
SKIP TO CONTENT
3,3,3,3,3,
Sign In
Subscribe
HEALTH
This Overlooked Variable Is the Key to the Pandemic
It’s not R.

ZEYNEP TUFEKCI
SEPTEMBER 30, 2020
'''
numberRegex.findall(story)
# numberRegex.search(story)

# %%
# 2 | The character class
# r'\d' == r'(0|1|2|3|4|5|6|7|8|9)'
# \d | Any numeric digit from 0 to 9.
# \D | Any character that is nit a numeric digit from 0 to 9.
# \w | Any letter, numeric digit, ot the underscore character.
# \W | Any character that is not a letter, numeric digit, ot the underscore character.
# \s | Any space, tab or newline character.
# \S | Any character that is nit a space, tab or newline character.
import re

lyrics = '12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, And a Partridge in a Pear Tree'

# Find a number and a word after it
xmasRegex = re.compile(r'\d+\s\w+')
# xmasRegex = re.compile(r'\d+\s\w+\s?\w{2,}')
mo = xmasRegex.findall(lyrics)
mo


# %%
import re
# 2 | building character classes
# ^ | The carrot simbol is for the negative character class
lowerCaseVowelRegex = re.compile(r'[aeiou]')  # r'(a|e|i|o|u)
a2zA2ZRegex = re.compile(r'[a-zA-Z]')  # r'(a|e|i|o|u)
vowelRegex = re.compile(r'[aeiouAEIOU]')  # r'(a|e|i|o|u)
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')  # r'(a|e|i|o|u)
notVowelRegex = re.compile(r'[^aeiouAEIOU]')  # r'(a|e|i|o|u)

mo1 = vowelRegex.findall('Robocop eats baby food')
mo1
mo2 = doubleVowelRegex.findall('Robocop eats baby food')
mo2
mo3 = notVowelRegex.findall('Robocop eats baby food')
mo3
