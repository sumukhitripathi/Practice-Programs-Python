#Function to concatenate two strings of name
def concatStr(first_name, last_name):
    return "Hello " + first_name + " " + last_name

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(concatStr(first_name, last_name))