# %%
# example 1 | a list - a value that contains values. multiple values in an ordered sequence
['cat', 'bat', 'rat', 'elephant'] # a basic list
# %%
# example 2 | a list can be saved into a variable
spam = ['cat', 'bat', 'rat', 'elephant'] # a basic list
spam
spam[0] # ['cat', 'bat', 'rat', 'elephant'][0]
spam[1] # ['cat', 'bat', 'rat', 'elephant'][1]
spam[2] # ['cat', 'bat', 'rat', 'elephant'][2]
spam[3] # ['cat', 'bat', 'rat', 'elephant'][3]
# %%
# example 3 | a list within a list
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0] # [['cat', 'bat'], [10, 20, 30, 40, 50]][0] == ['cat', 'bat']
spam[0][1] # ['cat', 'bat'][1] = 'bat'
spam[1][4]
# %%
# example 4 | negative indexes go from the end and backwards
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1] # last item on the list
spam[-2]
spam[-3]
spam[-4] # first item on the list
# %%
# example 5 | a string in a list can be used as we did before
spam = ['cat', 'bat', 'rat', 'elephant']
'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
# %%
# example 6 | how to define and use slices of lists
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1:3] # spam[m:n] - goes from spam[m] and iterates up to spam[n-1]
# %%
# example 7 | we can place list members and slices (which are in themselves lists) in variables.
#           | and list members and slices can recieve variables as inputs as well.
spam = [10, 20, 30]
spam[1] = 'Hello'
spam
spam[0:-1] = 'Uri' # if the string updates a slice - each char within the string will be saved as its own list member.
spam
spam[:] = 'Uri' # a simple way to devide a string into a list of characters
spam
spam[]
# %%
# example 8 | asserting lists into a list slice
spam = [10, 20, 30]
spam[1:3] = ['CAT', 'DOG', 'MOUSE']
spam
# %%
# example 9 | list index shortcuts explained properly
spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2] # blank first index means start at begining
spam[1:] # blank seconde index means go till the end of the list
# %%
# example 10 | delete an item on the list so it closes up the blank space
del spam[2]
spam
# %%
# example 11 | using len() to get the list length and concatinate lists
[1, 2, 3] + [4, 5, 6]
[1, 2, 3] * 3
len([1, 2, 3])
# %%
# example 11 | the list function
list('Hello')
# %%
# example 12 | check if an item exists in a list
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
'cat' in ['hello', 'hi', 'howdy', 'heyas']
'howdy' not in ['hello', 'hi', 'howdy', 'heyas']
