tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
  longest = [len(max(i, key=len)) for i in table]
  print(longest)
  
  for i in range(len(table[0])):
    print(end='\n')
    for list in range(len(table)):
       print(table[list][i].rjust(longest[list]), end=' ')

printTable(tableData)


'''
Your printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
  '''

  
