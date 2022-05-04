class Teacher:
   def __init__(self,name,age,subject):
       self.name = name
       self.age = age  
       self.subject = subject 

class Student(Teacher):
    def details(self):
        info = f"My name is{self.name}, i am {self.age}years old, i am reading {self.subject}" 
        return info
name = input("Enter Your full name:")
age = int(input("Enter your age:"))
subject = input("How many subject you study:")

sunil = Student(name,age,subject)
print(sunil.details())

    