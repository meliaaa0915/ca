# -*- coding: cp1252 -*-
from Tkinter import *
from tkMessageBox import * 
from PIL import ImageTk, Image

root = Tk()
root.title('Centre of mass theory')
root.geometry('800x600')

c = Canvas(root,width=800,height=500)
c.pack()

img = Image.open('stone.jpg')
img = img.resize((300,600),Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
panel = Label(root,image=photoImg)
panel.place(x=500,y=0)


l1 = Label(root, text='What is the Centre of Mass ?',font=('Georgia',20))
l1.place(x=10,y=30)

l2 = Label(root, text='The centre of mass is a position defined\n\
relative to an object or system of objects.\n\n\
It is the average position of all the parts of the system, \n\
weighted according to their masses.',font=('Georgia',15))
l2.place(x=1,y=100)

l3 = Label(root, text='Equation of the centre of mass',font=('Georgia',20))
l3.place(x=10,y=300)

l4 = Label(root, text='m  × x   + m   × x   ',font=('Georgia',15)) 
l4.place(x=90,y=350)

c.create_line(95,384,275,384)

l5 = Label(root,text='m   + m   ',font=('Georgia',15))
l5.place(x=140,y=385)

l6 = Label(root,text='1',font=('Georgia',11))
l6.place(x=120,y=360)

l7 = Label(root,text='1',font=('Georgia',11))
l7.place(x=160,y=360)

l8 = Label(root,text='2',font=('Georgia',11))
l8.place(x=210,y=360)

l9 = Label(root,text='2',font=('Georgia',11))
l9.place(x=255,y=360)

l10 = Label(root,text='1',font=('Georgia',11))
l10.place(x=160,y=395)

l11 = Label(root,text='2',font=('Georgia',11))
l11.place(x=212,y=395)

l12 = Label(root, text='where m   is the mass of the first object (in kg)',font=('Georgia',15))
l12.place(x=25,y=450)

l13 = Label(root, text='m   is the mass of second object (in kg)',font=('Georgia',15))
l13.place(x=85,y=480)

l14 = Label(root, text='x   is 0',font=('Georgia',15))
l14.place(x=87,y=510)

l15 = Label(root,text='x   is the distance between both objects (in m)',font=('Georgia',15))
l15.place(x=87,y=540)

l16 = Label(root,text='1',font=('Georgia',11))
l16.place(x=105,y=460)

l17 = Label(root,text='2',font=('Georgia',11))
l17.place(x=105,y=490)

l18 = Label(root,text='1',font=('Georgia',11))
l18.place(x=100,y=518)

l19 = Label(root,text='2',font=('Georgia',11))
l19.place(x=100,y=548)

def back():
    global root
    root.destroy()
    execfile('Homepage.py')

b1 = Button(root,text='Return back to\n home screen',bg='#F62217',font=('Georgia',13),command=back)
b1.place(x=650,y=530)


root.mainloop()
