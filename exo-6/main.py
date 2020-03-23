import json

f = open('doc.json', 'r+', encoding='utf-8', newline="")
print(f.read())
for entry in json.load(f.read()):
    print(entry)