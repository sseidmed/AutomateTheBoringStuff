tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

longest = [len(max(i, key=len)) for i in tableData]
print(longest)
  
for i in range(len(tableData[0])):
    print(end='\n')
    for list in range(len(tableData)):
       print(tableData[list][i].rjust(longest[list]), end=' ')




'''
Your printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
  '''

  
