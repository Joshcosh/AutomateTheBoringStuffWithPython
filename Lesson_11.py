# %% 
# example 1 | an error that occurs can make the app to exit before finishing
def div42by(dividBy):
    return 42 / dividBy

print(div42by(2))
print(div42by(12))
print(div42by(0)) # will cause an error
print(div42by(1)) # will exit before running this
# %% 
# example 2 | better to handle the error to allow the flow of the app to continue
def div42by(dividBy):
    try:
        return 42 / dividBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0)) # will cause an error
print(div42by(1)) # will exit before running this

# %%
# example 3 | using try and except to handle inputs from a user
print('How many cats do you have?')
numCats = input()
if int(numCats) >= 4:
    print('That is a lot of cats.')
else:
    print('That is not that many cats.')

# %%
# example 4 | we can handle the ValueError properly
print('How many cats do you have?')
try:
    numCats = input()
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')