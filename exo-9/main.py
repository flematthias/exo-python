# Exception

try:
    a = 12/0
except Exception as e:
    print(e)
finally:
    print('fin')