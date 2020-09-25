# example 1 | meaning of scope in the code
# global scope
# spam = 42 # global variable

# def eggs():
#     # local scope
#     spam = 42 # local variable 

# print('Some code here')
# print('Some more code')

# example 2 | and so this will cause an error since eggs is a local variable
# def spam():
#     eggs = 99

# spam()
# print(eggs)

# example 3 | another error, but here it's more severe because the code is still valid
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()


# %% example 4 | how to use a global variable within functions
def spam():
    print(eggs)

eggs = 42
spam()

# %% example 5 | the eggs variable is a string in the local scope
def spam():
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
# %%
# How to tell python to treat a variable as global within local scope

def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)