# %%
# 1 | regex recap
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')

mo.group()

# %%
# 2 | Groups in regex
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo.group()
# mo.group(1)
# mo.group(2)

# Good for when we just need a small part of the pattern

# %%
# 3 | To find regular parentheces as a part of the text use \
import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242')
mo.group()
mo.group(1)
mo.group(2)

# %%
# 4 | Use P|i|p|e|s to allow for several matching options
import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group(1)

# mo = batRegex.search('Batmotorcycle lost a wheel')
# print(mo)
# mo.group() # ERROR
