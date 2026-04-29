def add_address_book(address_book, name, number):
    address_book[name] = number
    print(f"{name} added successfully")
def search(address_book, name):
    if name in address_book:
        print(f"Number of {name} : {address_book[name]}")
    else:
        print(f"The name {name}, is not in the address_book")
def delete(address_book, name):
    if name in address_book:
        del address_book[name]
        print(f"Delete {name}")
    else:
        print(f"It's not possible delete, the name {name} are not in Address Book")

my_address_book = {}
add_address_book(my_address_book, "Sahil", "333 333 3333")
add_address_book(my_address_book, "Francesco", "444 444 4444")
search(my_address_book, "Sahil")
search(my_address_book, "Sara")
delete(my_address_book, "Francesco")
delete(my_address_book, "Sara")
