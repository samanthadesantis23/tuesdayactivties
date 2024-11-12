class ShoppingList:
    def __init__(self):
        # Internal storage for items and their quantities
        self.items = []
    
    def add(self, item, quantity):
        # Adds an item and its quantity to the shopping list
        self.items.append((item, quantity))
    
    def number_of_items(self):
        # Returns the total number of items in the shopping list
        return len(self.items)
    
    def item(self, index):
        # Returns the item name at the given index (1-based)
        if 1 <= index <= len(self.items):
            return self.items[index - 1][0]
        else:
            return None
    
    def amount(self, index):
        # Returns the quantity of the item at the given index (1-based)
        if 1 <= index <= len(self.items):
            return self.items[index - 1][1]
        else:
            return None

# Function to calculate the total units
def total_units(my_list: ShoppingList):
    # Sum the quantities of all items in the shopping list
    total = 0
    for i in range(1, my_list.number_of_items() + 1):
        total += my_list.amount(i)
    return total

# Testing the function
if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    # Output the total units
    print(total_units(my_list))  # Output should be 16
