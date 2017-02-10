from giocatore import Giocatore
from pistola import Pistola
import curses

stdscr=curses.initscr()

curses.curs_set(0)

chris = Giocatore("Christian", 100)
vinc = Giocatore("Vincenzo", 100)

stdscr.addstr (0,0,"Il giocatore "+chris.getName()+" ha "+str(chris.getLife())+" PV")
stdscr.addstr (0,40,"Il giocatore "+vinc.getName()+" ha "+str(vinc.getLife())+" PV")

#Giocatore 1

stdscr.addstr (2,5,"xxxx")
stdscr.addstr (3,4,"x")
stdscr.addstr (3,9,"x")
stdscr.addstr (4,4,"x")
stdscr.addstr (4,8,"xx")
stdscr.addstr (5,4,"x")
stdscr.addstr (5,9,"x")
stdscr.addstr (6,5,"xxxx")
stdscr.addstr (7,6,"x")
stdscr.addstr (8,6,"x")
stdscr.addstr (9,6,"x")
stdscr.addstr (10,6,"x")
stdscr.addstr (11,6,"x")
stdscr.addstr (11,6,"xxxxxxx")
stdscr.addstr (12,6,"x")
stdscr.addstr (13,6,"x")
stdscr.addstr (14,6,"x")
stdscr.addstr (15,6,"x")
stdscr.addstr (16,6,"x")
stdscr.addstr (17,6,"xxxx")
stdscr.addstr (10,11,"xxxx")
stdscr.addstr (12,11,"x")

#Giocatore 2

stdscr.addstr (2,50,"xxxx")
stdscr.addstr (3,49,"x")
stdscr.addstr (3,54,"x")
stdscr.addstr (4,49,"xx")
stdscr.addstr (4,54,"x")
stdscr.addstr (5,49,"x")
stdscr.addstr (5,54,"x")
stdscr.addstr (6,50,"xxxx")
stdscr.addstr (7,51,"x")
stdscr.addstr (8,51,"x")
stdscr.addstr (9,51,"x")
stdscr.addstr (10,51,"x")
stdscr.addstr (11,51,"x")
stdscr.addstr (11,51,"xxxxxxx")
stdscr.addstr (12,51,"x")
stdscr.addstr (13,51,"x")
stdscr.addstr (14,51,"x")
stdscr.addstr (15,51,"x")
stdscr.addstr (16,51,"x")
stdscr.addstr (17,51,"xxxx")
stdscr.addstr (10,56,"xxxx")
stdscr.addstr (12,56,"x")
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
