def duplicate(list_original):
    without_duplicates = []
    for x in list_original:
        if x not in without_duplicates:
            without_duplicates.append(x)
    return without_duplicates
list1 = [5, 5, 8, 5, 3, 2, 5, 7, 8, 9, 5, 4, 7, 8]
list1 = duplicate(list1)
print(list1)
        




