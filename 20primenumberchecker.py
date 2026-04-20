number = int(input("Enter the number: "))
is_prime = True
for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        print("Not prime number")
        break
        
if is_prime == True:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")
    
