from tkinter import *
from tkinter import ttk


def getvalues(selected):
    dropmenu2.set_menu(*Option2.get(selected))

def getvalues2(selected2):
    dropmenu3.set_menu(*Option3.get(selected2))

obj=Tk()
obj.geometry('400x400')
obj.title('Dropdoenlist')
obj.configure(bg='light blue')


Label(obj,text='Select a Meal',font=('calibri',20),bg='light blue').grid(row=1,column=1)

Option1=['Breakfast','Lunch','Dinner']

dropVar1=StringVar()
dropmenu1=ttk.OptionMenu(obj,dropVar1,'-----Select-----',*Option1,command=getvalues)
dropmenu1.grid(row=1,column=2)

Label(obj,text='Select Food',font=('calibri',20),bg='light blue').grid(row=2,column=1)

Option2={
    'Breakfast':['Dosa','idlly','Chapatti'],
    'Lunch':['Rice','Biriyani','parotta'],
    'Dinner':['FriedRice','Nan','Noodles']
    }

dropVar2=StringVar()
dropmenu2=ttk.OptionMenu(obj,dropVar2,'-----Select-----',*Option2,command=getvalues2)
dropmenu2.grid(row=2,column=2)

Label(obj,text='Select Type of Food',font=('calibri',20),bg='light blue').grid(row=3,column=1)

Option3={
    'Dosa':['Ghee Dosa','Rava Dosa','onion Dosa'],
    'idlly':['podi idlly','mini idlly','Chilli idlly'],
    'Chapatti':['Chilli Chapatti','Egg Chapatti','Panner Chapatti'],
    'Biriyani':['Mutton Biriyani','chicken Biriyani','fish Biriyani'],
    'Rice':['Tomato Rice','Curd rice','Lemon Rice'],
    'parotta':['Egg parotta','Kaima Porotta','veechu parotta'],
    'Nan': ['Butter Nan', 'Garlic Nan', 'BBQ nan'],
    'FriedRice': ['Chicken FriedRice', 'Prawn FriedRice', 'mutton FriedRice'],
    'Noodles': ['Panner Noodles', 'Egg Noodles', 'Prawn Noodles']
    }

dropVar3=StringVar()
dropmenu3=ttk.OptionMenu(obj,dropVar3,'-----Select-----')
dropmenu3.grid(row=3,column=2)

obj.mainloop()


