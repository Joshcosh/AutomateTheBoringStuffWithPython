# while loop example

# spam = 0
# while spam < 5:
#     print('Hello world')
#     spam = spam + 1

# while loop using an input

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

# avoid infinite loops example

# while True:
#     print('Hello!')

# infinite while loop using an input and break

# name = ''
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')

# continue  example

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

