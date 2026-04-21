def s_number(minn, maxx, skipp, type):
    print(f"\n{type}: ")
    for x in range(minn, maxx, skipp):
        print(x)
        
even = s_number(2, 102, 2, "even")
normal = s_number(1, 101, 1, "normal")
odd = s_number(1, 101, 2, "odd")



        







