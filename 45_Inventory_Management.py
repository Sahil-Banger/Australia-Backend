create_inventory = ["apple", "pineapple", "apple", "strawberry", "watermelon", "strawberry", "watermelon", "apple", "strawberry", "apple", "watermelon", "watermelon", "grape", "strawberry","grape", "watermelon", "cherry", "grape", "banana", "cherry", "pineapple", "cherry", "orange", "grape", "pineapple"]
def calculator_inventory(inv):
    inventory = {}
    for name in inv:
        if name not in inventory:
            inventory[name] = 1 
        else:
            inventory[name] += 1
    return inventory

create_inventory = calculator_inventory(create_inventory)
print(create_inventory)
new_inv = ["blueberry", "peach", "apple", "apple", "banana", "banana"]
def add_items(inventory, items_to_add):
    for name in items_to_add:
        if name not in inventory:
            inventory[name] = 1
        else:
            inventory[name] += 1
    return inventory
new_inv = add_items(create_inventory, new_inv)
print(new_inv)
def decremet_items(inventory, delete_items):
    for name in delete_items:
        if name in inventory:
            if inventory[name] > 0:
                inventory[name] -=  1
            else:
                print(f"there are no {name} available, {inventory[name]} left")
        else:
            print(f"{name} not in inventory")
    return inventory
updated_inventory = ["apple", "pineapple", "apple", "pineapple", "peach", "peach", "pear"]
updated_inventory = decremet_items(new_inv, updated_inventory)
print(updated_inventory)
def remove_items(inventory, fruits):
    for name in fruits:
        if name in inventory:
                del inventory[name]
        else:
            print(f"{name} not in inventory")
    return inventory
final_inventory = ["apple", "plum"]
final_inventory = remove_items(updated_inventory, final_inventory)
print(final_inventory)





