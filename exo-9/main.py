# Exception

from requests import request
try:
    r = request.__get__('https://github.com')
except Exception as e:
    print(e)
finally:
    print('fin')