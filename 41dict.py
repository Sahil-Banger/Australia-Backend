student = {
    "Marco" : 80 ,
    "Sara" : 90 ,
    "Matteo" : 50 ,
    "Francesco" : 40 ,
    "Chiara" : 60 
}
for keys in student:
    if student[keys] >= 60:
        print(f"{keys} Passed")
    else:
        print(f"{keys} Not passed")