# %% 
# 1 | methods and the index method
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') # the index method
spam.index('heyas')
spam.index('asdfasdf') # exception
# %%
# 2 | in the case a value apears more than once - the index() method returns the first item's index
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')
# %%
# 3 | methods to add item to a list
spam = ['cat', 'dog', 'bat']
spam.append('moose') # append() adds the item to the end of the list
print(spam)
spam.insert(1, 'chicken') # add anywhere in the list with insert
print(spam)
spam.insert(-2, 'kruven')
print(spam)
# the insert() and append() methods only work on lists
# %%
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
spam.remove('bat') # will return an error for an item that's not on the list
# del spam[0] will delete an item given an index and remove will delete the item where it first appears
# %%
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
print(spam)
spam.remove('cat')
print(spam)
# %%
# 4 | the sort() method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = ['cats', 'ants', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)


# %%
# 5 | you cannot sort a list that has both strings and numbers
spam = [1, 2, 3, 'Alice', 'Bob']
spam.sort()
# %%
# 6 | sort() works on strings in an "ascii-betical" order
#   | hense upper case before lower case
spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)
# %%
#  7 | true alpha-betical sorting
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)