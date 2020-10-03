#! python3
# %%
import os, re, shutil

# TODO: Create a list for python files and a list for other files
contents = os.listdir()
curPyItemName = ''

for item in contents:
    if item.endswith('.py'):
        curPyItemName = item[:-3]
    elif os.path.isfile(item) and curPyItemName in item:
        print('''%s → %s\n''' % (curPyItemName, item))
        if not os.path.isdir(curPyItemName):
            os.mkdir(curPyItemName)
        shutil.move(item, curPyItemName + '//' + item)
