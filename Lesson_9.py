# example 1 | a basic fucntion, definition and call
# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')

# hello()
# hello()
# hello()


# example 2 | better to avoid code duplication
# def hello(name):
#     print('Hello ' + name)

# hello('Alice')
# hello('Bob')


# example 3 | a function can return a value
# def plusOne(number):
#     return number + 1

# newNumber = plusOne(5)
# print(newNumber)


# example 4 | how to use print() and not go down a line automatically
# print('Hello', end=' ')
# print('World')

# example 5 | print() will automatically add spaces to comma seperated inputs
# print('cat', 'dog', 'mouse')

# example 5 | print() the separation is configurable
print('cat', 'dog', 'mouse', sep='ABC')