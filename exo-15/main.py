# Là c'est une liste avec un itérateur
mylist = range(3)
for i in mylist:
    print(i)

# Là c'est une liste avec un genarateur
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i

mygenerator = createGenerator()

for i in mygenerator:
    print(i)