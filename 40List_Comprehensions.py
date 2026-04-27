def even(list_original):
    return [
        x**2 
        for x in list_original
        if x % 2 == 0
        ]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = even(list1)
print(list1)