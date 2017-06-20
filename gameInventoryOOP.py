class GameInventory:

    inventory = {}

    # Initializes the inventory.
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else {}

    # Returns with the length of the longest item from the given list.
    def max_length_from_list(self, the_list):
        return max([len(str(i)) for i in list(the_list)])

    # Returns with the total number of items.
    def total_items_in_inventory(self):
        return sum(list(self.inventory.values()))

    # Displays the inventory in a minimal style.
    def display_inventory(self):
        # Calsulates the length of the longest number, to have a semi-formatted output.
        max_value_length = self.max_length_from_list(self.inventory.values())
        print('Inventory:')
        for item in self.inventory:
            print('%{}d {}'.format(max_value_length, item) % self.inventory[item])
        print('Total number of items: {}'.format(self.total_items_in_inventory()))

    # Adds items from list to the inventory, and returns with it.
    def add_to_inventory(self, added_items):
        for item in added_items:
            if self.inventory.get(item):
                self.inventory[item] += 1
            else:
                self.inventory.update({item: 1})
        return self.inventory

    # Displays the inventory in a more readable style.
    # You can sort by name and item count(desc,asc).
    def print_table(self, order=''):
        # Choose the order, sort of the list.
        if order == 'count,desc':
            # Order by item count desc.
            inventory_sorted = sorted(self.inventory, key=self.inventory.get, reverse=True)
        elif order == 'count,asc':
            # Order by item count asc.
            inventory_sorted = sorted(self.inventory, key=self.inventory.get)
        elif order == 'name,desc':
            # Order by item name desc.
            inventory_sorted = sorted(self.inventory, key=lambda x: x[0], reverse=True)
        elif order == 'name,asc':
            # Order by item name asc.
            inventory_sorted = sorted(self.inventory, key=lambda x: x[0])
        else:
            # There is no order.
            inventory_sorted = self.inventory
        # Calulates the length of the longest item count, add increase it by 2 to be more readable.
        first_col_length = (
            self.max_length_from_list(
                self.inventory.values()) if self.max_length_from_list(
                self.inventory.values()) > len('count') else len('count')) + 2
        # Calulates the length of the longest item name, add increase it by 4 to be more readable.
        second_col_length = (
            self.max_length_from_list(
                self.inventory.keys()) if self.max_length_from_list(
                self.inventory.keys()) > len('item name') else len('item name')) + 4
        # Prints the table using the ordered dictionary.
        print('Inventory:')
        # Prints the header of the table in a formatted style.
        print('%{}s%{}s'.format(first_col_length, second_col_length) % ('count', 'item name'))
        print('-' * (first_col_length + second_col_length))
        # Prints the items from the inventory in a formatted way
        for item in inventory_sorted:
            print('%{}d%{}s'.format(first_col_length, second_col_length) % (self.inventory[item], item))
        print('-' * (first_col_length + second_col_length))
        print('Total number of items: {}'.format(self.total_items_in_inventory()))

    # Imports item from a file.
    # Creates a list containing the items from the file, and calls the add_to_inventory method.
    def import_inventory(self, filename='import_inventory.csv'):
        try:
            file = open(filename, "r")
            # Creates a string without special characters, and then split it by ','.
            items = (''.join(i for i in file.read() if i.isalnum() or i in [',', ' '])).split(',')
            # Calls the add_to_inventory with the items list.
            self.add_to_inventory(items)
        finally:
            file.close()

    # Creates a list with all of the items, and exports them into a file.
    def export_inventory(self, filename='export_inventory.csv'):
        try:
            file = open(filename, "w")
            # Creates a list with all of the items, using nested inline loops(comprehensions).
            content = [item for item in self.inventory for i in range(self.inventory[item])]
            # Exports the list joined by ','.
            file.write(','.join(content))
        finally:
            file.close()
