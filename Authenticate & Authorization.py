import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='emp')
cursor = db.cursor()


def admin():
    global admin_frame
    global admin_username
    global admin_password
    admin_frame = Frame(homepage, width=350, height=200)
    admin_frame.place(x=50, y=130)
    admin_username = StringVar()
    admin_password = StringVar()
    Label(admin_frame, text='Username', font=('calibri', 13)).place(x=30, y=30)
    Label(admin_frame, text='Password', font=('calibri', 13)).place(x=30, y=80)
    Entry(admin_frame, textvariable=admin_username, font=('calibri', 13), bg='lightblue').place(x=140, y=30)
    Entry(admin_frame, textvariable=admin_password, font=('calibri', 13), bg='lightblue').place(x=140, y=80)
    Button(admin_frame, text='Login', command=admin_login, font=('calibri', 10), bg='gray', fg='white',
           width='10', height='1').place(x=220, y=130)


def admin_login():
    username = admin_username.get()
    password = admin_password.get()
    if username == 'admin' and password == 'admin321':
        tkinter.messagebox.showinfo('Authenticate', 'Welcome Admin')
        admin_page()
    else:
        tkinter.messagebox.showerror('Authenticate', 'Invalid')


def admin_page():
    global admin_home
    admin_home = Toplevel(homepage)
    admin_home.geometry('1400x500')
    admin_home.title('Admin Home')
    admin_home.configure(bg='lightblue')
    pending = Button(admin_home, text='Pending List', command=pending_data, font=('calibri', 15), bg='gray', fg='white',
                     width='10', height='1')
    pending.grid(row=0, column=0)
    approved = Button(admin_home, text='Approved  List', command=approved_data, font=('calibri', 15), bg='gray',
                      fg='white',
                      width='12', height='1')
    approved.grid(row=0, column=1)


def pending_data():
    cursor.execute('select * from logindetails where verify=%s', ['pending'])
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(admin_home, text='id', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=0)
    Label(admin_home, text='Name', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=1)
    Label(admin_home, text='Email', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=2)
    Label(admin_home, text='Address', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=3)
    Label(admin_home, text='Gender', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=4)
    Label(admin_home, text='Username', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=5)
    Label(admin_home, text='Password', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=6)
    Label(admin_home, text='Verify', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=7)
    Label(admin_home, text='Action', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=8)
    for i in range(rows):
        for j in range(cols):
            s = Entry(admin_home, font=('calibri', 11))
            s.grid(row=i + 2, column=j)
            s.insert(END, data[i][j])
        b1 = Button(admin_home, text='Approve', command=lambda: approve(data[i][0]), font=('calibri', 10),
                    width='8', height='1')
        b1.grid(row=i + 2, column=cols + 1)
        b2 = Button(admin_home, text='Delete', command=lambda: delete(data[i][0]), font=('calibri', 10),
                    width='8', height='1')
        b2.grid(row=i + 2, column=cols + 2)


def approve(id):
    cursor.execute('update logindetails set verify=%s where id=%s', ['Approved', id])
    db.commit()
    tkinter.messagebox.showinfo('Authorize', 'Status Updated')


