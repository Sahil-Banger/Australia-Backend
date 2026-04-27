def runner_up(list_original):
    without_dup = []
    for x in list_original:
        if x not in without_dup:
            without_dup.append(x)
    without_dup.sort()
    penultimate = without_dup[-2]
    return penultimate
list1 = [1, 2, 6, 6, 5]
list1 = runner_up(list1)
print(list1)