number = int(input("Enter the number: "))
while not number == 1:
    print(number/2)
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 3) + 1
        