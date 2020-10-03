# %% 
# 1 | Representing file and folder locations
# We save data files to make it persist after the program finishes its run

# The root folder changes depending which OS you are running:
# Windows ↔ C:\
# Linux\Mac ↔ /
# File endings help the OS to understand what file it is.
# .png/.jpeg will signal the OS to open the file with an image viewer.
# Files can be considered as giant strings.
# File and folders paths are also represented as strings.

# Some arbitrary paths as examples:
print('c:\\spam\\egs.png')
print(r'c:\\spam\\egs.png')
print('c:\spam\egs.png')
# A good way to make python treat \ as a \ is to give it a raw string.
print(r'c:\spam\egs.png') 
r'c:\spam\egs.png'

# %%
# 2 | Creating paths using the string join() method.
# For Windows:
'\\'.join(['folder1', 'folder2', 'folder3', 'file.png'])
# %%
# 3 | The os module allows us to create paths for the OS we're currently running on.
import os

os.path.join('folder1', 'folder2', 'folder3', 'file.png')

os.sep # The os variable that stores the separator
# %%
# 4 | Get the current working directory 
os.getcwd()

# If 'spam.png' is used by python it will assume it is in the current working directory
# %%
# 5 | Change the current working directory 
os.chdir('c:\\')
os.getcwd()

# %%
# 6 | Absolute and relative paths
# Absolute means that the the path string represents the entire path.
# Relative means in relation to the current working directory.

# %%
# 7 | . and .. operators
# .. means the parent folder.
# . means the current folder and is optional.

# %%
# 8 | The abspath() method will return the absolute path of the entered entity.
os.chdir('c:\\Users\\DELL\\Projects\\Playground\\AutomateTheBoringStuffWithPython')

# Absolute path uses.
os.path.abspath('Lesson_30.py') # Get the absolute path
os.path.abspath(r'..\..\..') # Get the absolute path of the great grandparent folder
os.path.isabs('Lesson_30.py') # False
os.path.isabs(os.path.abspath('Lesson_30.py')) # True
os.path.isabs('c:\\') # True

# %%
# 9 | The relpath() method → How to get from arg1 to arg0
os.path.relpath('c:\\', 'Lesson30.py')

# %%
# 10 | dirname() and basename()
# dirname() will return up to the upmost directory
abspathstr = os.path.abspath('Lesson_30.py')
os.path.dirname(abspathstr)
# basename() will return the last file\folder in the path given as a argument
os.path.basename(abspathstr)

# %%
# 11 | the exists() method to check if things.... exist!
import os 

somePath = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(os.path.exists(somePath))

existingPath = os.getcwd()
print(existingPath)
print(os.path.exists(existingPath))

# %%
# 12 | isfile() and isdir()
import os 

existingPath = os.getcwd()

print(os.path.isfile(existingPath))
print(os.path.isfile(existingPath + '\\Lesson_30.py'))
print(os.path.isdir(existingPath))
print(os.path.isdir(existingPath + '\\Lesson_30.py'))

# %%
# 13 | The getsize() and listdir() methods
import os
# getsize() | Byte in size as an integer:
print(os.path.getsize('Lesson_30.py')) 
# listdir() | Returns a list of the contents of a folder
print(os.listdir(os.getcwd()))

# %%
# 14 | Combining everything above into a small program 
# that returns the size and contents of a folder
import os

totalSize = 0
currDir = os.getcwd()
print('''
<Contents of> <%s>  
'''% (currDir))

for filename in os.listdir(currDir):
    if not os.path.isfile(os.path.join(currDir, filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(currDir, filename))
totalSize

# %%
# 15 | How to create new directories with the makedirs() method
import os 
print(os.path.exists('Lesson_30_AutoCreatedDir'))
print(os.makedirs(os.path.join('Lesson_30_AutoCreatedDir')))
print(os.path.exists('Lesson_30_AutoCreatedDir'))
