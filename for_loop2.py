# List employee of company
a = []
n = int(input("How many Employees your company have:?"))

for i in range(n):
    name = input("Enter Name of Employee:")
    post = input("Enter the post of employee:")
    salary = int(input("Enter salary of Employee:"))
    data =(name+  "Is employee of company. His post is "+post +"His salary is"+str(salary))

a.append(data)
print(a)





