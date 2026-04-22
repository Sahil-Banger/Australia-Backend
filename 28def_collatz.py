def collatz(number):
    result = []
    while number != 1:
        result.append(number / 2)
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
    return result
first = collatz(55)
print(first)
            


