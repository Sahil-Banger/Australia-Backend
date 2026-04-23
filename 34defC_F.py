def converter_temperature(c, f):
    result = []
    celsius = (f - 32) * 5/9
    fahrenheit = (c * 9/5) + 32
    result.append(f" Celsius are {celsius} and Fahrenheit are {fahrenheit}")
    return result
Temperature1 = converter_temperature(30, 150)
print(Temperature1)




