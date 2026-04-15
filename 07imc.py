weight = float(input("enter the weight:" ))
height = float(input("enter the height:" ))
print(f"The value of IMC is {(weight/(height*height))}")
print(f"The value of IMC is {round(weight/height**2, 2)}")