def counter_name(words):
    
    result = {}
    for name in words:
        if name in result:
            result[name] += 1
            
        else:
            result[name] = 1
            
    
    return result

list1 = ["apple", "banana", "apple", "pineapple", "orange", "apple", "banana"]
list1 = counter_name(list1)
print(list1)
