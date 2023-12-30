import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='cab')
cursor = db.cursor()



def user_login():
    username = user_username.get()
    password = user_password.get()
    cursor.execute('select * from details where username=%s and password=%s', [username, password])
    data = cursor.fetchone()
    if data != None:
        tkinter.messagebox.showinfo('Authenticate', 'Welcome User')
    else:
        tkinter.messagebox.showwarning('Authenticate', 'Invalid User')


def store_data():
    username = register_username.get()
    password = register_password.get()
    cursor.execute('insert into details(username,password)' 'values(%s,%s)', [ username, password])
    db.commit()
    tkinter.messagebox.showinfo('Authenticate', 'Registered Successfully')


def create_account():
    global register_home
    register_home = Toplevel(homepage)
    register_home.geometry('1000x500')
    register_home.title('Create Account')
    register_home.configure(bg='lightblue')
    Label(register_home, text='Create Your Account', font=('calibri', 30)).place(x=400, y=10)
    global register_username
    global register_password
    register_frame = Frame(register_home, width=400, height=200)
    register_frame.place(x=400, y=100)
    register_username = StringVar()
    register_password = StringVar()
    Label(register_frame, text='Username', font=('calibri', 13)).place(x=30, y=30)
    Label(register_frame, text='Password', font=('calibri', 13)).place(x=30, y=80)
    Entry(register_frame, textvariable=register_username, font=('calibri', 13), bg='lightblue').place(x=140, y=30)
    Entry(register_frame, textvariable=register_password, font=('calibri', 13), bg='lightblue').place(x=140, y=80)
    Button(register_frame, text='Submit', command=store_data, font=('calibri', 13), bg='gray', fg='white', width='10',
           height='1').place(x=100, y=130)
    Button(register_frame, text='Login', command=lambda: show_frame(user_frame), font=('calibri', 13), bg='gray', fg='white', width='10',
           height='1').place(x=250, y=130)


def show_frame(frame):
    frame.tkraise()

def startpage():
    global homepage
    homepage = Tk()
    homepage.geometry('1000x600')
    homepage.title('Login for Cab Booking system')
    homepage.configure(bg='lightblue')
    Label(homepage, text='Welcome to Login Page', font=('calibri', 30)).place(x=400, y=20)
    global user_frame
    global user_username
    global user_password
    user_frame = Frame(homepage, width=400, height=250)
    user_frame.place(x=400, y=130)
    user_username = StringVar()
    user_password = StringVar()
    Label(user_frame, text='Username', font=('calibri', 13)).place(x=30, y=30)
    Label(user_frame, text='Password', font=('calibri', 13)).place(x=30, y=80)
    Entry(user_frame, textvariable=user_username, font=('calibri', 13), bg='lightblue').place(x=140, y=30)
    Entry(user_frame, textvariable=user_password, font=('calibri', 13), bg='lightblue').place(x=140, y=80)
    Button(user_frame, text='Login', command=user_login, font=('calibri', 10), bg='gray', fg='white', width='12',
           height='1').place(x=80, y=130)
    Button(user_frame, text='Create Account', command=create_account, font=('calibri', 10), bg='gray', fg='white', width='12',
           height='1').place(x=220, y=130)

    homepage.mainloop()


startpage()
