import random
def guess_number(min_v, max_v):
    secret_number = random.randint(min_v, max_v)
    attempts = 0 
    while attempts < 5 :
        guess = int(input("Enter the guess: "))
        attempts = attempts + 1 
        if guess == secret_number :
            return "WIN!"
    else:
        return f"Lose, the sercret number is {secret_number}"
            
first = guess_number(int(input("enter the min: ")), int(input("enter the max :")))
print(first)

    