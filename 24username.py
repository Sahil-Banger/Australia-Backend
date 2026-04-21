def username_year(username, year):
    username = username.lower()
    result = username + str(year)
    return result
generic_username = username_year(input("Enter the username:"), int(input("Enter the year:")))
print(generic_username)