def delete(id):
    cursor.execute('delete from logindetails where id=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('Authorize', 'Deleted')


def approved_data():
    cursor.execute('select * from logindetails where verify=%s', ['Approved'])
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(admin_home, text='id', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=0)
    Label(admin_home, text='Name', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=1)
    Label(admin_home, text='Email', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=2)
    Label(admin_home, text='Address', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=3)
    Label(admin_home, text='Gender', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=4)
    Label(admin_home, text='Username', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=5)
    Label(admin_home, text='Password', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=6)
    Label(admin_home, text='Verify', font=('calibri', 13, 'bold'), bg='lightblue').grid(row=1, column=7)
    for i in range(rows):
        for j in range(cols):
            s = Entry(admin_home, font=('calibri', 11))
            s.grid(row=i + 2, column=j)
            s.insert(END, data[i][j])


def user():
    global user_frame
    global user_username
    global user_password
    user_frame = Frame(homepage, width=350, height=250)
    user_frame.place(x=450, y=130)
    user_username = StringVar()
    user_password = StringVar()
    Label(user_frame, text='Username', font=('calibri', 13)).place(x=30, y=30)
    Label(user_frame, text='Password', font=('calibri', 13)).place(x=30, y=80)
    Entry(user_frame, textvariable=user_username, font=('calibri', 13), bg='lightblue').place(x=140, y=30)
    Entry(user_frame, textvariable=user_password, font=('calibri', 13), bg='lightblue').place(x=140, y=80)
    Button(user_frame, text='Signup', command=register, font=('calibri', 10), bg='gray', fg='white', width='10',
           height='1').place(x=220, y=130)
    Button(user_frame, text='Login', command=user_login, font=('calibri', 10), bg='gray', fg='white', width='10',
           height='1').place(x=220, y=180)


def user_login():
    username = user_username.get()
    password = user_password.get()
    cursor.execute('select * from logindetails where username=%s and password=%s', [username, password])
    data = cursor.fetchone()
    if data != None:
        tkinter.messagebox.showinfo('Authenticate', 'Welcome User')
    else:
        tkinter.messagebox.showwarning('Authenticate', 'Invalid User')


def register():
    global register_frame
    global register_name
    global register_mail
    global register_address
    global register_gender
    global register_username
    global register_password
    register_frame = Frame(homepage, width=350, height=400)
    register_frame.place(x=900, y=130)
    register_name = StringVar()
    register_mail = StringVar()
    register_address = StringVar()
    register_gender = StringVar()
    register_username = StringVar()
    register_password = StringVar()
    Label(register_frame, text='Name', font=('calibri', 13)).place(x=30, y=30)
    Label(register_frame, text='Mail', font=('calibri', 13)).place(x=30, y=80)
    Label(register_frame, text='Address', font=('calibri', 13)).place(x=30, y=130)
    Label(register_frame, text='Gender', font=('calibri', 13)).place(x=30, y=180)
    Label(register_frame, text='Username', font=('calibri', 13)).place(x=30, y=230)
    Label(register_frame, text='Password', font=('calibri', 13)).place(x=30, y=280)
    Entry(register_frame, textvariable=register_name, font=('calibri', 13), bg='lightblue').place(x=140, y=30)
    Entry(register_frame, textvariable=register_mail, font=('calibri', 13), bg='lightblue').place(x=140, y=80)
    Entry(register_frame, textvariable=register_address, font=('calibri', 13), bg='lightblue').place(x=140, y=130)
    Radiobutton(register_frame, text='Male', variable=register_gender, value='Male',
                font=('calibri', 10)).place(x=140, y=180)
    Radiobutton(register_frame, text='Female', variable=register_gender, value='FeMale',
                font=('calibri', 10)).place(x=220, y=180)
    Entry(register_frame, textvariable=register_username, font=('calibri', 13), bg='lightblue').place(x=140, y=230)
    Entry(register_frame, textvariable=register_password, font=('calibri', 13), bg='lightblue').place(x=140, y=280)
    Button(register_frame, text='Submit', command=store_data, font=('calibri', 13), bg='gray', fg='white', width='10',
           height='1').place(x=180, y=330)


def store_data():
    name = register_name.get()
    mail = register_mail.get()
    address = register_address.get()
    gender = register_gender.get()
    username = register_username.get()
    password = register_password.get()
    cursor.execute('insert into logindetails(name,email,address,gender,username,password,verify)'
                   'values(%s,%s,%s,%s,%s,%s,%s)', [name, mail, address, gender, username, password, 'Pending'])
    db.commit()
    tkinter.messagebox.showinfo('Authenticate', 'Registered Successfully')


def startpage():
    global homepage
    homepage = Tk()
    homepage.geometry('1300x600')
    homepage.title('Authenticate & Authorization')
    homepage.configure(bg='lightblue')
    Label(homepage, text='Welcome to Login Page', font=('calibri', 30)).place(x=400, y=20)
    Button(homepage, text='Admin', command=admin, font=('calibri', 20), bg='gray', fg='white', width='12',
           height='1').place(x=100, y=50)
    Button(homepage, text='User', command=user, font=('calibri', 20), bg='gray', fg='white', width='12',
           height='1').place(x=900, y=50)
    homepage.mainloop()


startpage()
