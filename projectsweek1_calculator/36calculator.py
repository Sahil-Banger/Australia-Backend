def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b 
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def modulo(a, b):
    return a % b
def calculator():
    while True: 
        operation = input("Enter the operation +, -, /, *, % or quit: ")
        if operation == "quit":
            break
        elif operation not in ["+", "-", "*", "/", "%"]:
            print("Not valid, try again")
            continue
        try: 
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
        except ValueError:
            print("Error, enter the numbers")
            continue
        if operation == "+":
            outcome = addition(a, b)
            print(outcome)
        elif operation == "-":
            outcome = subtraction(a, b)
            print(outcome)
        elif operation == "*":
            outcome = multiplication(a, b)
            print(outcome)
        elif operation == "%":
            outcome = modulo(a, b)
            print(outcome)
        elif operation == "/" and b == 0:
            print("It's not possible")
            continue 
        else: 
            outcome = division(a, b)
            print(outcome)
    
    return "Goodbye!"
            
        
first = calculator()
print(first)
            
            
            

    