def cumulative(min_val, max_val):
    previous_number = 0
    result = []
    for x in range(min_val, max_val):
        current_n = x
        sum = previous_number + current_n
        result.append(f"Current number is :{current_n}, previous is {previous_number}, S is {sum}")
        previous_number = x
    return result
first = cumulative(0,10)

def even(word):
    e = word[::2]
    result = []
    result.append(f"{e}")
    return result
one = even("pynative")

def stop(n, word):
    result = []
    finish = word[n:]
    result.append(finish)
    return result
pynative = stop(4, "pynative")

def factorial(z):
    f = 1
    result = []
    for x in range(1, z+1):
        f = f * x
        result.append(f)
        
    return result
second = factorial(5)







        




    



