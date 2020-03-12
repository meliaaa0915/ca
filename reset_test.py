from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry('1600x1000')
root.title('Centre of mass')

showinfo("Instruction", "Welcome onboard!!! \nBefore starting our space exploration, there are a few instructions to follow. \n1. Select your planet. \n2. Move the distance of the planet using the scale. \n3. GREEN BUTTON - to locate the centre of mass \n4. BLUE BUTTON - centre of mass calculator \n\n Press 'OK' to begin.") #by J

x=600

#Reset screen
def reset():
    s1.set(x)
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    tb.config(text='Calculate and plot \nthe centre of mass',command=cal1)
   

#Frame 2
f2 = Frame(root)
f2.place(x=0,y=0,height=1000,width=1600)
c2 = Canvas(f2,width=1600,height=1000,bg='black')
c2.place(x=0,y=0)
img2 = Image.open('sun.jpg')
img2 = img2.resize((350,350), Image.ANTIALIAS)
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
    c2.delete(ALL)
    t2.destroy()
    la2.destroy()
    img22 = Image.open('sun.jpg')
    img22 = img22.resize((350,350), Image.ANTIALIAS)
    photoImg22 = ImageTk.PhotoImage(img2)
    panel22 = Label(f2,image=photoImg1,bg='black')
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
