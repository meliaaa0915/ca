from Tkinter import *
from tkMessageBox import * 
from PIL import ImageTk, Image

global raise_frame
def raise_frame(frame):
    frame.tkraise()

root=Tk()
root.title('Game')
root.geometry('800x500')

def callback(event):
    # to print the coordinates of the point of click
    print "clicked at", event.x, event.y

f2 = Frame(root,height=1000,width=1600)   
f2.pack()

c2 = Canvas(f2,width=800,height=500)
c2.bind("<Button-1>", callback)
c2.pack()

t1 = c2.create_polygon(100,250,100,450,400,450,fill='blue')

t2 = c2.create_polygon(160,290,310,390,320,210,fill='black')

line = c2.create_line(265,290,265,480,fill='white')

root.mainloop()