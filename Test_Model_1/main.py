import json

with open("json_data.json", "r") as f:
    data1 = json.load(f)
print(data1.items())