# Hero's Inventory 3.0

# Create a list with all the items. List all items with for statement.
inventory = ["sword", "armor", "shield", "healing portion"]

print("Your items:")
for item in inventory:
    print(item)

# Get the length of the item list
print("You have", len(inventory), "items in your possession.")

# Test the relationship with in statement
if "healing portion" in inventory:
    print("You will live to fight another day.")

# List all the items with index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# Show cut point
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("\nEnter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

# Connect 2 lists
chest = ["gold", "gems"]
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

# Give the value to the list by using index number
print("You trade your sword for a crossbow")
inventory[0] = "crossbow"
print("Your inventory is now:")
print(inventory)

# Give the value to the list by using index numbers
print("You use your gold and gems to by an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)

# Remove an item from the list
print("In a great battle, your shield is destroyed.")
del inventory[2]
print("Your inventory is now:")
print(inventory)

# Remove a slice from the list
print("Your crossbow and armor are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue")
