from tkinter import *
from random import *
import time
from time import sleep
import threading

win=Tk()
win.title("Test muskosti")
win.geometry("650x600+100+50")
win.configure(background="white")

broj=0
start=0
reza=Label(win,text=str(broj),bg="purple" , fg="white"\
           , font=("Courier", 40))
reza.place(x=300,y=130)

vreme=Label(win,text=str(broj),bg="purple" , fg="white")
vreme.place(x=80,y=80)

def tajmer():
    global start
    
    pocetak=time.time()
    start=1
    
    while time.time()-pocetak < 10:
        sleep(0.1)
        vreme.config(text=str( time.time()-pocetak ) )
    start=5

t1= threading.Thread(target=tajmer )

def stis1():
    global broj,start,pocetak
    if start==0:
        start=1
        t1.start()
    if start==5: #ako je proslo 10 sekundi i igra je u biti gotova da ne radi nis
        return
    broj+=1
    reza.config(text=str(broj))

gumb1=Button(win,text="pucaj" , width=10 , command=stis1 )

gumb1.place(x=200,y=130)

F1  = open("highscore.txt", "r")
kk=int(str(F1.read()))


highscore=Label( win, text="HIGHSCORE " + str(kk) , bg="purple" , fg="white" )
highscore.place( x=360 , y=360)

win.mainloop()

F1.close()

F1 = open("highscore.txt", "w")

if broj > kk:
    F1.write( str(broj) )
else :
    F1.write( str(kk) )
    
F1.close()
