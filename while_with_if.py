# print("Hello World")
# student_list = ["Sunil","Anil","Suresh","Jagdish","Santaram"]
# print(student_list)
# for i in student_list:
#     print(i)


# a = student_list.pop()
# student_list.append("Hari")

# print(student_list)



def info():

    student_dict = {
    'name':"Sunil Nepali",
    'age':20,
    'faculty':"BCA",
    'know_programming' : "js,JAVA,Pyton",
    'college':"TRITON",
    'p_address':'Gorkha,Nepal',
    'c_address':'KTM,Nepal',
    'favorite_color':"yellow"   
}
    que = input("Enter your Question [Question_LISTs= \nname\nage\nfaculty\nknow_programming\ncollege\np_address\nc_address\nfavorite_color:\n")
    a = student_dict[que]
    ''' if a not in student_dict:
        print(f'{a} is not in Given dictionary' )'''
    if que == 'age':
        print(a)
    else:
        print(a.upper())
   
info()
i = 0
while i<5:
    again = input("Do you want to ask Question again  Y/N = ")
    if again == "y":
        info()
    else:
        print("Program stopped")
        break



    