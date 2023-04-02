import json

with open('file.json', 'r') as f:
    data = json.load(f)
    print(data)

# writing data into json file
data = {'Name': 'Subhash', 'Age': 22, 'City': 'Lucknow'}

with open('file.json', 'w') as f:
    json.dump(data, f)

