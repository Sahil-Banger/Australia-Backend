def list_statistics(list_number):
    total = 0
    counter = 0 
    min_val = list_number[0]
    max_val = list_number[0]
    for x in list_number:
        total += x
        counter += 1
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    medium = total/counter
    return total, medium, min_val, max_val
list1 = [3, 4, 7, 2, 5, 9, 1]
list1 = list_statistics(list1)
print(list1)