# if exalmple

# name = 'Bob'
# if name == 'Alice':
#     print('Hi Alice')
# print('Done')

# else example

# password = 'swordfish'
# if password == 'swordfish':
#     print('Accedd granted.')
# else:
#     print('Wrong password.')

# if / elif example

# name = 'Bob'
# age = 3000
# if name == 'Alice':
#     print('Hi Alice')
# elif age < 12:
#     print('You are not Alice, Kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, imortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')

# using inputs example

print('Enter a name.')
name = input()
if name: # name != '':
    print('Thank you for entering a name')
else: # a blank string is considered False
    print('You did not enter a name')