import tkinter.messagebox
from tkinter import *

play=Tk()
play.geometry('600x600')
play.title('tic-tac-toe')
play.configure(bg='lightblue')

playerA=StringVar()
playerB=StringVar()
p1=StringVar()
p2=StringVar()
buttons=StringVar()
bclick=True
turns=0

def btnclick(buttons):
    global playerA,playerB,turns, bclick
    if buttons['text'] ==' ' and bclick == True:
        buttons['text'] = 'X'
        bclick = False
        playerA=p1.get()+' Wins!..'
        playerB=p2.get()+' Wins!..'
        possibilities()
        turns += 1
    elif buttons['text']==' ' and bclick == False:
        buttons['text']='O'
        bclick = True
        possibilities()
        turns +=1
    else:
        tkinter.messagebox.showwarning('tic-tac-toe','Buttons Already Clicked')

def possibilities():
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
          button4['text']=='X' and button5['text']=='X' and button6['text']=='X'  or
          button7['text']=='X' and button8['text']=='X' and  button9['text']=='X' or
          button1['text']=='X' and button4['text']=='X' and button7['text']=='X'  or
          button2['text']=='X' and button5['text']=='X' and button8['text']=='X'  or
          button3['text']=='X' and button6['text']=='X' and button9['text']=='X'  or
          button1['text']=='X' and button5['text']=='X' and button9['text']=='X'  or
          button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
        tkinter.messagebox.showinfo('tic-tac-toe',playerA)
    elif(button1['text']=='O' and button2['text']=='O'  and button3['text']=='O' or
          button4['text']=='O' and button5['text']=='O' and button9['text']=='O' or
          button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
          button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
          button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
          button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
          button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
        tkinter.messagebox.showinfo('tic-tac-toe',playerB)
    elif (turns==8):
        tkinter.messagebox.showinfo('tic-tac-toe','Match Draw')

Label(play, text='tic-tac-toe',font=('calibri',25),fg='blue').place(x=220,y=20)

Label(play, text='Player 1 name',font=('calibri',15),fg='blue').place(x=100,y=80)
Label(play, text='Player 2 name',font=('calibri',15),fg='blue').place(x=100,y=130)

Entry(play, textvariable=p1,font=('calibri',15)).place(x=270,y=80)
Entry(play, textvariable=p2,font=('calibri',15,)).place(x=270,y=130)


button1=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button1))
button1.place(x=100,y=200)

button2=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button2))
button2.place(x=230,y=200)


button3=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button3))
button3.place(x=360,y=200)

button4=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button4))
button4.place(x=100,y=300)

button5=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button5))
button5.place(x=230,y=300)

button6=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button6))
button6.place(x=360,y=300)

button7=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button7))
button7.place(x=100,y=400)

button8=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button8))
button8.place(x=230,y=400)

button9=Button(play, text=' ',font=('calibri',20,'bold'),bg='gray',fg='white', width='8', height='2',command=lambda :btnclick(button9))
button9.place(x=360,y=400)

play.mainloop()


        
