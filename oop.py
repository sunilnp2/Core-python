# class Employee:
#     a = 10

#     #function inside class
#     def employe_detail():
#         name = "Sunil"
#         age = 20
#         role = "CEO"
    

# obj = Employee()

# #Note You can gives any name to object
# print(obj.name)

# class Employee:
#     def sun(self):
#         print("This sunil nepali")

# sunil = Employee()
# print(sunil.sun)

# class Employee:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def details(self):
#         info = f"Hello my name is {self.name},I am {self.age} Years old,I am from {self.address}"
#         return info

# sunil = Employee("Sunil",20,"Kathmandu")

# print(sunil)

'''class Information:
    def __init__(self,my_name,age,add):
        self.name = my_name
        self.age = age
        self.add = add 
    def details(self):
        info = f"Hello my name is {self.name}.I am {self.age}years old,I am form {self.add}."
        return info

n = input("Enter your name:")
a = int(input("ENter your age:"))
add = input("ENter your address:")

sun = Information(n,a,add)
print(sun.details())


class Condition:
    def area(self,l,b):
        a = l*b
        return a

ar = Condition()
l = int(input("Enter Length:"))
b = int(input("Enter Breadth :"))


print(ar.area(l,b))'''

class Factor:
    def __init__(self,l,b,h):
        self.length = l
        self.breadth = b 
        self.height = h

    def area(self):
        a = self.length * self.breadth
        return a
    def volume(self):
        v = self.length * self.breadth * self.height
        return v
l = int(input("Enter Length:"))
b = int(input("Enter Breadth:"))
h = int(input("Enter Height:"))
fact = Factor(l,b,h)

print("The area is",fact.area())
print("The volume is",fact.volume())


