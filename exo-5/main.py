from datetime import datetime, timedelta
hui = datetime.now()

def toto(huidef) :
    def tata(huiimbriq) :
        huiimbriq +=  timedelta(days=2)

        return huiimbriq
    return tata(huidef)

print(toto(hui))