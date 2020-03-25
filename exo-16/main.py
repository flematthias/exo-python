import logging

logging.basicConfig()
log = logging.getLogger("MyClass")
log.setLevel(logging.CRITICAL)
log.warning('Attention')
log.error('erreur')
log.critical('critique')
log.log(50, "coucou")


class MyClass:
    @staticmethod
    def staticmethod(up):

        return up.upper()


print(MyClass.staticmethod('stringtoupper'))

