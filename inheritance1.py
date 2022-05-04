class Student():   
    def __init__(self,name,faculty,age):
        self.name = name
        self.faculty = faculty
        self.age = age
    def info(self):
        return f'This student is {self.name}.From {self.faculty} & it''s age is str({self.age})'

name = input("Enter your name:\n")
faculty = input("Enter your faculty:\n")
age = int(input("Enter your age:\n"))
info = Student()
a = info.info(name,faculty,age)

# a = info(info(name,faculty,age ))
print(a)