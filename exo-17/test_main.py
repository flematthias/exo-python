class MyClass:
    @staticmethod
    def staticmethod(up):
        return up.upper()


print(MyClass.staticmethod('stringtoupper'))

def test_myclass():
    assert MyClass.staticmethod('stringtoupper')

def test_bug():
    assert 1/0