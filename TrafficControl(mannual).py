from tkinter import *

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

play=Tk()
play.geometry('400x400')
play.title('Traffic Light Mannual')
play.configure(bg='aqua')


Button(play,bg='red',width='10',height='2',command=red).place(x=20,y=30)
Button(play,bg='yellow',width='10',height='2',command=yellow).place(x=20,y=100)
Button(play,bg='green',width='10',height='2',command=green).place(x=20,y=170)

canvas1=Canvas(play,height=150,width=150,bg='black')
canvas1.place(x=130,y=30)

canvas2=Canvas(play,height=150,width=150,bg='black')
canvas2.place(x=130,y=175)

canvas3=Canvas(play,height=150,width=150,bg='black')
canvas3.place(x=130,y=320)

play.mainloop()

