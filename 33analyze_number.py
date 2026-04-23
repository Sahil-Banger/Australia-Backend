def analyze_number(number):
    counter = 0
    result = []
    for x in range(0, number+1, 2):
           result.append(x)
           counter = counter + 1
    result.append(f"{counter} is the counter")
    if number % 2 == 0 and number < 0:
            result.append("Even, Negative")
    elif number % 2 == 0 and number > 0:
            result.append("Even, Positive")
    elif number == 0:
            result.append("Zero")
    elif number > 0:
            result.append("Odd, Positive")
    else:
            result.append("Odd, Negative")
    return result
first = analyze_number(int(input("Enter the number: ")))
second = analyze_number(30)
third = analyze_number(57)
print(first)
print(second)
print(third)
    