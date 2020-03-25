class MyClass:
    @staticmethod
    def staticmethod(up):
        return up.upper()


print(MyClass.staticmethod('stringtoupper'))

def test_myclass():
    assert MyClass.staticmethod('stringtoupper') == 'STRINGTOUPPER'
    assert MyClass.staticmethod('stringtoupper') == 'stringtoupper'

def test_bug():
    try:
        1/0
    except Exception as e:
        assert e
    