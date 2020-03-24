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
        b = a
        self._loto = a
        print("gagné !") if a == b else print("essaye encore", self)

lancer = MyClass()
print(lancer.number)
lancer.number = 12
print(lancer.number)
