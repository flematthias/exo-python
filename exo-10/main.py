def decorate_upper(func):
    def custom_upper():
        return func().upper()

    return custom_upper


@decorate_upper
def test():
    return "Hello"


print(test())
