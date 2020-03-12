# -*- coding: cp1252 -*-
from Tkinter import *
from tkMessageBox import * 
from PIL import ImageTk, Image

root2 = Tk()
root2.title('Centre of mass calculator')
root2.geometry('800x500')
root2.configure(background='#FBF6D9')


global h1
def h1():
    showinfo("Instruction", "This is a centre of mass calculator.\n\n\
1. Please input the masses of both objects (in kg)\n\
2. Please input the distance between both objects (in m)\n\
3. Click the 'Calculate' button to calculate the centre of mass between both objects.")


imgo4 = Image.open('QM.png')
imgo4 = imgo4.resize((20,20), Image.ANTIALIAS)
photoImgo4 = ImageTk.PhotoImage(imgo4)

ml = Label(root2, text='Centre of Mass Calculator',bg='#FBF6D9',fg='black',font=('Georgia',20))
ml.place(x=250,y=30)

mb3 = Button(root2, text='Help',width=40,height=40, image=photoImgo4,font=('Georgia',13),bg='#E7A1B0',compound='top',command=h1)
mb3.place(x=730,y=10)

l1 = Label(root2, text='mass of first object, m   =',bg='#FBF6D9',fg='black',font=('Georgia',15))
l1.place(x=140,y=130)
l3 = Label(root2, text='1',bg='#FBF6D9',fg='black',font=('Georgia',10))
l3.place(x=340,y=140)

l5 = Label(root2, text='mass of second object, m   =',bg='#FBF6D9',fg='black',font=('Georgia',15))
l5.place(x=115,y=180)
l4 = Label(root2, text='2',bg='#FBF6D9',fg='black',font=('Georgia',10))
l4.place(x=340,y=190)

l2 = Label(root2, text='distance between both objects(m), x =',bg='#FBF6D9',fg='black',font=('Georgia',15))
l2.place(x=30,y=250)

e1 = Entry(root2,width=20,bg='#F3E5AB',font=('Georgia',13))
e1.place(x=380,y=135)

e2 = Entry(root2,width=20,bg='#F3E5AB',font=('Georgia',13))
e2.place(x=380,y=185)

e3 = Entry(root2,width=20,bg='#F3E5AB',font=('Georgia',13))
e3.place(x=380,y=255)

def cal():
    global e1
    global e2
    global e3
    global la1
    global la2
    global la
    
    a = e1.get()
    b = e2.get()
    c = e3.get()

    if a == '' or b == '' or c=='':
        showinfo('Warning','Please input a number')

    elif a.isalpha() == True or b.isalpha() == True or c.isalpha() == True:
        showinfo('Warning','Please ensure that you have entered a valid number')

    else:
        v1 = float(b)*float(c)
        v2 = float(a)+float(b)

        fa = v1/v2
        
        la.config(text= 'Centre of Mass  = '+ '('+str(a)+' × 0 ' + ' +  ' + str(b)+' × ' + str(c)+')'+
                  ' ÷ ' + '('+ str(a) + ' + ' + str(b)+')')

        la1 = Label(root2,text='=',bg='#FBF6D9',fg='black',font=('Georgia',15))
        la1.place(x=295,y=430)

        la2.config(text= str(fa)+'m')
        
def back():
    global root2
    root2.destroy()
    execfile('Homepage.py')
    
la = Label(root2,text=' ' ,bg='#FBF6D9',fg='black',font=('Georgia',15))
la.place(x=150,y=400)

la2 = Label(root2,text=' ',bg='#FBF6D9',fg='black',font=('Georgia',15))
la2.place(x=320,y=430)

b1 = Button(root2,text='Calculate',width=10,height=1,bg='#FFD801',font=('Georgia',15),command=cal)
b1.place(x=280,y=320)

b2 = Button(root2,text='Return back to\n home screen',bg='#F62217',font=('Georgia',13),command=back)
b2.place(x=670,y=80)   

root2.mainloop()
