import json

# d = open('doc.json', 'r+', encoding='utf-8', newline="")
# print(json.load(d))

# for entry in json.load(d):
#     sourceFile = open('python.txt', 'a')
#     print(entry['members'][0]['name'], file = sourceFile)
#     print(entry.get('formed'))
#     sourceFile.close()

with open('doc.json') as f:
    data = json.load(f)

key = 0

for el in data :
    sourceFile = open('python.txt', 'a')
    print(data['members'][key]['name'], file = sourceFile)
    sourceFile.close()
    print(data['members'][key]['name'])
    key += 1


