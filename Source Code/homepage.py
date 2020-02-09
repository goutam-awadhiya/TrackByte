from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os.path
from datetime import datetime
from termcolor import colored
now =datetime.now()
nowstring = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowstring)
#### MYSQL LIBRARY ####
import mysql.connector

###### import other files and functions #######
#print '✓'

###### DATABASE #####
mydb = mysql.connector.connect(
    host='localhost',
    user='pycoders',
    passwd='gass',
    database='trackbyte'

)
mycursor = mydb.cursor()
uid = 1033
fname = 'Sparsh'

def importusername(username):

    global uid,fname
    sqlformula = 'select fname,uid from users where username = %s'
    mycursor.execute(sqlformula,(username,))
    fnamefetched = mycursor.fetchall()
    fname =fnamefetched[0][0]
    uid = fnamefetched[0][1]
    fname =fname.capitalize()


def Homepage():
    ###### see events #####
    def events():
        def gotohome():
            achroot.destroy()
            Homepage()
        homeroot.destroy()
        achroot = Tk()
        achroot.geometry("800x1001+711+10")
        achroot.title("Events")
        achroot.configure(background="#edbe00")

        topframe = tk.Frame(achroot)
        topframe.place(relx=0.0, rely=0.0, relheight=0.117, relwidth=1.0)
        topframe.configure(relief='groove')
        topframe.configure(borderwidth="2")
        topframe.configure(relief="groove")
        topframe.configure(background="black")

        tracklogolabel = tk.Label(topframe)
        tracklogolabel.place(relx=0.728, rely=-0.043, height=120, width=204)
        tracklogolabel.configure(background="#000000")
        tracklogolabel.configure(disabledforeground="#a3a3a3")
        tracklogolabel.configure(foreground="#000000")
        photo_location = os.path.join("logoSHORTNEW14.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        tracklogolabel.configure(image=_img0)
        tracklogolabel.configure(text='''Label''')

        achlogolabel = tk.Label(topframe)
        achlogolabel.place(relx=0.013, rely=0.087, height=104, width=104)
        achlogolabel.configure(background="#000000")
        achlogolabel.configure(disabledforeground="#a3a3a3")
        achlogolabel.configure(foreground="#000000")
        photo_location = os.path.join("goalach.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        achlogolabel.configure(image=_img1)
        achlogolabel.configure(text='''Label''')

        achheadlabel = tk.Label(topframe)
        achheadlabel.place(relx=0.146, rely=0.261, height=65, width=400)
        achheadlabel.configure(background="#000000")
        achheadlabel.configure(anchor='w')
        achheadlabel.configure(disabledforeground="#a3a3a3")
        achheadlabel.configure(font="-family {Comic Sans MS} -size 48 -weight bold ")
        achheadlabel.configure(foreground="#edbe00")
        achheadlabel.configure(text='''Events''')

        bottomframe = tk.Frame(achroot)
        bottomframe.place(relx=0.026, rely=0.13, relheight=0.834, relwidth=0.947)

        bottomframe.configure(relief='groove')
        bottomframe.configure(borderwidth="2")
        bottomframe.configure(relief="groove")
        bottomframe.configure(background="#000000")

        sumbitbutton = tk.Button(bottomframe)
        sumbitbutton.place(relx=0.35, rely=0.889, height=50, width=225)
        sumbitbutton.configure(activebackground="#ececec")
        sumbitbutton.configure(activeforeground="#000000")
        sumbitbutton.configure(background="#edbe00")
        sumbitbutton.configure(disabledforeground="#a3a3a3")
        sumbitbutton.configure(foreground="black")
        sumbitbutton.configure(font="-family {Comic Sans MS} -size 20")
        sumbitbutton.configure(highlightbackground="#d9d9d9")
        sumbitbutton.configure(highlightcolor="black")
        sumbitbutton.configure(pady="0")
        sumbitbutton.configure(text='''Go To Homepage''')
        sumbitbutton.configure(command=gotohome)


        sqlformula = 'select eid,ename,edate,etime,organiser,venue,city from events'
        mycursor.execute(sqlformula)
        allevents = mycursor.fetchall()
        allevents = list(allevents)
        headlist = ['    EID   ', '    Name   ', "     Date     ", "    Time     ", '      Organiser         ', '      Venue      ', '     City     ']
        allevents.insert(0,headlist)
        for i in range(len(allevents)):
            for j in range(len(allevents[i])):
                    emailabel = Label(bottomframe)
                    emailabel.grid(row = i,column = j)
                    emailabel.configure(background="#000000")  # 070707
                    emailabel.configure(disabledforeground="#a3a3a3")
                    emailabel.configure(font="-family {Comic Sans MS} -size 16")
                    emailabel.configure(foreground="white")
                    emailabel.configure(highlightcolor="#fc613a")
                    emailabel.configure(text=allevents[i][j])



        achroot.mainloop()


    ####### create events ######
    def createevent():

        def gotohome():
            createeventroot.destroy()
            Homepage()

        def saveevent():
            eventname = Eventname_entry.get()
            date = dateEntry.get()
            time = TimeEntry.get()
            organiser = OrganizerEntry.get()
            mobile1 = contact_entry1.get()
            mobile2 = contact_entry2.get()
            venue = venueEntry.get()
            city = cityEntry.get()

            eventdetail = (organiser,eventname,date,venue,city,time)
            print(eventdetail)
            sqlformula = 'insert into events (organiser,ename,edate,venue,city,etime) values (%s,%s,%s,%s,%s,%s)'
            mycursor.execute(sqlformula,eventdetail)
            mydb.commit()

            sqlformula = 'select eid from events where organiser = %s and ename = %s and venue = %s and city = %s'
            mycursor.execute(sqlformula,(organiser,eventname,venue,city))
            eid = mycursor.fetchall()
            eid = eid[0][0]
            print(eid)

            mobilenums = (mobile1, mobile2)
            for i in mobilenums:
                if i != '':
                    econtacttabledetails = (eid, i,)
                    sqlformula = 'insert into econtact(eid,mobile) values (%s,%s)'
                    mycursor.execute(sqlformula, econtacttabledetails)
                    mydb.commit()
            messagebox.showinfo("Congratulations", "Your Event Is Successfully Created\nSee Event in Event Section")
            createeventroot.destroy()
            Homepage()
        homeroot.destroy()
        createeventroot = tk.Tk();
        createeventroot.title("Home Page")
        createeventroot.geometry("755x1001+711+10")
        createeventroot.configure(background="#edbe00")
        createeventroot.resizable(FALSE, FALSE)

        Frame1 = tk.Frame(createeventroot)
        Frame1.place(relx=0.0, rely=0.0, relheight=0.105, relwidth=1.0)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="black")

        imglabel = tk.Label(Frame1)
        imglabel.place(relx=0.013, rely=0.095, height=89, width=89)
        imglabel.configure(background="#000000")
        imglabel.configure(disabledforeground="#a3a3a3")
        imglabel.configure(foreground="#000000")
        photo_location = os.path.join("create_events2.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        imglabel.configure(image=_img0)

        logoimg_label = tk.Label(Frame1)
        logoimg_label.place(relx=0.728, rely=0.0, height=100, width=204)
        logoimg_label.configure(background="black")
        logoimg_label.configure(disabledforeground="#a3a3a3")
        logoimg_label.configure(foreground="#000000")
        photo_location = os.path.join("logoSHORTNEW14.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        logoimg_label.configure(image=_img1)

        createvent_label = tk.Label(Frame1)
        createvent_label.place(relx=0.139, rely=0.0, height=86, width=350)
        createvent_label.configure(anchor='w')
        createvent_label.configure(background="#000000")
        createvent_label.configure(disabledforeground="#a3a3a3")
        createvent_label.configure(font="-family {Comic Sans MS} -size 40 -weight bold")
        createvent_label.configure(foreground="#edbe00")
        createvent_label.configure(text='''Create Event''')

        Frame2 = tk.Frame(createeventroot)
        Frame2.place(relx=0.026, rely=0.12, relheight=0.844, relwidth=0.947)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#000000")

        Eventname_Label = tk.Label(Frame2)
        Eventname_Label.place(relx=0.126, rely=0.03, height=40, width=163)
        Eventname_Label.configure(background="#000000")
        Eventname_Label.configure(disabledforeground="#a3a3a3")
        Eventname_Label.configure(font="-family {Comic Sans MS} -size 20 ")
        Eventname_Label.configure(foreground="#edbe00")
        Eventname_Label.configure(text='''Event Name :''')

        contact_Label1 = tk.Label(Frame2)
        contact_Label1.place(relx=0.126, rely=0.4068, height=40, width=180)
        contact_Label1.configure(activebackground="#f9f9f9")
        contact_Label1.configure(activeforeground="black")
        contact_Label1.configure(background="#000000")
        contact_Label1.configure(disabledforeground="#a3a3a3")
        contact_Label1.configure(font="-family {Comic Sans MS} -size 20")
        contact_Label1.configure(foreground="#edbe00")
        contact_Label1.configure(highlightbackground="#d9d9d9")
        contact_Label1.configure(highlightcolor="black")
        contact_Label1.configure(text='''Contact No.1 :''')

        contact_Label2 = tk.Label(Frame2)
        contact_Label2.place(relx=0.126, rely=0.501, height=40, width=180)
        contact_Label2.configure(activebackground="#f9f9f9")
        contact_Label2.configure(activeforeground="black")
        contact_Label2.configure(background="#000000")
        contact_Label2.configure(disabledforeground="#a3a3a3")
        contact_Label2.configure(font="-family {Comic Sans MS} -size 20")
        contact_Label2.configure(foreground="#edbe00")
        contact_Label2.configure(highlightbackground="#d9d9d9")
        contact_Label2.configure(highlightcolor="black")
        contact_Label2.configure(text='''Contact No.2 :''')

        venueLabel = tk.Label(Frame2)
        venueLabel.place(relx=0.168, rely=0.5952, height=40, width=103)
        venueLabel.configure(activebackground="#f9f9f9")
        venueLabel.configure(activeforeground="black")
        venueLabel.configure(background="#000000")
        venueLabel.configure(disabledforeground="#a3a3a3")
        venueLabel.configure(font="-family {Comic Sans MS} -size 20")
        venueLabel.configure(foreground="#edbe00")
        venueLabel.configure(highlightbackground="#d9d9d9")
        venueLabel.configure(highlightcolor="black")
        venueLabel.configure(text='''Venue :''')

        cityLabel = tk.Label(Frame2)
        cityLabel.place(relx=0.182, rely=0.69, height=40, width=83)
        cityLabel.configure(activebackground="#f9f9f9")
        cityLabel.configure(activeforeground="black")
        cityLabel.configure(background="#000000")
        cityLabel.configure(disabledforeground="#a3a3a3")
        cityLabel.configure(font="-family {Comic Sans MS} -size 20")
        cityLabel.configure(foreground="#edbe00")
        cityLabel.configure(highlightbackground="#d9d9d9")
        cityLabel.configure(highlightcolor="black")
        cityLabel.configure(text='''City :''')

        OrganizerLabel = tk.Label(Frame2)
        OrganizerLabel.place(relx=0.14, rely=0.3126, height=40, width=143)
        OrganizerLabel.configure(activebackground="#f9f9f9")
        OrganizerLabel.configure(activeforeground="black")
        OrganizerLabel.configure(background="#000000")
        OrganizerLabel.configure(disabledforeground="#a3a3a3")
        OrganizerLabel.configure(font="-family {Comic Sans MS} -size 20")
        OrganizerLabel.configure(foreground="#edbe00")
        OrganizerLabel.configure(highlightbackground="#d9d9d9")
        OrganizerLabel.configure(highlightcolor="black")
        OrganizerLabel.configure(text='''Organizer :''')

        TimeLabel = tk.Label(Frame2)
        TimeLabel.place(relx=0.182, rely=0.218, height=40, width=83)
        TimeLabel.configure(activebackground="#f9f9f9")
        TimeLabel.configure(activeforeground="black")
        TimeLabel.configure(background="#000000")
        TimeLabel.configure(disabledforeground="#a3a3a3")
        TimeLabel.configure(font="-family {Comic Sans MS} -size 20")
        TimeLabel.configure(foreground="#edbe00")
        TimeLabel.configure(highlightbackground="#d9d9d9")
        TimeLabel.configure(highlightcolor="black")
        TimeLabel.configure(text='''Time :''')

        dateLabel = tk.Label(Frame2)
        dateLabel.place(relx=0.182, rely=0.124, height=40, width=83)
        dateLabel.configure(activebackground="#f9f9f9")
        dateLabel.configure(activeforeground="black")
        dateLabel.configure(background="#000000")
        dateLabel.configure(disabledforeground="#a3a3a3")
        dateLabel.configure(font="-family {Comic Sans MS} -size 20")
        dateLabel.configure(foreground="#edbe00")
        dateLabel.configure(highlightbackground="#d9d9d9")
        dateLabel.configure(highlightcolor="black")
        dateLabel.configure(text='''Date :''')

        Eventname_entry = tk.Entry(Frame2)
        Eventname_entry.place(relx=0.413, rely=0.04, height=34, relwidth=0.400)
        Eventname_entry.configure(background="#211905")
        Eventname_entry.configure(disabledforeground="#a3a3a3")
        Eventname_entry.configure(font="-family {Comic Sans MS} -size 20")
        Eventname_entry.configure(foreground="white")
        Eventname_entry.configure(insertbackground="white")

        contact_entry1 = tk.Entry(Frame2)
        contact_entry1.place(relx=0.413, rely=0.4168, height=34, relwidth=0.400)
        contact_entry1.configure(background="#211905")
        contact_entry1.configure(disabledforeground="#a3a3a3")
        contact_entry1.configure(font="-family {Comic Sans MS} -size 20")
        contact_entry1.configure(foreground="white")
        contact_entry1.configure(highlightbackground="#d9d9d9")
        contact_entry1.configure(highlightcolor="black")
        contact_entry1.configure(insertbackground="white")
        contact_entry1.configure(selectbackground="#c4c4c4")
        contact_entry1.configure(selectforeground="black")

        contact_entry2 = tk.Entry(Frame2)
        contact_entry2.place(relx=0.42, rely=0.511, height=34, relwidth=0.400)
        contact_entry2.configure(background="#211905")
        contact_entry2.configure(disabledforeground="#a3a3a3")
        contact_entry2.configure(font="-family {Comic Sans MS} -size 20")
        contact_entry2.configure(foreground="white")
        contact_entry2.configure(highlightbackground="#d9d9d9")
        contact_entry2.configure(highlightcolor="black")
        contact_entry2.configure(insertbackground="white")
        contact_entry2.configure(selectbackground="#c4c4c4")
        contact_entry2.configure(selectforeground="black")

        venueEntry = tk.Entry(Frame2)
        venueEntry.place(relx=0.413, rely=0.6052, height=34, relwidth=0.400)
        venueEntry.configure(background="#211905")
        venueEntry.configure(disabledforeground="#a3a3a3")
        venueEntry.configure(font="-family {Comic Sans MS} -size 20")
        venueEntry.configure(foreground="white")
        venueEntry.configure(highlightbackground="#d9d9d9")
        venueEntry.configure(highlightcolor="black")
        venueEntry.configure(insertbackground="white")
        venueEntry.configure(selectbackground="#c4c4c4")
        venueEntry.configure(selectforeground="black")

        cityEntry = tk.Entry(Frame2)
        cityEntry.place(relx=0.413, rely=0.7, height=34, relwidth=0.400)
        cityEntry.configure(background="#211905")
        cityEntry.configure(disabledforeground="#a3a3a3")
        cityEntry.configure(font="-family {Comic Sans MS} -size 20")
        cityEntry.configure(foreground="white")
        cityEntry.configure(highlightbackground="#d9d9d9")
        cityEntry.configure(highlightcolor="black")
        cityEntry.configure(insertbackground="white")
        cityEntry.configure(selectbackground="#c4c4c4")
        cityEntry.configure(selectforeground="black")

        OrganizerEntry = tk.Entry(Frame2)
        OrganizerEntry.place(relx=0.413, rely=0.3226, height=34, relwidth=0.400)
        OrganizerEntry.configure(background="#211905")
        OrganizerEntry.configure(disabledforeground="#a3a3a3")
        OrganizerEntry.configure(font="-family {Comic Sans MS} -size 20")
        OrganizerEntry.configure(foreground="white")
        OrganizerEntry.configure(highlightbackground="#d9d9d9")
        OrganizerEntry.configure(highlightcolor="black")
        OrganizerEntry.configure(insertbackground="white")
        OrganizerEntry.configure(selectbackground="#c4c4c4")
        OrganizerEntry.configure(selectforeground="black")

        TimeEntry = tk.Entry(Frame2)
        TimeEntry.place(relx=0.413, rely=0.228, height=34, relwidth=0.400)
        TimeEntry.configure(background="#211905")
        TimeEntry.configure(disabledforeground="#a3a3a3")
        TimeEntry.configure(font="-family {Comic Sans MS} -size 20")
        TimeEntry.configure(foreground="white")
        TimeEntry.configure(highlightbackground="#d9d9d9")
        TimeEntry.configure(highlightcolor="black")
        TimeEntry.configure(insertbackground="white")
        TimeEntry.configure(selectbackground="#c4c4c4")
        TimeEntry.configure(selectforeground="black")

        dateEntry = tk.Entry(Frame2)
        dateEntry.place(relx=0.413, rely=0.134, height=34, relwidth=0.400)
        dateEntry.configure(background="#211905")
        dateEntry.configure(disabledforeground="#a3a3a3")
        dateEntry.configure(font="-family {Comic Sans MS} -size 20")
        dateEntry.configure(foreground="white")
        dateEntry.configure(highlightbackground="#d9d9d9")
        dateEntry.configure(highlightcolor="black")
        dateEntry.configure(insertbackground="white")
        dateEntry.configure(selectbackground="#c4c4c4")
        dateEntry.configure(selectforeground="black")

        savebutton = tk.Button(Frame2)
        savebutton.place(relx=0.37, rely=0.8, height=55, width=100)
        savebutton.configure(activebackground="#ececec")
        savebutton.configure(activeforeground="#000000")
        savebutton.configure(background="#edbe00")
        savebutton.configure(disabledforeground="#a3a3a3")
        savebutton.configure(font="-family {Comic Sans MS} -size 25 ")
        savebutton.configure(foreground="#000000")
        savebutton.configure(highlightbackground="#d9d9d9")
        savebutton.configure(highlightcolor="black")
        savebutton.configure(pady="0")
        savebutton.configure(text='''Save''')
        savebutton.configure(command = saveevent)

        homePageButton = tk.Button(Frame2)
        homePageButton.place(relx=0.240, rely=0.91, height=55, width=300)
        homePageButton.configure(activebackground="#ececec")
        homePageButton.configure(activeforeground="#000000")
        homePageButton.configure(background="#edbe00")
        homePageButton.configure(disabledforeground="#a3a3a3")
        homePageButton.configure(font="-family {Comic Sans MS} -size 25 ")
        homePageButton.configure(foreground="#000000")
        homePageButton.configure(highlightbackground="#d9d9d9")
        homePageButton.configure(highlightcolor="black")
        homePageButton.configure(pady="0")
        homePageButton.configure(text='''Go To Home Page''')
        homePageButton.configure(command = gotohome)

        createeventroot.mainloop()

    ######## achieved goals ####
    def goalachieved():

        def gotohome():
            achroot.destroy()
            Homepage()
        homeroot.destroy()
        achroot = Tk()
        achroot.geometry("800x1001+711+10")
        achroot.title("New Toplevel")
        achroot.configure(background="#edbe00")

        topframe = tk.Frame(achroot)
        topframe.place(relx=0.0, rely=0.0, relheight=0.117, relwidth=1.0)
        topframe.configure(relief='groove')
        topframe.configure(borderwidth="2")
        topframe.configure(relief="groove")
        topframe.configure(background="black")

        tracklogolabel = tk.Label(topframe)
        tracklogolabel.place(relx=0.728, rely=-0.043, height=120, width=204)
        tracklogolabel.configure(background="#000000")
        tracklogolabel.configure(disabledforeground="#a3a3a3")
        tracklogolabel.configure(foreground="#000000")
        photo_location = os.path.join("logoSHORTNEW14.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        tracklogolabel.configure(image=_img0)
        tracklogolabel.configure(text='''Label''')

        achlogolabel = tk.Label(topframe)
        achlogolabel.place(relx=0.013, rely=0.087, height=104, width=104)
        achlogolabel.configure(background="#000000")
        achlogolabel.configure(disabledforeground="#a3a3a3")
        achlogolabel.configure(foreground="#000000")
        photo_location = os.path.join("goalach.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        achlogolabel.configure(image=_img1)
        achlogolabel.configure(text='''Label''')

        achheadlabel = tk.Label(topframe)
        achheadlabel.place(relx=0.146, rely=0.261, height=65, width=400)
        achheadlabel.configure(background="#000000")
        achheadlabel.configure(anchor='w')
        achheadlabel.configure(disabledforeground="#a3a3a3")
        achheadlabel.configure(font="-family {Comic Sans MS} -size 40 -weight bold ")
        achheadlabel.configure(foreground="#edbe00")
        achheadlabel.configure(text='''Achieved Goals''')

        bottomframe = tk.Frame(achroot)
        bottomframe.place(relx=0.026, rely=0.13, relheight=0.834, relwidth=0.947)

        bottomframe.configure(relief='groove')
        bottomframe.configure(borderwidth="2")
        bottomframe.configure(relief="groove")
        bottomframe.configure(background="#000000")

        sumbitbutton = tk.Button(bottomframe)
        sumbitbutton.place(relx=0.35, rely=0.889, height=50, width=225)
        sumbitbutton.configure(activebackground="#ececec")
        sumbitbutton.configure(activeforeground="#000000")
        sumbitbutton.configure(background="#edbe00")
        sumbitbutton.configure(disabledforeground="#a3a3a3")
        sumbitbutton.configure(foreground="black")
        sumbitbutton.configure(font="-family {Comic Sans MS} -size 20")
        sumbitbutton.configure(highlightbackground="#d9d9d9")
        sumbitbutton.configure(highlightcolor="black")
        sumbitbutton.configure(pady="0")
        sumbitbutton.configure(text='''Go To Homepage''')
        sumbitbutton.configure(command=gotohome)



        sqlformula = 'select uid,steps,distance,calories,sleep,water,floor,weight from setgoals where uid  = %s'
        mycursor.execute(sqlformula,(uid,))
        goallist = mycursor.fetchall()
        print(goallist)


        sqlformula = 'select uid,activitydate,steps,distance,calories,sleep,water,floors,weight from activities where uid = %s group by activitydate order by activitydate '
        mycursor.execute(sqlformula,(uid,))
        allactivities = mycursor.fetchall()
        print(allactivities)
        sqlformula = 'select round(avg(steps),2),round(avg(distance),2),round(avg(calories),2),round(avg(sleep),2),round(avg(water),2),round(avg(floors),2),round(avg(weight),2)  from activities where uid = %s'
        mycursor.execute(sqlformula,(uid,))
        avglist = mycursor.fetchall()
        avglist = list(avglist[0])
        print(avglist)
        avglist.insert(0,'Average')
        print(avglist)
        #print(allactivities)
        justdate = str(allactivities[0][1])[0:10]
        reallist = []
        for i in allactivities:
            i = list(i)
            i.remove(uid)
            i[0]=str(i[0])[0:10]
            reallist.append(i)
        headlist = ['  Date  ', '   Steps  ', "  Distance  ", " Calories  ", ' Sleep  ', ' Water  ', ' Floor  ', " Weight  "]
        reallist.insert(0,headlist)
        reallist.append(['---------','-----','-----','-----','-----','-----','-----','-----'])
        print(reallist)
        reallist.append(avglist)
        print(reallist)
        print(len(reallist))
        print(len(goallist))
        print(reallist)
        for i in range(len(reallist)):
            for j in range(len(reallist[i])):
                if j == 0 or i ==0 or (i == len(reallist)-1 and j == 0) or i== len(reallist)-2:
                    emailabel = Label(bottomframe)
                    emailabel.grid(row = i,column = j)
                    emailabel.configure(background="#000000")  # 070707
                    emailabel.configure(disabledforeground="#a3a3a3")
                    emailabel.configure(font="-family {Comic Sans MS} -size 16")
                    emailabel.configure(foreground="white")
                    emailabel.configure(highlightcolor="#fc613a")
                    emailabel.configure(text=reallist[i][j])
                elif j == len(reallist[i])-1:
                    emailabel = Label(bottomframe)
                    emailabel.grid(row=i, column=j)
                    emailabel.configure(background="#000000")  # 070707
                    emailabel.configure(disabledforeground="#a3a3a3")
                    emailabel.configure(font="-family {Comic Sans MS} -size 16")
                    emailabel.configure(highlightcolor="#fc613a")
                    emailabel.configure(text=reallist[i][j])
                    if float(reallist[i][j]) <= float(goallist[0][j]):
                        emailabel.configure(foreground="#edbe00")
                    else:
                        emailabel.configure(foreground='white')
                else:
                    emailabel = Label(bottomframe)
                    emailabel.grid(row=i, column=j)
                    emailabel.configure(background="#000000")  # 070707
                    emailabel.configure(disabledforeground="#a3a3a3")
                    emailabel.configure(font="-family {Comic Sans MS} -size 16")
                    emailabel.configure(highlightcolor="#fc613a")
                    emailabel.configure(text=reallist[i][j])
                    if float(reallist[i][j]) >= float(goallist[0][j]):
                        emailabel.configure(foreground="#edbe00")
                    else:
                        emailabel.configure(foreground = 'white')



        achroot.mainloop()

    ####### set goals ######
    def setgoals():
        def gotohome():
            setroot.destroy()
            Homepage()

        def insertgoals():
            useruid = uid
            steps = stepentry.get()
            distance = entrydistance.get()#distanceentry.get()
            calorie = entrycalorie.get()##calorieentry.get()
            sleep = entrysleep.get()#floorentry.get()#sleepentry.get()
            floor =entryfloor.get() #floorentry.get()
            water = entrywater.get()#waterentry.get()
            weight =entryweight.get() #weightentry.get()
            goaltuple = (useruid,steps,distance,calorie,sleep,water,floor,weight)
            print(goaltuple)
            sqlformula = "delete from setgoals where uid = %s"
            mycursor.execute(sqlformula,(uid,))
            sqlformula = 'insert into setgoals (uid,steps,distance,calories,sleep,water,floor,weight) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            print(goaltuple)
            mycursor.execute(sqlformula,goaltuple)
            mydb.commit()
            messagebox.showinfo("Success","You Goals are Ready to Achieve")


        homeroot.destroy()
        setroot = Tk()
        setroot.geometry("755x1001+710+10")
        setroot.title("New Toplevel")
        setroot.configure(background="#edbe00")

        sqlformula = 'select steps,distance,calories,sleep,water,floor,weight from setgoals where uid =%s'
        mycursor.execute(sqlformula,(uid,))
        goals =  mycursor.fetchall()
        if len(goals) == 0:
            goals.append([0 for i in range (7)])
        print(goals)


        topframe = tk.Frame(setroot)
        topframe.place(relx=0.0, rely=0.0, relheight=0.115, relwidth=1.0)
        topframe.configure(relief='groove')
        topframe.configure(borderwidth="2")
        topframe.configure(relief="groove")
        topframe.configure(background="#000000")

        targetlabel = tk.Label(topframe)
        targetlabel.place(relx=0.013, rely=0.0, height=106, width=112)
        targetlabel.configure(background="#000000")
        targetlabel.configure(disabledforeground="#a3a3a3")
        targetlabel.configure(foreground="white")
        photo_location = os.path.join("target1.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        targetlabel.configure(image=_img0)
        targetlabel.configure(text='''Label''')

        tracklogo = tk.Label(topframe)
        tracklogo.place(relx=0.748, rely=0.0, height=106, width=200)
        tracklogo.configure(background="#d9d9d9")
        tracklogo.configure(disabledforeground="#a3a3a3")
        tracklogo.configure(foreground="white")
        photo_location = os.path.join("logoSHORTNEW14.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        tracklogo.configure(image=_img1)
        tracklogo.configure(text='''Label''')

        setgolslabel = tk.Label(topframe)
        setgolslabel.place(relx=0.146, rely=0.150, height=86, width=400)
        setgolslabel.configure(anchor='w')
        setgolslabel.configure(background="#000000")
        setgolslabel.configure(disabledforeground="#a3a3a3")
        setgolslabel.configure(font="-family {Comic Sans MS} -size 54 -weight bold ")
        setgolslabel.configure(foreground="#edbe00")
        setgolslabel.configure(text='''Set Goals !''')

        bottomframe = tk.Frame(setroot)
        bottomframe.place(relx=0.026, rely=0.125, relheight=0.834
                          , relwidth=0.947)
        bottomframe.configure(relief='groove')
        bottomframe.configure(borderwidth="2")
        bottomframe.configure(relief="groove")
        bottomframe.configure(background="#000000")

        stepslabel = tk.Label(bottomframe)
        stepslabel.place(relx=0.196, rely=0.06, height=46, width=152)
        stepslabel.configure(anchor='w')
        stepslabel.configure(background="#000000")
        stepslabel.configure(disabledforeground="#a3a3a3")
        stepslabel.configure(font="-family {Comic Sans MS} -size 18")
        stepslabel.configure(foreground="#EDBE00")
        stepslabel.configure(text='''Steps :''')

        floorlabel = tk.Label(bottomframe)
        floorlabel.place(relx=0.224, rely=0.551, height=46, width=152)
        floorlabel.configure(activebackground="#f9f9f9")
        floorlabel.configure(activeforeground="black")
        floorlabel.configure(anchor='w')
        floorlabel.configure(background="#000000")
        floorlabel.configure(disabledforeground="#a3a3a3")
        floorlabel.configure(font="-family {Comic Sans MS} -size 18")
        floorlabel.configure(foreground="#EDBE00")
        floorlabel.configure(highlightbackground="#d9d9d9")
        floorlabel.configure(highlightcolor="black")
        floorlabel.configure(text='''Floor :''')

        waterlabel = tk.Label(bottomframe)
        waterlabel.place(relx=0.154, rely=0.455, height=46, width=192)
        waterlabel.configure(activebackground="#f9f9f9")
        waterlabel.configure(activeforeground="black")
        waterlabel.configure(anchor='w')
        waterlabel.configure(background="#000000")
        waterlabel.configure(disabledforeground="#a3a3a3")
        waterlabel.configure(font="-family {Comic Sans MS} -size 18")
        waterlabel.configure(foreground="#EDBE00")
        waterlabel.configure(highlightbackground="#d9d9d9")
        waterlabel.configure(highlightcolor="black")
        waterlabel.configure(text='''Water (Ltr) :''')

        weightlabel = tk.Label(bottomframe)
        weightlabel.place(relx=0.182, rely=0.647, height=46, width=172)
        weightlabel.configure(activebackground="#f9f9f9")
        weightlabel.configure(activeforeground="black")
        weightlabel.configure(anchor='w')
        weightlabel.configure(background="#000000")
        weightlabel.configure(disabledforeground="#a3a3a3")
        weightlabel.configure(font="-family {Comic Sans MS} -size 18")
        weightlabel.configure(foreground="#EDBE00")
        weightlabel.configure(highlightbackground="#d9d9d9")
        weightlabel.configure(highlightcolor="black")
        weightlabel.configure(text='''Weight (kg)  :''')

        sleeplabel = tk.Label(bottomframe)
        sleeplabel.place(relx=0.168, rely=0.359, height=46, width=162)
        sleeplabel.configure(activebackground="#f9f9f9")
        sleeplabel.configure(activeforeground="black")
        sleeplabel.configure(anchor='w')
        sleeplabel.configure(background="#000000")
        sleeplabel.configure(disabledforeground="#a3a3a3")
        sleeplabel.configure(font="-family {Comic Sans MS} -size 18")
        sleeplabel.configure(foreground="#EDBE00")
        sleeplabel.configure(highlightbackground="#d9d9d9")
        sleeplabel.configure(highlightcolor="black")
        sleeplabel.configure(text='''Sleep Hours :''')

        calorieslabel = tk.Label(bottomframe)
        calorieslabel.place(relx=0.154, rely=0.263, height=46, width=192)
        calorieslabel.configure(activebackground="#f9f9f9")
        calorieslabel.configure(activeforeground="black")
        calorieslabel.configure(anchor='w')
        calorieslabel.configure(background="#000000")
        calorieslabel.configure(disabledforeground="#a3a3a3")
        calorieslabel.configure(font="-family {Comic Sans MS} -size 18")
        calorieslabel.configure(foreground="#EDBE00")
        calorieslabel.configure(highlightbackground="#d9d9d9")
        calorieslabel.configure(highlightcolor="black")
        calorieslabel.configure(text='''Calories Burnt :''')

        distancelabel = tk.Label(bottomframe)
        distancelabel.place(relx=0.154, rely=0.168, height=46, width=200)
        distancelabel.configure(activebackground="#f9f9f9")
        distancelabel.configure(activeforeground="black")
        distancelabel.configure(anchor='w')
        distancelabel.configure(background="#000000")
        distancelabel.configure(disabledforeground="#a3a3a3")
        distancelabel.configure(font="-family {Comic Sans MS} -size 18")
        distancelabel.configure(foreground="#EDBE00")
        distancelabel.configure(highlightbackground="#d9d9d9")
        distancelabel.configure(highlightcolor="black")
        distancelabel.configure(text='''Distance (km) :''')

        stepentry = tk.Entry(bottomframe)
        stepentry.place(relx=0.476, rely=0.072, height=34, relwidth=0.285)
        stepentry.configure(background="#211905")
        stepentry.configure(disabledforeground="#a3a3a3")
        stepentry.configure(font="-family {Comic Sans MS} -size 15")
        stepentry.configure(foreground="white")
        stepentry.configure(insertbackground="white")
        stepentry.insert(0,goals[0][0])

        entryweight = tk.Entry(bottomframe)
        entryweight.place(relx=0.476, rely=0.659, height=34, relwidth=0.285)
        entryweight.configure(background="#211905")
        entryweight.configure(disabledforeground="#a3a3a3")
        entryweight.configure(font="-family {Comic Sans MS} -size 15")
        entryweight.configure(foreground="white")
        entryweight.configure(highlightbackground="#d9d9d9")
        entryweight.configure(highlightcolor="black")
        entryweight.configure(insertbackground="white")
        entryweight.configure(selectbackground="#c4c4c4")
        entryweight.configure(selectforeground="black")
        entryweight.insert(0,goals[0][6])
        entryfloor = tk.Entry(bottomframe)
        entryfloor.place(relx=0.476, rely=0.563, height=34, relwidth=0.285)
        entryfloor.configure(background="#211905")
        entryfloor.configure(disabledforeground="#a3a3a3")
        entryfloor.configure(font="-family {Comic Sans MS} -size 15")
        entryfloor.configure(foreground="white")
        entryfloor.configure(highlightbackground="#d9d9d9")
        entryfloor.configure(highlightcolor="black")
        entryfloor.configure(insertbackground="white")
        entryfloor.configure(selectbackground="#c4c4c4")
        entryfloor.configure(selectforeground="black")
        entryfloor.insert(0,5)

        entrywater = tk.Entry(bottomframe)
        entrywater.place(relx=0.476, rely=0.467, height=34, relwidth=0.285)
        entrywater.configure(background="#211905")
        entrywater.configure(disabledforeground="#a3a3a3")
        entrywater.configure(font="-family {Comic Sans MS} -size 15")
        entrywater.configure(foreground="white")
        entrywater.configure(highlightbackground="#d9d9d9")
        entrywater.configure(highlightcolor="black")
        entrywater.configure(insertbackground="white")
        entrywater.configure(selectbackground="#c4c4c4")
        entrywater.configure(selectforeground="black")
        entrywater.insert(0,goals[0][4])

        entrysleep = tk.Entry(bottomframe)
        entrysleep.place(relx=0.476, rely=0.371, height=34, relwidth=0.285)
        entrysleep.configure(background="#211905")
        entrysleep.configure(disabledforeground="#a3a3a3")
        entrysleep.configure(font="-family {Comic Sans MS} -size 15")
        entrysleep.configure(foreground="white")
        entrysleep.configure(highlightbackground="#d9d9d9")
        entrysleep.configure(highlightcolor="black")
        entrysleep.configure(insertbackground="white")
        entrysleep.configure(selectbackground="#c4c4c4")
        entrysleep.configure(selectforeground="black")
        entrysleep.insert(0,goals[0][3])

        entrycalorie = tk.Entry(bottomframe)
        entrycalorie.place(relx=0.476, rely=0.275, height=34, relwidth=0.285)
        entrycalorie.configure(background="#211905")
        entrycalorie.configure(disabledforeground="#a3a3a3")
        entrycalorie.configure(font="-family {Comic Sans MS} -size 15")
        entrycalorie.configure(foreground="white")
        entrycalorie.configure(highlightbackground="#d9d9d9")
        entrycalorie.configure(highlightcolor="black")
        entrycalorie.configure(insertbackground="white")
        entrycalorie.configure(selectbackground="#c4c4c4")
        entrycalorie.configure(selectforeground="black")
        entrycalorie.insert(0,goals[0][2])

        entrydistance = tk.Entry(bottomframe)
        entrydistance.place(relx=0.476, rely=0.18, height=34, relwidth=0.285)
        entrydistance.configure(background="#211905")
        entrydistance.configure(disabledforeground="#a3a3a3")
        entrydistance.configure(font="-family {Comic Sans MS} -size 15")
        entrydistance.configure(foreground="white")
        entrydistance.configure(highlightbackground="#d9d9d9")
        entrydistance.configure(highlightcolor="black")
        entrydistance.configure(insertbackground="white")
        entrydistance.configure(selectbackground="#c4c4c4")
        entrydistance.configure(selectforeground="black")
        entrydistance.insert(0,goals[0][1])

        homebutton = tk.Button(bottomframe)
        homebutton.place(relx=0.224, rely=0.874, height=50, width=357)
        homebutton.configure(activebackground="#ececec")
        homebutton.configure(activeforeground="white")
        homebutton.configure(background="#EDBE00")
        homebutton.configure(disabledforeground="#a3a3a3")
        homebutton.configure(font="-family {Comic Sans MS} -size 20")
        homebutton.configure(foreground="black")
        homebutton.configure(highlightbackground="#d9d9d9")
        homebutton.configure(highlightcolor="black")
        homebutton.configure(pady="0")
        homebutton.configure(text='''Go Back to Home Page''')
        homebutton.configure(command = gotohome)

        setgoalbutton = tk.Button(bottomframe)
        setgoalbutton.place(relx=0.364, rely=0.766, height=50, width=147)
        setgoalbutton.configure(activebackground="#ececec")
        setgoalbutton.configure(activeforeground="white")
        setgoalbutton.configure(background="#EDBE00")
        setgoalbutton.configure(disabledforeground="#a3a3a3")
        setgoalbutton.configure(font="-family {Comic Sans MS} -size 18 ")
        setgoalbutton.configure(foreground="black")
        setgoalbutton.configure(highlightbackground="#d9d9d9")
        setgoalbutton.configure(highlightcolor="black")
        setgoalbutton.configure(pady="0")
        setgoalbutton.configure(text='''Set Goals''')
        setgoalbutton.configure(command =insertgoals)

        setroot.mainloop()

    ####### activity section
    def activity():
        #### get date and time ######
        now = datetime.now()
        nowstring = now.strftime("%Y-%m-%d %H:%M:%S")
        print(uid)

        def gotohome():
            activityroot.destroy()
            Homepage()

        def enteractivity():
            date =dateentry.get()
            steps = stepentry.get()
            distance = distanceentry.get()
            calories = calorieentry.get()
            bp = bpentry.get()
            sleep= sleepentry.get()
            water = waterentry.get()
            floor = floorentry.get()
            weight = weightentry.get()
            activitylist = (uid,date,steps,distance,calories,bp,sleep,water,floor,weight)
            sqlformula = 'insert into activities (uid,activitydate,steps,distance,calories,BP,sleep,water,floors,weight) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(sqlformula,activitylist)
            mydb.commit()
            messagebox.showinfo("SUCCESS","Your data is inserted successfully \n Keep Tracking Bit to Byte:-)) ")


        homeroot.destroy()
        activityroot = Tk()
        activityroot.geometry("755x1001+711+10")
        activityroot.title("Enter Activity")
        activityroot.configure(background="#edbe00")

        topframe = tk.Frame(activityroot)
        topframe.place(relx=0.0, rely=0.0, relheight=0.115, relwidth=1.013)
        topframe.configure(relief='groove')
        topframe.configure(borderwidth="2")
        topframe.configure(relief="groove")
        topframe.configure(background="#000000")

        activityicn = tk.Label(topframe)
        activityicn.place(relx=0.0, rely=0.087, height=101, width=124)
        activityicn.configure(background="#000000")
        activityicn.configure(disabledforeground="#a3a3a3")
        activityicn.configure(foreground="#000000")
        photo_location = os.path.join("activity0-200.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        activityicn.configure(image=_img0)
        activityicn.configure(text='''Label''')

        tracklabel = tk.Label(topframe)
        tracklabel.place(relx=0.732, rely=0.087, height=101, width=194)
        tracklabel.configure(background="#d9d9d9")
        tracklabel.configure(disabledforeground="#a3a3a3")
        tracklabel.configure(foreground="#000000")
        photo_location = os.path.join("logoSHORTNEW14.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        tracklabel.configure(image=_img1)
        tracklabel.configure(text='''Label''')

        enteractivitylabel = tk.Label(topframe)
        enteractivitylabel.place(relx=0.17, rely=0.174, height=91, width=394)
        enteractivitylabel.configure(anchor='w')
        enteractivitylabel.configure(background="#000000")
        enteractivitylabel.configure(disabledforeground="#a3a3a3")
        enteractivitylabel.configure(font="-family {Comic Sans MS} -size 40")
        enteractivitylabel.configure(foreground="#edbe00")
        enteractivitylabel.configure(text='''Enter Activity''')

        bottomframe = tk.Frame(activityroot)
        bottomframe.place(relx=0.013, rely=0.13, relheight=0.854, relwidth=0.96)
        bottomframe.configure(relief='groove')
        bottomframe.configure(borderwidth="2")
        bottomframe.configure(relief="groove")
        bottomframe.configure(background="#000000")

        datelabel = tk.Label(bottomframe)
        datelabel.place(relx = 0.08, rely=0.023, height=51, width=230)
        datelabel.configure(background="black")
        datelabel.configure(font = "-family {Comic Sans MS} -size 20")
        datelabel.configure(disabledforeground="#a3a3a3")
        datelabel.configure(foreground="#edbe00")
        datelabel.configure(text='''Date :''')

        steplabel = tk.Label(bottomframe)
        steplabel.place(relx = 0.08, rely=0.117, height=51, width=230)
        steplabel.configure(activebackground="#f9f9f9")
        steplabel.configure(activeforeground="black")
        steplabel.configure(background="black")
        steplabel.configure(font = "-family {Comic Sans MS} -size 20")
        steplabel.configure(disabledforeground="#a3a3a3")
        steplabel.configure(foreground="#edbe00")
        steplabel.configure(highlightbackground="#d9d9d9")
        steplabel.configure(highlightcolor="black")
        steplabel.configure(text='''Steps :''')

        distancelabel= tk.Label(bottomframe)
        distancelabel.place(relx = 0.08, rely=0.211, height=51, width=230)
        distancelabel.configure(font = "-family {Comic Sans MS} -size 20")
        distancelabel.configure(activebackground="#f9f9f9")
        distancelabel.configure(activeforeground="black")
        distancelabel.configure(background="black")
        distancelabel.configure(disabledforeground="#a3a3a3")
        distancelabel.configure(foreground="#edbe00")
        distancelabel.configure(highlightbackground="#d9d9d9")
        distancelabel.configure(highlightcolor="black")
        distancelabel.configure(text='''Distance (Km) :''')

        calorieslabel = tk.Label(bottomframe)
        calorieslabel.place(relx = 0.08, rely=0.304, height=51, width=230)
        calorieslabel.configure(activebackground="#f9f9f9")
        calorieslabel.configure(activeforeground="black")
        calorieslabel.configure(background="black")
        calorieslabel.configure(disabledforeground="#a3a3a3")
        calorieslabel.configure(foreground="#edbe00")
        calorieslabel.configure(font = "-family {Comic Sans MS} -size 20")
        calorieslabel.configure(highlightbackground="#d9d9d9")
        calorieslabel.configure(highlightcolor="black")
        calorieslabel.configure(text='''Calories Burned :''')

        bplabel = tk.Label(bottomframe)
        bplabel.place(relx = 0.08, rely=0.398, height=51, width=230)
        bplabel.configure(activebackground="#f9f9f9")
        bplabel.configure(activeforeground="black")
        bplabel.configure(background="black")
        bplabel.configure(font = "-family {Comic Sans MS} -size 20")
        bplabel.configure(disabledforeground="#a3a3a3")
        bplabel.configure(foreground="#edbe00")
        bplabel.configure(highlightbackground="#d9d9d9")
        bplabel.configure(highlightcolor="black")
        bplabel.configure(text='''BP Level :''')

        sleeplabel = tk.Label(bottomframe)
        sleeplabel.place(relx = 0.08, rely=0.491, height=51, width=230)
        sleeplabel.configure(activebackground="#f9f9f9")
        sleeplabel.configure(activeforeground="black")
        sleeplabel.configure(background="black")
        sleeplabel.configure(disabledforeground="#a3a3a3")
        sleeplabel.configure(foreground="#edbe00")
        sleeplabel.configure(font = "-family {Comic Sans MS} -size 20")
        sleeplabel.configure(highlightbackground="#d9d9d9")
        sleeplabel.configure(highlightcolor="black")
        sleeplabel.configure(text='''Sleep (Hrs) :''')

        Waterlabel = tk.Label(bottomframe)
        Waterlabel.place(relx = 0.08, rely=0.585, height=51, width=230)
        Waterlabel.configure(activebackground="#f9f9f9")
        Waterlabel.configure(activeforeground="black")
        Waterlabel.configure(background="black")
        Waterlabel.configure(disabledforeground="#a3a3a3")
        Waterlabel.configure(foreground="#edbe00")
        Waterlabel.configure(font = "-family {Comic Sans MS} -size 20")
        Waterlabel.configure(highlightbackground="#d9d9d9")
        Waterlabel.configure(highlightcolor="black")
        Waterlabel.configure(text='''Water (Ltr) ''')

        floorlabel = tk.Label(bottomframe)
        floorlabel.place(relx = 0.08, rely=0.678, height=51, width=230)
        floorlabel.configure(activebackground="#f9f9f9")
        floorlabel.configure(activeforeground="black")
        floorlabel.configure(background="black")
        floorlabel.configure(disabledforeground="#a3a3a3")
        floorlabel.configure(foreground="#edbe00")
        floorlabel.configure(font = "-family {Comic Sans MS} -size 20")
        floorlabel.configure(highlightbackground="#d9d9d9")
        floorlabel.configure(highlightcolor="black")
        floorlabel.configure(text='''Floor :''')

        wweightlabel = tk.Label(bottomframe)
        wweightlabel.place(relx = 0.08, rely=0.784, height=51, width=230)
        wweightlabel.configure(activebackground="#f9f9f9")
        wweightlabel.configure(activeforeground="black")
        wweightlabel.configure(background="black")
        wweightlabel.configure(font = "-family {Comic Sans MS} -size 20")
        wweightlabel.configure(disabledforeground="#a3a3a3")
        wweightlabel.configure(foreground="#edbe00")
        wweightlabel.configure(highlightbackground="#d9d9d9")
        wweightlabel.configure(highlightcolor="black")
        wweightlabel.configure(text='''Weight (Kg) :''')

        dateentry = tk.Entry(bottomframe)
        dateentry.place(relx = 0.5, rely=0.023, height=50, relwidth=0.300)
        dateentry.configure(background="#211905")
        dateentry.configure(disabledforeground="#a3a3a3")
        dateentry.configure(font="-family {Comic Sans MS} -size 16 ")
        dateentry.configure(foreground="white")
        dateentry.configure(insertbackground="white")
        dateentry.insert(0,nowstring[0:10])

        stepentry = tk.Entry(bottomframe)
        stepentry.place(relx = 0.5, rely=0.117, height=50, relwidth=0.300)
        stepentry.configure(background="#211905")
        stepentry.configure(disabledforeground="#a3a3a3")
        stepentry.configure(font="-family {Comic Sans MS} -size 20")
        stepentry.configure(foreground="white")
        stepentry.configure(highlightbackground="#d9d9d9")
        stepentry.configure(highlightcolor="black")
        stepentry.configure(insertbackground="white")
        stepentry.configure(selectbackground="#c4c4c4")
        stepentry.configure(selectforeground="black")

        distanceentry = tk.Entry(bottomframe)
        distanceentry.place(relx = 0.5, rely=0.211, height=50, relwidth=0.300)
        distanceentry.configure(background="#211905")
        distanceentry.configure(disabledforeground="#a3a3a3")
        distanceentry.configure(font="-family {Comic Sans MS} -size 20")
        distanceentry.configure(foreground="white")
        distanceentry.configure(highlightbackground="#d9d9d9")
        distanceentry.configure(highlightcolor="black")
        distanceentry.configure(insertbackground="white")
        distanceentry.configure(selectbackground="#c4c4c4")
        distanceentry.configure(selectforeground="black")

        calorieentry = tk.Entry(bottomframe)
        calorieentry.place(relx = 0.5, rely=0.304, height=50, relwidth=0.300)
        calorieentry.configure(background="#211905")
        calorieentry.configure(disabledforeground="#a3a3a3")
        calorieentry.configure(font="-family {Comic Sans MS} -size 20")
        calorieentry.configure(foreground="white")
        calorieentry.configure(highlightbackground="#d9d9d9")
        calorieentry.configure(highlightcolor="black")
        calorieentry.configure(insertbackground="white")
        calorieentry.configure(selectbackground="#c4c4c4")
        calorieentry.configure(selectforeground="black")

        bpentry = tk.Entry(bottomframe)
        bpentry.place(relx = 0.5, rely=0.398, height=50, relwidth=0.300)
        bpentry.configure(background="#211905")
        bpentry.configure(disabledforeground="#a3a3a3")
        bpentry.configure(font="-family {Comic Sans MS} -size 20")
        bpentry.configure(foreground="white")
        bpentry.configure(highlightbackground="#d9d9d9")
        bpentry.configure(highlightcolor="black")
        bpentry.configure(insertbackground="white")
        bpentry.configure(selectbackground="#c4c4c4")
        bpentry.configure(selectforeground="black")

        sleepentry = tk.Entry(bottomframe)
        sleepentry.place(relx = 0.5, rely=0.491, height=50, relwidth=0.300)
        sleepentry.configure(background="#211905")
        sleepentry.configure(disabledforeground="#a3a3a3")
        sleepentry.configure(font="-family {Comic Sans MS} -size 20")
        sleepentry.configure(foreground="white")
        sleepentry.configure(highlightbackground="#d9d9d9")
        sleepentry.configure(highlightcolor="black")
        sleepentry.configure(insertbackground="white")
        sleepentry.configure(selectbackground="#c4c4c4")
        sleepentry.configure(selectforeground="black")

        waterentry = tk.Entry(bottomframe)
        waterentry.place(relx = 0.5, rely=0.585, height=50, relwidth=0.300)
        waterentry.configure(background="#211905")
        waterentry.configure(disabledforeground="#a3a3a3")
        waterentry.configure(font="-family {Comic Sans MS} -size 20")
        waterentry.configure(foreground="white")
        waterentry.configure(highlightbackground="#d9d9d9")
        waterentry.configure(highlightcolor="black")
        waterentry.configure(insertbackground="white")
        waterentry.configure(selectbackground="#c4c4c4")
        waterentry.configure(selectforeground="black")

        floorentry = tk.Entry(bottomframe)
        floorentry.place(relx = 0.5, rely=0.678, height=50, relwidth=0.300)
        floorentry.configure(background="#211905")
        floorentry.configure(disabledforeground="#a3a3a3")
        floorentry.configure(font="-family {Comic Sans MS} -size 20")
        floorentry.configure(foreground="white")
        floorentry.configure(highlightbackground="#d9d9d9")
        floorentry.configure(highlightcolor="black")
        floorentry.configure(insertbackground="white")
        floorentry.configure(selectbackground="#c4c4c4")
        floorentry.configure(selectforeground="black")

        weightentry = tk.Entry(bottomframe)
        weightentry.place(relx = 0.5, rely=0.784, height=50, relwidth=0.300)
        weightentry.configure(background="#211905")
        weightentry.configure(disabledforeground="#a3a3a3")
        weightentry.configure(font="-family {Comic Sans MS} -size 20")
        weightentry.configure(foreground="white")
        weightentry.configure(highlightbackground="#d9d9d9")
        weightentry.configure(highlightcolor="black")
        weightentry.configure(insertbackground="white")
        weightentry.configure(selectbackground="#c4c4c4")
        weightentry.configure(selectforeground="black")

        sumbitbutton = tk.Button(bottomframe)
        sumbitbutton.place(relx=0.25, rely=0.889, height=50, width=120)
        sumbitbutton.configure(activebackground="#ececec")
        sumbitbutton.configure(activeforeground="#000000")
        sumbitbutton.configure(background="#edbe00")
        sumbitbutton.configure(disabledforeground="#a3a3a3")
        sumbitbutton.configure(foreground="black")
        sumbitbutton.configure(font ="-family {Comic Sans MS} -size 20")
        sumbitbutton.configure(highlightbackground="#d9d9d9")
        sumbitbutton.configure(highlightcolor="black")
        sumbitbutton.configure(pady="0")
        sumbitbutton.configure(text='''Submit''')
        sumbitbutton.configure(command = enteractivity)

        sumbitbutton = tk.Button(bottomframe)
        sumbitbutton.place(relx=0.55, rely=0.889, height=50, width=225)
        sumbitbutton.configure(activebackground="#ececec")
        sumbitbutton.configure(activeforeground="#000000")
        sumbitbutton.configure(background="#edbe00")
        sumbitbutton.configure(disabledforeground="#a3a3a3")
        sumbitbutton.configure(foreground="black")
        sumbitbutton.configure(font="-family {Comic Sans MS} -size 20")
        sumbitbutton.configure(highlightbackground="#d9d9d9")
        sumbitbutton.configure(highlightcolor="black")
        sumbitbutton.configure(pady="0")
        sumbitbutton.configure(text='''Go To Homepage''')
        sumbitbutton.configure(command = gotohome)

    ###### device section#####
    def devices():

        def gotohome():
            deviceroot.destroy()
            Homepage()

        def viewdevice():
            global now
            now = datetime.now()
            nowstring = now.strftime("%Y-%m-%d %H:%M:%S")
            print(nowstring)

            insideframe1 = tk.Frame(bottomframe)
            insideframe1.place(relx=0.042, rely=0.278, relheight=0.799
                               , relwidth=0.916)
            insideframe1.configure(relief='groove')
            # insideframe.configure(borderwidth="1")
            insideframe1.configure(relief="groove")
            insideframe1.configure(background="#000000")

            sqlformula = "select distinct concat(d.company,' ',d.model),u.dstatus from devicelist as d , userdevice as u where u.did = d.did and u.uid = %s"
            mycursor.execute(sqlformula,(uid,))
            devicelist = mycursor.fetchall()
            print(devicelist)
            place = 1
            row=0
            buttonlist = []
            for i in devicelist:



                devicelabe = tk.Label(insideframe1)
                devicelabe.grid(row=row, column=0)
                # devicelabel.place( height=91, width=300)#relx=0.05, rely=place*0.1,
                devicelabe.configure(anchor='w')
                devicelabe.configure(background="#000000")
                devicelabe.configure(disabledforeground="#a3a3a3")
                devicelabe.configure(font="-family {Comic Sans MS} -size 20")
                devicelabe.configure(foreground="#edbe00")
                devicelabe.configure(justify='left')
                devicelabe.configure(text=i[0])


                devicelabel = tk.Label(insideframe1)
                devicelabel.grid(row=row, column=1)
                # devicelabel.place( height=91, width=300)#relx=0.05, rely=place*0.1,
                devicelabel.configure(anchor='w')
                devicelabel.configure(background="#000000")
                devicelabel.configure(disabledforeground="#a3a3a3")
                devicelabel.configure(font="-family {Comic Sans MS} -size 20")
                devicelabel.configure(foreground="#edbe00")
                devicelabel.configure(justify='left')
                devicelabel.configure(text='------------>')

                viewbutton = tk.Button(insideframe1)
                viewbutton.grid(row=row,column =2)
                #viewbutton.place(,height=50, width=150 )#relx=0.75, rely=place *0.15,
                viewbutton.configure(activebackground="#ececec")
                viewbutton.configure(activeforeground="#000000")
                viewbutton.configure(background="#edbe00")
                viewbutton.configure(cursor="hand2")
                viewbutton.configure(disabledforeground="#a3a3a3")
                viewbutton.configure(font="-family {Comic Sans MS} -size 20")
                viewbutton.configure(foreground="#000000")
                viewbutton.configure(highlightbackground="#d9d9d9")
                viewbutton.configure(highlightcolor="black")
                viewbutton.configure(pady="0")
                viewbutton.configure(text=i[1])
                #viewbutton.configure(command=changestatus)
                buttonlist.append(viewbutton)
                place = place + 1
                row = row+1


        def adddevice():
            global now
            now = datetime.now()
            nowstring = now.strftime("%Y-%m-%d %H:%M:%S")
            print(nowstring)
            def addtouserdevice():
                global uid
                devicename = devicebox.get()
                devicestatus = statusbox.get()
                useruid = uid
                brokendevicename = devicename.split(" ",1)
                devicemodelname = brokendevicename[1]
                sqlformula = 'select did from devicelist where model = %s'
                mycursor.execute(sqlformula,(devicemodelname,))
                deviceid = (mycursor.fetchone())[0]
                insertdetails = (useruid,deviceid,devicestatus)
                sqlformula ='insert into userdevice(uid,did,dstatus) values(%s,%s,%s)'
                mycursor.execute(sqlformula,insertdetails)
                mydb.commit()
                messagebox.showinfo("Success", "Device Added Successfully")
                ######## added later for displaying status timings#############
                ###sqlformula = 'select did from devicelist where model = %s'
                #########  taking device id from above query###################
                mycursor.execute(sqlformula, (deviceid))
                did = (mycursor.fetchall())[0][0]
                activetimelist = (uid, deviceid, nowstring, nowstring)
                formula = 'insert into activitytime(uid,did,activetime,deactivetime) values (%s,%s,%s,%s)'
                mycursor.execute(formula, activetimelist)
                mydb.commit()
                viewdevice()


            insideframe2 = tk.Frame(bottomframe)
            insideframe2.place(relx=0.042, rely=0.178, relheight=0.799
                               , relwidth=0.916)
            insideframe2.configure(relief='groove')
            # insideframe.configure(borderwidth="1")
            insideframe2.configure(relief="groove")
            insideframe2.configure(background="black")

            mycursor.execute( "select distinct concat(company,' ',model) from devicelist")
            devices = mycursor.fetchall()
            devicenames = []
            for i in devices:
                devicenames.append(i[0])


            devicelabe = tk.Label(insideframe2)
            devicelabe.place( relx=0.25, rely=0.1,height=91, width=300)#
            devicelabe.configure(anchor='w')
            devicelabe.configure(background="#000000")
            devicelabe.configure(disabledforeground="#a3a3a3")
            devicelabe.configure(font="-family {Comic Sans MS} -size 20")
            devicelabe.configure(foreground="#edbe00")
            devicelabe.configure(justify='left')
            devicelabe.configure(text='Choose Device to Add :')

            devicebox = ttk.Combobox(insideframe2, values=(devicenames), state='readonly')  # ,textvariable=monthofbirth
            devicebox.place(relx=0.25, rely=0.220, height=40, width=300)
            devicebox.configure(font="-family {Comic Sans MS} -size 15", justify='center')

            devicelabe = tk.Label(insideframe2)
            devicelabe.place(relx=0.25, rely=0.28, height=91, width=300)  #
            devicelabe.configure(anchor='w')
            devicelabe.configure(background="#000000")
            devicelabe.configure(disabledforeground="#a3a3a3")
            devicelabe.configure(font="-family {Comic Sans MS} -size 20")
            devicelabe.configure(foreground="#edbe00")
            devicelabe.configure(justify='left')
            devicelabe.configure(text='Choose Device Status :')

            statuslist=['Active','Deactive']
            statusbox = ttk.Combobox(insideframe2, values=(statuslist), state='readonly')  # ,textvariable=monthofbirth
            statusbox.place(relx=0.25, rely=0.400, height=40, width=300)
            statusbox.configure(font="-family {Comic Sans MS} -size 15", justify='center')

            addbutton = tk.Button(insideframe2)
            addbutton.place(relx=0.25, rely=0.520, height=54, width=300)
            addbutton.configure(activebackground="#ececec")
            addbutton.configure(activeforeground="#000000")
            addbutton.configure(background="#edbe00")
            addbutton.configure(cursor="hand2")
            addbutton.configure(disabledforeground="#a3a3a3")
            addbutton.configure(font="-family {Comic Sans MS} -size 16")
            addbutton.configure(foreground="#000000")
            addbutton.configure(highlightbackground="#d9d9d9")
            addbutton.configure(highlightcolor="black")
            addbutton.configure(pady="0")
            addbutton.configure(text='''Add Device To profile''')
            addbutton.configure(command=addtouserdevice)


        def modifydevice():
            global now
            now = datetime.now()
            nowstring = now.strftime("%Y-%m-%d %H:%M:%S")
            print(nowstring)

            def deletedevice():
                devicename = devicebox.get()
                justdevicename = (((devicename.split('---',1))[0]).split(' ',1))[1]
                sqlformula = 'delete from userdevice where uid = %s and did in (select did from devicelist where model = %s)'
                mycursor.execute(sqlformula,(uid,justdevicename,))
                mydb.commit()
                messagebox.showinfo("Success", "Device Deleted Successfully")
                viewdevice()

            def changestatus():
                devicename = devicebox.get()
                justdevicename = (((devicename.split('---', 1))[0]).split(' ', 1))[1]
                justdevicestatus = (((devicename.split('---(',1))[1]).split(')',1))[0]
                if justdevicestatus == "Active":
                    detailstochange = ("Deactive",justdevicename)
                    sqlformula= 'update userdevice set dstatus = %s where did in (select did from devicelist where model = %s)'
                    mycursor.execute(sqlformula,detailstochange,)
                    mydb.commit()
                    ######## added later for displaying status timings#############
                    sqlformula = 'select did from devicelist where model = %s'
                    mycursor.execute(sqlformula,(justdevicename,))
                    did = (mycursor.fetchall())[0][0]
                    activetimelist = (uid,did,nowstring,nowstring)
                    formula = 'insert into activitytime(uid,did,activetime,deactivetime) values (%s,%s,%s,%s)'
                    mycursor.execute(formula,activetimelist)
                    mydb.commit()

                elif justdevicestatus == "Deactive":
                    detailstochange = ("Active",justdevicename)
                    print(detailstochange)
                    sqlformula= 'update userdevice set dstatus = %s where did in (select did from devicelist where model = %s)'
                    mycursor.execute(sqlformula,detailstochange,)
                    mydb.commit()
                    ######## added later for displaying status timings#############
                    sqlformula = 'select did from devicelist where model = %s'
                    mycursor.execute(sqlformula, (justdevicename,))
                    did = (mycursor.fetchall())[0][0]
                    deactivelist = (nowstring,did,uid)
                    formula = 'update activitytime set deactivetime = %s where did = %s and uid = %s and activetime = deactivatetime'
                    mycursor.execute(formula,deactivelist)
                    mydb.commit()

                messagebox.showinfo("Success", "Device Status Changed Successfully")
                viewdevice()

            def statustime():
                global now

                now = datetime.now()
                nowstring = now.strftime("%Y-%m-%d %H:%M:%S")
                print(nowstring)

                insideframe4 = tk.Frame(bottomframe)
                insideframe4.place(relx=0.042, rely=0.278, relheight=0.799
                                   , relwidth=0.916)
                insideframe4.configure(relief='groove')
                # insideframe.configure(borderwidth="1")
                insideframe4.configure(relief="groove")
                insideframe4.configure(background="black")
                devicename = devicebox.get()
                #justdevicename = (((devicename.split('---', 1))[0]).split(' ', 1))[1]
                #justdevicestatus = (((devicename.split('---(', 1))[1]).split(')', 1))[0]
                sqlformula = 'select concat(dl.company," ",dl.model), at.activetime,at.deactivetime from devicelist as dl, activitytime as at where uid = %s and dl.did = at.did'
                mycursor.execute(sqlformula,(uid,))
                statustimelist = mycursor.fetchall()
                headlist = [ "Device Name ", "          Active Time       ", "         Deactive Time       "]
                statustimelist = list(statustimelist)
                statustimelist.insert(0,headlist)
                for i in range(len(statustimelist)):
                    for j in range(len(statustimelist[i])):
                        emailabel = Label(insideframe4)
                        emailabel.grid(row=i, column=j)
                        emailabel.configure(background="#000000")  # 070707
                        emailabel.configure(disabledforeground="#a3a3a3")
                        emailabel.configure(font="-family {Comic Sans MS} -size 14")
                        emailabel.configure(foreground="white")
                        emailabel.configure(highlightcolor="#fc613a")
                        emailabel.configure(text=statustimelist[i][j])



            devicestatustime = tk.Button(bottomframe)
            devicestatustime.place(relx=0.76, rely=0.047, height=74, width=150)
            devicestatustime.configure(activebackground="#ececec")
            devicestatustime.configure(activeforeground="#000000")
            devicestatustime.configure(background="#edbe00")
            devicestatustime.configure(cursor="hand2")
            devicestatustime.configure(disabledforeground="#a3a3a3")
            devicestatustime.configure(font="-family {Comic Sans MS} -size 16")
            devicestatustime.configure(foreground="#000000")
            devicestatustime.configure(highlightbackground="#d9d9d9")
            devicestatustime.configure(highlightcolor="black")
            devicestatustime.configure(pady="0")
            devicestatustime.configure(text='''Activity Time''')
            devicestatustime.configure(command=statustime)

            insideframe3 = tk.Frame(bottomframe)
            insideframe3.place(relx=0.042, rely=0.178, relheight=0.799
                               , relwidth=0.916)
            insideframe3.configure(relief='groove')
            # insideframe.configure(borderwidth="1")
            insideframe3.configure(relief="groove")
            insideframe3.configure(background="black")

            sqlformula = "select distinct concat(d.company,' ',d.model,'---(',u.dstatus,')---') from devicelist as d , userdevice as u where u.did = d.did and u.uid = %s"
            mycursor.execute(sqlformula,(uid,))
            alluserdevice = mycursor.fetchall()
            justname = []
            for i in alluserdevice:
                justname.append(i[0])

            devicelabe = tk.Label(insideframe3)
            devicelabe.place(relx=0.24, rely=0.1, height=91, width=400)  #
            devicelabe.configure(anchor='w')
            devicelabe.configure(background="#000000")
            devicelabe.configure(disabledforeground="#a3a3a3")
            devicelabe.configure(font="-family {Comic Sans MS} -size 25")
            devicelabe.configure(foreground="#edbe00")
            devicelabe.configure(justify='left')
            devicelabe.configure(text='Choose Device to Modify :')

            devicebox = ttk.Combobox(insideframe3, values=(justname), state='readonly')  # ,textvariable=monthofbirth
            devicebox.place(relx=0.25, rely=0.220, height=40, width=350)
            devicebox.configure(font="-family {Comic Sans MS} -size 15", justify='center')

            addbutton = tk.Button(insideframe3)
            addbutton.place(relx=0.35, rely=0.320, height=54, width=200)
            addbutton.configure(activebackground="#ececec")
            addbutton.configure(activeforeground="#000000")
            addbutton.configure(background="#edbe00")
            addbutton.configure(cursor="hand2")
            addbutton.configure(disabledforeground="#a3a3a3")
            addbutton.configure(font="-family {Comic Sans MS} -size 16")
            addbutton.configure(foreground="#000000")
            addbutton.configure(highlightbackground="#d9d9d9")
            addbutton.configure(highlightcolor="black")
            addbutton.configure(pady="0")
            addbutton.configure(text='''Delete Device''')
            addbutton.configure(command=deletedevice)

            addbutton = tk.Button(insideframe3)
            addbutton.place(relx=0.35, rely=0.4350, height=54, width=200)
            addbutton.configure(activebackground="#ececec")
            addbutton.configure(activeforeground="#000000")
            addbutton.configure(background="#edbe00")
            addbutton.configure(cursor="hand2")
            addbutton.configure(disabledforeground="#a3a3a3")
            addbutton.configure(font="-family {Comic Sans MS} -size 16")
            addbutton.configure(foreground="#000000")
            addbutton.configure(highlightbackground="#d9d9d9")
            addbutton.configure(highlightcolor="black")
            addbutton.configure(pady="0")
            addbutton.configure(text='''Change Status''')
            addbutton.configure(command=changestatus)





        homeroot.destroy()
        deviceroot = Tk()
        deviceroot.geometry("755x1001+710+10")
        deviceroot.title("New Toplevel")
        deviceroot.configure(background="#edbe00")

        topframe = tk.Frame(deviceroot)
        topframe.place(relx=0.0, rely=0.0, relheight=0.125, relwidth=1.0)
        topframe.configure(relief='groove')
        topframe.configure(borderwidth="2")
        topframe.configure(relief="groove")
        topframe.configure(background="#000000")

        deviceicon = tk.Label(topframe)
        deviceicon.place(relx=0.013, rely=0.08, height=101, width=124)
        deviceicon.configure(background="#d9d9d9")
        deviceicon.configure(disabledforeground="#a3a3a3")
        deviceicon.configure(foreground="#000000")
        photo_location = os.path.join("C:/Users/Goutam Awadhiya/TrackByte/index.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        deviceicon.configure(image=_img0)
        deviceicon.configure(text='''Label''')

        devicelabel = tk.Label(topframe)
        devicelabel.place(relx=0.199, rely=0.16, height=91, width=254)
        devicelabel.configure(anchor='w')
        devicelabel.configure(background="#000000")
        devicelabel.configure(disabledforeground="#a3a3a3")
        devicelabel.configure(font="-family {Comic Sans MS} -size 40")
        devicelabel.configure(foreground="#edbe00")
        devicelabel.configure(justify='left')
        devicelabel.configure(text='''Devices''')

        tracklogo = tk.Label(topframe)
        tracklogo.place(relx=0.742, rely=0.08, height=111, width=194)
        tracklogo.configure(background="#d9d9d9")
        tracklogo.configure(disabledforeground="#a3a3a3")
        tracklogo.configure(foreground="#000000")
        photo_location = os.path.join("logoSHORTNEW14.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        tracklogo.configure(image=_img1)
        tracklogo.configure(text='''Label''')

        bottomframe = tk.Frame(deviceroot)
        bottomframe.place(relx=0.026, rely=0.14, relheight=0.844, relwidth=0.947)

        bottomframe.configure(relief='groove')
        bottomframe.configure(borderwidth="2")
        bottomframe.configure(relief="groove")
        bottomframe.configure(background="#000000")

        viewbutton = tk.Button(bottomframe)
        viewbutton.place(relx=0.02, rely=0.047, height=74, width=150)
        viewbutton.configure(activebackground="#ececec")
        viewbutton.configure(activeforeground="#000000")
        viewbutton.configure(background="#edbe00")
        viewbutton.configure(cursor="hand2")
        viewbutton.configure(disabledforeground="#a3a3a3")
        viewbutton.configure(font="-family {Comic Sans MS} -size 16")
        viewbutton.configure(foreground="#000000")
        viewbutton.configure(highlightbackground="#d9d9d9")
        viewbutton.configure(highlightcolor="black")
        viewbutton.configure(pady="0")
        viewbutton.configure(text='''View Devices''')
        viewbutton.configure(command = viewdevice)

        addbutton = tk.Button(bottomframe)
        addbutton.place(relx=0.27, rely=0.047, height=74, width=150)
        addbutton.configure(activebackground="#ececec")
        addbutton.configure(activeforeground="#000000")
        addbutton.configure(background="#edbe00")
        addbutton.configure(cursor="hand2")
        addbutton.configure(disabledforeground="#a3a3a3")
        addbutton.configure(font="-family {Comic Sans MS} -size 16")
        addbutton.configure(foreground="#000000")
        addbutton.configure(highlightbackground="#d9d9d9")
        addbutton.configure(highlightcolor="black")
        addbutton.configure(pady="0")
        addbutton.configure(text='''Add Device''')
        addbutton.configure(command= adddevice )

        modifybutton = tk.Button(bottomframe)
        modifybutton.place(relx=0.51, rely=0.047, height=74, width=150)
        modifybutton.configure(activebackground="#ececec")
        modifybutton.configure(activeforeground="#000000")
        modifybutton.configure(background="#edbe00")
        modifybutton.configure(cursor="hand2")
        modifybutton.configure(disabledforeground="#a3a3a3")
        modifybutton.configure(font="-family {Comic Sans MS} -size 16")
        modifybutton.configure(foreground="#000000")
        modifybutton.configure(highlightbackground="#d9d9d9")
        modifybutton.configure(highlightcolor="black")
        modifybutton.configure(pady="0")
        modifybutton.configure(text='''Modify Device''')
        modifybutton.configure(command = modifydevice)



        sumbitbutton = tk.Button(deviceroot)
        sumbitbutton.place(relx=0.35, rely=0.889, height=50, width=225)
        sumbitbutton.configure(activebackground="#ececec")
        sumbitbutton.configure(activeforeground="#000000")
        sumbitbutton.configure(background="#edbe00")
        sumbitbutton.configure(disabledforeground="#a3a3a3")
        sumbitbutton.configure(foreground="black")
        sumbitbutton.configure(font="-family {Comic Sans MS} -size 20")
        sumbitbutton.configure(highlightbackground="#d9d9d9")
        sumbitbutton.configure(highlightcolor="black")
        sumbitbutton.configure(pady="0")
        sumbitbutton.configure(text='''Go To Homepage''')
        sumbitbutton.configure(command=gotohome)

    ####### profile function ########
    def profile():
        global uid
        homeroot.destroy()

        ##### details to print in details #########

        puid = uid
        sqlformula= 'select  fname,lname,email,gender,dob,houseno,street,city,country,weight from users where uid = %s'
        mycursor.execute(sqlformula,(puid,))
        usertabledetail= mycursor.fetchall()
        pfname = usertabledetail[0][0]
        plname = usertabledetail[0][1]
        pemail = usertabledetail[0][2]
        pgender = usertabledetail[0][3]
        pbirthdate = usertabledetail[0][4]
        phouse = usertabledetail[0][5]
        pstreet = usertabledetail[0][6]
        pcity   = usertabledetail[0][7]
        pcountry = usertabledetail[0][8]
        print(usertabledetail)
        if usertabledetail[0][9] == None:
            pweight = 0
        else:
            pweight = usertabledetail[0][9]

        sqlformula = 'select mobile from ucontact where uid = %s'
        mycursor.execute(sqlformula,(uid,))
        contacttabledetail = mycursor.fetchall()
        if len(contacttabledetail) == 0:
            pass
        elif len(contacttabledetail) == 1:
            pmobile1 = contacttabledetail[0][0]
        elif len(contacttabledetail) == 2:
            pmobile1 = contacttabledetail[0][0]
            pmobile2 = contacttabledetail[1][0]
        else:
            pmobile1 = " "
            pmobile2 = " "

        def enterpass():

            def checkpass():

                global uid
                sqlformula='select password from users where uid = %s'
                mycursor.execute(sqlformula,(uid,))
                passlist = mycursor.fetchall()
                print(passentry.get())
                print(passlist[0][0])
                if passentry.get() == passlist[0][0]:
                    cfname = fnameentry.get()
                    clname = lnamenentry.get()
                    cemail = emailentry.get()
                    cgender = genderentry.get()
                    cdob = dobentry.get()
                    cmobile1 = mobile1entry.get()
                    cmobile2 = mobile2entry.get()
                    chouse = houseentry.get()
                    cstreet = streetentry.get()
                    ccity = cityentry.get()
                    ccountry = countryentry.get()
                    cweight = weightentry.get()
                    UserTableDetail = (cfname,clname,cemail,cgender,cdob,chouse,cstreet,ccity,ccountry,cweight,uid)
                    sqlformula = 'update users set fname = %s , lname = %s , email = %s , gender = %s , dob = %s , houseno = %s , street = %s , city = %s , country = %s , weight = %s where uid = %s'
                    mycursor.execute(sqlformula, UserTableDetail)
                    mydb.commit()
                    messagebox.showinfo("Success","Changes Saves Successfully")

                    passroot.destroy()
                    profileroot.destroy()
                    Homepage()
                else:
                    spasslabel = tk.Label(passroot)
                    spasslabel.place(relx=0.0200, rely=0.55, height=20, width=400)
                    spasslabel.configure(activebackground="#f9f9f9")
                    spasslabel.configure(activeforeground="black")
                    spasslabel.configure(background="#000000")
                    spasslabel.configure(disabledforeground="#a3a3a3")
                    spasslabel.configure(font="-family {Comic Sans MS} -size 10")
                    spasslabel.configure(foreground="#edbe00")
                    spasslabel.configure(highlightbackground="#d9d9d9")
                    spasslabel.configure(highlightcolor="black")
                    spasslabel.configure(text='''Enter correct password ''')



            passroot =Tk()
            passroot.geometry("400x200+685+500")
            passroot.title("Password Required")
            passroot.configure(background="#000000")
            passroot.resizable(FALSE,FALSE)

            spasslabel = tk.Label(passroot)
            spasslabel.place(relx=0.0180, rely=0.0350, height=46, width=400)
            spasslabel.configure(activebackground="#f9f9f9")
            spasslabel.configure(activeforeground="black")
            spasslabel.configure(background="#000000")
            spasslabel.configure(disabledforeground="#a3a3a3")
            spasslabel.configure(font="-family {Comic Sans MS} -size 16")
            spasslabel.configure(foreground="#edbe00")
            spasslabel.configure(highlightbackground="#d9d9d9")
            spasslabel.configure(highlightcolor="black")
            spasslabel.configure(text='''Enter password to save changes :''')

            passentry = Entry(passroot, show='*')
            passentry.place(relx=0.100, rely=0.250, height=46, width=300)
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

            submitbutton = tk.Button(passroot)
            submitbutton.place(relx=0.370, rely=0.7, height=44, width=127)
            submitbutton.configure(activebackground="#ececec")
            submitbutton.configure(activeforeground="#000000")
            submitbutton.configure(background="#edbe00")
            submitbutton.configure(cursor="hand2")
            submitbutton.configure(disabledforeground="#a3a3a3")
            submitbutton.configure(font="-family {Segoe UI} -size 16")
            submitbutton.configure(foreground="#000000")
            submitbutton.configure(highlightbackground="#d9d9d9")
            submitbutton.configure(highlightcolor="black")
            submitbutton.configure(pady="0")
            submitbutton.configure(text='''Submit''')
            submitbutton.configure(command = checkpass)


            passroot.mainloop()

        def redirect2home():
            profileroot.destroy()
            Homepage()





        #### MAIN PROFILE WINDOW ######
        profileroot = Tk()
        profileroot.geometry("755x1001+685+30")
        profileroot.title("Profile Page")
        profileroot.configure(background="#edbe00")
        profileroot.resizable(FALSE, FALSE)

        topframe = tk.Frame(profileroot)
        topframe.place(relx=0.0, rely=0.0, relheight=0.085, relwidth=1.013)
        topframe.configure(relief='groove')
        topframe.configure(borderwidth="2")
        topframe.configure(relief="groove")
        topframe.configure(background="#000000")

        profilelabel = tk.Label(topframe)
        profilelabel.place(relx=0.131, rely=0.118, height=71, width=184)
        profilelabel.configure(background="#000000")
        profilelabel.configure(disabledforeground="#a3a3a3")
        profilelabel.configure(font="-family {Comic Sans MS} -size 40")
        profilelabel.configure(foreground="#edbe00")
        profilelabel.configure(text='''Profile''')

        jokerlabel = tk.Label(topframe)
        jokerlabel.place(relx=0.013, rely=0.118, height=71, width=84)
        jokerlabel.configure(background="#d9d9d9")
        jokerlabel.configure(disabledforeground="#a3a3a3")
        jokerlabel.configure(foreground="#000000")
        photo_location = os.path.join("blackprofile-14 045726.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        jokerlabel.configure(image=_img0)
        jokerlabel.configure(text='''Label''')

        bottomframe = tk.Frame(profileroot)
        bottomframe.place(relx=0.013, rely=0.1, relheight=0.884, relwidth=0.974)
        bottomframe.configure(relief='groove')
        bottomframe.configure(borderwidth="2")
        bottomframe.configure(relief="groove")
        bottomframe.configure(background="#000000")

        fnamelabel = tk.Label(bottomframe)
        fnamelabel.place(relx=0.014, rely=0.023, height=41, width=114)
        fnamelabel.configure(activebackground="#f9f9f9")
        fnamelabel.configure(activeforeground="black")
        fnamelabel.configure(background="#000000")
        fnamelabel.configure(disabledforeground="#a3a3a3")
        fnamelabel.configure(font="-family {Comic Sans MS} -size 14")
        fnamelabel.configure(foreground="#edbe00")
        fnamelabel.configure(highlightbackground="#d9d9d9")
        fnamelabel.configure(highlightcolor="black")
        fnamelabel.configure(text='''First Name :''')

        fnameentry = tk.Entry(bottomframe)
        fnameentry.place(relx=0.204, rely=0.023, height=40, relwidth=0.25)
        fnameentry.configure(background="#211905")
        fnameentry.configure(disabledforeground="#a3a3a3")
        fnameentry.configure(font="-family {Comic Sans MS} -size 14")
        fnameentry.configure(foreground="white")
        fnameentry.configure(insertbackground="white")
        fnameentry.insert(0,pfname)

        lnamenentry = tk.Entry(bottomframe)
        lnamenentry.place(relx=0.735, rely=0.023, height=40, relwidth=0.25)
        lnamenentry.configure(background="#211905")
        lnamenentry.configure(disabledforeground="#a3a3a3")
        lnamenentry.configure(font="-family {Comic Sans MS} -size 14")
        lnamenentry.configure(foreground="white")
        lnamenentry.configure(highlightbackground="#d9d9d9")
        lnamenentry.configure(highlightcolor="black")
        lnamenentry.configure(insertbackground="white")
        lnamenentry.configure(selectbackground="#c4c4c4")
        lnamenentry.configure(selectforeground="black")
        lnamenentry.insert(0,plname)

        lnamelabel = tk.Label(bottomframe)
        lnamelabel.place(relx=0.558, rely=0.023, height=41, width=114)
        lnamelabel.configure(activebackground="#f9f9f9")
        lnamelabel.configure(activeforeground="black")
        lnamelabel.configure(background="#000000")
        lnamelabel.configure(disabledforeground="#a3a3a3")
        lnamelabel.configure(font="-family {Comic Sans MS} -size 14")
        lnamelabel.configure(foreground="#edbe00")
        lnamelabel.configure(highlightbackground="#d9d9d9")
        lnamelabel.configure(highlightcolor="black")
        lnamelabel.configure(text='''Last Name :''')

        emaillabel = tk.Label(bottomframe)
        emaillabel.place(relx=0.014, rely=0.09, height=41, width=114)
        emaillabel.configure(background="#000000")
        emaillabel.configure(disabledforeground="#a3a3a3")
        emaillabel.configure(font="-family {Comic Sans MS} -size 14")
        emaillabel.configure(foreground="#edbe00")
        emaillabel.configure(text='''Email :''')

        emailentry = tk.Entry(bottomframe)
        emailentry.place(relx=0.204, rely=0.09, height=40, relwidth=0.631)
        emailentry.configure(background="#211905")
        emailentry.configure(disabledforeground="#a3a3a3")
        emailentry.configure(font="-family {Comic Sans MS} -size 14")
        emailentry.configure(foreground="white")
        emailentry.configure(insertbackground="white")
        emailentry.insert(0,pemail)

        genderlabel = tk.Label(bottomframe)
        genderlabel.place(relx=0.014, rely=0.158, height=41, width=114)
        genderlabel.configure(background="#000000")
        genderlabel.configure(disabledforeground="#a3a3a3")
        genderlabel.configure(font="-family {Comic Sans MS} -size 14")
        genderlabel.configure(foreground="#edbe00")
        genderlabel.configure(text='''Gender :''')

        genderentry = tk.Entry(bottomframe)
        genderentry.place(relx=0.204, rely=0.158, height=40, relwidth=0.223)
        genderentry.configure(background="#211905")
        genderentry.configure(disabledforeground="#a3a3a3")
        genderentry.configure(font="-family {Comic Sans MS} -size 14")
        genderentry.configure(foreground="white")
        genderentry.configure(insertbackground="white")
        genderentry.insert(0,pgender)

        doblabel = tk.Label(bottomframe)
        doblabel.place(relx=0.018, rely=0.226, height=41, width=124)
        doblabel.configure(background="#000000")
        doblabel.configure(disabledforeground="#a3a3a3")
        doblabel.configure(font="-family {Comic Sans MS} -size 14")
        doblabel.configure(foreground="#edbe00")
        doblabel.configure(text='''Birthdate :''')

        dobentry = tk.Entry(bottomframe)
        dobentry.place(relx=0.204, rely=0.226, height=40, relwidth=0.305)
        dobentry.configure(background="#211905")
        dobentry.configure(disabledforeground="#a3a3a3")
        dobentry.configure(font="-family {Comic Sans MS} -size 14")
        dobentry.configure(foreground="white")
        dobentry.configure(insertbackground="white")
        dobentry.insert(0,pbirthdate)

        mobile1label = tk.Label(bottomframe)
        mobile1label.place(relx=0.014, rely=0.294, height=41, width=124)
        mobile1label.configure(background="#000000")
        mobile1label.configure(disabledforeground="#a3a3a3")
        mobile1label.configure(font="-family {Comic Sans MS} -size 14")
        mobile1label.configure(foreground="#edbe00")
        mobile1label.configure(text='''Moblile  1 :''')

        mobile1entry = tk.Entry(bottomframe)
        mobile1entry.place(relx=0.204, rely=0.294, height=40, relwidth=0.414)
        mobile1entry.configure(background="#211905")
        mobile1entry.configure(disabledforeground="#a3a3a3")
        mobile1entry.configure(font="-family {Comic Sans MS} -size 14")
        mobile1entry.configure(foreground="white")
        mobile1entry.configure(insertbackground="white")
        mobile1entry.insert(0,pmobile1)

        mobile2label = tk.Label(bottomframe)
        mobile2label.place(relx=0.014, rely=0.373, height=41, width=124)
        mobile2label.configure(background="#000000")
        mobile2label.configure(disabledforeground="#a3a3a3")
        mobile2label.configure(font="-family {Comic Sans MS} -size 14")
        mobile2label.configure(foreground="#edbe00")
        mobile2label.configure(text='''Mobile 2 :''')

        mobile2entry = tk.Entry(bottomframe)
        mobile2entry.place(relx=0.204, rely=0.373, height=40, relwidth=0.414)
        mobile2entry.configure(background="#211905")
        mobile2entry.configure(disabledforeground="#a3a3a3")
        mobile2entry.configure(font="-family {Comic Sans MS} -size 14")
        mobile2entry.configure(foreground="white")
        mobile2entry.configure(insertbackground="white")
        mobile2entry.insert(0,pmobile2)

        houseentry = tk.Entry(bottomframe)
        houseentry.place(relx=0.204, rely=0.452, height=40, relwidth=0.427)
        houseentry.configure(background="#211905")
        houseentry.configure(disabledforeground="#a3a3a3")
        houseentry.configure(font="-family {Comic Sans MS} -size 14")
        houseentry.configure(foreground="white")
        houseentry.configure(insertbackground="white")
        houseentry.insert(0,phouse)

        houselabel = tk.Label(bottomframe)
        houselabel.place(relx=0.014, rely=0.452, height=41, width=124)
        houselabel.configure(background="#000000")
        houselabel.configure(disabledforeground="#a3a3a3")
        houselabel.configure(font="-family {Comic Sans MS} -size 14")
        houselabel.configure(foreground="#edbe00")
        houselabel.configure(text='''House No.:''')

        streetlabel = tk.Label(bottomframe)
        streetlabel.place(relx=0.014, rely=0.530, height=41, width=124)
        streetlabel.configure(background="#000000")
        streetlabel.configure(disabledforeground="#a3a3a3")
        streetlabel.configure(font="-family {Comic Sans MS} -size 14")
        streetlabel.configure(foreground="#edbe00")
        streetlabel.configure(text='''Street :''')

        streetentry = tk.Entry(bottomframe)
        streetentry.place(relx=0.204, rely=0.531, height=40, relwidth=0.414)
        streetentry.configure(background="#211905")
        streetentry.configure(disabledforeground="#a3a3a3")
        streetentry.configure(font="-family {Comic Sans MS} -size 14")
        streetentry.configure(foreground="white")
        streetentry.configure(insertbackground="white")
        streetentry.insert(0,pstreet)

        citylabel = tk.Label(bottomframe)
        citylabel.place(relx=0.014, rely=0.588, height=51, width=124)
        citylabel.configure(background="#000000")
        citylabel.configure(disabledforeground="#a3a3a3")
        citylabel.configure(font="-family {Comic Sans MS} -size 14")
        citylabel.configure(foreground="#edbe00")
        citylabel.configure(text='''City :''')

        cityentry = tk.Entry(bottomframe)
        cityentry.place(relx=0.204, rely=0.599, height=40, relwidth=0.427)
        cityentry.configure(background="#211905")
        cityentry.configure(disabledforeground="#a3a3a3")
        cityentry.configure(font="-family {Comic Sans MS} -size 14")
        cityentry.configure(foreground="white")
        cityentry.configure(insertbackground="white")
        cityentry.insert(0,pcity)

        countrylabel = tk.Label(bottomframe)
        countrylabel.place(relx=0.014, rely=0.667, height=41, width=124)
        countrylabel.configure(background="#000000")
        countrylabel.configure(disabledforeground="#a3a3a3")
        countrylabel.configure(font="-family {Comic Sans MS} -size 14")
        countrylabel.configure(foreground="#edbe00")
        countrylabel.configure(text='''Country :''')

        countryentry = tk.Entry(bottomframe)
        countryentry.place(relx=0.204, rely=0.667, height=40, relwidth=0.414)
        countryentry.configure(background="#211905")
        countryentry.configure(disabledforeground="#a3a3a3")
        countryentry.configure(font="-family {Comic Sans MS} -size 14")
        countryentry.configure(foreground="white")
        countryentry.configure(insertbackground="white")
        countryentry.insert(0,pcountry)

        weightlabel = tk.Label(bottomframe)
        weightlabel.place(relx=0.014, rely=0.734, height=51, width=124)
        weightlabel.configure(background="#000000")
        weightlabel.configure(disabledforeground="#a3a3a3")
        weightlabel.configure(font="-family {Comic Sans MS} -size 14")
        weightlabel.configure(foreground="#edbe00")
        weightlabel.configure(text='''Weight :''')

        weightentry = tk.Entry(bottomframe)
        weightentry.place(relx=0.204, rely=0.734, height=50, relwidth=0.291)
        weightentry.configure(background="#211905")
        weightentry.configure(disabledforeground="#a3a3a3")
        weightentry.configure(font="-family {Comic Sans MS} -size 14")
        weightentry.configure(foreground="white")
        weightentry.configure(insertbackground="white")
        weightentry.insert(0,pweight)

        savechages = tk.Label(bottomframe)
        savechages.place(relx=0.225, rely=0.800, height=71, width=334)
        savechages.configure(anchor='w')
        savechages.configure(background="#000000")
        savechages.configure(disabledforeground="#a3a3a3")
        savechages.configure(font="-family {Comic Sans MS} -size 16")
        savechages.configure(foreground="#edbe00")
        savechages.configure(text='Edit the values to save changes')

        savebutton = tk.Button(bottomframe)
        savebutton.place(relx=0.180, rely=0.893, height=44, width=127)
        savebutton.configure(activebackground="#ececec")
        savebutton.configure(activeforeground="#000000")
        savebutton.configure(background="#edbe00")
        savebutton.configure(cursor="hand2")
        savebutton.configure(disabledforeground="#a3a3a3")
        savebutton.configure(font="-family {Comic Sans MS} -size 16")
        savebutton.configure(foreground="#000000")
        savebutton.configure(highlightbackground="#d9d9d9")
        savebutton.configure(highlightcolor="black")
        savebutton.configure(pady="0")
        savebutton.configure(text='''Save''')
        savebutton.configure(command = enterpass)

        gotohomebutton= tk.Button(bottomframe)
        gotohomebutton.place(relx=0.380, rely=0.893, height=44, width=230)
        gotohomebutton.configure(activebackground="#ececec")
        gotohomebutton.configure(activeforeground="#000000")
        gotohomebutton.configure(background="#edbe00")
        gotohomebutton.configure(cursor="hand2")
        gotohomebutton.configure(disabledforeground="#a3a3a3")
        gotohomebutton.configure(font="-family {Comic Sans MS} -size 16")
        gotohomebutton.configure(foreground="#000000")
        gotohomebutton.configure(highlightbackground="#d9d9d9")
        gotohomebutton.configure(highlightcolor="black")
        gotohomebutton.configure(pady="0")
        gotohomebutton.configure(text='''Go Back To homepage''')
        gotohomebutton.configure(command = redirect2home)

    global uid,fname
    homeroot = Tk()
    homeroot.geometry("755x1001+711+10")
    homeroot.title("Homepage")
    homeroot.configure(background="#edbe00")
    homeroot.configure(highlightcolor="#000000")
    homeroot.resizable(FALSE,FALSE)

    topframe = tk.Frame(homeroot)
    topframe.place(relx=0.0, rely=0.0, relheight=0.125, relwidth=1.0)
    topframe.configure(relief='groove')
    #topframe.configure(borderwidth="1")
    topframe.configure(relief="groove")
    topframe.configure(background="#000000")

    logolabel = tk.Label(topframe)
    logolabel.place(relx=0.715, rely=0.0, height=131, width=204)
    logolabel.configure(background="#000000")
    logolabel.configure(disabledforeground="#a3a3a3")
    logolabel.configure(foreground="#000000")
    photo_location = os.path.join("logoSHORTNEW14.png")
    global _img0
    _img0 = tk.PhotoImage(file=photo_location)
    logolabel.configure(image=_img0)
    logolabel.configure(text='''Label''')

    hellolabel = tk.Label(topframe)
    hellolabel.place(relx=0.013, rely=0.08, height=71, width=164)
    hellolabel.configure(anchor='e')
    hellolabel.configure(background="#000000")
    hellolabel.configure(disabledforeground="#a3a3a3")
    hellolabel.configure(font="-family {Comic Sans MS} -size 40")
    hellolabel.configure(foreground="#edbe00")
    hellolabel.configure(justify='right')
    hellolabel.configure(text='''Hello,''')

    fnamelabel = tk.Label(topframe)
    fnamelabel.place(relx=0.225, rely=0.08, height=71, width=334)
    fnamelabel.configure(anchor='w')
    fnamelabel.configure(background="#000000")
    fnamelabel.configure(disabledforeground="#a3a3a3")
    fnamelabel.configure(font="-family {Comic Sans MS} -size 40")
    fnamelabel.configure(foreground="#edbe00")
    fnamelabel.configure(text=fname)

    welcomelabel = tk.Label(topframe)
    welcomelabel.place(relx=0.0, rely=0.72, height=21, width=534)
    welcomelabel.configure(background="#edbe00")
    welcomelabel.configure(disabledforeground="#a3a3a3")
    welcomelabel.configure(font="-family {Comic Sans MS} -size 14")
    welcomelabel.configure(foreground="#000000")
    welcomelabel.configure(text='''------------Welcome to trackbyte-----------------------------''')

    bottomframe = tk.Frame(homeroot)
    bottomframe.place(relx=0.04, rely=0.12, relheight=0.854, relwidth=0.921)
    bottomframe.configure(relief='groove')
    #bottomframe.configure(borderwidth="1")
    bottomframe.configure(relief="groove")
    bottomframe.configure(background="#000000")

    profilebutton = tk.Button(bottomframe)
    profilebutton.place(relx=0.288, rely=0.07, height=60, width=300)
    profilebutton.configure(activebackground="#ececec")
    profilebutton.configure(activeforeground="#000000")
    profilebutton.configure(background="#edbe00")
    profilebutton.configure(disabledforeground="#a3a3a3")
    profilebutton.configure(font="-family {Comic Sans MS} -size 25")
    profilebutton.configure(foreground="#000000")
    profilebutton.configure(highlightbackground="#d9d9d9")
    profilebutton.configure(highlightcolor="black")
    profilebutton.configure(pady="0")
    profilebutton.configure(text='''Profile''')
    profilebutton.configure(command=profile)

    profilebutton = tk.Button(bottomframe)
    profilebutton.place(relx=0.288, rely=0.205, height=60, width=300)
    profilebutton.configure(activebackground="#ececec")
    profilebutton.configure(activeforeground="#000000")
    profilebutton.configure(background="#edbe00")
    profilebutton.configure(disabledforeground="#a3a3a3")
    profilebutton.configure(font="-family {Comic Sans MS} -size 25")
    profilebutton.configure(foreground="#000000")
    profilebutton.configure(highlightbackground="#d9d9d9")
    profilebutton.configure(highlightcolor="black")
    profilebutton.configure(pady="0")
    profilebutton.configure(text='''Your Devices''')
    profilebutton.configure(command= devices)

    enterstatbutton = tk.Button(bottomframe)
    enterstatbutton.place(relx=0.288, rely=0.34, height=60, width=300)
    enterstatbutton.configure(activebackground="#ececec")
    enterstatbutton.configure(activeforeground="#000000")
    enterstatbutton.configure(background="#edbe00")
    enterstatbutton.configure(disabledforeground="#a3a3a3")
    enterstatbutton.configure(font="-family {Comic Sans MS} -size 25")
    enterstatbutton.configure(foreground="#000000")
    enterstatbutton.configure(highlightbackground="#d9d9d9")
    enterstatbutton.configure(highlightcolor="black")
    enterstatbutton.configure(pady="0")
    enterstatbutton.configure(text='''Enter Stats''')
    enterstatbutton.configure(command = activity)

    seegoalsbutton = tk.Button(bottomframe)
    seegoalsbutton.place(relx=0.288, rely=0.475, height=60, width=300)
    seegoalsbutton.configure(activebackground="#ececec")
    seegoalsbutton.configure(activeforeground="#000000")
    seegoalsbutton.configure(background="#edbe00")
    seegoalsbutton.configure(disabledforeground="#a3a3a3")
    seegoalsbutton.configure(font="-family {Comic Sans MS} -size 25")
    seegoalsbutton.configure(foreground="#000000")
    seegoalsbutton.configure(highlightbackground="#d9d9d9")
    seegoalsbutton.configure(highlightcolor="black")
    seegoalsbutton.configure(pady="0")
    seegoalsbutton.configure(text='''See Goals''')
    seegoalsbutton.configure(command = goalachieved)

    setgoalsbutton = tk.Button(bottomframe)
    setgoalsbutton.place(relx=0.288, rely=0.61, height=60, width=300)
    setgoalsbutton.configure(activebackground="#ececec")
    setgoalsbutton.configure(activeforeground="#000000")
    setgoalsbutton.configure(background="#edbe00")
    setgoalsbutton.configure(disabledforeground="#a3a3a3")
    setgoalsbutton.configure(font="-family {Comic Sans MS} -size 25")
    setgoalsbutton.configure(foreground="#000000")
    setgoalsbutton.configure(highlightbackground="#d9d9d9")
    setgoalsbutton.configure(highlightcolor="black")
    setgoalsbutton.configure(pady="0")
    setgoalsbutton.configure(text='''Set Goals''')
    setgoalsbutton.configure(command =setgoals)

    eventsbutton = tk.Button(bottomframe)
    eventsbutton.place(relx=0.288, rely=0.745, height=60, width=300)
    eventsbutton.configure(activebackground="#ececec")
    eventsbutton.configure(activeforeground="#000000")
    eventsbutton.configure(background="#edbe00")
    eventsbutton.configure(disabledforeground="#a3a3a3")
    eventsbutton.configure(font="-family {Comic Sans MS} -size 25")
    eventsbutton.configure(foreground="#000000")
    eventsbutton.configure(highlightbackground="#d9d9d9")
    eventsbutton.configure(highlightcolor="black")
    eventsbutton.configure(pady="0")
    eventsbutton.configure(text='''Events''')
    eventsbutton.configure(command = events)

    ceventbutton = tk.Button(bottomframe)
    ceventbutton.place(relx=0.288, rely=0.88, height=60, width=300)
    ceventbutton.configure(activebackground="#ececec")
    ceventbutton.configure(activeforeground="#000000")
    ceventbutton.configure(background="#edbe00")
    ceventbutton.configure(disabledforeground="#a3a3a3")
    ceventbutton.configure(font="-family {Comic Sans MS} -size 25")
    ceventbutton.configure(foreground="#000000")
    ceventbutton.configure(highlightbackground="#d9d9d9")
    ceventbutton.configure(highlightcolor="black")
    ceventbutton.configure(pady="0")
    ceventbutton.configure(text='''Create Event''')
    ceventbutton.configure(command = createevent)

    homeroot.mainloop()
if __name__ == "__main__":
    Homepage()
