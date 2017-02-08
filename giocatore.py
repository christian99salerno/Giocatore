from pistola import Pistola
import random


class Giocatore:
    def __init__(self, name, life):
         self.name=name
         self.life=life
         self.p=Pistola(10)
    
    def setLife(self, life):
        self.life=life
    def getLife(self):
        return self.life
    def setName(self, name):
        self.name=name
    def getName(self):
        return self.name
    def danno_colpo(self,giocatore2):
        self.p.spara() 
        giocatore2.life=giocatore2.life-random.randrange(5,26)
    def getMunizioni(self):
        return self.p
