from tkinter import *
from tkinter import ttk


def add():
    num1=number1.get()
    num2=number2.get()
    num3=number3.get()
    result=num1+num2+num3
    labelresult.config(text='Result=%d'%result)

obj=Tk()
obj.geometry('400x400')
obj.title('Operations')
obj.configure(bg='aqua')


Label(obj,text='Enter Value of A:',font=('calibri',20,'bold'),bg='aqua').grid(row=1,column=1)
Label(obj,text='Enter Value of B:',font=('calibri',20,'bold'),bg='aqua').grid(row=2,column=1)
Label(obj,text='Enter Value of C:',font=('calibri',20,'bold'),bg='aqua').grid(row=3,column=1)

number1=IntVar()
number2=IntVar()
number3=IntVar()


Entry(obj,textvariable=number1,font=('calibri',15)).grid(row=1,column=2)
Entry(obj,textvariable=number2,font=('calibri',15)).grid(row=2,column=2)
Entry(obj,textvariable=number3,font=('calibri',15)).grid(row=3,column=2)

#Create Button
Button(obj,text='Add',command=add,font=('calibri',15),bg='black',fg='white',width='13',height='2').grid(row=4,column=2)

#Display List in Label
labelresult=Label(obj,font=('calibri',20,'bold'),bg='aqua',fg='red')
labelresult.grid(row=5,column=2)

obj.mainloop()


