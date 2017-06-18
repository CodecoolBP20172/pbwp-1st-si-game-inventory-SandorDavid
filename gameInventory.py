# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    d = 0
    print("Inventory:")
    for item in inventory:
        print (str(inventory.get(item)) + " " + str(item))
        d += inventory.get(item)
    print("Total number of items: %s" % d)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    d = 0
    print("Inventory:")
    print("  count    item name")
    print("-" * 20)
    for item in inventory:
        print ((" " * (7 - len(str(inventory.get(item)))) + str(inventory.get(item)) + (" " * (13 - len(item))) + str(item)))
        d += inventory.get(item)
    print("-" * 20)
    print("Total number of items: %s" % d)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
