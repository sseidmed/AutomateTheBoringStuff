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
