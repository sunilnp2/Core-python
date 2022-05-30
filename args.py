print("THis is practice in args in python")

def info(*args):
    for i in args:
        print(i)

data = ['Sunil', 'Prasanna', 'Hari', 'GOpal', 'Anil']

info(*data)



# we can give name in args and kwargs as our wish
print("we can give name in args and kwargs as our wish")
def info(*argssunil):
    for i in argssunil:
        print(i)

data = ['Sunil', 'Prasanna', 'Hari', 'GOpal', 'Anil']

info(*data)