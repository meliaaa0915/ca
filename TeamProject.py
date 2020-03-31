from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image

global h1
def h1():
    showinfo("Instruction", "Welcome onboard !!! \nTo start our space exploration, there are a few instruction to follow.\n\
         \n1. Select your planet of different masses. \n2. Move the distance of the planet using the scale.\
         \n3. GREEN BUTTON - to locate the centre of mass \n4. RED BUTTON - return back to home page")

    
global raise_frame
def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry('1600x1000')
root.title('Centre of mass')

f2 = Frame(root)
f2.place(x=0,y=0,height=1000,width=1600)
c2 = Canvas(f2,width=1600,height=1000,bg='black')
c2.place(x=0,y=0)
img2 = Image.open('sun.jpg')
img2 = img2.resize((350,350), Image.ANTIALIAS)
global photoImg2
photoImg2 = ImageTk.PhotoImage(img2)
panel2 = Label(f2,image=photoImg2,bg='black')
panel2.place(x=115,y=100)
l2 = Label(f2, text='Sun \n Mass = 1000 kg',fg='white',bg='black',font=('Georgia',16))
l2.place(x=225,y=40)
c2.create_oval(1050,200,1200,350, fill='#bc13fe')
t2 = Label(f2,text="PLANET 2\nMass= 300 kg",height=2,width=10,fg='WHITE',bg='BLACK',font=('Georgia',15))
t2.place(x=1085,y=130)
la2 = Label(f2, text='None')
la2.place(x=0,y=0)

def move2(z):
    global t2
    global c2
    global f2
    global s2
    c2.delete(ALL)
    t2.destroy()
    la2.destroy()
    img22 = Image.open('sun.jpg')
    img22 = img22.resize((350,350), Image.ANTIALIAS)
    photoImg22 = ImageTk.PhotoImage(img22)
    panel22 = Label(f2,image=photoImg2,bg='black')
    panel22.place(x=115,y=100)
    a = s2.get()
    c2.create_oval(a,200,a+150,350, fill='#bc13fe')
    
    t2 = Label(f2,text="PLANET 2\nMass= 300 kg",height=2,width=10,fg='WHITE',bg='BLACK',font=('Georgia',15))
    t2.place(x=a+15,y=130)

    for x in range(500,a+1):
        c2.create_line(400,275,x,275, fill='white')

lla2 = False
def cal2():
    global la2
    global lla2
    s = s2.get()
    if lla2==True:
        la2.destroy()
        lla2 = False
        a = 1000000*0
        b = float(300000*s)
        ca = 1000000+300000
        d = float((a+b)/ca)
        d = round(d,2)
        la2 = Label(f2, text = 'Centre of mass = ' + str(d) +' km' ,fg='white', bg='black',font=('Georgia',15))
        la2.place(x=500,y=380)
        lla2 = True

        aa = s-460
        bb = 1000000*0
        cc = float(300000*aa)
        cca = 1000000+300000
        dd = float((bb+cc)/cca)
        ee = round(dd)
        c2.create_oval(ee+460,270,ee+470,280, fill='red')

    else:
        a = 1000000*0
        b = float(300000*s)
        ca = 1000000+300000
        d = float((a+b)/ca)
        d = round(d,2)
        la2 = Label(f2, text = 'Centre of mass = ' + str(d) +' km' ,fg='white', bg='black',font=('Georgia',15))
        la2.place(x=500,y=380)
        lla2= True

        aa = s-460
        bb = 1000000*0
        cc = float(300000*aa)
        cca = 1000000+300000
        dd = float((bb+cc)/cca)
        ee = round(dd)
        c2.create_oval(ee+460,270,ee+470,280, fill='red')
       



