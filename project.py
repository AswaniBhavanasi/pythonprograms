from tkinter import *
from tkinter import Tk
from tkinter import ttk
import pymysql

class StudentsData:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1500x800')
        title1=Label(self.root, text='Welcome To NTH Students Data',font=('Berlin sans FB',40),bg='green',fg='white',bd=5,relief=RAISED)
        title1.pack(fill='x')

        self.rollnoVar=StringVar()
        self.fnameVar=StringVar()
        self.lnameVar=StringVar()
        self.courseVar=StringVar()
        self.contactVar=StringVar()
        self.emailVar=StringVar()
        self.locationVar=StringVar()
        self.instituteVar=StringVar()

        #creating Frames
        dataEntryFrame=Frame(self.root,bg='green')
        dataEntryFrame.place(x=10,y=80,width=500,height=700)
        
        dataDisplayFrame=Frame(self.root,bg='green')
        dataDisplayFrame.place(x=520, y=80, width=970 ,height=700)
        
        # working with data entry frame
        title2=Label(dataEntryFrame,text='Students  data entry',font=('Berlin sans FB',20),bg='green',fg='white',bd=5)
        title2.grid(row=0,columnspan=2,padx=120,pady=20)

        #roll no
        rollnoL=Label(dataEntryFrame,text='Roll no:', font=('Dubai',20),bg='green',fg='white')
        rollnoL.grid(row=1, column=0, sticky='w',padx=10)

        rollnoE=Entry(dataEntryFrame,textvariable=self.rollnoVar, font=('Dubai',15))
        rollnoE.grid(row=1, column=1, sticky='E')
        #First Name
        fnameL=Label(dataEntryFrame,text='First Name:',font=('Dubai',20), bg='green', fg='white')
        fnameL.grid(row=2, column=0, sticky='W', padx=10)

        fnameE=Entry(dataEntryFrame,textvariable=self.fnameVar ,font=('Dubai',15))
        fnameE.grid(row=2, column=1, sticky='E',pady=20)
        #last name
        lnameL=Label(dataEntryFrame,text='last Name:',font=('Dubai',20), bg='green', fg='white')
        lnameL.grid(row=3, column=0, sticky='W', padx=10,)

        lnameE=Entry(dataEntryFrame,textvariable=self.lnameVar,font=('Dubai',15))
        lnameE.grid(row=3, column=1, sticky='E')
        #course
        courseL=Label(dataEntryFrame,text='course:',font=('Dubai',20), bg='green', fg='white')
        courseL.grid(row=4, column=0, sticky='W', padx=10,)

        courseE=Entry(dataEntryFrame,textvariable=self.courseVar, font=('Dubai',15))
        courseE.grid(row=4, column=1, sticky='E',pady=20)
        #contact
        
        contactL=Label(dataEntryFrame,text='contact:',font=('Dubai',20), bg='green', fg='white')
        contactL.grid(row=5, column=0, sticky='W', padx=10,)

        contactE=Entry(dataEntryFrame,textvariable=self.contactVar, font=('Dubai',15))
        contactE.grid(row=5, column=1, sticky='E',)
        #Email ID
        
        emailidL=Label(dataEntryFrame,text='Email ID:',font=('Dubai',20), bg='green', fg='white')
        emailidL.grid(row=6, column=0, sticky='W', padx=10,)

        emailidE=Entry(dataEntryFrame,textvariable=self.emailVar,font=('Dubai',15))
        emailidE.grid(row=6, column=1, sticky='E',pady=20)
        #Location
        
        LocationL=Label(dataEntryFrame,text='Location:',font=('Dubai',20), bg='green', fg='white')
        LocationL.grid(row=7, column=0, sticky='W', padx=10,)

        LocationE=Entry(dataEntryFrame,textvariable=self.locationVar, font=('Dubai',15))
        LocationE.grid(row=7, column=1, sticky='E')
        #institute
                      
        instituteL=Label(dataEntryFrame,text='institute:',font=('Dubai',20), bg='green', fg='white')
        instituteL.grid(row=8, column=0, sticky='W', padx=10,)

        instituteE=Entry(dataEntryFrame,textvariable=self.instituteVar, font=('Dubai',15))
        instituteE.grid(row=8, column=1, sticky='E',pady=20,)

        # creating frame for button
        btnFrame=Frame(dataEntryFrame,bg='green', bd=5, relief=RAISED)
        btnFrame.place(x=10,y=520,width=470,height=120)

        addbtn=Button(btnFrame,text='add',command = self.addingData,font=('Dubai',15), bg='red', fg='white')
        addbtn.grid(row=0, column=0, padx=20, pady=30)


        updatebtn=Button(btnFrame,text='update',command = self.updatingData,font=('Dubai',15), bg='blue', fg='white')
        updatebtn.grid(row=0, column=1, padx= 20, pady =30)

    
        deletebtn=Button(btnFrame,text='delete',command = self.deletingData,font=('Dubai',15), bg='pink', fg='white')
        deletebtn.grid(row=0, column=2, padx=20, pady=30)

        clearbtn=Button(btnFrame,text='clear',command = self.clearingData,font=('Dubai',15), bg='black', fg='white')
        clearbtn.grid(row=0, column=3, padx=20, pady=30)


        # WORKING WITH DATA DISPLAY FRAME
        title3 = Label(dataDisplayFrame, text='Students Data display', font=('Berlin sans FB',20),bg='green', fg='white',bd=5)
        title3.place(x=300,y=20)

        tblFrame=Frame(dataDisplayFrame,  bg='green', bd=5,relief=RAISED)
        tblFrame.place(x=10,y=80,width=950,height=530)
        

        self.StudentInfo=ttk.Treeview(tblFrame,columns=('rollno','fname','lname','course','contact','email','location','institute'))
        self.StudentInfo.heading('rollno', text='Roll No')
        self.StudentInfo.heading('fname', text='First Name')
        self.StudentInfo.heading('lname',text='Last Name')
        self.StudentInfo.heading('course',text='Course')
        self.StudentInfo.heading('contact',text='Concat')
        self.StudentInfo.heading('email',text='Email ID')       
        self.StudentInfo.heading('location',text='Location')
        self.StudentInfo.heading('institute',text='Institute')
        
        self.StudentInfo.column('rollno',width=100)
        self.StudentInfo.column('fname',width=100)
        self.StudentInfo.column('lname',width=100)
        self.StudentInfo.column('course',width=100)                        
        self.StudentInfo.column('contact',width=100)
        self.StudentInfo.column('email',width=100)
        self.StudentInfo.column('location',width=100)
        self.StudentInfo.column('institute',width=100)

        self.StudentInfo['show']='headings'
        self.fetchingData()
        self.StudentInfo.pack()
        
        self.StudentInfo.bind('<ButtonRelease-1>',self.cursor_row)

    def addingData(self):
        connection=pymysql.connect(host='localhost', user='root', password='admin2k', db='studentdb')
        c=connection.cursor()               
        c.execute('insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s)',
                   (
                        self.rollnoVar.get(),
                        self.fnameVar.get(),
                        self.lnameVar.get(),
                        self.courseVar.get(),
                        self.contactVar.get(),
                        self.emailVar.get(),
                        self.locationVar.get(),
                        self.instituteVar.get()
                         ))
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()
    def clearingData(self):
        self.rollnoVar.set('')
        self.fnameVar.set('')
        self.lnameVar.set('')
        self.courseVar.set('')
        self.contactVar.set('')
        self.emailVar.set('')
        self.locationVar.set('')
        self.instituteVar.set('')

    def fetchingData(self):
        connection=pymysql.connect(host='localhost', user='root', password='admin2k', db='studentdb')
        c=connection.cursor() 
        c.execute('select * from studentdata')  
        data=c.fetchall()
        self.StudentInfo.delete(*self.StudentInfo.get_children())

        for i in data:
            self.StudentInfo.insert('',END,value=i)
        connection.commit()
        connection.close()
        
    def cursor_row(self,a):
        cursor_row=self.StudentInfo.focus()
        content=self.StudentInfo.item(cursor_row)
        row=content['values']

        self.rollnoVar.set(row[0])
        self.fnameVar.set(row[1])
        self.lnameVar.set(row[2])
        self.courseVar.set(row[3])
        self.contactVar.set(row[4])
        self.emailVar.set(row[5])
        self.locationVar.set(row[6])
        self.instituteVar.set(row[7])

    def updatingData(self):
        connection=pymysql.connect(host='localhost', user='root', password='admin2k', db='studentdb')
        c=connection.cursor()               
        c.execute('update studentdata set fname=%s,lname=%s,course=%s,contact=%s,emailid=%s,location=%s,institute=%s where rollno=%s',
                  (
                        self.fnameVar.get(),
                        self.lnameVar.get(),
                        self.courseVar.get(),
                        self.contactVar.get(),
                        self.emailVar.get(),
                        self.locationVar.get(),
                        self.instituteVar.get(),
                        self.rollnoVar.get()
                        ))

        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()

    def deletingData(self):
        connection=pymysql.connect(host='localhost', user='root', password='admin2k', db='studentdb')
        c=connection.cursor()               
        c.execute('delete from studentdata where rollno=%s',self.rollnoVar.get())
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()          


        
       
root=Tk()
s=StudentsData(root)
