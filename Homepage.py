rom Tkinter import *
from tkMessageBox import * 
from PIL import ImageTk, Image

root1 = Tk()
root1.title('Centre of mass')
root1.geometry('800x500')

img = Image.open('space.jpg')
img = img.resize((800,500),Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
panel = Label(root1,image=photoImg)
panel.place(x=0,y=0)

l1 = Label(root1,text='Centre of Mass',bg='#151B54',fg='white',width=20,font=('Georgia',30))
l1.place(x=130,y=30)

def p4():
    global root1
    root1.destroy()
    execfile('Theory.py')
    
def p1():
    global root1
    root1.destroy()
    execfile('Calculator.py')
    
def p2():
    global root1
    root1.destroy()
    execfile('Teamproject.py')

def p3():
    global root1
    root1.destroy()
    execfile('Slope.py')
  
def q():
    global root1
    aq = askquestion('Leaving?','Are you sure you want to quit?')
    if aq == "yes":
        root1.destroy()

b4 = Button(root1,text='What is Centre of Mass?',font=('Georgia',15),fg='WHITE',bg='#151B54',width = 25, height=1,command=p4)
b4.place(x=230,y=130)

b1 = Button(root1, text='Centre of Mass Calculator',font=('Georgia',15),fg='WHITE',bg='#151B54',width = 25, height=1,command=p1)
b1.place(x=230,y=200)

b2 = Button(root1, text='Space Exploration!',font=('Georgia',15),fg='WHITE',bg='#151B54',width = 25, height=1,command=p2)
b2.place(x=230,y=270)

b3 = Button(root1, text='Topple Game',font=('Georgia',15),fg='WHITE',bg='#151B54',width = 25, height=1,command=p3)
b3.place(x=230,y=340)

b5= Button(root1, text='QUIT',font=('Georgia',15),fg='BLACK',bg='RED',width=25,height=1,command=q)
b5.place(x=230,y=430)


root1.mainloop()

