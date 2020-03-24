from random import randint

a = randint(0,10)

print(a)

with open('randomnumber.txt', 'a') as f:
    a = str(a)
    f.write(a)