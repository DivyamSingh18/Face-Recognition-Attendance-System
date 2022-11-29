from dataclasses import dataclass
from distutils import dep_util
from multiprocessing import parent_process
from os import stat
from tkinter import * # tkinter is used for GUI developlment
from tkinter import ttk
from turtle import st, width  # used to style the tkinter widgets
from PIL import Image , ImageTk
from numpy import expand_dims
from sklearn import exceptions  # image processing
from tkcalendar import DateEntry  # date entry from calender
from tkinter import messagebox   
import re    # regular expressions for email validating
import mysql.connector   # for mysql database
import cv2   # computer vision library
from pymysql.converters import escape_string




class Student:
    def __init__(self,root):  # root is window's name
        self.root = root
        self.root.geometry('1600x790+0+0')   # width x height + x_start + y_start
        self.root.title("Student Details Section")
        self.root.iconphoto(False, ImageTk.PhotoImage(file='Images/appicon.ico'))

        # ============================= variables decalaration ================================================================
        self.var_deg= StringVar()
        self.var_branch= StringVar()
        self.var_year= StringVar()
        self.var_sem= StringVar()
        self.var_stu_id= StringVar()
        self.var_stu_name= StringVar()
        self.var_roll= StringVar()
        self.var_class= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone= StringVar()

        self.radio=StringVar()
        self.radio.set('No')  # selected radio-button value by default
        self.var_dob.set('')  # default value of dob(calendar)

        # these variables are connected to their respective fields 

        img = Image.open(r'Images\student_details_uppr.jpg')
        img = img.resize((1600,130),Image.Resampling.LANCZOS)  # ANTIALIAS reduces visual defects that occur while reducing the size of image
        self.uppr_img = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image=self.uppr_img)  #creating label
        first_lbl.place(x=0,y=0,width=1600, height =130)

        # background image----------------------------------------------------------------------------------------------------
        bg_img = Image.open(r'Images\background.jpg')  # declaring image
        bg_img = bg_img.resize((1600,790),Image.Resampling.LANCZOS)  
        self.bg_img = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root,image=self.bg_img)  #creating label
        bg_lbl.place(x=0,y=130,width=1600, height =790)  # placing label on window

        #title-----------------------------------------------------------------------------
        title_lbl = Label(bg_lbl,text='Student Details   ',font=('times new roman',35,'bold'),bg='white',fg='green')
        title_lbl.place(x=0,y=0,width=1550, height =50) 

        # main Frame
        main_frame = Frame(bg_lbl,bd=2)
        main_frame.place(x=5,y=60,width=1515,height=600)

        #Left Label Frame 
        Left_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text='Details',font=('times new roman',12,'bold'))
        Left_frame.place(x=10 ,y=10,width=760, height=580)

        img_left = Image.open(r'Images\student.jpg')
        img_left = img_left.resize((735,130),Image.Resampling.LANCZOS)  # ANTIALIAS reduces visual defects that occur while reducing the size of image
        self.img_left = ImageTk.PhotoImage(img_left)

        img_left = Label(Left_frame,image=self.img_left)  #creating label
        img_left.place(x=10,y=10,width=735, height =130)

        # current course 
        curr_course_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text='Current Course Information',font=('times new roman',12,'bold'))
        curr_course_frame.place(x=20 ,y=180,width=735, height=110)

        # ..............................Degree ..................................................................
        
        deg_label =Label(curr_course_frame,text='Degree',font=('times new roman',12,'bold'))
        deg_label.grid(row=0,column=0,padx=10)

        deg_combo =ttk.Combobox(curr_course_frame,textvariable=self.var_deg,font=('times new roman',12,'bold'),state='readonly')
        deg_combo['values']= ('Select Degree','B.tech','BBA','B.Sc','BA','B.Pharmacy','BDS','MBBS','M.tech','MBA')
        deg_combo.current(0) 
        deg_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

         # ..............................Branch ..................................................................
        
        bran_label =Label(curr_course_frame,text='Branch',font=('times new roman',12,'bold'))
        bran_label.grid(row=0,column=2,padx=5)

        bran_combo =ttk.Combobox(curr_course_frame,textvariable=self.var_branch,font=('times new roman',12,'bold'),state='readonly')
        bran_combo['values']= ('Select Branch','Computer Science','Information Technology','Civil','Mechanical','Chemistry','Physics','Mathematics','Finance','Marketing','agriculture')
        bran_combo.current(0) 
        bran_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # ..............................Year ..................................................................
        
        yr_label =Label(curr_course_frame,text='Admission Year',font=('times new roman',12,'bold'))
        yr_label.grid(row=1,column=0,padx=10)

        yr_combo =ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=('times new roman',12,'bold'),state='readonly')
        yr_combo['values']= ('Select Year',2018,2019,2020,2021,2022,2023)
        yr_combo.current(0) 
        yr_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # ..............................Semester ..................................................................
        
        sem_label =Label(curr_course_frame,text='Semester',font=('times new roman',12,'bold'))
        sem_label.grid(row=1,column=2,padx=10)

        sem_combo =ttk.Combobox(curr_course_frame,textvariable=self.var_sem,font=('times new roman',12,'bold'),state='readonly')
        sem_combo['values']= ('Select Semester',1,2,3,4,5,6,7,8)
        sem_combo.current(0) 
        sem_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # student information ####################################################### next block
        stu_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text='Student Information',font=('times new roman',12,'bold'))
        stu_frame.place(x=20 ,y=300,width=735, height=280)

        #.............................stu id.........................................................................

        stu_id_label =Label(stu_frame,text='Student ID',font=('times new roman',12,'bold'))
        stu_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stu_id_entry = ttk.Entry(stu_frame,textvariable=self.var_stu_id,width=20,font=('times new roman',12,'bold'))
        stu_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #.............................Student name...................................................................

        stu_name_label =Label(stu_frame,text='Student Name',font=('times new roman',12,'bold'))
        stu_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stu_name_entry = ttk.Entry(stu_frame,textvariable=self.var_stu_name,width=20,font=('times new roman',12,'bold'))
        stu_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #.............................Student Class...................................................................

        stu_class_label =Label(stu_frame,text='Student Class',font=('times new roman',12,'bold'))
        stu_class_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        stu_class_entry = ttk.Entry(stu_frame,textvariable=self.var_class,width=20,font=('times new roman',12,'bold'))
        stu_class_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

          #.............................DOB...................................................................

        dob_label =Label(stu_frame,text='DOB',font=('times new roman',12,'bold'))
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=DateEntry(stu_frame,selectmode='day',date_pattern='yyyy-mm-dd',textvariable=self.var_dob)
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        self.var_dob.set('')



        #.............................Gender..................................................................

        gender_label =Label(stu_frame,text='Gender.',font=('times new roman',12,'bold'))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo =ttk.Combobox(stu_frame,textvariable=self.var_gender,font=('times new roman',12,'bold'),state='readonly')
        gender_combo['values']= ('Select Gender','Male','Female')
        gender_combo.current(0) 
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         #.............................Roll no................................................................email
        roll_label =Label(stu_frame,text='Roll No.',font=('times new roman',12,'bold'))
        roll_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        roll_entry = ttk.Entry(stu_frame,textvariable=self.var_roll,width=20,font=('times new roman',12,'bold'))
        roll_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #.............................Email...................................................................

        email_label =Label(stu_frame,text='Email',font=('times new roman',12,'bold'))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(stu_frame,textvariable=self.var_email,width=20,font=('times new roman',12,'bold'))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #.............................Phone no. .................................................................
        phone_label =Label(stu_frame,text='Phone No.',font=('times new roman',12,'bold'))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry = ttk.Entry(stu_frame,textvariable=self.var_phone,width=20,font=('times new roman',12,'bold'))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        
        radio1 = ttk.Radiobutton(stu_frame, text='Photo Sample Taken',variable=self.radio,value='Yes')
        radio1.grid(row=4,column=0)

        
        radio2 = ttk.Radiobutton(stu_frame, text='No Photo Sample',variable=self.radio,value='No')
        radio2.grid(row=4,column=1)

        #button Frame #############################################################################
        btn_frame = Frame(stu_frame,bd=2,relief=RIDGE,)
        btn_frame.place(x=5,y=180,width=720,height=35)

        save_btn = Button(btn_frame, text='Save',command=self.add_data,width=19,font=('times new roman',12,'bold'),bg='#50C878',cursor='hand2')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text='Update',command=self.update_data,width=19,font=('times new roman',12,'bold'),bg='#FFAC1C',cursor='hand2')
        update_btn.grid(row=0,column=1)

        del_btn = Button(btn_frame, text='Delete',command=self.delete_data,width=19,font=('times new roman',12,'bold'),bg='#CE1141',fg='white',cursor='hand2')
        del_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame, text='Reset',command=self.reset_data,width=19,font=('times new roman',12,'bold'),bg='#00AEEF',cursor='hand2')
        reset_btn.grid(row=0,column=3)

        #button Frame
        btn_frame1 = Frame(stu_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=5,y=215,width=720,height=35)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text='Take Photo Sample',width=79,font=('times new roman',12,'bold'),bg='#FFB6C1',cursor='hand2')
        take_photo_btn.grid(row=0,column=0)

        # update_photo_btn = Button(btn_frame1, text='Update Photo Sample',width=39,font=('times new roman',12,'bold'),bg='#FFB6C1',cursor='hand2')
        # update_photo_btn.grid(row=0,column=1)




        #Right Label Frame 
        Right_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text='Data',font=('times new roman',12,'bold'))
        Right_frame.place(x=780 ,y=10,width=720, height=580)

        #..................................  Search System  ..............................................................

        search_frame = LabelFrame(Right_frame, bd=2,relief=RIDGE,text='Search System',font=('times new roman',12,'bold'))
        search_frame.place(x=10 ,y=0,width=695, height=80)

        search_label =Label(search_frame,text='Search by:',font=('times new roman',13,'bold'),bg='#E4D00A')
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        self.combo= StringVar()
        search_combo =ttk.Combobox(search_frame,textvariable=self.combo,font=('times new roman',12,'bold'),state='readonly')
        search_combo['values']= ('Select','Roll_No','Name','Year')
        search_combo.current(0) 
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        self.var_search_by= StringVar()
        search_entry = ttk.Entry(search_frame,width=20,textvariable=self.var_search_by,font=('times new roman',12,'bold'))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn = Button(search_frame,command=self.search_by, text='Search',width=10,font=('times new roman',12,'bold'),bg='#50C878',cursor='hand2')
        search_btn.grid(row=0,column=3)

        showall_btn = Button(search_frame, text='Show All',command=self.fetch_data,width=10,font=('times new roman',12,'bold'),bg='#50C878',cursor='hand2')
        showall_btn.grid(row=0,column=4)

        # table frame

        table_frame = Frame(Right_frame, bd=2,relief=RIDGE)
        table_frame.place(x=10 ,y=90,width=695, height=460)


        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=('Degree','Branch','Year','Sem','ID','Name','Class','DOB','Gender','Roll no.','Email','Phone','Photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # to show the column headings 
        self.student_table.heading('Degree',text='Degree')
        self.student_table.heading('Branch',text='Branch')
        self.student_table.heading('Year',text='Year')
        self.student_table.heading('Sem',text='Sem')
        self.student_table.heading('ID',text='ID')
        self.student_table.heading('Name',text='Name')
        self.student_table.heading('Class',text='Class')
        self.student_table.heading('DOB',text='DOB')
        self.student_table.heading('Gender',text='Gender')
        self.student_table.heading('Roll no.',text='Roll no.')
        self.student_table.heading('Email',text='Email')
        self.student_table.heading('Phone',text='Phone')
        self.student_table.heading('Photo',text='PhotoSampleStatus')
        self.student_table['show'] = 'headings'

        #setting the width of columns 
        self.student_table.column('Degree',width=100)
        self.student_table.column('Branch',width=100)
        self.student_table.column('Year',width=100)
        self.student_table.column('Sem',width=100)
        self.student_table.column('ID',width=100)
        self.student_table.column('Name',width=100)
        self.student_table.column('Class',width=100)
        self.student_table.column('Roll no.',width=100)
        self.student_table.column('Gender',width=100)
        self.student_table.column('DOB',width=100)
        self.student_table.column('Phone',width=100)
        self.student_table.column('Email',width=150)
        self.student_table.column('Photo',width=150)
        self.student_table['show'] = 'headings'
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor)  # binding(connecting) the event with function
        self.fetch_data()   # fetches the data on opening the window

    # _______________________________________ Button Functions_______________________________________________________

    def add_data(self):

      # errors for course column
      if self.var_deg.get() == 'Select Degree' or self.var_branch.get() == 'Select Branch' or self.var_year.get() == 'Select Year' or self.var_sem.get() == 'Select Semester':
        messagebox.showerror('Error','Fill all the Details',parent=self.root)

      # errors for student id
      elif self.var_stu_id.get() == '' or self.var_stu_id.get() == 0:
        messagebox.showerror('Error','Student ID cannot be empty or zero!',parent=self.root)

      elif not self.var_stu_id.get().isdigit():
        messagebox.showerror('Error','Student ID must be Filled Correctly (numeric value)',parent=self.root)

      #errors for student name
      elif self.var_stu_name.get() == '':
        messagebox.showerror('Error','Student Name cannot be empty!',parent=self.root)

      elif not self.var_stu_name.get().replace(' ','').isalpha():
        messagebox.showerror('Error','Student Name must be Filled Correctly (alphabets only)',parent=self.root)

      elif len(self.var_stu_name.get()) <= 2 or  len(self.var_stu_name.get()) >25:
        messagebox.showerror('Error','Length of Student Name should be from 3 to 25 characters!',parent=self.root)

      #errors for student class
      elif self.var_class.get() == '':
        messagebox.showerror('Error','Student Class cannot be empty!',parent=self.root)

      elif not self.var_class.get().isalnum():
        messagebox.showerror('Error','Student Class can not contain special characters like -, +, @, _, etc',parent=self.root)

      #errors for gender
      elif self.var_gender.get() == 'Select Gender':
        messagebox.showerror('Error','Please, Select a Gender.',parent=self.root)
      
      #errors for Roll no
      elif self.var_roll.get() == '' or self.var_roll.get() == 0 :
        messagebox.showerror('Error','Roll No. cannot be empty or zero!',parent=self.root)
      
      elif not self.var_roll.get().isdigit():
        messagebox.showerror('Error','Roll No. must be Filled Correctly (numeric value)',parent=self.root)

      #errors for email
      elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',self.var_email.get()):
        messagebox.showerror('Error','Invalid Email Address!',parent=self.root)
      
      elif self.var_email.get() == '':
        messagebox.showerror('Error','Email Address cannot be empty!',parent=self.root)

      #errors for phone no
      elif self.var_phone.get() == '' :
        messagebox.showerror('Error','Phone No. cannot be empty!',parent=self.root)
      
      elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
        messagebox.showerror('Error','Invalid Phone number',parent=self.root)

      else:
        try:       # conn stands for connection #########################  mySQL  ###################################
          conn = mysql.connector.connect(host='localhost',username='root',password='987@Cs',database='data')
          my_cursor = conn.cursor()
          my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_deg.get(),
            self.var_branch.get(),
            self.var_year.get(),
            self.var_sem.get(),
            self.var_stu_id.get(),
            self.var_stu_name.get(),
            self.var_class.get(),
            self.var_dob.get(),
            self.var_gender.get(),
            self.var_roll.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.radio.get()
          ))
          conn.commit()
          self.fetch_data()   # fetches the data after adding it to the database
          conn.close()
          messagebox.showinfo("Success",'Student data has been added successfully.',parent=self.root)
        
        except Exception as e:
          messagebox.showerror('SQL Error',f'Due to:{str(e)}',parent=self.root)


    # ------------------------- Fetching data from MySQL --------------------------------------------------------------
    def fetch_data(self):
      conn = mysql.connector.connect(host='localhost',username='root',password='987@Cs',database='data')
      my_cursor = conn.cursor()   
      my_cursor.execute('select * from student')
      data= my_cursor.fetchall()

      if len(data)!= 0:
        self.student_table.delete(*self.student_table.get_children())  # delete previous student_table data

        for i in data:
          self.student_table.insert('',END,values=i)
          conn.commit()
      elif len(data)==0:
          self.student_table.delete(*self.student_table.get_children())
          conn.commit()
      conn.close()

    #-------------------------------------get cursor (put the data into the entry fields)-----------------------

    def get_cursor(self,event=''):
      cursor_focus = self.student_table.focus()
      content = self.student_table.item(cursor_focus)
      data = content['values']

      self.var_deg.set(data[0])
      self.var_branch.set(data[1])
      self.var_year.set(data[2])
      self.var_sem.set(data[3])
      self.var_stu_id.set(data[4])
      self.var_stu_name.set(data[5])
      self.var_class.set(data[6])
      self.var_dob.set(data[7])
      self.var_gender.set(data[8])
      self.var_roll.set(data[9])
      self.var_email.set(data[10])
      self.var_phone.set(data[11])
      self.radio.set(data[12])

    # -------------------------- Update Function -------------------------------------------------------
    def update_data(self):
       
      # errors for course column
      if self.var_deg.get() == 'Select Degree' or self.var_branch.get() == 'Select Branch' or self.var_year.get() == 'Select Year' or self.var_sem.get() == 'Select Semester':
        messagebox.showerror('Error','Fill all the Details',parent=self.root)

      # errors for student id
      elif self.var_stu_id.get() == '' or self.var_stu_id.get() == 0:
        messagebox.showerror('Error','Student ID cannot be empty or zero!',parent=self.root)

      elif not self.var_stu_id.get().isdigit():
        messagebox.showerror('Error','Student ID must be Filled Correctly (numeric value)',parent=self.root)

      #errors for student name
      elif self.var_stu_name.get() == '':
        messagebox.showerror('Error','Student Name cannot be empty!',parent=self.root)

      elif not self.var_stu_name.get().replace(' ','').isalpha():
        messagebox.showerror('Error','Student Name must be Filled Correctly (alphabets only)',parent=self.root)

      elif len(self.var_stu_name.get()) <= 2 or  len(self.var_stu_name.get()) >25:
        messagebox.showerror('Error','Length of Student Name should be from 3 to 25 characters!',parent=self.root)

      #errors for student class
      elif self.var_class.get() == '':
        messagebox.showerror('Error','Student Class cannot be empty!',parent=self.root)

      elif not self.var_class.get().isalnum():
        messagebox.showerror('Error','Student Class can not contain special characters like -, +, @, _, etc',parent=self.root)

      #errors for gender
      elif self.var_gender.get() == 'Select Gender':
        messagebox.showerror('Error','Please, Select a Gender.',parent=self.root)
      
      #errors for Roll no
      elif self.var_roll.get() == '' or self.var_roll.get() == 0 :
        messagebox.showerror('Error','Roll No. cannot be empty or zero!',parent=self.root)
      
      elif not self.var_roll.get().isdigit():
        messagebox.showerror('Error','Roll No. must be Filled Correctly (numeric value)',parent=self.root)

      #errors for email
      elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',self.var_email.get()):
        messagebox.showerror('Error','Invalid Email Address!',parent=self.root)
      
      elif self.var_email.get() == '':
        messagebox.showerror('Error','Email Address cannot be empty!',parent=self.root)

      #errors for phone no
      elif self.var_phone.get() == '' :
        messagebox.showerror('Error','Phone No. cannot be empty!',parent=self.root)
      
      elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
        messagebox.showerror('Error','Invalid Phone number',parent=self.root)
      else:
        try:
          update= messagebox.askyesno('Update',"Do you want to update this student's details \n WARNING: Please Note that the student ID can not be updated!",parent=self.root)
          if update==True:
            conn = mysql.connector.connect(host='localhost',username='root',password='987@Cs',database='data')
            my_cursor = conn.cursor()
            my_cursor.execute('update student set Degree=%s,Branch=%s,Year=%s,Sem=%s,ID=%s,Name=%s,Class=%s,DOB=%s,Gender=%s,Roll_No=%s,Email=%s,Phone=%s,PhotoSampleStatus=%s where ID =%s',(
            self.var_deg.get(),
            self.var_branch.get(),
            self.var_year.get(),
            self.var_sem.get(),
            self.var_stu_id.get(),
            self.var_stu_name.get(),
            self.var_class.get(),
            self.var_dob.get(),
            self.var_gender.get(),
            self.var_roll.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.radio.get(),
            self.var_stu_id.get()
            ))
          else:
            return
          messagebox.showinfo('Success','Information successfully updated.',parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()

        except Exception as e:
          messagebox.showerror('Error',f'Due to: {str(e)}',parent=self.root) 

    # -------------------------- Delete Function -------------------------------------------------------
    def delete_data(self):
      if self.var_stu_id.get() == '':
        messagebox.showerror('Error','Student ID is required to perform delete operation',parent=self.root)
      else:
        try:
          delete =messagebox.askyesno('Delete','The data will be permanently deleted,are you sure?',parent=self.root)
          if delete:
            conn = mysql.connector.connect(host='localhost',username='root',password='987@Cs',database='data')
            my_cursor = conn.cursor()
            my_cursor.execute('delete from student where ID=%s',(self.var_stu_id.get(),))
          elif not delete:
            return
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo('Data Deleted','Data is successfully deleted from the database.')
        except Exception as e:
          messagebox.showerror('Error',f'Due to: {str(e)}',parent=self.root)


    # ---------------------------------- Reset Function --------------------------------------------------
    
    def reset_data(self):
      self.var_deg.set('Select Degree')
      self.var_branch.set('Select Branch')  
      self.var_year.set('Select Year')  
      self.var_sem.set('Select Semester')  
      self.var_stu_id.set('')  
      self.var_stu_name.set('')  
      self.var_class.set('')
      self.var_dob.set('')  
      self.var_gender.set('Select Gender')  
      self.var_roll.set('')          
      self.var_email.set('')  
      self.var_phone.set('')  
      self.radio.set('No')    

    #----------------------------- Taking photos(generate dataset) ------------------------------------------

    def generate_dataset(self):
       # errors for course column
      if self.var_deg.get() == 'Select Degree' or self.var_branch.get() == 'Select Branch' or self.var_year.get() == 'Select Year' or self.var_sem.get() == 'Select Semester':
        messagebox.showerror('Error','Fill all the Details',parent=self.root)

      # errors for student id
      elif self.var_stu_id.get() == '' or self.var_stu_id.get() == 0:
        messagebox.showerror('Error','Student ID cannot be empty or zero!',parent=self.root)

      elif not self.var_stu_id.get().isdigit():
        messagebox.showerror('Error','Student ID must be Filled Correctly (numeric value)',parent=self.root)

      #errors for student name
      elif self.var_stu_name.get() == '':
        messagebox.showerror('Error','Student Name cannot be empty!',parent=self.root)

      elif not self.var_stu_name.get().replace(' ','').isalpha():
        messagebox.showerror('Error','Student Name must be Filled Correctly (alphabets only)',parent=self.root)

      elif len(self.var_stu_name.get()) <= 2 or  len(self.var_stu_name.get()) >25:
        messagebox.showerror('Error','Length of Student Name should be from 3 to 25 characters!',parent=self.root)

      #errors for student class
      elif self.var_class.get() == '':
        messagebox.showerror('Error','Student Class cannot be empty!',parent=self.root)

      elif not self.var_class.get().isalnum():
        messagebox.showerror('Error','Student Class can not contain special characters like -, +, @, _, etc',parent=self.root)

      #errors for gender
      elif self.var_gender.get() == 'Select Gender':
        messagebox.showerror('Error','Please, Select a Gender.',parent=self.root)
      
      #errors for Roll no
      elif self.var_roll.get() == '' or self.var_roll.get() == 0 :
        messagebox.showerror('Error','Roll No. cannot be empty or zero!',parent=self.root)
      
      elif not self.var_roll.get().isdigit():
        messagebox.showerror('Error','Roll No. must be Filled Correctly (numeric value)',parent=self.root)

      #errors for email
      elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',self.var_email.get()):
        messagebox.showerror('Error','Invalid Email Address!',parent=self.root)
      
      elif self.var_email.get() == '':
        messagebox.showerror('Error','Email Address cannot be empty!',parent=self.root)

      #errors for phone no
      elif self.var_phone.get() == '' :
        messagebox.showerror('Error','Phone No. cannot be empty!',parent=self.root)
      
      elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
        messagebox.showerror('Error','Invalid Phone number',parent=self.root)
      else:
        try:
           # updating the value of Photo Taken Status after getting the data
          conn = mysql.connector.connect(host='localhost',username='root',password='987@Cs',database='data')
          my_cursor = conn.cursor()
          my_cursor.execute('update student set PhotoSampleStatus=%s where ID=%s',
          (
            'Yes',
            self.var_stu_id.get()))

          conn.commit()

          # connecting the id of photo to the student id 
          my_cursor.execute('select * from student')
          my_result = my_cursor.fetchall()
          id = 0
          for i in my_result:
            id+=1
          
          my_cursor.execute('update student set Degree=%s,Branch=%s,Year=%s,Sem=%s,ID=%s,Name=%s,Class=%s,DOB=%s,Gender=%s,Roll_No=%s,Email=%s,Phone=%s,PhotoSampleStatus=%s where ID =%s',(
            self.var_deg.get(),
            self.var_branch.get(),
            self.var_year.get(),
            self.var_sem.get(),
            self.var_stu_id.get(),
            self.var_stu_name.get(),
            self.var_class.get(),
            self.var_dob.get(),
            self.var_gender.get(),
            self.var_roll.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.radio.get(),  
            self.var_stu_id.get() == id+1  # mapping of id with Student ids 
            ))
          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()

          

          
          # ---------------------------------------- openCV -----------------------------------------------

          # 'haarcascade_frontalface_default.xml' file contains a pre-trained model that was created through extensive training and uploaded by Rainer Lienhart on behalf of Intel in 2000. Rainer's model makes use of the Adaptive Boosting Algorithm (AdaBoost) in order to yield better results and accuracy.

          face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # model loaded

          def face_crop(img):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # converting rgb image into grey image
            faces = face_classifier.detectMultiScale(gray,1.3,5)  # 1.3 is scaling factor, 5 is minimum neighbor
            
            for (x,y,w,h) in faces:      # creates rectangle around the face
              face_cropped = img[y:y+h,x:x+w]
              return face_cropped

          capture =cv2.VideoCapture(0) #opens webcam
          
          img_id = 0
          while True:              # clicking 100 images and turning them into grayscale 
            ret,myframe = capture.read()    
            if face_crop(myframe) is not None:
              img_id+=1
              face = cv2.resize(face_crop(myframe),(450,450))
              face= cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

              #putting image in the given data folder
              file_path = 'data/user_'+str(id)+'_'+str(img_id)+'.jpg'
              cv2.imwrite(file_path,face)

              #showing text and image on screen 
              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
              cv2.imshow("Cropped Face",face)

            if cv2.waitKey(1) == 13 or int(img_id) == 100:    # 13 means pressing enter key 
              break      # break infinite loop
          
          capture.release()
          cv2.destroyAllWindows()
          messagebox.showinfo('Result','Dataset generated successfully.')

        except Exception as e:
          messagebox.showerror('Error',f'Due to:{str(e)}',parent=self.root)

    def search_by(self):
      conn = mysql.connector.connect(host='localhost',username='root',password='987@Cs',database='data')
      my_cursor = conn.cursor()  
      my_cursor.execute("select * from student where "+ self.combo.get()+" = %s",(
        self.var_search_by.get(),)
          )
      sql = my_cursor.statement
      print(sql)

      data= my_cursor.fetchall()
      print(data)
      if len(data)!= 0:
        self.student_table.delete(*self.student_table.get_children())  # delete previous student_table data

        for i in data:
          self.student_table.insert('',END,values=i)
          conn.commit()
      elif len(data)==0:
          self.student_table.delete(*self.student_table.get_children())
          conn.commit()
      conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = Student(root)   # create an instance of class 
    root.mainloop()      # starts the main loop
    