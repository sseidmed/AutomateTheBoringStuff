'''
Write a function named displayInventory() that would take any possible “inventory” and display it like the following:


Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
Hint: You can use a for loop to loop through all the keys in a dictionary.
'''


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        item_total = item_total + inventory.get(k, 0)
        print(str(inventory[k]) + ' ' + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)


#Step 2: List to Dictionary Function for Fantasy Game Inventory

def addToInventory(inventory, addedItems):
    # your code goes here
    print("\n")
    for k, v in inventory.items():
      for i in addedItems:        
          inventory[i] = inventory.get(i, 0) + 1           
      return inventory
    
     


inv = {'gold coin': 42, 'rope': 10} #player's original inv
dragonLoot = ['ruby', 'ruby', 'ruby', 'ruby', 'ruby', 'ruby', 'ruby', 'ruby', 'gold coin', 'dagger', 'dagger', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'gold coin'] #new items

inv = addToInventory(inv, dragonLoot) #assign the results of my second function to inv
displayInventory(inv) #run my first function on a new result



'''
The previous program (with your displayInventory() function from the previous project) would output the following:

Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
'''
