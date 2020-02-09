from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os.path

#### MYSQL LIBRARY ####
import mysql.connector

###### import other files and functions #######


###### DATABASE #####
mydb = mysql.connector.connect(
    host='localhost',
    user='pycoders',
    passwd='gass',
    database='trackbyte'
)
mycursor = mydb.cursor()
queryvariable = 0



def ALLFAQ():
    global queryvariable


    querylist = ['1List all the users drinking average 2 L of water and sleep more than 6 hours.',
                 '2 Count the number of users who walked more than or equal to 4 km on a 10-dec-2019.',
                 ' 3List the name of users whose name starts and ends with "A" using Fitbit devices.',
                 '4 List all upcoming events.',
                 '5List the users and their total steps using a MI device.',
                 ' List the users by decreasing/increasing number of steps.',
                 ' List all the registered users or device?',
                 'Name the most popular device among users.',
                 ' How many users are using a Honor device?',
                 ' How many fitbit devices are available?',
                 ' List the users has weight between 80-150?',
                 'List the fitbit users attending Trekking Event.',
                 'Average and total distance covered by all users in month of December.',
                 ' Name the oldest user. ',
                 ' List the users who has been using devices for more than a year.',
                 'List the users who achieved all his goals for last week.',
                 ' Display all the users who have events on their birthdate.',
                 'List the number of users each country attended more than 3 event.',
                 ' Display all the female users who are attending either zumba or trekking event.',
                 'Modify the event name trekking to hiking where the event id is 103.']
    def one():
        query= 'List all the users drinking average 2 L of water and sleep more than 6 hours.'
        Text3 = tk.Text(Frame3, wrap='word')
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905")
        Text3.configure(font="-family {Comic Sans MS} -size 20")
        Text3.configure(foreground="#ffffff")
        Text3.configure(highlightbackground="#d9d9d9")
        Text3.configure(highlightcolor="black")
        Text3.configure(insertbackground="black")
        Text3.configure(selectbackground="#c4c4c4")
        Text3.configure(selectforeground="black")
        global queryvariable
        queryvariable = 1
        Text1.delete(1.0, END)
        Text3.delete(1.0, END)
        Text2.delete(1.0, END)
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text=" Concat, avg, having, where, and, >, round")
        sqlcode = 'select concat(u.fname, " ", u.lname), round(avg(a.water),2), round(avg(a.sleep),2)   from users as u, activities as a where u.uid = a.uid having avg(a.water) > 2 and avg(a.sleep) > 6'
        Text2.delete(1.0, END)
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)

        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['   Name   ', '     Average Water     ', '    Average Sleep     ']
        ans.insert(0, headlist)
        Text3.delete(1.0, END)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

        giveanswer()
        
    def two():
        query = ' Count the number of users who walked 6 km on a 11-aug-2019.'
        Text3 = tk.Text(Frame3, wrap='word')
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905",font="-family {Comic Sans MS} -size 20",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="#c4c4c4",selectforeground="black")
        global queryvariable
        queryvariable = 2
        Text3.delete(1.0, END)
        Text2.delete(1.0, END)
        Text1.delete(1.0, END)
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text=" distinct,date format,group by, concat")
        sqlcode = 'select distinct date_format(activitydate,"%y-%m-%d" ), concat( u.fname, "  " ,u.lname), a.distance from users u, activities a where a.activitydate = "2019-08-11" group by u.fname having distance = 6'
        Text2.delete(1.0, END)
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        headlist = ['      Date        ', '       Name       ', '    Distance   ']
        ans.insert(0, headlist)
        Text3.delete(1.0, END)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

    def three():
        query = ' List the name of users whose name starts and ends with "A" using Fitbit devices.'
        Text3 = tk.Text(Frame3, wrap='word')
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text1.delete(1.0, END)
        Text2.delete(1.0, END)
        Text3.delete(1.0, END)
        global queryvariable
        queryvariable = 3
        Text1.insert(INSERT, query)
        conlabel.configure(text=" concat, aliases, and, like")
        sqlcode = 'select concat(u.fname,"  ",u.lname),concat(dl.company," ",dl.model) from users as u, devicelist as dl, userdevice as ud where dl.company = "fitbit" and u.fname like "a%" and dl.did = ud.did and ud.uid = u.uid '
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        headlist = ['       Name        ', '     Device Name   ']
        ans.insert(0, headlist)

        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

    def four():
        query = ' List all upcoming events.'
        Text3 = tk.Text(Frame3, wrap='word')
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text1.delete(1.0, END)
        Text2.delete(1.0, END)
        Text3.delete(1.0, END)
        global queryvariable
        queryvariable = 4
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text=" NOW()")
        sqlcode ='select ename,edate from events where edate > NOW()'
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['       Name        ', '        Date      ']
        ans.insert(0, headlist)

        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])


    def five():
        query = 'List the users and their total steps and maximum distance where device id is 104'
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text1.delete(1.0,END)
        Text2.delete(1.0,END)
        Text3.delete(1.0,END)
        global queryvariable
        queryvariable = 5
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text=" Sum and Max aggregate functions")
        sqlcode = "select ud.did,concat(u.fname,' ',u.lname),sum(a.steps),concat(max(distance),' km') from users u, activities a,userdevice ud where ud.did =104 and u.uid=ud.uid"
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['Device ID', '      Name        ', '        Total Steps      ','        Max Distance    ']
        ans.insert(0, headlist)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

    def six():
        query =  'List the users by decreasing/increasing number of steps on 2019-08-10.'
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.delete(1.0,END)
        Text2.delete(1.0,END)
        Text3.delete(1.0, END)
        Text2.delete(1.0, END)
        Text1.delete(1.0, END)
        global queryvariable
        queryvariable = 6
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text="order by, date format")
        sqlcode = 'select date_format(a.activitydate,"%y-%m-%d" ),concat(u.fname," ",u.lname), a.steps from users u,activities a where u.uid =a.uid and activitydate = "2019-08-10" order by a.steps'
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['      Date       ', '        Name          ', '          Steps        ']
        ans.insert(0, headlist)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

    def seven():
        query = 'List all the registered users who have event on their birthday?'
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.delete(1.0,END)
        Text2.delete(1.0,END)
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text="nested query")
        sqlcode = "select concat(fname,' ',lname), dob from users where dob in(select edate from events)"
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['      Name      ', '        Birthdate          ']
        ans.insert(0, headlist)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

    def eight():
        query = 'Name the device and the number of users using that device'
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.delete(1.0, END)
        Text2.delete(1.0, END)
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text="concat,count, group by, order by DESC")
        sqlcode = "select ud.did, concat(dl.company,' ',dl.model), count(ud.uid) as count from userdevice as ud, devicelist as dl where ud.did = dl.did group by ud.did order by count DESC"
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['      Device Id    ', '        Name          ','  Number Of User ']
        ans.insert(0, headlist)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])
    def nine():
        query = 'Show device id and name of all Fitbit device'
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.delete(1.0, END)
        Text2.delete(1.0, END)
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text="concat, like")
        sqlcode = "select did, concat(company, ' ', model) from devicelist where company like '%Fitbit%' "
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['      Device Id    ', '        Device Name    ']
        ans.insert(0, headlist)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

    def ten():
        query = "Show users whose weight ranges between 70 to 120"
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.delete(1.0, END)
        Text2.delete(1.0, END)
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text="between , concat , order by")
        sqlcode = "select concat(fname,' ',lname) ,weight from users where weight between 70 and 120  order by weight "
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['      Name   ', '       Weight   ']
        ans.insert(0, headlist)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])


    def eleven():
        query = "show the average and total distance coverd by all the users in the month of August"
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.delete(1.0, END)
        Text2.delete(1.0, END)
        Text1.delete(1.0, END)
        Text1.insert(INSERT, query)
        conlabel.configure(text="concat,round, sum, avg, group by")
        sqlcode = "select concat(u.fname,' ' ,lname), round(avg(a.distance),2), sum(a.distance) from users u, activities a where u.uid = a.uid and a.activitydate like '%-08-%' group by a.uid"
        Text2.insert(INSERT, sqlcode)
        mycursor.execute(sqlcode)
        ans = list(mycursor.fetchall())
        print(ans)
        headlist = ['     Name    ', '  Average Distance   ','   Total Distance  ']
        ans.insert(0, headlist)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                emailabel = Label(Text3)
                emailabel.grid(row=i, column=j)
                emailabel.configure(background="#211905")  # 070707
                emailabel.configure(disabledforeground="#a3a3a3")
                emailabel.configure(font="-family {Comic Sans MS} -size 16")
                emailabel.configure(foreground="white")
                emailabel.configure(highlightcolor="#fc613a")
                emailabel.configure(text=ans[i][j])

    def twelve():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 12
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[11])

    def thirteen():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 13
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[12])

    def fourteen():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 14
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[13])

    def fifteen():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 15
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[14])

    def sixteen():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 16
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[15])

    def seventeen():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 17
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[16])

    def eightteen():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 18
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[17])

    def nineteen():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 19
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[18])

    def twenty():
        Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
        Text3.configure(background="#211905", font="-family {Comic Sans MS} -size 20", foreground="#ffffff",
                        highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                        selectbackground="#c4c4c4", selectforeground="black")
        Text3.insert(INSERT, 'Give me Some Question, I am Hungry')
        global queryvariable
        queryvariable = 20
        Text1.delete(1.0, END)
        Text1.insert(INSERT, querylist[19])

    def giveanswer():

        global queryvariable

        if queryvariable == 0:
            pass
        if queryvariable == 1:
            pass
        if queryvariable == 2:
            pass
        if queryvariable == 3:
            pass
        if queryvariable == 4:
            pass
        if queryvariable == 5:
            pass
        if queryvariable == 6:
            pass
        if queryvariable == 7:
            pass
        if queryvariable == 8:
            pass
        if queryvariable == 9:
            pass
        if queryvariable == 10:
            pass
        if queryvariable == 11:
            pass
        if queryvariable == 12:
            pass
        if queryvariable == 13:
            pass
        if queryvariable == 14:
            pass
        if queryvariable == 15:
            pass
        if queryvariable == 16:
            pass
        if queryvariable == 17:
            pass
        if queryvariable == 18:
            pass
        if queryvariable == 19:
            pass
        if queryvariable == 20:
            pass
    faqroot = Tk()
    faqroot.geometry("755x1001+711+10")
    faqroot.title("New Toplevel")
    faqroot.configure(background="#edbe00")

    Frame1 = tk.Frame(faqroot)
    Frame1.place(relx=0.0, rely=0.0, relheight=0.105, relwidth=1.0)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="black")

    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.013, rely=0.095, height=83, width=87)
    Label1.configure(background="#000000")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    photo_location = os.path.join("quries.png")
    global _img0
    _img0 = tk.PhotoImage(file=photo_location)
    Label1.configure(image=_img0)
    Label1.configure(text='''Label''')

    Label2 = tk.Label(Frame1)
    Label2.place(relx=0.728, rely=-0.099, height=120, width=204)
    Label2.configure(background="black")
    Label2.configure(anchor = "e")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    photo_location = os.path.join("logoSHORTNEW14.png")
    global _img1
    _img1 = tk.PhotoImage(file=photo_location)
    Label2.configure(image=_img1)
    Label2.configure(text='''Label''')

    Label3 = tk.Label(Frame1)
    Label3.place(relx=0.146, rely=0.19, height=55, width=400)
    Label3.configure(anchor='w')
    Label3.configure(background="#000000")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Comic Sans MS} -size 40")
    Label3.configure(foreground="#edbe00")
    Label3.configure(text='''Queries''')

    Frame2 = tk.Frame(faqroot)
    Frame2.place(relx=0.013, rely=0.12, relheight=0.105, relwidth=0.974)

    Frame2.configure(relief='groove')
    Frame2.configure(borderwidth="2")
    Frame2.configure(relief="groove")
    Frame2.configure(background="black")

    Button1 = tk.Button(Frame2)
    Button1.place(relx=0.027, rely=0.095, height=34, width=46)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#edbe00")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font="-family {Comic Sans MS} -size 18")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#edbe00")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''1''')
    Button1.configure(command = one)

    Button1_10 = tk.Button(Frame2)
    Button1_10.place(relx=0.605, rely=0.095, height=34, width=46)
    Button1_10.configure(activebackground="#ececec")
    Button1_10.configure(activeforeground="#000000")
    Button1_10.configure(background="#edbe00")
    Button1_10.configure(disabledforeground="#a3a3a3")
    Button1_10.configure(font="-family {Comic Sans MS} -size 18")
    Button1_10.configure(foreground="#000000")
    Button1_10.configure(highlightbackground="#edbe00")
    Button1_10.configure(highlightcolor="black")
    Button1_10.configure(pady="0")
    Button1_10.configure(text='''7''')
    Button1_10.configure(command=seven)

    Button1_11 = tk.Button(Frame2)
    Button1_11.place(relx=0.211, rely=0.095, height=34, width=46)
    Button1_11.configure(activebackground="#ececec")
    Button1_11.configure(activeforeground="#000000")
    Button1_11.configure(background="#edbe00")
    Button1_11.configure(disabledforeground="#a3a3a3")
    Button1_11.configure(font="-family {Comic Sans MS} -size 18")
    Button1_11.configure(foreground="#000000")
    Button1_11.configure(highlightbackground="#edbe00")
    Button1_11.configure(highlightcolor="black")
    Button1_11.configure(pady="0")
    Button1_11.configure(text='''3''')
    Button1_11.configure(command=three)

    Button1_12 = tk.Button(Frame2)
    Button1_12.place(relx=0.116, rely=0.095, height=34, width=46)
    Button1_12.configure(activebackground="#ececec")
    Button1_12.configure(activeforeground="#000000")
    Button1_12.configure(background="#edbe00")
    Button1_12.configure(disabledforeground="#a3a3a3")
    Button1_12.configure(font="-family {Comic Sans MS} -size 18")
    Button1_12.configure(foreground="#000000")
    Button1_12.configure(highlightbackground="#edbe00")
    Button1_12.configure(highlightcolor="black")
    Button1_12.configure(pady="0")
    Button1_12.configure(text='''2''')
    Button1_12.configure(command=two)

    Button1_13 = tk.Button(Frame2)
    Button1_13.place(relx=0.503, rely=0.095, height=34, width=46)
    Button1_13.configure(activebackground="#ececec")
    Button1_13.configure(activeforeground="#000000")
    Button1_13.configure(background="#edbe00")
    Button1_13.configure(disabledforeground="#a3a3a3")
    Button1_13.configure(font="-family {Comic Sans MS} -size 18")
    Button1_13.configure(foreground="#000000")
    Button1_13.configure(highlightbackground="#edbe00")
    Button1_13.configure(highlightcolor="black")
    Button1_13.configure(pady="0")
    Button1_13.configure(text='''6''')
    Button1_13.configure(command=six)

    Button1_14 = tk.Button(Frame2)
    Button1_14.place(relx=0.401, rely=0.095, height=34, width=46)
    Button1_14.configure(activebackground="#ececec")
    Button1_14.configure(activeforeground="#000000")
    Button1_14.configure(background="#edbe00")
    Button1_14.configure(disabledforeground="#a3a3a3")
    Button1_14.configure(font="-family {Comic Sans MS} -size 18")
    Button1_14.configure(foreground="#000000")
    Button1_14.configure(highlightbackground="#edbe00")
    Button1_14.configure(highlightcolor="black")
    Button1_14.configure(pady="0")
    Button1_14.configure(text='''5''')
    Button1_14.configure(command=five)

    Button1_15 = tk.Button(Frame2)
    Button1_15.place(relx=0.306, rely=0.095, height=34, width=46)
    Button1_15.configure(activebackground="#ececec")
    Button1_15.configure(activeforeground="#000000")
    Button1_15.configure(background="#edbe00")
    Button1_15.configure(disabledforeground="#a3a3a3")
    Button1_15.configure(font="-family {Comic Sans MS} -size 18")
    Button1_15.configure(foreground="#000000")
    Button1_15.configure(highlightbackground="#edbe00")
    Button1_15.configure(highlightcolor="black")
    Button1_15.configure(pady="0")
    Button1_15.configure(text='''4''')
    Button1_15.configure(command=four)

    Button1_16 = tk.Button(Frame2)
    Button1_16.place(relx=0.707, rely=0.095, height=34, width=46)
    Button1_16.configure(activebackground="#ececec")
    Button1_16.configure(activeforeground="#000000")
    Button1_16.configure(background="#edbe00")
    Button1_16.configure(disabledforeground="#a3a3a3")
    Button1_16.configure(font="-family {Comic Sans MS} -size 18")
    Button1_16.configure(foreground="#000000")
    Button1_16.configure(highlightbackground="#edbe00")
    Button1_16.configure(highlightcolor="black")
    Button1_16.configure(pady="0")
    Button1_16.configure(text='''8''')
    Button1_16.configure(command=eight)

    Button1_17 = tk.Button(Frame2)
    Button1_17.place(relx=0.81, rely=0.095, height=34, width=46)
    Button1_17.configure(activebackground="#ececec")
    Button1_17.configure(activeforeground="#000000")
    Button1_17.configure(background="#edbe00")
    Button1_17.configure(disabledforeground="#a3a3a3")
    Button1_17.configure(font="-family {Comic Sans MS} -size 18")
    Button1_17.configure(foreground="#000000")
    Button1_17.configure(highlightbackground="#edbe00")
    Button1_17.configure(highlightcolor="black")
    Button1_17.configure(pady="0")
    Button1_17.configure(text='''9''')
    Button1_17.configure(command=nine)

    Button1_18 = tk.Button(Frame2)
    Button1_18.place(relx=0.905, rely=0.095, height=34, width=46)
    Button1_18.configure(activebackground="#ececec")
    Button1_18.configure(activeforeground="#000000")
    Button1_18.configure(background="#edbe00")
    Button1_18.configure(disabledforeground="#a3a3a3")
    Button1_18.configure(font="-family {Comic Sans MS} -size 18")
    Button1_18.configure(foreground="#000000")
    Button1_18.configure(highlightbackground="#edbe00")
    Button1_18.configure(highlightcolor="black")
    Button1_18.configure(pady="0")
    Button1_18.configure(text='''10''')
    Button1_18.configure(command=ten)

    Button1_19 = tk.Button(Frame2)
    Button1_19.place(relx=0.034, rely=0.571, height=34, width=46)
    Button1_19.configure(activebackground="#ececec")
    Button1_19.configure(activeforeground="#000000")
    Button1_19.configure(background="#edbe00")
    Button1_19.configure(disabledforeground="#a3a3a3")
    Button1_19.configure(font="-family {Comic Sans MS} -size 18")
    Button1_19.configure(foreground="#000000")
    Button1_19.configure(highlightbackground="#edbe00")
    Button1_19.configure(highlightcolor="black")
    Button1_19.configure(pady="0")
    Button1_19.configure(text='''11''')
    Button1_19.configure(command=eleven)

    Button1_20 = tk.Button(Frame2)
    Button1_20.place(relx=0.116, rely=0.571, height=34, width=46)
    Button1_20.configure(activebackground="#ececec")
    Button1_20.configure(activeforeground="#000000")
    Button1_20.configure(background="#edbe00")
    Button1_20.configure(disabledforeground="#a3a3a3")
    Button1_20.configure(font="-family {Comic Sans MS} -size 18")
    Button1_20.configure(foreground="#000000")
    Button1_20.configure(highlightbackground="#edbe00")
    Button1_20.configure(highlightcolor="black")
    Button1_20.configure(pady="0")
    Button1_20.configure(text='''12''')
    Button1_20.configure(command=twelve)

    Button1_21 = tk.Button(Frame2)
    Button1_21.place(relx=0.612, rely=0.571, height=34, width=46)
    Button1_21.configure(activebackground="#ececec")
    Button1_21.configure(activeforeground="#000000")
    Button1_21.configure(background="#edbe00")
    Button1_21.configure(disabledforeground="#a3a3a3")
    Button1_21.configure(font="-family {Comic Sans MS} -size 18")
    Button1_21.configure(foreground="#000000")
    Button1_21.configure(highlightbackground="#edbe00")
    Button1_21.configure(highlightcolor="black")
    Button1_21.configure(pady="0")
    Button1_21.configure(text='''17''')
    Button1_21.configure(command=seventeen)

    Button1_22 = tk.Button(Frame2)
    Button1_22.place(relx=0.503, rely=0.571, height=34, width=46)
    Button1_22.configure(activebackground="#ececec")
    Button1_22.configure(activeforeground="#000000")
    Button1_22.configure(background="#edbe00")
    Button1_22.configure(disabledforeground="#a3a3a3")
    Button1_22.configure(font="-family {Comic Sans MS} -size 18")
    Button1_22.configure(foreground="#000000")
    Button1_22.configure(highlightbackground="#edbe00")
    Button1_22.configure(highlightcolor="black")
    Button1_22.configure(pady="0")
    Button1_22.configure(text='''16''')
    Button1_22.configure(command=sixteen)

    Button1_23 = tk.Button(Frame2)
    Button1_23.place(relx=0.408, rely=0.571, height=34, width=46)
    Button1_23.configure(activebackground="#ececec")
    Button1_23.configure(activeforeground="#000000")
    Button1_23.configure(background="#edbe00")
    Button1_23.configure(disabledforeground="#a3a3a3")
    Button1_23.configure(font="-family {Comic Sans MS} -size 18")
    Button1_23.configure(foreground="#000000")
    Button1_23.configure(highlightbackground="#edbe00")
    Button1_23.configure(highlightcolor="black")
    Button1_23.configure(pady="0")
    Button1_23.configure(text='''15''')
    Button1_23.configure(command=fifteen)

    Button1_24 = tk.Button(Frame2)
    Button1_24.place(relx=0.306, rely=0.571, height=34, width=46)
    Button1_24.configure(activebackground="#ececec")
    Button1_24.configure(activeforeground="#000000")
    Button1_24.configure(background="#edbe00")
    Button1_24.configure(disabledforeground="#a3a3a3")
    Button1_24.configure(font="-family {Comic Sans MS} -size 18")
    Button1_24.configure(foreground="#000000")
    Button1_24.configure(highlightbackground="#edbe00")
    Button1_24.configure(highlightcolor="black")
    Button1_24.configure(pady="0")
    Button1_24.configure(text='''14''')
    Button1_24.configure(command=fourteen)

    Button1_25 = tk.Button(Frame2)
    Button1_25.place(relx=0.218, rely=0.571, height=34, width=46)
    Button1_25.configure(activebackground="#ececec")
    Button1_25.configure(activeforeground="#000000")
    Button1_25.configure(background="#edbe00")
    Button1_25.configure(disabledforeground="#a3a3a3")
    Button1_25.configure(font="-family {Comic Sans MS} -size 18")
    Button1_25.configure(foreground="#000000")
    Button1_25.configure(highlightbackground="#edbe00")
    Button1_25.configure(highlightcolor="black")
    Button1_25.configure(pady="0")
    Button1_25.configure(text='''13''')
    Button1_25.configure(command=thirteen)

    Button1_26 = tk.Button(Frame2)
    Button1_26.place(relx=0.816, rely=0.571, height=34, width=46)
    Button1_26.configure(activebackground="#ececec")
    Button1_26.configure(activeforeground="#000000")
    Button1_26.configure(background="#edbe00")
    Button1_26.configure(disabledforeground="#a3a3a3")
    Button1_26.configure(font="-family {Comic Sans MS} -size 18")
    Button1_26.configure(foreground="#000000")
    Button1_26.configure(highlightbackground="#edbe00")
    Button1_26.configure(highlightcolor="black")
    Button1_26.configure(pady="0")
    Button1_26.configure(text='''19''')
    Button1_26.configure(command=nineteen)


    Button1_27 = tk.Button(Frame2)
    Button1_27.place(relx=0.707, rely=0.571, height=34, width=46)
    Button1_27.configure(activebackground="#ececec")
    Button1_27.configure(activeforeground="#000000")
    Button1_27.configure(background="#edbe00")
    Button1_27.configure(disabledforeground="#a3a3a3")
    Button1_27.configure(font="-family {Comic Sans MS} -size 18")
    Button1_27.configure(foreground="#000000")
    Button1_27.configure(highlightbackground="#edbe00")
    Button1_27.configure(highlightcolor="black")
    Button1_27.configure(pady="0")
    Button1_27.configure(text='''18''')
    Button1_27.configure(command=eightteen)


    Button1_28 = tk.Button(Frame2)
    Button1_28.place(relx=0.905, rely=0.571, height=34, width=46)
    Button1_28.configure(activebackground="#ececec")
    Button1_28.configure(activeforeground="#000000")
    Button1_28.configure(background="#edbe00")
    Button1_28.configure(disabledforeground="#a3a3a3")
    Button1_28.configure(font="-family {Comic Sans MS} -size 18")
    Button1_28.configure(foreground="#000000")
    Button1_28.configure(highlightbackground="#edbe00")
    Button1_28.configure(highlightcolor="black")
    Button1_28.configure(pady="0")
    Button1_28.configure(text='''20''')
    Button1_28.configure(command=twenty)


    Frame3 = tk.Frame(faqroot)
    Frame3.place(relx=0.013, rely=0.24, relheight=0.745, relwidth=0.974)

    Frame3.configure(relief='groove')
    Frame3.configure(borderwidth="2")
    Frame3.configure(relief="groove")
    Frame3.configure(background="black")

    conlabel = tk.Label(Frame3)
    conlabel.place(relx=0.027, rely=0.00, height=40, relwidth=0.944)
    conlabel.configure(background="#000000")
    conlabel.configure(disabledforeground="#a3a3a3")
    conlabel.configure(font="-family {Comic Sans MS} -size 20")
    conlabel.configure(foreground="#edbe00")
    conlabel.configure(text='''Queries''')

    Text1 = tk.Text(Frame3,wrap ='word')
    Text1.place(relx=0.027, rely=0.080, relheight=0.12, relwidth=0.944)
    Text1.configure(background="#211905")
    Text1.configure(font="-family {Comic Sans MS} -size 20")
    Text1.configure(foreground="#ffffff")
    Text1.configure(highlightbackground="#d9d9d9")
    Text1.configure(highlightcolor="black")
    Text1.configure(insertbackground="black")
    Text1.configure(selectbackground="#c4c4c4")
    Text1.configure(selectforeground="black")
    Text1.insert(INSERT,'CLICK QUERY NUMBER ABOVE TO SEE AND EXECUTE QUERY \n KEEP SMILING   :-)) ')

    Label3 = tk.Label(Frame3)
    Label3.place(relx=0.027, rely=0.19, height=40, relwidth=0.944)
    Label3.configure(background="#000000")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Comic Sans MS} -size 20")
    Label3.configure(foreground="#edbe00")
    Label3.configure(text='''MySQL Query Code''')

    Text2 = tk.Text(Frame3, wrap='word')
    Text2.place(relx=0.027, rely=0.26, relheight=0.24, relwidth=0.944)
    Text2.configure(background="#211905")
    Text2.configure(font="-family {Comic Sans MS} -size 20")
    Text2.configure(foreground="#ffffff")
    Text2.configure(highlightbackground="#d9d9d9")
    Text2.configure(highlightcolor="black")
    Text2.configure(insertbackground="black")
    Text2.configure(selectbackground="#c4c4c4")
    Text2.configure(selectforeground="black")
    Text2.insert(INSERT, 'Waiting for Question')

    Label3 = tk.Label(Frame3)
    Label3.place(relx=0.027, rely=0.50, height=40, relwidth=0.944)
    Label3.configure(background="#000000")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Comic Sans MS} -size 20")
    Label3.configure(foreground="#edbe00")
    Label3.configure(text='''Output''')

    Text3 = tk.Text(Frame3, wrap='word')
    Text3.place(relx=0.027, rely=0.57, relheight=0.40, relwidth=0.944)
    Text3.configure(background="#211905")
    Text3.configure(font="-family {Comic Sans MS} -size 20")
    Text3.configure(foreground="#ffffff")
    Text3.configure(highlightbackground="#d9d9d9")
    Text3.configure(highlightcolor="black")
    Text3.configure(insertbackground="black")
    Text3.configure(selectbackground="#c4c4c4")
    Text3.configure(selectforeground="black")
    Text3.insert(INSERT, 'Give me Some Question, I am Hungry')

    faqroot.mainloop()
    #Text1.delete(1.0, END)


if __name__ == "__main__":
    ALLFAQ()