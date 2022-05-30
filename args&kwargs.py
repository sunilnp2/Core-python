def information(normal,*args, **kwargs):\

    # normal print
    print(normal)
    print('\n')

    # for loop in args
    print("THis is for args\n")
    for item in args:
        print(f'This is args item {item}\n')
    
    # for loop in kwargs
    print("This is for kwargs\n")
    for key, value in kwargs.items():
        print(f'this is key:{key} And this is value{value}')


data_args = ['Sunil Nepali', 'Prasanna', "Samir", "Sachin GOle", 'Rajendra']

data_kwargs = {'Name':"Sunil Nepali", 
                'Address':"Kathmandu", "age":20, "Study":"BCA"}
normal = "This is SUnil NEpali from gorkha"

# call the function 
information(normal,*data_args, **data_kwargs )