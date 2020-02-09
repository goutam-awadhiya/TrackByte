

#### LIBRARIES ####
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os.path
##### OTHER FILES #####
from homepage import Homepage
from homepage import importusername
#### MYSQL LIBRARY ####
import mysql.connector

###### DATABASE #####
mydb = mysql.connector.connect(
    host='localhost',
    user='pycoders',
    passwd='gass',
    database='trackbyte'
)
mycursor = mydb.cursor()

def SignUp():

    def CheckAvailable():
        mycursor.execute('select username from Users')
        username_list = mycursor.fetchall()
        enteredname = (usernameentry.get(),)
        permission = not(enteredname in username_list or usernameentry.get() =='')
        emailabel = Label(BottomFrame)
        emailabel.place(relx=0.75, rely=0.265, height=46, width=41)
        emailabel.configure(background="#000000")  # 070707
        emailabel.configure(disabledforeground="#a3a3a3")
        emailabel.configure(font="-family {Comic Sans MS} -size 10")
        emailabel.configure(foreground="#edbe00")
        emailabel.configure(highlightcolor="#fc613a")
        if permission == True:
            emailabel.configure(text='''(--Valid--)''')
        elif usernameentry.get() == '':
            messagebox.showerror("Error","Username Cannot Be Empty")
        else:
            messagebox.showerror("Error","Username Already Exists")
        return permission

    def checkpassword():
        upass = passwordentry.get()
        urepass = repasswordentry.get()
        if upass == urepass and upass != '' and urepass != '':
            return True
        elif upass == '' and urepass == '':
            messagebox.showerror("Error", "Password can not be empty")
            return False
        else:
            messagebox.showerror("Error", "Password and Confirm password should match")
            return False

    def monthalpha2num():
        umonthofbirth = monthbox.get()
        monthdict ={'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August': '08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
        if umonthofbirth != "":
            monthnum = monthdict[umonthofbirth]
            return monthnum

    def SignToHome():
        ufname = Fnameentry.get()
        ulname =  Lnameentry.get()
        uemail = emailentry.get()
        ugender = gender.get()
        uusername = usernameentry.get()
        upass = passwordentry.get()
        urepass = repasswordentry.get()
        udateofbirth = datebox.get()
        umonthofbirth = monthbox.get()
        uyearofbirth = yearbox.get()
        umobile1 =  mobile1entry.get()
        umobile2 =  mobile2entry.get()
        uhouseno = houseentry.get()
        ustreet = streetentry.get()
        ucity = cityentry.get()
        ucountry = countryentry.get()
        monthnum = monthalpha2num()
        try:
            databasedate = str(uyearofbirth+'-'+monthnum+'-'+udateofbirth)
        except TypeError:
            pass

        userpermission = CheckAvailable()
        passpermission = checkpassword()
        if userpermission == True  and passpermission == True:
            UserTableDetail = ( ufname, ulname, uusername,uemail,upass,ugender,databasedate,uhouseno,ustreet,ucity,ucountry)
            sqlformula = 'insert into Users (fname,lname,username,email,password,gender,dob,houseno,street,city,country) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(sqlformula,UserTableDetail)
            mydb.commit()
            sqlformula = 'select uid from users where username = %s'
            mycursor.execute(sqlformula,(uusername,))
            uid = mycursor.fetchall()
            mobilenums = (umobile1,umobile2)
            for i in mobilenums:
                if i != '':
                    contacttabledetails=(uid[0][0],i,)
                    sqlformula = 'insert into ucontact(uid,mobile) values (%s,%s)'
                    mycursor.execute(sqlformula,contacttabledetails)
                    mydb.commit()
            messagebox.showinfo("Congratulations", "Your Account Is Successfully Created, Please setup your devices")
            signuproot.destroy()
            importusername(uusername)
            Homepage()

    #### MAIN SIGNUP WINDOW ######
    signuproot = Tk()
    signuproot.geometry("755x1001+711+10")
    signuproot.title("Sign Up")
    signuproot.configure(background="#000000")
    signuproot.resizable(FALSE,FALSE)
    
    ##### CREATE ACCOUNT FRAME ######## 
    Topframe = tk.Frame(signuproot)
    Topframe.place(relx=-0.013, rely=0.0, relheight=0.135, relwidth=1.026)
    Topframe.configure(relief='groove')
    Topframe.configure(borderwidth="0")
    Topframe.configure(relief="groove")
    Topframe.configure(background="#000000")

    ####### LOGO LABLE FOR SIGN UP PAGE ########
    LogoLabel = tk.Label(Topframe)
    LogoLabel.place(relx=0.697, rely=0.074, height=111, width=194)
    LogoLabel.configure(background="#d9d9d9")
    LogoLabel.configure(disabledforeground="#a3a3a3")
    LogoLabel.configure(foreground="#000000")
    photo_location = os.path.join("logoSHORTNEW14.png")
    global _img0
    _img0 = tk.PhotoImage(file=photo_location)
    LogoLabel.configure(image=_img0)
    LogoLabel.configure(text='''Label''')

    ########## create account heading ########
    SignUpLabel = tk.Label(Topframe)
    SignUpLabel.place(relx=0.065, rely=0.074, height=101, width=494)
    SignUpLabel.configure(background="#000000")
    SignUpLabel.configure(cursor="fleur")
    SignUpLabel.configure(disabledforeground="#a3a3a3")
    SignUpLabel.configure(font="-family {Comic Sans MS} -size 35")
    SignUpLabel.configure(foreground="#edbe00")
    SignUpLabel.configure(text='''Create Your Account''')

    ######### First step toward a better health heading ######

    SignUpLabel = tk.Label(Topframe)
    SignUpLabel.place(relx=0.09, rely=0.65, height=18, width=460)
    SignUpLabel.configure(background="#edbe00")
    SignUpLabel.configure(cursor="fleur")
    SignUpLabel.configure(disabledforeground="#a3a3a3")
    SignUpLabel.configure(font="-family {Comic Sans MS} -size 12")
    SignUpLabel.configure(foreground="#000000")
    SignUpLabel.configure(text='''-------------------------First Step Towards Better Health-------------------------''')

    ##### CREATE BOTTOM FRAME ########
    BottomFrame = tk.Frame(signuproot)
    BottomFrame.place(relx=0.00, rely=0.13, relheight=0.84, relwidth=1)
    BottomFrame.configure(relief='groove')
    BottomFrame.configure(borderwidth="0")
    BottomFrame.configure(relief="groove")
    BottomFrame.configure(background="#000000")

    Fnamelabel = Label(BottomFrame)
    Fnamelabel.place(relx=0.02, rely=0.055, height=46, width=162)
    Fnamelabel.configure(background="#000000")  # 070707
    Fnamelabel.configure(disabledforeground="#a3a3a3")
    Fnamelabel.configure(font="-family {Comic Sans MS} -size 16")
    Fnamelabel.configure(foreground="#edbe00")
    Fnamelabel.configure(highlightcolor="#fc613a")
    Fnamelabel.configure(text='''First Name :''')

    Fnameentry = Entry(BottomFrame)  # borderwidth=5
    Fnameentry.place(relx=0.225, rely=0.065, height=30, relwidth=0.23)
    Fnameentry.configure(background="#211905")
    Fnameentry.configure(disabledforeground="#a3a3a3")
    Fnameentry.configure(font="-family {Comic Sans MS} -size 13")
    Fnameentry.configure(foreground="White")
    Fnameentry.configure(highlightcolor="#ffed4a")
    Fnameentry.configure(insertbackground="white")
    Fnameentry.configure(readonlybackground="#efedee")

    Lnamelabe = Label(BottomFrame)
    Lnamelabe.place(relx=0.500, rely=0.055, height=46, width=162)
    Lnamelabe.configure(background="#000000")  # 070707
    Lnamelabe.configure(disabledforeground="#a3a3a3")
    Lnamelabe.configure(font="-family {Comic Sans MS} -size 16")
    Lnamelabe.configure(foreground="#edbe00")
    Lnamelabe.configure(highlightcolor="#fc613a")
    Lnamelabe.configure(text='''Last Name :''')

    Lnameentry = Entry(BottomFrame)  # borderwidth=5
    Lnameentry.place(relx=0.71, rely=0.065, height=30, relwidth=0.23)
    Lnameentry.configure(background="#211905")
    Lnameentry.configure(disabledforeground="#a3a3a3")
    Lnameentry.configure(font="-family {Comic Sans MS} -size 13")
    Lnameentry.configure(foreground="White")
    Lnameentry.configure(highlightcolor="#ffed4a")
    Lnameentry.configure(insertbackground="white")
    Lnameentry.configure(readonlybackground="#efedee")

    emailabel = Label(BottomFrame)
    emailabel.place(relx=0.02, rely=0.125, height=46, width=162)
    emailabel.configure(background="#000000")  # 070707
    emailabel.configure(disabledforeground="#a3a3a3")
    emailabel.configure(font="-family {Comic Sans MS} -size 16")
    emailabel.configure(foreground="#edbe00")
    emailabel.configure(highlightcolor="#fc613a")
    emailabel.configure(text='''Email :''')

    emailentry = Entry(BottomFrame)  # borderwidth=5
    emailentry.place(relx=0.225, rely=0.135, height=30, relwidth=0.60)
    emailentry.configure(background="#211905")
    emailentry.configure(disabledforeground="#a3a3a3")
    emailentry.configure(font="-family {Comic Sans MS} -size 13")
    emailentry.configure(foreground="White")
    emailentry.configure(highlightcolor="#ffed4a")
    emailentry.configure(insertbackground="white")
    emailentry.configure(readonlybackground="#efedee")

    Genderlabel = Label(BottomFrame)
    Genderlabel.place(relx=0.02, rely=0.195, height=46, width=150)
    Genderlabel.configure(background="#000000")  # 070707
    Genderlabel.configure(disabledforeground="#a3a3a3")
    Genderlabel.configure(font="-family {Comic Sans MS} -size 16")
    Genderlabel.configure(foreground="#edbe00")
    Genderlabel.configure(highlightcolor="#fc613a")
    Genderlabel.configure(text='''Gender :''')

    gender = StringVar()

    maleradio = Radiobutton(BottomFrame,text="Male",value="male",var=gender)
    maleradio.place(relx=0.250, rely=0.210, height=30, relwidth=0.1)
    maleradio.configure(background="#000000")  # 070707
    maleradio.configure(disabledforeground="#a3a3a3")
    maleradio.configure(font="-family {Comic Sans MS} -size 14")
    maleradio.configure(foreground="#edbe00")
    maleradio.configure(highlightcolor="#000000")

    femaleradio = Radiobutton(BottomFrame, text="Female", value="female", var=gender)
    femaleradio.place(relx=0.420, rely=0.210, height=30, relwidth=0.12)
    femaleradio.configure(background="#000000")  # 070707
    femaleradio.configure(disabledforeground="#a3a3a3")
    femaleradio.configure(font="-family {Comic Sans MS} -size 14")
    femaleradio.configure(foreground="#edbe00")
    femaleradio.configure(highlightcolor="#000000")

    usenamelabel = Label(BottomFrame)
    usenamelabel.place(relx=0.02, rely=0.265, height=46, width=150)
    usenamelabel.configure(background="#000000")  # 070707
    usenamelabel.configure(disabledforeground="#a3a3a3")
    usenamelabel.configure(font="-family {Comic Sans MS} -size 16")
    usenamelabel.configure(foreground="#edbe00")
    usenamelabel.configure(highlightcolor="#fc613a")
    usenamelabel.configure(text='''Username :''')


    usernameentry = Entry(BottomFrame)  # borderwidth=5
    usernameentry.place(relx=0.225, rely=0.275, height=30, relwidth=0.30)
    usernameentry.configure(background="#211905")
    usernameentry.configure(disabledforeground="#a3a3a3")
    usernameentry.configure(font="-family {Comic Sans MS} -size 13")
    usernameentry.configure(foreground="White")
    usernameentry.configure(highlightcolor="#ffed4a")
    usernameentry.configure(insertbackground="white")
    usernameentry.configure(readonlybackground="#efedee")

    checkuserbutton = Button(BottomFrame)
    checkuserbutton.place(relx=0.550, rely=0.28, height=1, width=140, relheight=0.025)
    checkuserbutton.configure(activebackground="#000000")
    checkuserbutton.configure(activeforeground="#000000")
    checkuserbutton.configure(background="#000000")
    checkuserbutton.configure(disabledforeground="#000000")
    checkuserbutton.configure(font="-family {Comic Sans MS} -size 12")
    checkuserbutton.configure(foreground="#edbe00")
    checkuserbutton.configure(highlightbackground="#000000")
    checkuserbutton.configure(pady="0")
    checkuserbutton.configure(relief="flat")
    checkuserbutton.configure(text='''Check Availability''')
    checkuserbutton.configure(cursor="hand2")
    checkuserbutton.configure(anchor='w')
    checkuserbutton.configure(command = CheckAvailable)

    passwordlabel = Label(BottomFrame)
    passwordlabel.place(relx=0.02, rely=0.335, height=46, width=150)
    passwordlabel.configure(background="#000000")  # 070707
    passwordlabel.configure(disabledforeground="#a3a3a3")
    passwordlabel.configure(font="-family {Comic Sans MS} -size 16")
    passwordlabel.configure(foreground="#edbe00")
    passwordlabel.configure(highlightcolor="#fc613a")
    passwordlabel.configure(text='''Password :''')

    passwordentry = Entry(BottomFrame,show='*')  # borderwidth=5
    passwordentry.place(relx=0.225, rely=0.345, height=30, relwidth=0.22)
    passwordentry.configure(background="#211905")
    passwordentry.configure(disabledforeground="#a3a3a3")
    passwordentry.configure(font="-family {Comic Sans MS} -size 13")
    passwordentry.configure(foreground="White")
    passwordentry.configure(highlightcolor="#ffed4a")
    passwordentry.configure(insertbackground="white")
    passwordentry.configure(readonlybackground="#efedee")

    repasswordlabel = Label(BottomFrame)
    repasswordlabel.place(relx=0.47, rely=0.335, height=46, width=190)
    repasswordlabel.configure(background="#000000")  # 070707
    repasswordlabel.configure(disabledforeground="#a3a3a3")
    repasswordlabel.configure(font="-family {Comic Sans MS} -size 16")
    repasswordlabel.configure(foreground="#edbe00")
    repasswordlabel.configure(highlightcolor="#fc613a")
    repasswordlabel.configure(text='''Confirm Password :''')

    repasswordentry = Entry(BottomFrame, show='*')  # borderwidth=5
    repasswordentry.place(relx=0.74, rely=0.345, height=30, relwidth=0.22)
    repasswordentry.configure(background="#211905")
    repasswordentry.configure(disabledforeground="#a3a3a3")
    repasswordentry.configure(font="-family {Comic Sans MS} -size 13")
    repasswordentry.configure(foreground="White")
    repasswordentry.configure(highlightcolor="#ffed4a")
    repasswordentry.configure(insertbackground="white")
    repasswordentry.configure(readonlybackground="#efedee")

    datelabel = Label(BottomFrame)
    datelabel.place(relx=0.03, rely=0.405, height=46, width=150)
    datelabel.configure(background="#000000")  # 070707
    datelabel.configure(disabledforeground="#a3a3a3")
    datelabel.configure(font="-family {Comic Sans MS} -size 16")
    datelabel.configure(foreground="#edbe00")
    datelabel.configure(highlightcolor="#fc613a")
    datelabel.configure(text='''Date Of Birth :''')

    #dateofbirth = int()
    dates = list(range(1,32))
    #monthofbirth = StringVar()
    months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    #yearofbirth = int()
    years = list(range(1980,2019))

    datebox = ttk.Combobox(BottomFrame,values=(dates),state='readonly')#citylabel1
    datebox.place(relx=0.26, rely=0.420, height=23, width=50)
    datebox.configure(font="-family {Comic Sans MS} -size 10",justify = 'center')

    monthbox = ttk.Combobox(BottomFrame, values=(months), state='readonly')#,textvariable=monthofbirth
    monthbox.place(relx=0.4, rely=0.420, height=23, width=100)
    monthbox.configure(font="-family {Comic Sans MS} -size 10",justify = 'center')
    
    yearbox = ttk.Combobox(BottomFrame, values=(years), state='readonly')#, textvariable=yearofbirth
    yearbox.place(relx=0.6, rely=0.420, height=23, width=70)
    yearbox.configure(font="-family {Comic Sans MS} -size 10",justify = 'center')

    mobile1label = Label(BottomFrame)
    mobile1label.place(relx=0.002, rely=0.475, height=46, width=180)
    mobile1label.configure(background="#000000")  # 070707
    mobile1label.configure(disabledforeground="#a3a3a3")
    mobile1label.configure(font="-family {Comic Sans MS} -size 16")
    mobile1label.configure(foreground="#edbe00")
    mobile1label.configure(highlightcolor="#fc613a")
    mobile1label.configure(text='''Mobile 1 :''')

    mobile1entry = Entry(BottomFrame)  # borderwidth=5
    mobile1entry.place(relx=0.225, rely=0.485, height=30, relwidth=0.3)
    mobile1entry.configure(background="#211905")
    mobile1entry.configure(disabledforeground="#a3a3a3")
    mobile1entry.configure(font="-family {Comic Sans MS} -size 13")
    mobile1entry.configure(foreground="White")
    mobile1entry.configure(highlightcolor="#ffed4a")
    mobile1entry.configure(insertbackground="white")
    mobile1entry.configure(readonlybackground="#efedee")

    mobile2label = Label(BottomFrame)
    mobile2label.place(relx=0.002, rely=0.545, height=46, width=180)
    mobile2label.configure(background="#000000")  # 070707
    mobile2label.configure(disabledforeground="#a3a3a3")
    mobile2label.configure(font="-family {Comic Sans MS} -size 16")
    mobile2label.configure(foreground="#edbe00")
    mobile2label.configure(highlightcolor="#fc613a")
    mobile2label.configure(text='''Mobile 2 :''')

    mobile2entry = Entry(BottomFrame)  # borderwidth=5
    mobile2entry.place(relx=0.225, rely=0.555, height=30, relwidth=0.3)
    mobile2entry.configure(background="#211905")
    mobile2entry.configure(disabledforeground="#a3a3a3")
    mobile2entry.configure(font="-family {Comic Sans MS} -size 13")
    mobile2entry.configure(foreground="White")
    mobile2entry.configure(highlightcolor="#ffed4a")
    mobile2entry.configure(insertbackground="white")
    mobile2entry.configure(readonlybackground="#efedee")

    Houselabel = Label(BottomFrame)
    Houselabel.place(relx=0.03, rely=0.615, height=46, width=150)
    Houselabel.configure(background="#000000")  # 070707
    Houselabel.configure(disabledforeground="#a3a3a3")
    Houselabel.configure(font="-family {Comic Sans MS} -size 16")
    Houselabel.configure(foreground="#edbe00")
    Houselabel.configure(highlightcolor="#fc613a")
    Houselabel.configure(text='''House No :''')

    houseentry = Entry(BottomFrame)  # borderwidth=5
    houseentry.place(relx=0.225, rely=0.625, height=30, relwidth=0.3)
    houseentry.configure(background="#211905")
    houseentry.configure(disabledforeground="#a3a3a3")
    houseentry.configure(font="-family {Comic Sans MS} -size 13")
    houseentry.configure(foreground="White")
    houseentry.configure(highlightcolor="#ffed4a")
    houseentry.configure(insertbackground="white")
    houseentry.configure(readonlybackground="#efedee")

    streetlabel = Label(BottomFrame)
    streetlabel.place(relx=0.03, rely=0.675, height=46, width=150)
    streetlabel.configure(background="#000000")  # 070707
    streetlabel.configure(disabledforeground="#a3a3a3")
    streetlabel.configure(font="-family {Comic Sans MS} -size 16")
    streetlabel.configure(foreground="#edbe00")
    streetlabel.configure(highlightcolor="#fc613a")
    streetlabel.configure(text='''Street :''')

    streetentry = Entry(BottomFrame)  # borderwidth=5
    streetentry.place(relx=0.225, rely=0.685, height=30, relwidth=0.40)
    streetentry.configure(background="#211905")
    streetentry.configure(disabledforeground="#a3a3a3")
    streetentry.configure(font="-family {Comic Sans MS} -size 13")
    streetentry.configure(foreground="White")
    streetentry.configure(highlightcolor="#ffed4a")
    streetentry.configure(insertbackground="white")
    streetentry.configure(readonlybackground="#efedee")
 
    citylabel = Label(BottomFrame)
    citylabel.place(relx=0.03, rely=0.745, height=46, width=150)
    citylabel.configure(background="#000000")  # 070707
    citylabel.configure(disabledforeground="#a3a3a3")
    citylabel.configure(font="-family {Comic Sans MS} -size 16")
    citylabel.configure(foreground="#edbe00")
    citylabel.configure(highlightcolor="#fc613a")
    citylabel.configure(text='''City :''')

    cityentry = Entry(BottomFrame)  # borderwidth=5
    cityentry.place(relx=0.225, rely=0.755, height=30, relwidth=0.40)
    cityentry.configure(background="#211905")
    cityentry.configure(disabledforeground="#a3a3a3")
    cityentry.configure(font="-family {Comic Sans MS} -size 13")
    cityentry.configure(foreground="White")
    cityentry.configure(highlightcolor="#ffed4a")
    cityentry.configure(insertbackground="white")
    cityentry.configure(readonlybackground="#efedee")

    countrylabel = Label(BottomFrame)
    countrylabel.place(relx=0.03, rely=0.815, height=46, width=150)
    countrylabel.configure(background="#000000")  # 070707
    countrylabel.configure(disabledforeground="#a3a3a3")
    countrylabel.configure(font="-family {Comic Sans MS} -size 16")
    countrylabel.configure(foreground="#edbe00")
    countrylabel.configure(highlightcolor="#fc613a")
    countrylabel.configure(text='''Country :''')

    countryentry = Entry(BottomFrame)  # borderwidth=5
    countryentry.place(relx=0.225, rely=0.825, height=30, relwidth=0.40)
    countryentry.configure(background="#211905")
    countryentry.configure(disabledforeground="#a3a3a3")
    countryentry.configure(font="-family {Comic Sans MS} -size 13")
    countryentry.configure(foreground="White")
    countryentry.configure(highlightcolor="#ffed4a")
    countryentry.configure(insertbackground="white")
    countryentry.configure(readonlybackground="#efedee")

    Fnamelabel = Label(BottomFrame)
    Fnamelabel.place(relx=0.05, rely=0.875, height=46, width=650)
    Fnamelabel.configure(background="#000000")  # 070707
    Fnamelabel.configure(disabledforeground="#a3a3a3")
    Fnamelabel.configure(font="-family {Comic Sans MS} -size 16")
    Fnamelabel.configure(foreground="#edbe00")
    Fnamelabel.configure(highlightcolor="#fc613a")
    Fnamelabel.configure(text='''Username and Password are Required Now !\nYou can always add and edit details in profile section''')


    loginbutton = Button(BottomFrame)
    loginbutton.place(relx=0.367, rely=0.950, height=47, width=200)
    loginbutton.configure(activebackground="#ececec")
    loginbutton.configure(activeforeground="#000000")
    loginbutton.configure(background="#edbe00")
    loginbutton.configure(disabledforeground="#a3a3a3")
    loginbutton.configure(font="-family {Comic Sans MS} -size 18")
    loginbutton.configure(foreground="#000000")
    loginbutton.configure(highlightbackground="#d9d9d9")
    loginbutton.configure(highlightcolor="black")
    loginbutton.configure(pady="0")
    loginbutton.configure(text='''Submit''')
    loginbutton.configure(cursor="hand2")
    loginbutton.configure(command=SignToHome)
    signuproot.mainloop()

if __name__ == "__main__":
    SignUp()