f3 = Frame(root)
f3.place(x=0,y=0,height=1000,width=1600)
c3 = Canvas(f3,width=1600,height=1000,bg='black')
c3.place(x=0,y=0)
img3 = Image.open('sun.jpg')
img3 = img3.resize((350,350), Image.ANTIALIAS)
global photoImg3
photoImg3 = ImageTk.PhotoImage(img3)
panel3 = Label(f3,image=photoImg3,bg='black')
panel3.place(x=115,y=100)
l3 = Label(f3, text='Sun \n Mass = 1000 kg',fg='white',bg='black',font=('Georgia',16))
l3.place(x=225,y=40)
c3.create_oval(1050,175,1250,375, fill='#faed27')
t3 = Label(f3,text="PLANET 3\nMass= 400 kg",height=2,width=10,fg='WHITE',bg='BLACK',font=('Georgia',15))
t3.place(x=1110,y=110)
la3 = Label(f3, text='None')
la3.place(x=0,y=0)

def move3(z):
    global t3
    global c3
    global f3
    global s3
    c3.delete(ALL)
    t3.destroy()
    la3.destroy()
    img33 = Image.open('sun.jpg')
    img33 = img33.resize((350,350), Image.ANTIALIAS)
    photoImg33 = ImageTk.PhotoImage(img33)
    panel33 = Label(f3,image=photoImg3,bg='black')
    panel33.place(x=115,y=100)
    a = s3.get()
    c3.create_oval(a,175,a+200,375, fill='#faed27')
    t3 = Label(f3,text="PLANET 3\nMass= 400 kg",height=2,width=10,fg='WHITE',bg='BLACK',font=('Georgia',15))
    t3.place(x=a+40,y=100)

    for x in range(500,a+1):
        c3.create_line(400,275,x,275, fill='white')

lla3 = False
def cal3():
    global la3
    global lla3
    s = s3.get()
    if lla3==True:
        la3.destroy()
        lla3 = False
        a = 1000000*0
        b = float(400000*s)
        ca = 1000000+400000
        d = float((a+b)/ca)
        d = round(d,2)
        la3 = Label(f3, text = 'Centre of mass = ' + str(d) +' km' ,fg='white', bg='black',font=('Georgia',15))
        la3.place(x=500,y=380)
        lla3 = True

        aa = s-460
        bb = 1000000*0
        cc = float(400000*aa)
        cca = 1000000+400000
        dd = float((bb+cc)/cca)
        ee = round(dd)
        c3.create_oval(ee+460,270,ee+470,280, fill='red')

    else:
        a = 1000000*0
        b = float(400000*s)
        ca = 1000000+400000
        d = float((a+b)/ca)
        d = round(d,2)
        la3 = Label(f3, text = 'Centre of mass = ' + str(d) +' km' ,fg='white', bg='black',font=('Georgia',15))
        la3.place(x=500,y=380)
        lla3= True
        e = float(d)
        f = round(e/6)

        aa = s-460
        bb = 1000000*0
        cc = float(400000*aa)
        cca = 1000000+400000
        dd = float((bb+cc)/cca)
        ee = round(dd)
        c3.create_oval(ee+460,270,ee+470,280, fill='red')

        
f1 = Frame(root)
f1.place(x=0,y=0,height=1000,width=1600)
c1 = Canvas(f1,width=1600,height=1000,bg='black')
c1.place(x=0,y=0)
img1 = Image.open('sun.jpg')
img1 = img1.resize((350,350), Image.ANTIALIAS)
global photoImg1
photoImg1 = ImageTk.PhotoImage(img1)
panel1 = Label(f1,image=photoImg1)
panel1.place(x=115,y=100)
l1 = Label(f1, text='Sun \n Mass = 1000 kg',fg='white',bg='black',font=('Georgia',16))
l1.place(x=225,y=40)
c1.create_oval(1050,225,1150,325, fill='cyan')
t1 = Label(f1,text="PLANET 1\nMass= 200 kg",height=2,width=10,fg='WHITE',bg='BLACK',font=('Georgia',15))
t1.place(x=1057,y=150)
la1 = Label(f1, text='None')
la1.place(x=0,y=0)


