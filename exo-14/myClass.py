class myClass:
    """classe pour agrandir
    """
    @staticmethod
    def staticmethod(up):
        """methode pour agrandir
        
        Arguments:
            a {str} -- le string en minuscule
        
        Returns:
            str -- le resultat en capitale
        """
        return up.upper()


print(myClass.staticmethod('stringtoupper'))
