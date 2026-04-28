student = {
    "Marco" : 80 ,
    "Sara" : 90 ,
    "Matteo" : 50 ,
    "Francesco" : 40 ,
    "Chiara" : 60 
}
for name, vote in student.items():
    if vote >= 60:
        print(f"{name} Passed")
    else:
        print(f"{name} Not Passed")
