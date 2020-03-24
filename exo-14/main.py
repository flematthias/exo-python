class MyClass:
    """[classe pour agrandir]
    
    Returns:
        [type] -- [description]
    """
    @staticmethod
    def staticmethod(up):
    """[methode pour agrandir]
        
        Arguments:
            a {[string]} -- [le string en minuscule]
        
        Returns:
            [string] -- [le resultat en capitale]
        """
        return up.upper()


print(MyClass.staticmethod('stringtoupper'))
