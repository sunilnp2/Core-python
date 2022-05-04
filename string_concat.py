
a = (input("Enter First Name:"))
b = (input("Enter Last Name:"))
def info():
    c = int(input("Enter Your Age :"))
    info = "My name is "+a+" " + b + " I am "+str(c) + "Years Old"
    return info

a = info()
print(a)
