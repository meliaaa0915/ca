from Tkinter import *
from tkMessageBox import * 
from PIL import ImageTk, Image

root=Tk()
root.title('Freedom Universe')
root.geometry('1100x500')

img = Image.open('space2.jpg')
img = img.resize((2200,1000),Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)    

c = Canvas(root,width=1100,height=500)
c.place(x=0,y=0)

c.create_image(0,0, image=photoImg)

ini = c.create_oval(150,150,200,200, fill='#736AFF')

ini2 = c.create_oval(700,150,750,200, fill='#667C26')

line = c.create_line(200,175,700,175, fill='white')

fin = c.create_oval(445,170,455,180,fill='red')

def h1():
    showinfo("Instruction", "***DISCLAIMER***\n\
The name 'Planet' is not a real planet and the scale used are not according to the real measurement.\n\
This program is an example/name to help understand how the centre of mass can differ when its mass and distance changes.\n\
All units used is this program are according to SI unit.\n\n\
The following are how to use the program:\n\
1. Black scale - To adjust the distance between both 'Planets' (in m)\n\
2. Purple scale - To adjust the distance of purple planet (in kg)\n\
3. Green scale - To adjust the distance of green planet (in kg)\n\
4. Blue Button - Calculate the centre of mass\n\
5. Red dot - The centre of mass between both planets\n\n\
     Have Fun !!!")

def ex1(z):
    global ini
    global line
    global fin
    global s1
    global s2
    global s3
    global c
    x = s1.get()-49
    xx = s2.get()-49
    xxx = s3.get()-9
    c.delete(ini)
    c.delete(line)
    c.delete(fin)
    ini = c.create_oval(150-x,150-x,200+x,200+x,fill='#736AFF')
    line = c.create_line(200+x,175,(700-xx)+xxx,175,fill='white')

    a = s1.get()
    b = s2.get()
    cc = s3.get()
    ab = a*0
    bcc = b*cc
    a_b = a+b
    d = (bcc)/(a_b)
    fin = c.create_oval(d+444,170,d+454,180,fill='red')

def ex2(z): 
    global ini2
    global line
    global fin
    global s1
    global s2
    global s3
    global c
    x = s1.get()-49
    xx = s2.get()-49
    xxx = s3.get()-9
    c.delete(ini2)
    c.delete(line)
    c.delete(fin)
    ini2 = c.create_oval((700-xx)+xxx,150-xx,(750+xx)+xxx,200+xx,fill='#667C26')
    line = c.create_line(200+x,175,(700-xx)+xxx,175,fill='white')

    a = s1.get()
    b = s2.get()
    cc = s3.get()
    ab = a*0
    bcc = b*cc
    a_b = a+b
    d = (bcc)/(a_b)
    fin = c.create_oval(d+444,170,d+454,180,fill='red')


def ex3(z):
    global ini2
    global line
    global fin
    global s1
    global s2
    global s3
    global c
    x = s1.get()-49
    xx = s2.get()-49
    xxx = s3.get()-9
    c.delete(ini2)
    c.delete(line)
    c.delete(fin)
    ini2 = c.create_oval((700-xx)+xxx,150-(xx),(750+xx)+xxx,200+(xx),fill='#667C26')
    line = c.create_line(200+x,175,(700-xx)+xxx,175,fill='white')

    a = s1.get()
    b = s2.get()
    cc = s3.get()
    ab = a*0
    bcc = b*cc
    a_b = a+b
    d = (bcc)/(a_b)
    fin = c.create_oval(d+444,170,d+454,180,fill='red')

def cal():
    global l5
    g = s1.get()
    h = s2.get()
    i = s3.get()
    j = float(h*i)
    k = float(g+h)
    l = float(j/k)
    l5.config(text= 'Centre of Mass = ' + str(l) + 'm')
    


imgo4 = Image.open('QM.png')
imgo4 = imgo4.resize((23,23), Image.ANTIALIAS)
photoImgo4 = ImageTk.PhotoImage(imgo4)

s1 = Scale(root,from_=50,to=150,orient=HORIZONTAL, fg='black',bg='#6A287E',command=ex1,font=('Georgia',15),troughcolor='#C8A2C8',activebackground='#6C2DC7',width=25)
s1.place(x=130,y=350)

s2 = Scale(root,from_=50,to=150,orient=HORIZONTAL, fg='black',bg='#347C17',command=ex2,font=('Georgia',15),troughcolor='#98FF98',activebackground='#617C58',width=25)
s2.place(x=770,y=350)

s3 = Scale(root,from_=10,to=200,orient=HORIZONTAL,fg='white',bg='black',command=ex3,font=('Georgia',15),troughcolor='white',activebackground='grey',width=25)
s3.place(x=450,y=350)

b1 = Button(root, text='Help',width=40,height=40, image=photoImgo4,font=('Georgia',13),bg='white',compound='top',command=h1)
b1.place(x=1040,y=10)

b2 = Button(root, text='Calculate', bg='#3BB9FF',fg='black',font=('Georgia',15),command=cal)
b2.place(x=400,y=440)

def back():
    global root
    root.destroy()
    execfile('Teamproject.py')
    
b3 = Button(root, text='Return back to \nspace exploration',bg='red',font=('Georgia',12),command=back)
b3.place(x=950,y=440)

l1 = Label(root, text='Mass of Purple Planet (in kg)',font=('Georgia',13),fg='black',bg='#A74AC7')
l1.place(x=75,y=320)

l2 = Label(root, text='Distance between both planets (in m)',font=('Georgia',14),fg='white',bg='black')
l2.place(x=350,y=320)

l3 = Label(root, text='Mass of Green Planet (in kg)',font=('Georgia',13),fg='black',bg='#5FFB17')
l3.place(x=715,y=320)

l5 = Label(root, text= '',fg='white',bg='black',font=('Georgia',15))
l5.place(x=550,y=445)


root.mainloop()

