# %%
# 1 | basic iteration over a basic list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is : ' + supplies[i])
# %%
# 2 | multiple assignment
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# %%
size, color, disposition = cat
# %%
size, color, disposition = 'skinny', 'black', 'quite'
a = 'AAA'
b = 'BBB'
a, b = b, a
print('a = ' + a) 
print('b = ' + b) 
# %%
#  3 | augmented assignment operators
spam = 42
spam = spam + 1
spam += 1 # augmented operator
spam