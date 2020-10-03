# %%
# 1 | The os.walk() method to navigate the tree
import os, shutil

shutil.copytree('Lesson_32', 'Lesson_34') 

# for folderName, subfolders, filenames in os.walk(r'./'):
for folderName, subfolders, filenames in os.walk('Lesson_34'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))

    for subfolder in subfolders:
        print(subfolder)
        # os.rmdir(subfolder) # Example
        # if 'fish' in subfolder: # Example
        #     os.rmdir(subfolder)

        # for file in filenames: # Example
        #     if file.endswith('.py'):
        #         shutil.copy(os.join(folderName,file) , os.join(folderName, file + '.backup')

    print()