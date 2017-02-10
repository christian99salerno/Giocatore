from giocatore import Giocatore
from pistola import Pistola
import curses

stdscr=curses.initscr()

curses.curs_set(0)

chris = Giocatore("Christian", 100)
vinc = Giocatore("Vincenzo", 100)

stdscr.addstr (0,0,"Il giocatore "+chris.getName()+" ha "+str(chris.getLife())+" PV")
stdscr.addstr (0,40,"Il giocatore "+vinc.getName()+" ha "+str(vinc.getLife())+" PV")

stdscr.refresh()
stdscr.getch()
curses.endwin()

#while chris.getLife() > 0 and chris.getMunizioni() > 0 or vinc.getLife() > 0 and vinc.getMunizioni() > 0:
   # chris.danno_colpo(vinc)
    #print chris.getName(),"spara a",vinc.getName(),"PV=",vinc.getLife(),"e",chris.getName(),"ha munizioni=",chris.getMunizioni()
    #if vinc.getLife()<=0:
       #print "GAME OVER per il giocatore",vinc.getName()
     #  break
    #elif chris.getMunizioni() == 0:
       #print "GAME OVER per il Giocatore",chris.getName(),"poiche' ha",chris.getMunizioni(),"munizioni"
     #  break
    #vinc.danno_colpo(chris)
    #print vinc.getName(),"spara a",chris.getName(),"PV=",chris.getLife(),"e",vinc.getName(),"ha munizioni=",vinc.getMunizioni()
    #if chris.getLife()<=0: 
      # print "GAME OVER per il Giocatore",chris.getName()
     #  break
    #elif vinc.getMunizioni() == 0:
       #print "GAME OVER per il Giocatore",vinc.getName(),"poiche' ha",vinc.getMunizioni(),"munizioni"
     #  break
