import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='pycoders',
    passwd='gass',
    database='trackbyte'
)

mycursor  = mydb.cursor()

##### CREATE DATABASE  ######

#mycursor.execute("create database trackbyte")
mycursor.execute('use trackbyte')

##### TABLES #########
'''
##### USER TABLE $
mycursor.execute("create table Users(uid int primary key auto_increment, fname varchar(100) not null, lname varchar (100), username varchar(20) unique not null,email varchar(50) not null, password varchar (30) not null, gender varchar(20) not null, dob date not null,houseno varchar(20), street varchar(20), city varchar(20), country varchar(20), startdate datetime  default NOW(), weight float)ENGINE=InnoDB AUTO_INCREMENT=1001")

##### INSERT DATA INTO USERS TABLE ####
mycursor.execute("insert into Users "
                 "(fname,lname,username,email,password,gender,dob,houseno,street,city,country,weight) "
                 "values"
                 "('goutam','awadhiya','goutam_awadhiya','gouawa19@gmail.com','19021998','male','1998-02-19','16/1','ward no. 17','ghansore','India',65),"
                 "('shraddha','soni','shraddha_soni','shrisoni12@gmail.com','12021998','female','1998-04-12','16/1','ward no. 17','ghansore','India',55)")
mydb.commit()

#### DEVICE LIST TABLE #####
mycursor.execute("create table DeviceList(did int primary key auto_increment, company varchar(20), model varchar(20), connectiviy varchar(20))ENGINE=InnoDB AUTO_INCREMENT=101")
  
##### USER DEVICE TABLE  #####
mycursor.execute( "create table UserDevice (uid int,did int,dstatus varchar(20),foreign key(uid) references Users(uid), foreign key(did) references DeviceList(did))")

##### ACTIVITIES TABLE #####
mycursor.execute( "create table Activities (uid int,activitydate date default curdate(),steps int,distance float,calories float,BP varchar(10),sleep int,water float,floors int, weight float,foreign key(uid) references Users(uid))")

####### SETGOALS TABLE #####
mycursor.execute("create table SetGoals(uid int,steps int,distance float,calories float,sleep int,water float,floor int,weight float,foreign key(uid) references Users(uid))")

###### GOAL ACHIEVED #########
mycursor.execute("create table GoalsAchieved(uid int,goaldate datetime default now(),steps int, distance float,calories float,sleep int,water float,floor int, weight float,foreign key(uid) references Users(uid))")

###### EVENTS TABLE #######
mycursor.execute("create table Events (eid int primary key auto_increment,contactno varchar(20),organiser varchar(20),ename varchar (50),edate date,venue varchar(50),city varchar(20),etime time)ENGINE=InnoDB AUTO_INCREMENT=10001")

###### EVENT ATTENDED TABLE ######
mycursor.execute( "create table AttEvents(eid int,uid int,foreign key(eid) references Events(eid),foreign key(uid) references Users(uid))")

###### USERNAME CONTACT TABLE ####
mycursor.execute("create table Ucontact(uid int,mobile1 varchar(20),mobile2 varchar(20),foreign key(uid) references Users(uid))")

###### ORGANISER CONTACT TABLE ######
mycursor.execute("create table Econtact(eid int, mobile1 varchar(20), mobile2 varchar(20), foreign key (eid) references Events(eid))")

'''
'''
mycursor.execute('insert into devicelist (did,company,model,connectivity) values ('Fitbit','charge','bluetooth'),('Fitbit','charge 2','bluetooth'),('Fitbit','energy','bluetooth'),('Fitbit',Energy 2, 'bluetooth'),('Samsung','galaxy band', 'wifi'),('samsung','galaxy band 2','wifi') 
insert into userdevice(uid,did,dstatus) values (1001,101,'active'),(1001,102,'deactive'),(1027,105,'active'),(1027,104,'deactive');
'''