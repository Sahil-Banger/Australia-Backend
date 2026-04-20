import random
min_val = int(input("Enter the min: "))
max_val = int(input("Enter the max: "))
secret_number = random.randint(min_val, max_val) 
attempts = 0
print(f"I thinking of a number between {min_val} and {max_val} ")
while attempts < 5:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1
    if guess == secret_number:
        print("Correct")
    else:
        print("Try Again")