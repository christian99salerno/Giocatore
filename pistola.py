class Pistola:
    def __init__(self, munizioni):
        self.munizioni=munizioni
    def setMunizioni(self, munizioni):
        self.munizioni=munizioni
    def getMunizioni(self):
        return self.munizioni
    def spara(self):
        self.munizioni=self.munizioni-1


