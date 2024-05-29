import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, "r") as myfile:
    data = myfile.add
obj = json.loads(data)
print(str(obj[jsonkey]))