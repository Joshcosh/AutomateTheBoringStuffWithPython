# %%
# 1 | concatenating strings
'hello' + 'world'

name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

spam = 'Hello ' + name + ', you are invited to a patry at ' + place + \
' at ' + time + '. Please bring ' + food + '.'

print(spam)
# %%
# 2 | do it better with string formatting
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

spam = '''Hello %s,
You are invited to a party at %s at %s.
Please bring %s''' % (name, place, time, food)

print(spam)