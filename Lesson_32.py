# %%
# 1 | How to reorganize files and directiries using the shutil module
import shutil

print(shutil.copy('spam.txt', 'Lesson_32'))
shutil.copy('spam.txt', r'Lesson_32\spamspamspam.txt')

# %%
# 2 | How to copy multiple files from dir A to dir B
import shutil

shutil.copytree('Lesson_32', 'Lesson_32_backup')

# %%
# 3 | Use the move() method to move things around
import shutil

shutil.move('spam.txt', r'Lesson_32\spamfolder')


# %%
# 4 | We also use the move() method to rename things
import shutil

# shutil.move(r'Lesson_32\spamfolder\spam.txt', r'Lesson_32\spamfolder\spammoved.txt')
shutil.move(r'Lesson_32\spamfolder\spammoved.txt', r'Lesson_32\spamfolder\spam.txt')
