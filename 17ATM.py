balance = int(input("Enter the balance: "))
pin = "1234"
withdrawal = int(input("Enter the withdrawal: "))
newb = balance - withdrawal
attempts = 0 
while attempts < 3 :
    enterpin = input("Enter the pin: ")
    attempts = attempts + 1
    if enterpin == pin:
        if withdrawal <= balance:
            print(f"You took {withdrawal}, and your balance is {newb}")
            break
        else:
            print("You cannot withdraw this amout, please enter another amout")
    else:
          print("Pin not correct, try again")      
       