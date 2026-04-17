year = int(input("Enter the year:" ))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap")  
    else:        
        print(f"{year} leap year")
else:
    print(f"{year} is not leap")        