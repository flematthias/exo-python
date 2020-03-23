import json

d = open('doc.json', 'r+', encoding='utf-8', newline="")
# print(d.read())

for entry in d:
    sourceFile = open('python.txt', 'a')
    print(entry, file = sourceFile)
    print(entry)
    sourceFile.close()


