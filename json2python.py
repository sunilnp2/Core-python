import json

# convert json to python in python

json_data = {"Name":"Sunil", "age":20}

parse_data = json.loads(json_data)
print(parse_data)