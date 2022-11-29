from multiprocessing import parent_process
from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog    



data = [] 

class Attendance_Record:
    def __init__(self, root):
        self.root= root
        self.root.geometry('1600x790+0+0')   # width x height + x_start + y_start
        self.root.title("Divyam's Application")

        # ==========================================  Variables  ========================================================================================

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_class = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()




         #title
        title_lbl = Label(self.root, text="Attendance Record",font=('times new roman',35,'bold'),bg='#87CEEB',fg='Blue')
        title_lbl.place(x=0,y=0,width=1600, height=55,)

        # background image----------------------------------------------------------------------------------------------------
        bg_img = Image.open(r'C:Images\background.jpg')  # declaring image
        bg_img = bg_img.resize((1600,790),Image.Resampling.LANCZOS)  
        self.bg_img = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root,image=self.bg_img)  #creating label
        bg_lbl.place(x=0,y=55,width=1600, height =790)  # placing label on window

        # main Frame
        main_frame = Frame(bg_lbl,bd=2)
        main_frame.place(x=5,y=60,width=1515,height=600)

         #Left Label Frame 
        Left_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text='Details',font=('times new roman',12,'bold'))
        Left_frame.place(x=10 ,y=10,width=760, height=580)

        img_left = Image.open(r'Images\attendance_matters.jpg')
        img_left = img_left.resize((735,230),Image.Resampling.LANCZOS)  # ANTIALIAS reduces visual defects that occur while reducing the size of image
        self.img_left = ImageTk.PhotoImage(img_left)

        img_left = Label(Left_frame,image=self.img_left)  #creating label
        img_left.place(x=10,y=10,width=735, height =230)

        # left Frame
        left_inside_frame = Frame(Left_frame,bd=2, relief=RIDGE)
        left_inside_frame.place(x=10,y=250,width=735,height=300)
        
        # ############################################## entery fields ########################################################################

        #.............................stu id.........................................................................

        stu_id_label =Label(left_inside_frame,text='Student ID',font=('times new roman',12,'bold'))
        stu_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stu_id_entry_atten = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=('times new roman',12,'bold'))
        stu_id_entry_atten.grid(row=0,column=1,padx=10,pady=5,sticky=W)        

        #.............................Student name...................................................................

        stu_name_label =Label(left_inside_frame,text='Student Name',font=('times new roman',12,'bold'))
        stu_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stu_name_entry_atten = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=('times new roman',12,'bold'))
        stu_name_entry_atten.grid(row=0,column=3,padx=10,pady=15,sticky=W)

        #.............................Roll no...............................................................
        roll_label =Label(left_inside_frame,text='Roll No.',font=('times new roman',12,'bold'))
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=('times new roman',12,'bold'))
        roll_entry.grid(row=1,column=1,padx=10,pady=15,sticky=W)


        #.............................Student Class...................................................................

        stu_class_label =Label(left_inside_frame,text='Student Class',font=('times new roman',12,'bold'))
        stu_class_label.grid(row=1,column=2,padx=10,pady=15,sticky=W)

        stu_class_entry_atten = ttk.Entry(left_inside_frame,textvariable=self.var_atten_class,width=20,font=('times new roman',12,'bold'))
        stu_class_entry_atten.grid(row=1,column=3,padx=10,pady=15,sticky=W)

        #.............................  Date   ...................................................................

        date_label =Label(left_inside_frame,text='Date',font=('times new roman',12,'bold'))
        date_label.grid(row=2,column=0,padx=10,pady=15,sticky=W)

        atten_date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=('times new roman',12,'bold'))
        atten_date_entry.grid(row=2,column=1,padx=10,pady=15,sticky=W)

        #.............................  Time   ...................................................................

        atten_time_label =Label(left_inside_frame,text='Time',font=('times new roman',12,'bold'))
        atten_time_label.grid(row=2,column=2,padx=10,pady=15,sticky=W)

        atten_time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=('times new roman',12,'bold'))
        atten_time_entry.grid(row=2,column=3,padx=10,pady=15,sticky=W)

        #.............................attendance status..................................................................

        status_label =Label(left_inside_frame,text='Attendance Status',font=('times new roman',12,'bold'))
        status_label.grid(row=3,column=0,padx=10,pady=15,sticky=W)

        status_combo =ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=('times new roman',12,'bold'),state='readonly')
        status_combo['values']= ('Select Status','Present','Absent')
        status_combo.current(0) 
        status_combo.grid(row=3,column=1,padx=10,pady=15,sticky=W)


        ##################################### button Frame #############################################################################
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,)
        btn_frame.place(x=5,y=220,width=720,height=70)

        import_btn = Button(btn_frame, text='Import CSV',command=self.import_csv,width=40,font=('times new roman',12,'bold'),bg='#FFB6C1',cursor='hand2')
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame, text='Export CSV',command=self.export_csv,width=40,font=('times new roman',12,'bold'),bg='#FFB6C1',cursor='hand2')
        export_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame, text='Update',width=40,font=('times new roman',12,'bold'),bg='#FFAC1C',cursor='hand2')
        update_btn.grid(row=1,column=0)

        reset_btn = Button(btn_frame, text='Reset',command=self.reset_data,width=40,font=('times new roman',12,'bold'),bg='#00AEEF',cursor='hand2')
        reset_btn.grid(row=1,column=1)

        #Right Label Frame 
        Right_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,text='Data',font=('times new roman',12,'bold'))
        Right_frame.place(x=780 ,y=10,width=720, height=580)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=10,y=5,width=695,height=545)

        # scroll bars +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attend_report_table = ttk.Treeview(table_frame,column=('ID','Name','Roll no','Class','Date','Time','Attendance'),
        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side= RIGHT , fill=Y)

        scroll_x.config(command=self.attend_report_table.xview)
        scroll_y.config(command=self.attend_report_table.yview)

         # to show the column headings 
        self.attend_report_table.heading('ID',text='ID')
        self.attend_report_table.heading('Name',text='Name')
        self.attend_report_table.heading('Roll no',text='Roll no')
        self.attend_report_table.heading('Class',text='Class')
        self.attend_report_table.heading('Date',text='Date')
        self.attend_report_table.heading('Time',text='Time')
        self.attend_report_table.heading('Attendance',text='Attendance')

        self.attend_report_table['show'] = 'headings'

        #setting the width of columns 
        self.attend_report_table.column('ID',width=100)
        self.attend_report_table.column('Name',width=100)
        self.attend_report_table.column('Attendance',width=100)
        self.attend_report_table.column('Class',width=100)
        self.attend_report_table.column('Roll no',width=100)
        self.attend_report_table.column('Date',width=100)
        self.attend_report_table.column('Time',width=100)
        
        self.attend_report_table.pack(fill=BOTH,expand=1)

        self.attend_report_table.bind('<ButtonRelease>',self.get_cursor)

    # ========================================  FUNCTIONS ===========================================================================

    def fetch_data(self,rows):
        self.attend_report_table.delete(*self.attend_report_table.get_children())
        for i in rows:
            self.attend_report_table.insert('',END,values=i)
    
    # import csv function
    def import_csv(self):
        global data
        data.clear()
        file_find= filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV file",filetypes=(('CSV File','*.csv'),('ALL FILE','*.*')),parent=self.root)
        with open(file_find) as myfile:
            csvread = csv.reader(myfile, delimiter=',')
            for i in csvread:
                data.append(i)   #appending the elements of the csv file into the empty list named 'data'
            self.fetch_data(data)  # fetching the data from the data list to the attend_report_table

    # export csv function
    def export_csv(self):
        try:
            if len(data) < 1:
                messagebox.showerror('No Data','No Data found to export.',parent=self.root)
                return False

            file_saved= filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV file",filetypes=(('CSV File','*.csv'),('ALL FILE','*.*')),parent=self.root)
            if file_saved == True:
                with open(file_saved,'w',newline='') as file:
                    export_write = csv.writer(file,delimiter=',')    # declaring export_write variable for writing data
                    for i in data:
                        export_write.writerow(i)      # appending/writing data in export_write
                    messagebox.showinfo("Data Exported","Your Data is successfully exported to "+ os.path.basename(file_saved))
        except Exception as e:
            messagebox.showerror('Error',f"Due to: {str(e)}",parent=self.root)


    #-------------------------------------get cursor (put the data into the entry fields)-----------------------

    def get_cursor(self,event=''):
      cursor_focus = self.attend_report_table.focus()
      content = self.attend_report_table.item(cursor_focus)
      data = content['values']

      self.var_atten_id.set(data[0])
      self.var_atten_name.set(data[1])
      self.var_atten_roll.set(data[2])
      self.var_atten_class.set(data[3])
      self.var_atten_date.set(data[4])
      self.var_atten_time.set(data[5])
      self.var_atten_attendance.set(data[6]) 

    # ---------------------------------- Reset Function --------------------------------------------------
    
    def reset_data(self):
      self.var_atten_id.set('')
      self.var_atten_name.set('')
      self.var_atten_roll.set('')
      self.var_atten_class.set('')
      self.var_atten_date.set('')
      self.var_atten_time.set('')
      self.var_atten_attendance.set('Select Status') 

            
            

            




if __name__ == '__main__':
    root = Tk()
    obj =Attendance_Record(root)
    root.mainloop()
          