from pistola import Pistola
import random
import curses

class Giocatore:
    def __init__(self, name, life):
         self.name=name
         self.life=life
         self.p=Pistola(5)
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
        giocatore2.life=giocatore2.life-random.randrange(5,41)
    def getMunizioni(self):
        return self.p.munizioni
    def disegno_giocatore(self, lato):

        stdscr=curses.initscr()

        curses.curs_set(0)

        if lato=="s":
            stdscr.addstr (0,0,"Il giocatore "+self.getName()+" ha "+str(self.getLife())+" PV")
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
        elif lato=="d":
            stdscr.addstr (0,40,"Il giocatore "+self.getName()+" ha "+str(self.getLife())+" PV")
            stdscr.addstr (2,50,"xxxx")
	    stdscr.addstr (3,49,"x")
	    stdscr.addstr (3,54,"x")
            stdscr.addstr (4,49,"xx") 
            stdscr.addstr (4,54,"x")
            stdscr.addstr (5,49,"x")
            stdscr.addstr (5,54,"x")
            stdscr.addstr (6,50,"xxxx")
            stdscr.addstr (7,52,"x")
            stdscr.addstr (8,52,"x")
	    stdscr.addstr (9,52,"x")
     	    stdscr.addstr (10,52,"x")
	    stdscr.addstr (11,52,"x")
	    stdscr.addstr (11,45,"xxxxxxx")
	    stdscr.addstr (12,52,"x")
            stdscr.addstr (13,52,"x")
            stdscr.addstr (14,52,"x")
            stdscr.addstr (15,52,"x")
            stdscr.addstr (16,52,"x")
            stdscr.addstr (17,49,"xxxx")
            stdscr.addstr (10,43,"xxxx")
            stdscr.addstr (12,46,"x")
            stdscr.refresh()
        stdscr.getch()
        curses.endwin() 
    def proiettile(self, lato)
        stdscr=curses.initscr()

        curses.curs_set(0)

        if lato=="s":
            for i in range(13,52):
               stdscr.addstr (10,i,"-")
               stdscr.getch()
        elif lato=="d":
            for i in range(47, 
           
        

 
