class MyClass:
    @staticmethod
    def staticmethod(up):
        return up.upper()


print(MyClass.staticmethod('stringtoupper'))

def test_myclass():
    MyClass.staticmethod('stringtoupper')

def test_bug():
    return 1/0