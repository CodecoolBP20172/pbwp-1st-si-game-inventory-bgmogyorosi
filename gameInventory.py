# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


# Returns with the length of the longest item from the given parameter
def max_length_item_from_list(the_list):
    return max([len(str(i)) for i in list(the_list)])


# Displays the inventory.
def display_inventory(inventory):
    # Calculates the length of the longest number, to have a semi-formatted output.
    max_length = max_length_item_from_list(inventory.values())
    print('Inventory:')
    for item in inventory:
        print('%{}d {}'.format(max_length, item) % inventory[item])
    print('Total number of items: {}'.format(sum(list(inventory.values()))))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        # Check if there is any label with the name of the item.
        if inventory.get(item):
            # If is, increases it's value by one.
            inventory[item] += 1
        else:
            # If isn't, adds that item to the inventory with a starting number one.
            inventory.update({item: 1})
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=''):
    # Order the inventory dictionary, by items count or name.
    if order == 'count,desc':
        # Order by item count desc
        inventory_sorted = sorted(inventory, key=inventory.get, reverse=True)
    elif order == 'count,asc':
        # Order by item count asc
        inventory_sorted = sorted(inventory, key=inventory.get)
    elif order == 'name,desc':
        # Order by item name desc
        inventory_sorted = sorted(inventory, key=lambda x: x[0], reverse=True)
    elif order == 'name,asc':
        # Order by item name asc
        inventory_sorted = sorted(inventory, key=lambda x: x[0])
    else:
        # If there were no order parameter, or it was invalid, then it is random.
        inventory_sorted = inventory
    # Calulates the first column, the length of the longest item count, add increase it by 2 to be more readable.
    first_col_length = (
        max_length_item_from_list(inventory.values()) if max_length_item_from_list(
            inventory.values()) > len('count') else len('count')) + 2
    # Calulates the secong column, the length of the longest item name, add increase it by 4 to be more readable.
    second_col_length = (
        max_length_item_from_list(inventory.keys()) if max_length_item_from_list(
            inventory.keys()) > len('item name') else len('item name')) + 4
    # Write out the table, with the title
    print('Inventory:')
    # Prints the header of the table in a formatted style.
    print('%{}s%{}s'.format(first_col_length, second_col_length) % ('count', 'item name'))
    print('-' * (first_col_length + second_col_length))
    # Prints the items from the inventory in a formatted way
    for item in inventory_sorted:
        print('%{}d%{}s'.format(first_col_length, second_col_length) % (inventory[item], item))
    print('-' * (first_col_length + second_col_length))
    print('Total number of items: {}'.format(sum(list(inventory.values()))))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename='import_inventory.csv'):
    try:
        file = open(filename, "r")
        # Creates a string without special characters, and then split it by ','.
        items = (''.join(i for i in file.read() if i.isalnum() or i in [',', ' '])).split(',')
        # Calls the add_to_inventory with the items list.
        inventory = add_to_inventory(inventory, items)
    finally:
        file.close()
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename='export_inventory.csv'):
    try:
        file = open(filename, "w")
        # Creates a list with all of the items, using nested inline loops(comprehensions).
        content = [item for item in inventory for i in range(inventory[item])]
        # Exports the list joined by ','.
        file.write(','.join(content))
    finally:
        file.close()
