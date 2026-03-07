menu = {"Pizza": 120, "Burger": 80, "Pasta": 100}
order = input("Enter item name: ")
if order in menu:
    print(order, "costs", menu[order], "₹")
else:
    print("Item not available")
    # This code defines a simple restaurant menu with item names and their corresponding prices. It prompts the user to enter the name of an item they wish to order. If the item is available in the menu, it displays the cost of the item. If the item is not available, it informs the user that the item is not available.