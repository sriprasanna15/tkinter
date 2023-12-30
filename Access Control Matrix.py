from tkinter import *
import mysql.connector
import tkinter.messagebox

db= mysql.connector.connect(host='localhost',user='root',password='',db='products')
cursor=db.cursor()

def calculate():
    product_tot.set(product_price.get() * product_qty.get())

def add():
    id=product_id.get()
    name=product_name.get()
    price=product_price.get()
    qty=product_qty.get()
    tot=product_tot.get()
    cursor.execute('insert into values(%s%s%s%s%s)',[id,name,price,qty,tot])
    db.commit()
    tkinter.messagebox.showinfo('Access','Products Added')

def view():
    id=product_id.get()
    data=cursor.fetchone()
    cursor.execute('select * from details where proId=%s',[id])
    if data !=0:
        product_name.set(data[1])
        product_price.set(data[2])
        product_qty.set(data[3])
        product_tot.set(data[4])
    else:
        tkinter.messagebox.showwarning('Access','No Data')

def update():
    id=product_id.get()
    name = product_name.get()
    price = product_price.get()
    qty = product_qty.get()
    tot = product_tot.get()
    cursor.execute('Update details set proprice=%s,proqty=%s,totalprice=%s where proId=%s',[price,name,qty,id])
    db.commit()
    tkinter.messagebox.showinfo('Access','Products Updated')

def delete():
    id=id=product_id.get()
    cursor.execute('delete from details where proId=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Access','Products deleted')

def clear():
    id = product_id.set('')
    name = product_name.set('')
    price = product_price.set('')
    qty = product_qty.set('')
    tot = product_tot.set('')

def overall():
    global viewpage
    viewpage=toplevel(obj)
    viewpage.geometry('700x500')
    viewpage.title('Access Control Matrix')
    viewpage.configure(bg='lightblue')
    cursor.execute('select * from details')
    data=cursor.fetchall()
    rows=len(data)
    cols=len(data[0])
    Label(viewpage, text='Pro Id', font=('calibri', 18), bg='lightblue').grid(row=0,column=0)
    Label(viewpage, text='Pro Name', font=('calibri', 18), bg = 'lightblue').grid(row=0, column=1)
    Label(viewpage, text='Pro Price', font=('calibri', 18), bg = 'lightblue').grid(row=0, column=2)
    Label(viewpage, text='Pro Qty', font=('calibri', 18), bg = 'lightblue').grid(row=0, column=3)
    Label(viewpage, text='Total Price', font=('calibri', 18), bg = 'lightblue').grid(row=0, column=4)
    for i in range(rows):
        for j in range(cols):
            s=entry(viewpage, font=('calibri', 14))
            s.grid(row=i+1,column=j)
            s.insert(END,data[i][j])

obj=Tk()
obj.geometry('600x600')
obj.title('Access Control Matrix')
obj.configure(bg='lightblue')

Label(obj,text='Products Entry', font=('calibri',25),fg='blue').place(x=180,y=20)

product_id_label=Label(obj,text='Product Id', font=('calibri',18),bg='lightblue')
product_id_label.place(x=100,y=100)
product_id=StringVar()
product_id_entry=Entry(obj,textvariable=product_id, font=('calibri',15))
product_id_entry.place(x=290,y=100)

product_name_label=Label(obj,text='Product Name', font=('calibri',18),bg='lightblue')
product_name_label.place(x=100,y=150)
product_name=StringVar()
product_name_entry=Entry(obj,textvariable=product_name, font=('calibri',15))
product_name_entry.place(x=290,y=150)

product_price_label=Label(obj,text='Product Price', font=('calibri',18),bg='lightblue')
product_price_label.place(x=100,y=200)
product_price=IntVar()
product_price_entry=Entry(obj,textvariable=product_price, font=('calibri',15))
product_price_entry.place(x=290,y=200)

product_qty_label=Label(obj,text='Product Qty', font=('calibri',18),bg='lightblue')
product_qty_label.place(x=100,y=250)
product_qty=IntVar()
product_qty_entry=Entry(obj,textvariable=product_qty, font=('calibri',15))
product_qty_entry.place(x=290,y=250)

product_tot_label=Label(obj,text='Total Price', font=('calibri',18),bg='lightblue')
product_tot_label.place(x=100,y=300)
product_tot=IntVar()
product_tot_entry=Entry(obj,textvariable=product_tot, font=('calibri',15))
product_tot_entry.place(x=290,y=300)

but_cal=Button(obj, text='Calculate', command=calculate, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_cal.place(x=510,y=250)

but_add=Button(obj, text='Add', command=add, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_add.place(x=100,y=370)

but_view=Button(obj, text='View', command=view, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_view.place(x=240,y=370)

but_upd=Button(obj, text='Update',command=update, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_upd.place(x=380,y=370)

but_clr=Button(obj, text='Delete',command=delete, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_clr.place(x=100,y=420)

but_ovr=Button(obj, text='Clear',command=clear, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_ovr.place(x=240,y=420)

but_cal=Button(obj, text='Overall',command=overall, font=('calibri',10),bg='blue',fg='white',width='8',height='1')
but_cal.place(x=380,y=420)

obj.mainloop()

