class ThisAnimal(espece,sousEspece,nom,famille):
    _espece = "chien"
    _sousEspece = "Caniche"
    _nom = "Brutus"
    _famille = "canidé"

    def __init__(self):
        super().__init__()