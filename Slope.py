from Tkinter import *
from tkMessageBox import * 
from PIL import ImageTk, Image

global raise_frame
def raise_frame(frame):
    frame.tkraise()

root=Tk()
root.title('Slope')
root.geometry('800x500')

global h1
def h1():
    showinfo("Instruction", "***DISCLAIMER***\n\
The unit/measurement used in this program is not in real scale and is just an example only\n\n\
This program allows you to see how the centre of mass of object shift when the angle of inclination changes and when will the object start to topple\n\n\
*IMPORTANT*\n\
The slope has a high friction to prevent the object from sliding down\n\n\
1. Use the scale to adjust the angle of inclination of the plane \
2. Use the 'Check' button to check if the object has toppled")

global f2
f2 = Frame(root,height=1000,width=1600)   
f2.pack()

c2 = Canvas(f2,width=800,height=500,bg='#C68E17')
c2.pack()

t1 = c2.create_polygon(100,250,100,450,400,450,fill='grey')

t2 = c2.create_polygon(160,290,310,390,320,210,fill='black')

line = c2.create_line(265,290,265,480,fill='white')

global move
def move(z):
    global t1
    global t2
    global line
    global s1
    global l1
    global b1
    global l2
    global c2
    l2.destroy()
    c2.delete(ALL)
    a = s1.get()
    t1 = c2.create_polygon(100,250-(3*a),100,450,400,450,fill='grey')
    t2 = c2.create_polygon(170+a,(270-a/2),310+(a/2),(385-(a/9)),330+(1.4*a),(198-(a/3))+10,fill='black')
    line = c2.create_line(265+(1.1*a),290,265+(1.1*a),480,fill='white')
    aaa = s1.get()-34
    l2 = Label(f2, text='Centre of Mass',font=('Georgia',13),fg='black',bg='#C68E17')
    l2.place(x=250+aaa,y=465)

img = Image.open('topple.png')
img = img.resize((660,200), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)

global new
def new():
    global panel
    global photoImg
    global b5
    global b1
    b5.config(state=DISABLED)
    b1.config(state=DISABLED)
    new = Toplevel()
    new.config(background= '#B7CEEC')
    new.geometry('660x400')
    new.title('Explanation')
    inl = Label(new, text='When an object is tilted where its vertical line of centre of gravity falls outside its base,\n\
the object will topple',font=('Georgia',13),bg='#B7CEEC')
    inl.place(x=0,y=10)
    
    panel = Label(new,image=photoImg)
    panel.place(x=0,y=80)

    inl2 = Label(new,text='1. The vertical line of centre \n of mass is still inside the \n object base',font=('Georgia',11),bg='#B7CEEC')
    inl2.place(x=0,y=290)

    inl3 = Label(new,text='2. The vertical line of centre \n of mass is exactly on the \n tip of the object base',font=('Georgia',11),bg='#B7CEEC')
    inl3.place(x=230,y=290)

    inl4 = Label(new,text='3. The vertical line of centre \n of mass has exceeded the \n object base, hence it topples',font=('Georgia',11),bg='#B7CEEC')
    inl4.place(x=460,y=290)

    def abc():
        new.destroy()
        b5.config(state=NORMAL)
        b1.config(state=NORMAL)

    inb1 = Button(new,text='Back',font=('Georgia',11),bg='Red',command=abc)
    inb1.place(x=300,y=360)
    
global check
def check():
    global t1
    global t2
    global line
    global s1
    global l1
    global b1
    global l2
    global b4
    global b5
    a = s1.get()
    if a < 75:
        showinfo('Info','Your triangle is still on the slope')

    elif a == 75:
        showinfo('Info','Your triangle is about to topple')
        
    elif a==76:
        l1.destroy()
        b4.destroy()
        s1.destroy()
        l2.destroy()
        for i in range(550):
            c2.delete(t2)
            c2.delete(line)
            t2 = c2.create_polygon(170+a+(i/2.2),(270-a/2)+i/15,310+(a/2),(385-(a/9)),330+(1.4*a)+i/7.5,(198-(a/3))+10+i/2,fill='black')
            c2.update()
            c2.after(1)
    

            def reset():
                global b5
                b1.destroy()
                b5.destroy()
                global t1
                global t2
                global line
                global s1
                global l1
                global l2
                global b4
                t1 = c2.create_polygon(100,250,100,450,400,450,fill='grey')

                t2 = c2.create_polygon(160,290,310,390,320,210,fill='black')

                line = c2.create_line(265,290,265,480,fill='white')

                s1 = Scale(f2,from_=35,to=76,orient=HORIZONTAL, fg='black',command=move,bg='#D4A017',font=('Georgia',15),troughcolor='#F9966B',activebackground='#F88017',width=25)
                s1.place(x=570,y=390)

                l1 = Label(f2, text='Angle of inclination',font=('Georgia',13),fg='black',bg='#C68E17')
                l1.place(x=550,y=360)

                l2 = Label(f2, text='Centre of Mass',font=('Georgia',13),fg='black',bg='#C68E17')
                l2.place(x=250,y=465)

                b4 = Button(f2,text='Check',bg='#FFCBA4',font=('Georgia',13),command=check)
                b4.place(x=700,y=420)

        b1 = Button(f2,text='Reset',font=('Georgia',13),fg='black',bg='#FFCBA4',command=reset)
        b1.place(x=660,y=400)

        b5 = Button(f2, text='What just happened?',font=('Georgia',13),bg='#FFCBA4',command=new)
        b5.place(x=600,y=350)


def back():
    global root
    root.destroy()
    execfile('Homepage.py')


s1 = Scale(f2,from_=35,to=76,orient=HORIZONTAL, fg='black',command=move,bg='#D4A017',font=('Georgia',15),troughcolor='#F9966B',activebackground='#F88017',width=25)
s1.place(x=570,y=390)

l1 = Label(f2, text='Angle of inclination',font=('Georgia',13),fg='black',bg='#C68E17')
l1.place(x=550,y=360)

l2 = Label(f2, text='Centre of Mass',font=('Georgia',13),fg='black',bg='#C68E17')
l2.place(x=250,y=465)

b4 = Button(f2,text='Check',bg='#FFCBA4',font=('Georgia',13),command=check)
b4.place(x=700,y=410)

imgo4 = Image.open('QM.png')
imgo4 = imgo4.resize((20,20), Image.ANTIALIAS)
photoImgo4 = ImageTk.PhotoImage(imgo4)

b3 = Button(f2, text='Help',width=40,height=40, image=photoImgo4,font=('Georgia',13),bg='#E7A1B0',compound='top',command=h1)
b3.place(x=740,y=10)

b2 = Button(f2,text='Return back to\n home screen',bg='#F62217',font=('Georgia',13),command=back)
b2.place(x=660,y=70)

root.mainloop()
