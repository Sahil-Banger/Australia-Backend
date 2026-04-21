def greet(name):
    print(f"Hello {name}")
greet("S")
greet("N")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last 
full_name = create_name("sahil", "banger")
print(full_name)