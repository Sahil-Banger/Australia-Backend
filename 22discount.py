def discount(price, number, percentage):
    final_price = price - ((price * number) / percentage)
    return final_price
bike = discount(250, 25, 100)
tv = discount(400, 40, 100)
smartphone = discount(1200, 57, 100)

print(f"The final price of bike is {bike}")
print(f"The final price of tv is {tv}")
print(f"The final price of smartphone is {smartphone}")