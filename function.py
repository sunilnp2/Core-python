# def vol():
#     l = int(input("Enter Length:"))
#     b = int(input("Enter breadth:"))
#     h = int(input("Enter height:"))
#     volume = l*b*h
#     print("The volume is " + str(volume))
#     return volume

# vol()

'''class Cal:
    def __init__(self,x,y,z):
        self.l =x
        self.b = y
        self.h = z
    def area(self):
        a = self.l*self.b
        print("The area is = ",a)
    def volume(self):
        v = self.l*self.b*self.h
        print("The volume is",v)

l = int(input("Enter l = "))
b = int(input("Enter b = "))
h = int(input("Enter h = "))
obj = Cal(l,b,h)
obj.area()
obj.volume()'''

class Information:
    def __str__(self,my_name,age,add):
        self.name = my_name
        self.age = age
        self.add = add 
    def details(self):
        print(self.name,self.age,self.add)

sun = Information("Sunil",20 ,"KTM")