def move1(z):
    global t1
    global c1
    global f1
    global s1
    c1.delete(ALL)
    t1.destroy()
    la1.destroy()

    panel11 = Label(f1,image=photoImg1,bg='black')
    panel11.place(x=115,y=100)
    a = s1.get()
    c1.create_oval(a,225,a+100,325, fill='cyan')
    t1 = Label(f1,text="PLANET 1\nMass= 200 kg",height=2,width=10,fg='WHITE',bg='BLACK',font=('Georgia',15))
    t1.place(x=a-10,y=150)

    for x in range(500,a+1):
        c1.create_line(400,275,x,275, fill='white')

lla1 = False
def cal1():
    global la1
    global lla1
    s = s1.get()
    if lla1==True:
        lla1 = False
        la1.destroy()
        a = 1000000*0
        b = float(200000*s)
        ca = 1000000+200000
        d = float((a+b)/ca)
        d = round(d,2)
        la1 = Label(f1, text = 'Centre of mass = ' + str(d) +' km' ,fg='white', bg='black',font=('Georgia',15))
        la1.place(x=500,y=350)
        lla1 = True

        aa = s-460
        bb = 1000000*0
        cc = float(200000*aa)
        cca = 1000000+200000
        dd = float((bb+cc)/cca)
        ee = round(dd)
        c1.create_oval(ee+460,270,ee+470,280, fill='red')

        
    else:
        a = 1000000*0
        b = float(200000*s)
        ca = 1000000+200000
        d = float((a+b)/ca)
        d = round(d,2)
        la1 = Label(f1, text = 'Centre of mass = ' + str(d) +' km' ,fg='white', bg='black',font=('Georgia',15))
        la1.place(x=500,y=350)
        lla1 = True

        aa = s-460
        bb = 1000000*0
        cc = float(200000*aa)
        cca = 1000000+200000
        dd = float((bb+cc)/cca)
        ee = round(dd)
        c1.create_oval(ee+460,270,ee+470,280, fill='red')
       

       

imgo1 = Image.open('planet1.jpg')
imgo1 = imgo1.resize((100,100), Image.ANTIALIAS)
photoImgo1 = ImageTk.PhotoImage(imgo1)

imgo2 = Image.open('planet2.gif')
imgo2 = imgo2.resize((100,100), Image.ANTIALIAS)
photoImgo2 = ImageTk.PhotoImage(imgo2)

imgo3 = Image.open('planet3.png')
imgo3 = imgo3.resize((100,100), Image.ANTIALIAS)
photoImgo3 = ImageTk.PhotoImage(imgo3)

b1 = Button(f1,text='Planet 1',width = 100, height=120, image=photoImgo1,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f1),state=DISABLED)
b1.place(x=100,y=550)
b2 = Button(f1,text='Planet 2',width = 100, height=120, image=photoImgo2,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f2))
b2.place(x=250,y=550)
b3 = Button(f1,text='Planet 3',width = 100, height=120, image=photoImgo3,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f3))
b3.place(x=400,y=550)
outl1 = Label(f1,text='Distance between Sun and Planet 1 (km)',fg='white', bg='black',font=('Georgia',15))
outl1.place(x=630,y=525)
s1 = Scale(f1,from_=600,to=1300,orient=HORIZONTAL, fg='white',bg='black',command=move1,font=('Georgia',15),troughcolor='white',activebackground='grey',width=25)
s1.place(x=740,y=555)
tb = Button(f1,text='Calculate and plot \nthe centre of mass', fg='black',width = 25, height=4,bg='green',font=('Georgia',15),command=cal1)
tb.place(x=650,y=650)

