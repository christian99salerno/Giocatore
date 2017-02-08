from giocatore import Giocatore
from pistola import Pistola

chris = Giocatore("Christian", 100)
vinc = Giocatore("Vincenzo", 100)


print "Il giocatore",chris.getName(),"ha",chris.getLife(),"PV"
print "Il giocatore",vinc.getName(),"ha",vinc.getLife(),"PV"

while chris.getLife() > 0 or vinc.getLife() > 0:
    chris.danno_colpo(vinc)
    print "Dopo il colpo subito il giocatore",vinc.getName(),"ha",vinc.getLife(),"PV"
    if vinc.getLife()<=0 or vinc.getMunizioni() == 0:
       print "GAME OVER per il giocatore",vinc.getName()
       break
    vinc.danno_colpo(chris)
    print "Dopo il colpo subito il giocatore",chris.getName(),"ha",chris.getLife(),"PV"
    if chris.getLife()<=0 or vinc.getMunizioni() == 0:
       print "GAME OVER per il Giocatore",chris.getName()
       break
