import json

# // Json Using Loads 
# translate Json to Python Dictionary
''' x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y) '''

# mydata = '{"name":"Sunil", "age":20, "language":["python","Js", "Php"]}'
# info = json.loads(mydata)
# print(info)
# print(info['name'])
# print(info['age'])
# print(info['language'])

# Dumps🧑
# it translate python dictionary to Json

mydict = {'name':'prasanna', 
            'age':20, 
            'skills':['bike', 'car', 'coding', 'editing']}

pra = json.dumps(mydict , sort_keys=True)
print(pra)
# print(pra[])