vote = float(input("Enter the vote: "))
if vote < 60: 
    print("F")
elif vote < 70:
    print("D")
elif vote < 80:
    print("C")
elif vote < 90:
    print("B")
else:
    print("A")