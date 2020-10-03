# %%
# 1| There are Three steps to opening a file:
import os
# The default is open in Read Mode. Can't modify or write.
# open() → read() → close()

# The open method calles os.getcwd() method automatically and adds the argument to it
helloFile = open('Lesson_31.txt')
helloFile.read()
helloFile.close()

helloFile = open('Lesson_31.txt')
content = helloFile.read()
print(content)
helloFile.close()

# %%
# 2 | Read a file line by line in a list
import os

helloFile = open('Lesson_31.txt')
helloFile.readlines()
helloFile.close()

# %%
# 3 | How to change a file with Write Mode
# Write Mode will delete the existing content of the file and 
# start from blank

# Will create a new file if one does not exist
import os 

helloFile = open('Lesson_31_hello.txt', 'w')
# The write() method doesn't add a new line automatically
helloFile.write('Hello!!!!!!!\n')
helloFile.write('Hello!!!!!!!')
helloFile.write('Hello!!! !!!!')
helloFile.write('Hello!!!!!!!\n')
print(helloFile.write('Hello!!!!!!!')) # The write() method returns the number of bytes writen
helloFile.close()

# %%
# 4 | Add lines to a file using Append Mode
import os

baconFile = open('Lesson_31_bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('Lesson_31_bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()

# %%
# 5 | Save binaries into python variables with Shelve Mode
# We can manipulate and change data as if it were a dictionary
import shelve 

shelfFile = shelve.open('Lesson_31_mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

# list any attribute of the shelve file
shelfFile = shelve.open('Lesson_31_mydata')
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