b1 = Button(f2,text='Planet 1',width = 100, height=120, image=photoImgo1,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f1))
b1.place(x=100,y=550)
b2 = Button(f2,text='Planet 2',width = 100, height=120, image=photoImgo2,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f2),state=DISABLED)
b2.place(x=250,y=550)
b3 = Button(f2,text='Planet 3',width = 100, height=120, image=photoImgo3,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f3))
b3.place(x=400,y=550)
outl1 = Label(f2,text='Distance between Sun and Planet 2 (km)',fg='white', bg='black',font=('Georgia',15))
outl1.place(x=630,y=525)
s2 = Scale(f2,from_=600,to=1300,orient=HORIZONTAL, fg='white',bg='black',width = 25,command=move2,font=('Georgia',15),troughcolor='white',activebackground='grey')
s2.place(x=740,y=555)
tb = Button(f2,text='Calculate and plot \nthe centre of mass', fg='black',width = 25, height=4,bg='green',font=('Georgia',15),command=cal2)
tb.place(x=650,y=650)

b1 = Button(f3,text='Planet 1',width = 100, height=120, image=photoImgo1,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f1))
b1.place(x=100,y=550)
b2 = Button(f3,text='Planet 2',width = 100, height=120, image=photoImgo2,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f2))
b2.place(x=250,y=550)
b3 = Button(f3,text='Planet 3',width = 100, height=120, image=photoImgo3,font=('Georgia',15), compound='bottom',bg='black',fg='white',command=lambda:raise_frame(f3),state=DISABLED)
b3.place(x=400,y=550)
outl1 = Label(f3,text='Distance between Sun and Planet 3 (km)',fg='white', bg='black',font=('Georgia',15))
outl1.place(x=630,y=525)
s3 = Scale(f3,from_=600,to=1300,orient=HORIZONTAL, fg='white',bg='black',width = 25,command=move3,font=('Georgia',15),troughcolor='white',activebackground='grey')
s3.place(x=740,y=555)
tb = Button(f3,text='Calculate and plot \nthe centre of mass', fg='black',width = 25, height=4,bg='green',font=('Georgia',15),command=cal3)
tb.place(x=650,y=650)

imgo4 = Image.open('QM.png')
imgo4 = imgo4.resize((30,30), Image.ANTIALIAS)
photoImgo4 = ImageTk.PhotoImage(imgo4)


mb1 = Button(f1, text='Help',width=50,height=50, image=photoImgo4,font=('Georgia',13),bg='white',compound='top',command=h1)
mb1.place(x=1450,y=10)
mb2 = Button(f2, text='Help',width=50,height=50, image=photoImgo4,font=('Georgia',13),bg='white',compound='top',command=h1)
mb2.place(x=1450,y=10)
mb3 = Button(f3, text='Help',width=50,height=50, image=photoImgo4,font=('Georgia',13),bg='white',compound='top',command=h1)
mb3.place(x=1450,y=10)


def back():
    global root
    root.destroy()
    execfile('Homepage.py')


b8 = Button(f1,text='Return back to home screen',width = 25, height=2, bg='red',fg='black',font=('Georgia',15), command=back)
b8.place(x=1150,y=600)
b8 = Button(f2,text='Return back to home screen',width = 25, height=2, bg='red',fg='black',font=('Georgia',15), command=back)
b8.place(x=1150,y=600)
b8 = Button(f3,text='Return back to home screen',width = 25, height=2, bg='red',fg='black',font=('Georgia',15), command=back)
b8.place(x=1150,y=600)

def p3():
    global root
    root.destroy()
    execfile('Free.py')
    
b33 = Button(f1, text='Freedom Universe',font=('Georgia',15),fg='black',bg='#488AC7', height=2,command=p3)
b33.place(x=1205,y=600)
b33 = Button(f2, text='Freedom Universe',font=('Georgia',15),fg='black',bg='#488AC7', height=2,command=p3)
b33.place(x=1205,y=600)
b33 = Button(f3, text='Freedom Universe',font=('Georgia',15),fg='black',bg='#488AC7', height=2,command=p3)
b33.place(x=1205,y=600)

root.mainloop()
