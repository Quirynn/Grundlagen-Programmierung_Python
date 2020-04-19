class Nutzer:
    def __init__(self, vorname, nachname):
        self.__vorname = vorname
        self.__nachname = nachname

    def getVorname(self):
        return self.__vorname

    def getNachname(self):
        return self.__nachname

