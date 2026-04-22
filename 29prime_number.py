def prime(number):
    
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
            

    if is_prime == True:
        return f"{number} is prime"
    else:
        return f"{number} is not prime"    
    
first = prime(10)
print(first)
        