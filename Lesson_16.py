# %%
# 1 | strings and lists are similar
name = 'Zophie'
print(name)
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)
print('xxx' in name)

for letter in name:
    print(letter)
# %%
# 2 | but also different -list is a mutable data type, a string is immutible
name = 'Zophie the cat'
print(name[7])
name[7] = 'x' # exception is thrown because a string is an immutible object
# %%
# 3 | the propper way to change a string is using assertion to a new string
name = 'Zophie a cat'
print(name)
newName = name[0:7] + 'the' + name[8:12]
print(newName)
# %%
# 4 | so what's the difference between mutibles and immutibles?
spam = 42
cheese = spam # pass by value
spam = 100
print(spam)
print(cheese)
# %%
# 5 | lists don't work the same way as variables
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # pass by reference
cheese[1] = 'Hello'
print(cheese)
print(spam)
# %%
# 6 | passing lists in function calls
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # changes in eggs() reflect in the local scope because spam is a reference to a list
# %%
# 7 | passing a copy of a list as a parameter to a function
import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)

cheese[1] = 42
print('spam = ' + str(spam))
print('cheese = ' + str(cheese))
# %%
# 8 | loading up lists with indentation
spam = ['apples',
        'oranges',
        'bananas', 
        'cats']
print(spam)
# %%
# 9 | line indentation in general
print('Four score and seven' + \
    ' years ago')