from tkinter import *
import time



def red():
    canvas1.create_oval(110,110,30,30,fill="red",outline='white',width=4)
    canvas2.create_oval(110,110,30,30,fill="white",outline='white',width=4)
    canvas3.create_oval(110,110,30,30,fill="white",outline='white',width=4)

def yellow():
    canvas1.create_oval(110,110,30,30,fill="white",outline='white',width=4)
    canvas2.create_oval(110,110,30,30,fill="yellow",outline='white',width=4)
    canvas3.create_oval(110,110,30,30,fill="white",outline='white',width=4)

def green():
    canvas1.create_oval(110,110,30,30,fill="white",outline='white',width=4)
    canvas2.create_oval(110,110,30,30,fill="white",outline='white',width=4)
    canvas3.create_oval(110,110,30,30,fill="green",outline='white',width=4)

count=25

def start():
    counter(count)

def counter(value):
    if value >0:
        value=value-1
        new(value)

def new(c):
    if c>15:
        green()
        internal.config(text=c)
        play.update()
        time.sleep(1)
        counter(c)
    elif c>10 and c<=15:
        yellow()
        internal.config(text=c)
        play.update()
        time.sleep(1)
        counter(c)
    elif c>0 and c<=10:
        red()
        internal.config(text=c)
        play.update()
        time.sleep(1)
        counter(c)
    elif c==0:
        green()
        internal.config(text=c)
        play.update()
        time.sleep(1)
        count=25
        counter(count)

play=Tk()
play.geometry('400x400')
play.title('Traffic Light Mannual')
play.configure(bg='aqua')


Button(play,text='Start',command=start,bg='black',fg='red',font=('calibri',15,'bold'),width='10',height='2').place(x=10,y=30)


internal=Label(play,font=('calibri',35,'bold'),bg='black',fg='red')
internal.place(x=20,y=200)

canvas1=Canvas(play,height=150,width=150,bg='black')
canvas1.place(x=130,y=30)

canvas2=Canvas(play,height=150,width=150,bg='black')
canvas2.place(x=130,y=175)

canvas3=Canvas(play,height=150,width=150,bg='black')
canvas3.place(x=130,y=320)

play.mainloop()

