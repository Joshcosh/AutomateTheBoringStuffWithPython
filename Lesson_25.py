# %%
# 1 | Number of appeareneces operators
# ? | Zero or one times
# \? | Back slash the question mark to look for its character
import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adentures of Batman')
mo.group()
mo = batRegex.search('The Adentures of Batwoman')
mo.group()
mo = batRegex.search('The Adentures of Batwowowoman')
print(mo)

# We can implement this with the phone number example
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo)
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo)
mo.group()

# %%
# 2
# * | Zero or more times
# \* | Back slash the star to look for its character
import re

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adentures of Batwowowowowowowowoman')
print(mo.group())

mo = batRegex.search('The Adentures of Batman')
print(mo.group())

# %%
# 2
# + | One or more times
# \+ | Back slash the plus sign to look for its character
import re

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adentures of Batwowowowowowowowoman')
print(mo.group())

mo = batRegex.search('The Adentures of Batman')
print(mo)

# %%
# 4
# Escaping the usage of regex characters usage so we can find them 
import re

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

regex = re.compile(r'(\+\*\?)')
mo = regex.search('I learned about +*?+*?+*?+*?+*?+*?+*?+*? regex syntax')
print(mo.group())

regex = re.compile(r'(\+|\*|\?)')
mo = regex.search('I learned about ++??*?*?*?+*?+*? regex syntax')
print(mo.group())

# %%
# 5
# {n} | Exactly n repetitions
import re

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said HaHaHa')
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())

# %%
# 5
# {m, n} | Exactly from m to n repetitions
import re

haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said HaHaHaHaHa')
print(mo.group())
mo = haRegex.search('He said HaHaHaHaHaHaHa')
print(mo.group())

# %%
# 6 | Greedy search, the default.
# Regex will return the first and longest match it finds.
import re
digitRegex = re.compile(r'(\d){3,5}')
digitRegex.search('1234567890')

# %%
# 7 | Non-Greedy search
# Regex will return the first and smallest match it finds.
import re
digitRegex = re.compile(r'(\d){3,5}?')

digitRegex.search('1234567890')
