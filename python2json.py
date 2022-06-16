import json


python_data = {'name':"sunil", 'age':20}

json_data = json.dumps(python_data)
print(json_data)
print(type(json_data))