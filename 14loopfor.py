for x in range(1, 101):
    print(x)
for x in range(2, 102, 2):
    print(x)
for x in range(1, 101, 2):
    print(x)

print("Numbers from 1 to 100: ")
for x in range(1, 101): 
    print(x)
print("\nEven Numbers: ")
for x in range(2, 101, 2):
    print(x)
print("\nOdd Numbers: ")
for x in range(1, 101, 2):
    print(x)

number = "909376967352"
for x in number:
    if x == "9":
        continue 
    else:
        print(x)
print("\nSecond: ")
for x in number:
    if x == "2":
        break
    else:
        print(x)