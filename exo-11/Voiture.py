from direction import Direction
class voiture(Direction):


    NB_ROUE = 4
    __couleur = 'bleu'


    def __init__(self):
      super().__init__()


    def demarrer(self):
        print("vroum vroum")