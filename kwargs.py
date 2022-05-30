print("This is **kwargs in python:")

def myinfo(normal,**kwargs):
    print(normal)
    for key, value in kwargs.items():
        print(f'{key} is {value}')

data = {'name':'sunil', 'age':20}
normal = "My name is sunil Nepali"

myinfo(normal,**data)

# we can give any name in kwargs as our wish like **kwargssunil
# key point kwargs is always in dictionary form 
print("we can give any name in kwargs as our wish like **kwargssunil")
def myinfo(normal,**kwargssunil):
    print(normal)
    for key, value in kwargssunil.items():
        print(f'{key} is {value}')

data = {'name':'sunil', 'age':20}
normal = "My name is sunil Nepali"

myinfo(normal,**data)