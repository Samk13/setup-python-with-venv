from validator import Validator

username = input("Enter your username: ")
isValid = Validator()

if isValid.username_is_valid(username):
    print("Username is valid.")
else:
    print("Username is not valid.")
