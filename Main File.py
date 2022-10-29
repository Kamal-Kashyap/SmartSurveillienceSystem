import smtplib as s
import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Thief And Crime Detection System')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#FFD000")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="orange")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Thief And Crime Detection System Login",fg="white",bg="orange")
    heading.config(font=('impact 18'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                
                menu(a)
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('TCD App')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    district = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#BADA55")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Thief And Crime Detection App SignUp",fg="#006B88",bg="#BADA55")
    heading.config(font=('impact 18'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='white',bg='black')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #district
    clabel = Label(sup_frame,text="District",fg='white',bg='black')
    clabel.place(relx=0.217,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = district)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        district = c.get()
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Username and password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Username can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('TCDS1.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,DISTRICT text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,district)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('TCDS1.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="#BADA55", fg="black")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Thief And Crime Detection App Menu')
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="orange")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#7FFFD4")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  T C D  S T A T I O N ',fg="white",bg="orange") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    abcdefgh='Welcome '+ abcdefgh
    level34 = Label(menu_frame,text=abcdefgh,bg="black",font="calibri 18",fg="white")
    level34.place(relx=0.17,rely=0.1)
    
    level = Label(menu_frame,text='Select your Problem !!',bg="red",font="calibri 18")
    level.place(relx=0.25,rely=0.2)
    
    
    var = IntVar()
    abcR = Radiobutton(menu_frame,text='Detect Objects',bg="#7FFFD4",font="calibri 16",value=1,variable = var)
    abcR.place(relx=0.25,rely=0.3)
    
    efgR = Radiobutton(menu_frame,text='Detect Motion',bg="#7FFFD4",font="calibri 16",value=2,variable = var)
    efgR.place(relx=0.25,rely=0.4)
    
    hijR = Radiobutton(menu_frame,text='Detect Face',bg="#7FFFD4",font="calibri 16",value=3,variable = var)
    hijR.place(relx=0.25,rely=0.5)
    

    uvwR = Radiobutton(menu_frame,text='Add your Details',bg="#7FFFD4",font="calibri 16",value=4,variable = var)
    uvwR.place(relx=0.25,rely=0.6)

    xyzR = Radiobutton(menu_frame,text='Report your Problem on the basis of Attendance Details',bg="#7FFFD4",font="calibri 16",value=5,variable = var)
    xyzR.place(relx=0.25,rely=0.7)
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            abc()
        elif x == 2:
            efg()
        
        elif x == 3:
            hij()

        elif x == 4:
            uvw()

        elif x == 5:
            xyz()
            
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="black",fg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()

def efg():
    exec(open("Motion.py").read())

def abc():
    exec(open("object1.py").read())

def hij():
    exec(open("Face main.py").read())


def uvw():
    exec(open("partc.py").read())

def xyz():
    exec(open("part3.py").read())


def start():
    global root 
    root = Tk()
    root.title('Welcome To TCDS Smart Survillance')
    canvas = Canvas(root,width = 1040,height = 540, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="TCDS.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage,bg="red",fg="yellow") 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
def ttt():
    global root 
    root = Tk()
    root.title('We got your Contact!!!!')
    canvas = Canvas(root,width = 800,height = 600, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)

def lbw():
    global root 
    root = Tk()
    root.title('Your problem has been reported!!!!')
    canvas = Canvas(root,width = 800,height = 600, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    ob=s.SMTP("smtp.gmail.com",587)

    ob.starttls()

    ob.login("abc@gmail.com","abcd")

    subject="TCDS Smart survillance"
    body="Your Report has been forwarded Successfully  \n  It is an comformation email****"

    message="Subject:{}\n\n{}".format(subject,body)

    listofAddress=["xyz@gmail.com"]

    ob.sendmail("abc",listofAddress,message)
    print("send successfully...")
    ob.quit()



if __name__=='__main__':
    start()
