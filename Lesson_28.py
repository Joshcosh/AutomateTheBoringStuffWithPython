# %% 
# 1 | The sub() method
import re

namesRegex = re.compile(r'Agent \w+')
namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')

namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')

# %%
# 2 | Substitute just a part of the text using the original text
import re

namesRegex = re.compile(r'Agent (\w)\w*')
# namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')

namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')

# %%
# 3 | The Verbose mode - Writing clearer regex filters
import re
# An example we saw in a previos lesson.
re.compile(r'\(\d\d\d\)(-)?\d\d\d-\d\d\d\d') # (415) 555-5555, 415-555-5555

# VERBOSE using triple quotes.
# Comments can be added within the string.
# Spaces will not be campiled by regex.
re.compile(r'''
(\d\d\d) |    # area code (without parens, with dash)
(\(\d\d\d\))  # -or- area code with parens and no dash
-        # first dash
\d\d\d   # first 3 digits
-        # second dash
\d\d\d\d # last 4 digits
\sx\d{2,4}  # extention, like x1234''', re.VERBOSE)

# %%
# 4 | Using multuple regex compiling options with the or bitwise operator
import re

re.compile(r'''
(\d\d\d) |    # area code (without parens, with dash)
(\(\d\d\d\))  # -or- area code with parens and no dash
-        # first dash
\d\d\d   # first 3 digits
-        # second dash
\d\d\d\d # last 4 digits
\sx\d{2,4}  # extention, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
 