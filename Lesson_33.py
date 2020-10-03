# %%
# 1 | Permanently delete a file using os.unlink()
import os 
os.unlink('spam.txt')
# %%
# 2 | Permanently delete a folder using os.rmdir()
import os
# The folder has to be empty for rmdir() to succeed.
os.rmdir('Lesson_33')
# %%
# 3 | Use shutil.rmtree() to remove a folder and all its contents.
import shutil

# shutil.copytree('Lesson_32', 'Lesson_33')
# We should be very careful when using the shutil.rmtree() method.
shutil.rmtree('Lesson_33')

# %%
# 4 | We can do a Dry Run before permanently
# deleting things using the methods above.
import os

os.chdir(os.path.join('AB:\\', 'Users', 'DELL', 'Downloads'))

for filename in os.listdir():
    if filename.endswith('.exe'):
        # os.unlink(filename)
        print(filename) # Do a Dry Run and then comment out anr uncomment above line.

# %%
# 5 | Instead of deleting things permanently we can send 
# them to the trash using send2trash module
import os, send2trash

tmp = open('spam.txt', 'w')
tmp.close()
send2trash.send2trash('spam.txt')
