from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
     def __init__(self,root):
          
         self.root = root
         titlespace = " "
         self.root.title(102 * titlespace + "Student Record")
         self.root.geometry("800x700+300+0")
         self.root.resizable(width = False, height=False)

         MainFrame = Frame (self.root, bd=10, width = 770, height=700, relief= RIDGE, bg='cadet blue')
         MainFrame.grid()

         TitleFrame = Frame (MainFrame, bd=7, width = 770, height=100, relief= RIDGE)
         TitleFrame.grid(row= 0, column= 0)

         TopFrame = Frame (MainFrame, bd=5, width = 770, height=500, relief= RIDGE)
         TopFrame.grid(row= 1, column= 0)

         LeftFrame = Frame (TopFrame, bd=5, width = 770, height=400,padx=2, bg='cadet blue', relief= RIDGE)
         LeftFrame.pack(side=LEFT)
         LeftFrame1= Frame (LeftFrame, bd=5, width = 600, height=180,padx=12,pady=9, relief= RIDGE)
         LeftFrame1.pack(side=TOP)

         RightFrame = Frame (TopFrame, bd=5, width = 100, height=400,padx=2,bg='cadet blue', relief= RIDGE)
         RightFrame.pack(side=RIGHT)
         RightFrame1= Frame (RightFrame, bd=5, width = 90, height=300,padx=2,pady=2, relief= RIDGE)
         RightFrame1.pack(side=TOP)
         #==============================================================
         studentid=StringVar()
         firstname=StringVar()
         lastname=StringVar()
         address=StringVar()
         gender=StringVar()
         mobile=StringVar()
         #==========================================================
         def iExit ():

             iExit = tkinter.messagebox.askyesno("Student Record","Confirm if you want to exit")
             if iExit > 0:
                 root.destroy()
                 return

         def reset ():
             self.enid.delete(0,END)
             self.enfstname.delete(0,END)
             self.enlstname.delete(0,END)
             self.enaddress.delete(0,END)
             gender.set("")
             self.enmobile.delete(0,END)


         

                


             
         #================================================================
         self.lbtitle=Label(TitleFrame, font=('arial',40,'bold'),text="Student Record",bd=7)
         self.lbtitle.grid(row=0,column=0,padx=132)

         self.lbid=Label(LeftFrame1, font=('arial',12,'bold'),text="STUDENT ID",bd=7)
         self.lbid.grid(row=0,column=0,padx=5, sticky=W)
         self.enid=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44, justify='left', textvariable=studentid)
         self.enid.grid(row=0,column=1,padx=5, sticky=W)
         
         self.lbfstname=Label(LeftFrame1, font=('arial',12,'bold'),text="First Name",bd=7)
         self.lbfstname.grid(row=1,column=0,padx=5, sticky=W)
         self.enfstname=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44, justify='left', textvariable=firstname)
         self.enfstname.grid(row=1,column=1,padx=5, sticky=W)
        
         self.lblstname=Label(LeftFrame1, font=('arial',12,'bold'),text="Last Name",bd=7)
         self.lblstname.grid(row=2,column=0,padx=5, sticky=W)
         self.enlstname=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44, justify='left', textvariable=lastname)
         self.enlstname.grid(row=2,column=1,padx=5, sticky=W)
        #====================================================================
         self.lbaddress=Label(LeftFrame1, font=('arial',12,'bold'),text="Address",bd=7)
         self.lbaddress.grid(row=3,column=0,padx=5, sticky=W)
         self.enaddress=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44, justify='left', textvariable=address)
         self.enaddress.grid(row=3,column=1)
         
         self.lbgender=Label(LeftFrame1, font=('arial',12,'bold'),text="Gender",bd=5)
         self.lbgender.grid(row=4,column=0,padx=5, sticky=W)
         self.comgender=ttk.Combobox(LeftFrame1, font=('arial',12,'bold'),state='readonly',width=42, textvariable=gender)
         self.comgender['values']=(' ', 'Male','Female')
         self.comgender.current(0)
         self.comgender.grid(row=4,column=1)
        
         self.lbmobile=Label(LeftFrame1, font=('arial',12,'bold'),text="Mobile",bd=7)
         self.lbmobile.grid(row=5,column=0,padx=5, sticky=W)
         self.enmobile=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44, justify='left', textvariable=mobile)
         self.enmobile.grid(row=5,column=1,padx=5, sticky=W)
         #===========================================================================
         scrolly=Scrollbar(LeftFrame, orient=VERTICAL)
         self.studentrecord=ttk.Treeview(LeftFrame, height=14, columns=("stdid","firstname","lastname","address","gender","mobile"),yscrollcommand= scrolly.set)
         scrolly.pack(side=RIGHT, fill=Y)

         self.studentrecord.heading("stdid",text="StudentID")
         self.studentrecord.heading("firstname",text="First Name")
         self.studentrecord.heading("lastname",text="Last Name")
         self.studentrecord.heading("address",text="Address")
         self.studentrecord.heading("gender",text="Gender")
         self.studentrecord.heading("mobile",text="Mobile")

         self.studentrecord['show']='headings'

         self.studentrecord.column("stdid", width=70)
         self.studentrecord.column("firstname", width=100)
         self.studentrecord.column("lastname", width=100)
         self.studentrecord.column("address", width=100)
         self.studentrecord.column("gender", width=70)
         self.studentrecord.column("mobile", width=70)

         self.studentrecord.pack(fill =BOTH, expand=1)
         #===========================================================================
         self.btnaddnew=Button(RightFrame1,font=('arial',16,'bold'),text="Add New",bd=4, padx=24, pady=1, width=8, height=2,).grid(row=1,column=0,padx=1)
         self.btndisplay=Button(RightFrame1,font=('arial',16,'bold'),text="Display",bd=4, padx=24, pady=1, width=8, height=2).grid(row=2,column=0,padx=1)
         self.btnupdate=Button(RightFrame1,font=('arial',16,'bold'),text="Update",bd=4, padx=24, pady=1, width=8, height=2).grid(row=3,column=0,padx=1)
         self.btndelete=Button(RightFrame1,font=('arial',16,'bold'),text="Delete",bd=4, padx=24, pady=1, width=8, height=2).grid(row=4,column=0,padx=1)
         self.btnsearch=Button(RightFrame1,font=('arial',16,'bold'),text="Search",bd=4, padx=24, pady=1, width=8, height=2).grid(row=5,column=0,padx=1)
         self.btnreset=Button(RightFrame1,font=('arial',16,'bold'),text="Reset",bd=4, padx=24, pady=1, width=8, height=2, command=reset).grid(row=6,column=0,padx=2)
         self.btnexit=Button(RightFrame1,font=('arial',16,'bold'),text="Exit",bd=4, padx=24, pady=1, width=8, height=2, command=iExit).grid(row=7,column=0,padx=1)

         #===========================================================================
        
        











if __name__=='__main__':
    root=Tk()
    application = ConnectorDB(root)
    root.mainloop()
     
     