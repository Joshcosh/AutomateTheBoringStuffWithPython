# %%
# 1 | a little bit about strings
print('This is fine')
print("Also valid")
# print('This could cause a 'problem'')
print('But this would be \'OK\'')
print('Hello there!\n\tHow are you?\n\t\tI\'m fine.')
# %%
# 2 | raw strings also exist in python
print('raw string - ' + r'This is Carol\'s cat.')
print('string - ' + 'This is Carol\'s cat.')
# %%
# 3 | triple quotes to write as long as you want into a string
print('''Dear Alice, 
Eve's cat has been arrested for catnapping, cat burglary, 
and extortion,
Sincerely, 
Bob.''')

# works the same with """ bla bla bla """
spam = """Dear Alice, 
Eve's cat has been arrested for catnapping, cat burglary, 
and extortion,
Sincerely, 
Bob."""
print(len(spam))
# %%
# 4 | choosing specific characters
spam = 'Hello world!'
print(spam[0])
print(spam[1:5])
print(spam[-1])
print('Hello' in spam)
print('Hello' in spam)
print('HELLO' in spam)

