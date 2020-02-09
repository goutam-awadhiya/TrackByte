####  LIBRARIES ####
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os.path
##### OTHER FILES #####
from homepage import Homepage
from homepage import importusername
from SignUp import SignUp
from FAQ import ALLFAQ
#### MYSQL LIBRARY ####
import mysql.connector

#### EMAIL LIBRARY ####
import smtplib
import time
###### DATABASE #####
mydb = mysql.connector.connect(
    host='localhost',
    user='pycoders',
    passwd='gass',
    database='trackbyte'
)
mycursor = mydb.cursor()

####### LOGIN PAGE####
def LoginPage():


    def FAQ():
        root.destroy()
        ALLFAQ()

    ###### Sign up page #####
    def UserSignUp():
        root.destroy()
        SignUp()


    ##### LOGIN FUNCTION ####
    def UserLogin():
        username = userentry.get()
        password = passentry.get()
        id_pass = (username,password)
        ####### CHECK INTO DATABASE #######
        sqlformula = 'select username, password from Users where username = %s and password = %s '
        mycursor.execute(sqlformula,(username,password,))
        all_users = mycursor.fetchall()
        permission = id_pass in all_users
        wronguserpass = Label(root)
        if permission == True:
            root.destroy()
            importusername(username)
            Homepage()
        else:
            wronguserpass.place(relx=0.58, rely=0.595, height=20, width=210)
            wronguserpass.configure(background="#000000")  # 070707
            wronguserpass.configure(disabledforeground="#a3a3a3")
            wronguserpass.configure(font="-family {Comic Sans MS} -size 10")
            wronguserpass.configure(foreground="#edbe00")
            wronguserpass.configure(highlightcolor="#fc613a")
            if username == '' or password == '':
                wronguserpass.configure(text='''Username and Password Required !''')
            elif permission == False:
                wronguserpass.configure(text='''Invalid Username or Password !''')

    root = Tk()
    root.geometry("536x724+700+180")
    root.title("Login Page")
    root.configure(background="#000000")
    root.resizable(FALSE,FALSE)
    root.overrideredirect(True)

    close_button = Button(root, text='X', command=root.destroy)
    close_button.place(relx=0.935, rely=0.0070, height=10, width=25, relheight=0.02)
    close_button.configure(activebackground="#000000")
    close_button.configure(activeforeground="#000000")
    close_button.configure(background="#000000")
    close_button.configure(disabledforeground="#000000")
    close_button.configure(font="-family {Comic Sans MS} -size 16")
    close_button.configure(foreground="#edbe00")
    close_button.configure(highlightbackground="#000000")
    close_button.configure(pady="0")
    close_button.configure(relief="flat")
    close_button.configure(cursor="hand2")

    minimize = Button(root, text='--',)
    minimize.place(relx=0.875, rely=0.0070, height=10, width=25, relheight=0.02)
    minimize.configure(activebackground="#000000")
    minimize.configure(activeforeground="#000000")
    minimize.configure(background="#000000")
    minimize.configure(disabledforeground="#000000")
    minimize.configure(font="-family {Comic Sans MS} -size 16")
    minimize.configure(foreground="#edbe00")
    minimize.configure(highlightbackground="#000000")
    minimize.configure(pady="0")
    minimize.configure(relief="flat")
    minimize.configure(cursor="hand2")

    logolabel = Label(root)
    logolabel.place(relx=0.243, rely=0.083, height=212, width=251)
    logolabel.configure(background="#000000")#d9d9d9
    logolabel.configure(disabledforeground="#a3a3a3")
    logolabel.configure(foreground="#000000")
    photo_location = os.path.join("C:/Users/Goutam Awadhiya/TrackByte/logo14.png")
    global _img0
    _img0 = tk.PhotoImage(file=photo_location)
    logolabel.configure(image=_img0)
    logolabel.configure(text='''Label''')

    userlabel =Label(root)
    userlabel.place(relx=0.01   , rely=0.401, height=46, width=162)
    userlabel.configure(background="#000000")#070707
    userlabel.configure(disabledforeground="#a3a3a3")
    userlabel.configure(font="-family {Comic Sans MS} -size 16")
    userlabel.configure(foreground="#edbe00")
    userlabel.configure(highlightcolor="#fc613a")
    userlabel.configure(text='''Username''')

    userentry =Entry(root)#borderwidth=5
    userentry.place(relx=0.299, rely=0.401, height=54, relwidth=0.623)
    userentry.configure(background="#211905")
    userentry.configure(disabledforeground="#a3a3a3")
    userentry.configure(font="-family {Comic Sans MS} -size 14")
    userentry.configure(foreground="White")
    userentry.configure(highlightcolor="#ffed4a")
    userentry.configure(insertbackground="white")
    userentry.configure(readonlybackground="#efedee")
    userentry.configure(relief="groove")
    userentry.configure(selectbackground="#edbe00")
    userentry.configure(selectforeground="#fefffc")

    passlabel = Label(root)
    passlabel.place(relx=0.047, rely=0.511, height=46, width=122)
    passlabel.configure(activebackground="#f9f9f9")
    passlabel.configure(activeforeground="#070707")
    passlabel.configure(background="#000000")#070707
    passlabel.configure(disabledforeground="#a3a3a3")
    passlabel.configure(font="-family {Comic Sans MS} -size 16")
    passlabel.configure(foreground="#edbe00")
    passlabel.configure(highlightbackground="#d9d9d9")
    passlabel.configure(highlightcolor="#fc613a")
    passlabel.configure(text='''Password''')

    passentry = Entry(root,show='*')
    passentry.place(relx=0.299, rely=0.511, height=54, relwidth=0.623)
    passentry.configure(background="#211905")
    passentry.configure(disabledforeground="#a3a3a3")
    passentry.configure(font="-family {Comic Sans MS} -size 16")
    passentry.configure(foreground="White")
    passentry.configure(highlightbackground="#d9d9d9")
    passentry.configure(highlightcolor="#ffed4a")
    passentry.configure(insertbackground="white")
    passentry.configure(readonlybackground="#efedee")
    passentry.configure(relief="groove")
    passentry.configure(selectbackground="#edbe00")
    passentry.configure(selectforeground="#fefffc")



    keepmecheck = tk.Checkbutton(root)
    keepmecheck.place(relx=0.056, rely=0.622, relheight=0.043, relwidth=0.369)
    keepmecheck.configure(activebackground="#000000")#ececec
    keepmecheck.configure(activeforeground="#000000")
    keepmecheck.configure(background="#000000")
    keepmecheck.configure(disabledforeground="#000000")#a3a3a3
    keepmecheck.configure(font="-family {Comic Sans MS} -size 12")
    keepmecheck.configure(foreground="#edbe00")
    keepmecheck.configure(highlightbackground="#000000") #d9d9d9
    keepmecheck.configure(highlightcolor="black")
    keepmecheck.configure(justify='left')
    keepmecheck.configure(text='''Keep me signed in''')
    keepmecheck.configure(cursor="hand2")
    #keepmecheck.configure(variable=loginpg_support.che64)

    loginbutton = Button(root)
    loginbutton.place(relx=0.12, rely=0.710, height=47, width=410)
    loginbutton.configure(activebackground="#ececec")
    loginbutton.configure(activeforeground="#000000")
    loginbutton.configure(background="#edbe00")
    loginbutton.configure(disabledforeground="#a3a3a3")
    loginbutton.configure(font="-family {Comic Sans MS} -size 18")
    loginbutton.configure(foreground="#000000")
    loginbutton.configure(highlightbackground="#d9d9d9")
    loginbutton.configure(highlightcolor="black")
    loginbutton.configure(pady="0")
    loginbutton.configure(text='''Login''')
    loginbutton.configure(cursor="hand2")
    loginbutton.configure(command = UserLogin)

    createbutton = Button(root)
    createbutton.place(relx=0.09, rely=0.815, height=10, width=200, relheight=0.02)
    createbutton.configure(activebackground="#000000")
    createbutton.configure(activeforeground="#000000")
    createbutton.configure(background="#000000")
    createbutton.configure(disabledforeground="#000000")
    createbutton.configure(font="-family {Comic Sans MS} -size 12")
    createbutton.configure(foreground="#edbe00")
    createbutton.configure(highlightbackground="#000000")
    createbutton.configure(pady="0")
    createbutton.configure(relief="flat")
    createbutton.configure(text='''Create your account''')
    createbutton.configure(cursor="hand2")
    createbutton.configure(anchor='w')
    createbutton.configure(command = UserSignUp)

    forgotpsdbutton = Button(root)
    forgotpsdbutton.place(relx=0.09, rely=0.865, height=10, width=200, relheight=0.02)
    forgotpsdbutton.configure(activebackground="#000000")
    forgotpsdbutton.configure(activeforeground="#000000")
    forgotpsdbutton.configure(background="#000000")
    forgotpsdbutton.configure(disabledforeground="#000000")
    forgotpsdbutton.configure(font="-family {Comic Sans MS} -size 12")
    forgotpsdbutton.configure(foreground="#edbe00")
    forgotpsdbutton.configure(highlightbackground="#000000")
    forgotpsdbutton.configure(pady="0")
    forgotpsdbutton.configure(relief="flat")
    forgotpsdbutton.configure(text='''Forgot Password''')
    forgotpsdbutton.configure(cursor="hand2")
    forgotpsdbutton.configure(anchor='w')

    aboutusbutton = Button(root)
    aboutusbutton.place(relx=0.09, rely=0.915, height=1, width=200, relheight=0.02)
    aboutusbutton.configure(activebackground="#000000")
    aboutusbutton.configure(activeforeground="#000000")
    aboutusbutton.configure(background="#000000")
    aboutusbutton.configure(disabledforeground="#000000")
    aboutusbutton.configure(font="-family {Comic Sans MS} -size 12")
    aboutusbutton.configure(foreground="#edbe00")
    aboutusbutton.configure(highlightbackground="#000000")
    aboutusbutton.configure(pady="0")
    aboutusbutton.configure(relief="flat")
    aboutusbutton.configure(text='''About us''')
    aboutusbutton.configure(cursor="hand2")
    aboutusbutton.configure(anchor='w')

    aboutusbutton1 = Button(root)
    aboutusbutton1.place(relx=0.09, rely=0.955, height=1, width=100, relheight=0.02)
    aboutusbutton1.configure(activebackground="#000000")
    aboutusbutton1.configure(activeforeground="#000000")
    aboutusbutton1.configure(background="#000000")
    aboutusbutton1.configure(disabledforeground="#000000")
    aboutusbutton1.configure(font="-family {Comic Sans MS} -size 12")
    aboutusbutton1.configure(foreground="#edbe00")
    aboutusbutton1.configure(highlightbackground="#000000")
    aboutusbutton1.configure(pady="0")
    aboutusbutton1.configure(relief="flat")
    aboutusbutton1.configure(text='''FAQ's''')
    aboutusbutton1.configure(cursor="hand2")
    aboutusbutton1.configure(anchor='w')
    aboutusbutton1.configure(command = FAQ)

    passlabel = Label(root)
    passlabel.place(relx=0.75, rely=0.95, height=46, width=122)
    passlabel.configure(activebackground="#f9f9f9")
    passlabel.configure(activeforeground="#070707")
    passlabel.configure(background="#000000")  # 070707
    passlabel.configure(disabledforeground="#a3a3a3")
    passlabel.configure(font="-family {Comic Sans MS} -size 8")
    passlabel.configure(foreground="#edbe00")
    passlabel.configure(highlightbackground="#d9d9d9")
    passlabel.configure(highlightcolor="#fc613a")
    passlabel.configure(text='''All  Rights  Reserved @''')
    root.mainloop()



####### MAIN ##########

if __name__ == '__main__':
    LoginPage()