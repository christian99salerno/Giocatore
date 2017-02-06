from giocatore import Giocatore

chris = Giocatore("Christian", 100)

print "Il giocatore",chris.getName(),"ha",chris.getLife(),"PV"

while(chris.getLife()>0):
    chris.danno_colpo()

