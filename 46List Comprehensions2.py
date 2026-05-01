student = {
    "Marco" : 80,
    "Sara"  : 70,
    "Matteo" : 40,
    "Chiara" : 30,
    "Sahil"  : 90
}

students_passed = {name : grade for name, grade in student.items() if grade >= 60}
students_failed = {name : grade for name, grade in student.items() if grade < 60 }
# print(f"Students who passed the test: {students_passed}")
# print(f"Students who failed del test: {students_failed}")

random_words = ("apple", "banana", "pear", "apple", "apple", "banana")

def counter_words(words):
    return {word: words.count(word) for word in set(words)}

result = counter_words(random_words)
# print(result)

def add_address_book(address_book, name, number):
    address_book[name] = number
    return (f"Add {name} : {address_book[name]} to {address_book}")
def search_contact(address_book, name):
    result = [address_book[n] for n in address_book if n == name]
    if result:
        print(f"Number: {result[0]}")
    else:
        print("Not found")
def delete_contact(address_book, name_to_delete):
    updated_book = {k: v for k, v in address_book.items() if k != name_to_delete}
    return updated_book
my_address_book = {}
# print(add_address_book(my_address_book, "Sahil", "333333333333"))
# print(add_address_book(my_address_book, "Francesco", "444444444444"))
# search_contact(my_address_book, "Sahil")
# search_contact(my_address_book, "Sara")
# my_address_book = delete_contact(my_address_book, "Francesco")
# print(my_address_book)
# my_address_book = delete_contact(my_address_book, "Sara")
# print(my_address_book)



    
