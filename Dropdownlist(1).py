from tkinter import *
from tkinter import ttk


def getvalues(selected):
    dropmenu2.set_menu(*Option2.get(selected))

obj=Tk()
obj.geometry('400x400')
obj.title('Dropdoenlist')
obj.configure(bg='aqua')


Label(obj,text='Select State',font=('calibri',20),bg='aqua').grid(row=1,column=1)

Option1=['Andra Pradesh','Goa','Karnataka','Kearla','Tamil Nadu']

dropVar1=StringVar()
dropmenu1=ttk.OptionMenu(obj,dropVar1,'-----Select-----',*Option1,command=getvalues)
dropmenu1.grid(row=1,column=2)

Label(obj,text='Select district',font=('calibri',20),bg='aqua').grid(row=2,column=1)

Option2={
    'Andra Pradesh':['Chittor','Guntur','Nellore'],
    'Goa':['North Goa','South Goa'],
    'Karnataka':['Kolar','Mysore','Bangalore'],
    'Kearla':['Kollam','Ernakulam','Munnar'],
    'Tamil Nadu':['Chennai','Covai','Trichy']
    }

dropVar2=StringVar()
dropmenu2=ttk.OptionMenu(obj,dropVar2,'-----Select-----')
dropmenu2.grid(row=2,column=2)

obj.mainloop()


