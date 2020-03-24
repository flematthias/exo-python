class MyClass:
    def __init__(self):
        self._loto = 0

    @property
    def number(self):
        print("getter")
        return self._loto

    @number.setter
    def number(self, a):
        print("setter")
        return self._loto

lancer = MyClass()
print(lancer.number)
lancer.number = 12
print(lancer.number)
