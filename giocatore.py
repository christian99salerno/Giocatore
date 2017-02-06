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
            print "Il giocatore",self.getName()," e' GAME OVER"
        else:
            self.p.spara() 
            self.life=self.life-10
         
#g=Giocatore("chrgianvinc", 10)
#print g.getLife() 
#g.danno_colpo()
#print g.getLife()

#if __name__=='__main__':
   # g = Giocatore("chris", 100)
   # print g
