# %%
# 1 | data structures
# dictionary
cat = {'name': 'Zophie', 'age': 7, 'color':'gray'}
# list of dictionaries
allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color':'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color':'black'})
allCats.append({'name': 'Fat-tail', 'age': 5, 'color':'gray'})
allCats.append({'???': 'Fat-tail', 'age': -1, 'color':'orange'})
allCats
# %%
# use data structures to represent the tic-tac-toe game
import pprint
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }
pprint.pprint(theBoard)

theBoard['mid-M'] = 'X' # example to set a play on the board
pprint.pprint(theBoard)
# %%
# 2 | print out the board
import pprint
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }

def printBoard(board):
    print(type(board))
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----') 
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])  
    print('-----') 
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

