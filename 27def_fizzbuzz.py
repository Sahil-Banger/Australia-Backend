def fizzbuzz(limit):
    result = []
    for x in range(1, limit + 1):
        if x % 3 == 0 and x % 5 == 0:
            result.append("FizzBuzz")
        elif x % 3 == 0:
            result.append("Fizz")
        elif x % 5 == 0:
            result.append("Buzz")
        else:
            result.append(x)
    return result
number = fizzbuzz(int(input("Enter limit: ")))
print(number)
