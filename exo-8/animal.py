#PEP 8
from espece import Espece
class Animal(Espece):
    _espece = "chien"

    def __init__(self):
        super().__init__()
    
    def infos(self):
        print("ok")
    