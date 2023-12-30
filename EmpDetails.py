from tkinter import *
import mysql.connector
import tkinter.messagebox

db= mysql.connector.connect(host='localhost',user='root',password='',db='emp')
cursor=db.cursor()


def add():
    id=Employee_id.get()
    name=Employee_name.get()
    salary=Employee_salary.get()
    dept=Employee_dept.get()
    cursor.execute('insert into values(%s%s%s%s)',[id,name,salary,dept])
    db.commit()
    tkinter.messagebox.showinfo('Access','Employee Added')

def view():
    id=Employee_id.get()
    data=cursor.fetchone()
    cursor.execute('select * from details where proId=%s',[id])
    if data !=0:
        Employee_name.set(data[1])
        Employee_salary.set(data[2])
        Employee_dept.set(data[3])
    else:
        tkinter.messagebox.showwarning('Access','No Data')

def update():
    id = Employee_id.get()
    name = Employee_name.get()
    salary = Employee_salary.get()
    dept= Employee_dept.get()
    cursor.execute('Update details set proprice=%s,proqty=%s,totalprice=%s where proId=%s',[price,name,qty,id])
    db.commit()
    tkinter.messagebox.showinfo('Access','Employee Updated')

def delete():
    id=Employee_id.get()
    cursor.execute('delete from details where proId=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Access','Employee  deleted')

def clear():
    id = Employee_id.set('')
    name = Employee_name.set('')
    salary = Employee_salary.set('')
    dept= Employee_dept.set('')

def overall():
    global viewpage
    viewpage=toplevel(obj)
    viewpage.geometry('700x500')
    viewpage.title('Employee details')
    viewpage.configure(bg='lightblue')
    cursor.execute('select * from details')
    data=cursor.fetchall()
    rows=len(data)
    cols=len(data[0])
    Label(viewpage, text='Emp Id', font=('calibri', 18), bg='lightblue').grid(row=0,column=0)
    Label(viewpage, text='Emp Name', font=('calibri', 18), bg = 'lightblue').grid(row=0, column=1)
    Label(viewpage, text='Emp salary', font=('calibri', 18), bg = 'lightblue').grid(row=0, column=2)
    Label(viewpage, text='Emp dept', font=('calibri', 18), bg = 'lightblue').grid(row=0, column=3)
    for i in range(rows):
        for j in range(cols):
            s=entry(viewpage, font('calibri', 14))
            s.grid(row=i+1,column=j)
            s.insert(END,data[i][j])

obj=Tk()
obj.geometry('600x600')
obj.title('Employee Details')
obj.configure(bg='green')

Label(obj,text='Employee Entry', font=('calibri',25),bg='lightgreen').place(x=180,y=20)

Employee_id_label=Label(obj,text='Employee Id', font=('calibri',18),bg='lightgreen')
Employee_id_label.place(x=100,y=100)
Employee_id=StringVar()
Employee_id_entry=Entry(obj,textvariable=Employee_id, font=('calibri',15))
Employee_id_entry.place(x=290,y=100)

Employee_name_label=Label(obj,text='Employee Name', font=('calibri',18),bg='lightgreen')
Employee_name_label.place(x=100,y=150)
Employee_name=StringVar()
Employee_name_entry=Entry(obj,textvariable=Employee_name, font=('calibri',15))
Employee_name_entry.place(x=290,y=150)

Employee_salary_label=Label(obj,text='Employee salary', font=('calibri',18),bg='lightgreen')
Employee_salary_label.place(x=100,y=200)
Employee_salary=IntVar()
Employee_salary_entry=Entry(obj,textvariable=Employee_salary, font=('calibri',15))
Employee_salary_entry.place(x=290,y=200)

Employee_dept_label=Label(obj,text='Employee dept', font=('calibri',18),bg='lightgreen')
Employee_dept_label.place(x=100,y=250)
Employee_dept=StringVar()
Employee_dept_entry=Entry(obj,textvariable=Employee_dept, font=('calibri',15))
Employee_dept_entry.place(x=290,y=250)



but_add=Button(obj, text='Add', command=add, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_add.place(x=100,y=370)

but_view=Button(obj, text='View', command=view, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_view.place(x=240,y=370)

but_upd=Button(obj, text='Update',command=update, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_upd.place(x=380,y=370)

but_del=Button(obj, text='Delete',command=delete, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_del.place(x=100,y=420)

but_clr=Button(obj, text='Clear',command=clear, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_clr.place(x=240,y=420)

but_ovr=Button(obj, text='Overall',command=overall, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_ovr.place(x=380,y=420)

obj.mainloop()

