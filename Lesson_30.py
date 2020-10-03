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