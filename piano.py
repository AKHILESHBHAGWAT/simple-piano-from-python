import pygame
import sys
from tkinter import *
pygame.init()
#INITIALIZE PYGAME
root = Tk()
frame = Frame(root)
frame.pack()
root.title("PIANO")
num1 = StringVar()

frame1 = Frame(root)
label1=Label(frame,text="PIANO BUILD BY PYTHON",font=("ARAL", 55),bg="White",relief="groove",bd=10).pack(side=TOP)
frame1.pack()


frame2 = Frame(root)
text=Entry(frame,textvariable=num1,font=("ARAL"),bg="White",relief="groove",width=3,bd=10,insertwidth=1).pack(side=TOP)
frame2.pack()

from playsound import playsound

playsound("START.mp3")


def value_A():
    num1.set("SA")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\C_s.wav")
    sound.play()
    return
Button1 = Button(root,text="",command=value_A,width=5,height=20,borderwidth="5",relief="raised",bg="White").pack(side=LEFT)                
def value_B():
    num1.set("B")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\B.wav")
    sound.play()
    return
Button2 = Button(root,text="",command=value_B,width=5,height=20,borderwidth="5",relief="raised",bg="Black").pack(side=LEFT)                
def value_Bb():
    num1.set("RE")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\D_s.wav")
    sound.play()
    return
Button3 = Button(root,text="",command=value_Bb,width=5,height=20,borderwidth="5",relief="raised",bg="White").pack(side=LEFT)
def value_C():
    num1.set("A#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\C.wav")
    sound.play()
    return
Button4 = Button(root,text="",command=value_A,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
def value_C_s():
    num1.set("GA")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\F_s.wav")
    sound.play()
    return
Button5 = Button(root,text="",command=value_C_s,width=5,height=20,borderwidth="5",relief="groove",bg="White").pack(side=LEFT)
def value_C_s1():
    num1.set("C#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\C_s1.wav")
    sound.play()
    return
Button6 = Button(root,text="",command=value_C_s1,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
def value_C1():
    num1.set("MA")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\A.wav")
    sound.play()
    return
Button7 = Button(root,text="",command=value_C1,width=5,height=20,borderwidth="5",relief="groove",bg="White").pack(side=LEFT)
def value_D():
    num1.set("C#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\D.wav")
    sound.play()
    return
Button8 = Button(root,text="",command=value_D,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
def value_D_s():
    num1.set("PA")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\G_s.wav")
    sound.play()
    return
Button9 = Button(root,text="",command=value_D_s,width=5,height=20,borderwidth="5",relief="groove",bg="White").pack(side=LEFT)
def value_D_s1():
    num1.set("C#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\Bb.wav")
    sound.play()
    return
Button10 = Button(root,text="",command=value_D_s1,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
def value_D1():
    num1.set("DA")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\D1.wav")
    sound.play()
    return
Button11 = Button(root,text="",command=value_D1,width=5,height=20,borderwidth="5",relief="groove",bg="White").pack(side=LEFT)
def value_E():
    num1.set("C#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\G.wav")
    sound.play()
    return
Button12 = Button(root,text="",command=value_E,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
def value_E1():
    num1.set("NI")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\E1.wav")
    sound.play()
    return
Button13 = Button(root,text="",command=value_E1,width=5,height=20,borderwidth="5",relief="groove",bg="White").pack(side=LEFT)
def value_F():
    num1.set("C#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\F.wav")
    sound.play()
    return
Button14 = Button(root,text="",command=value_F,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
def value_F_s():
    num1.set("SA")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\D_s.wav")
    sound.play()
    return
Button15 = Button(root,text="",command=value_F_s,width=5,height=20,borderwidth="5",relief="groove",bg="White").pack(side=LEFT)
def value_F1():
    num1.set("C#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\C1.wav")
    sound.play()
    return
Button16 = Button(root,text="",command=value_F1,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
def value_G():
    num1.set("AA")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\E.wav")
    sound.play()
    return
Button17 = Button(root,text="",command=value_G,width=5,height=20,borderwidth="5",relief="groove",bg="White").pack(side=LEFT)
def value_G_s():
    num1.set("C#")
    sound = pygame.mixer.Sound("D:\AKHILESH\PYTHON\Music_Notes\F_s.wav")
    sound.play()
    return
Button18 = Button(root,text="",command=value_G_s,width=5,height=20,borderwidth="5",relief="groove",bg="Black").pack(side=LEFT)
mainloop()
