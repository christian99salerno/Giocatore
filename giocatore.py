from pistola import Pistola


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
    def danno_colpo(self):
        if self.life<=0:
            return -1
        else:
            self.p.spara() 
            self.life=self.life-10
