from giocatore import Giocatore

chris = Giocatore("chris", 100)

while(chris.getLife>0):
    chris.danno_colpo()
    print chris.getLife()

