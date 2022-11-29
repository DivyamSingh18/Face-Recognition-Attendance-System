from tkinter import * # tkinter is used for GUI developlment
from tkinter import ttk  # used to style the tkinter widgets
from PIL import Image , ImageTk  # image processing
from student import Student
from take_attendance import Take_attendance
from attendance_record import Attendance_Record
from chatbot import Chatbot
from feedback_section import Feedback_Section

class Face_recognition:
    def __init__(self,root):  # root is window's name
        self.root = root
        self.root.geometry('1600x790+0+0')   # width x height + x_start + y_start
        self.root.title("Face Recognition Attendance System")
        self.root.iconphoto(False, ImageTk.PhotoImage(file='Images/appicon.ico'))

        # background image----------------------------------------------------------------------------------------------------
        bg_img = Image.open(r'Images\background.jpg')  # declaring image
        bg_img = bg_img.resize((1600,790),Image.Resampling.LANCZOS)  
        self.bg_img = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root,image=self.bg_img)  #creating label
        bg_lbl.place(x=0,y=0,width=1600, height =790)  # placing label on window

        # BUTTONS------------------------------------------------------------------------------------------------------------------

        #  button image 1  (ROW 1)
        btn_img = Image.open(r'Images\student_details.webp')  # declaring image
        btn_img = btn_img.resize((250,220),Image.Resampling.LANCZOS)  
        self.btn_img = ImageTk.PhotoImage(btn_img)

        b1_img = Label(bg_lbl, image= self.btn_img)
        b1_img.place(x=240,y=100,width=250,height=220)
        #button
        b1_txt = Button(bg_lbl,text='Student Details',command= self.student_details, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_txt.place(x=240,y=300,width=250,height=40)

        #  button image 2
        btn_img2 = Image.open(r'Images\attendance.jpg')  # declaring image
        btn_img2 = btn_img2.resize((250,220),Image.Resampling.LANCZOS)  
        self.btn_img2 = ImageTk.PhotoImage(btn_img2)

        b2_img = Label(bg_lbl, image= self.btn_img2)
        b2_img.place(x=600,y=100,width=250,height=220)
        #button
        b2_txt = Button(bg_lbl,text='Take Attendance',command=self.take_attendance, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2_txt.place(x=600,y=300,width=250,height=40)

        #  button image 3
        btn_img3 = Image.open(r'Images\attendance_record.jpg')  # declaring image
        btn_img3 = btn_img3.resize((250,220),Image.Resampling.LANCZOS)  
        self.btn_img3 = ImageTk.PhotoImage(btn_img3)

        b3_img = Label(bg_lbl, image= self.btn_img3)
        b3_img.place(x=960,y=100,width=250,height=220)
        #button
        b3_txt = Button(bg_lbl,text='Attendance Record',command=self.attendance_record, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b3_txt.place(x=960,y=300,width=250,height=40)

        #  #  button image 4
        # btn_img4 = Image.open(r'Images\backg.jpg')  # declaring image
        # btn_img4 = btn_img4.resize((220,220),Image.Resampling.LANCZOS)  
        # self.btn_img4 = ImageTk.PhotoImage(btn_img4)

        # b4_img = Label(bg_lbl, image= self.btn_img4)
        # b4_img.place(x=1100,y=100,width=220,height=220)
        # #button
        # b4_txt = Button(bg_lbl,text='Performance Predict', cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        # b4_txt.place(x=1100,y=300,width=220,height=40)

         #  button image 5  (ROW 2)
        btn_img5 = Image.open(r'Images\assistant.jpg')  # declaring image
        btn_img5 = btn_img5.resize((250,220),Image.Resampling.LANCZOS)  
        self.btn_img5 = ImageTk.PhotoImage(btn_img5)

        b5_img = Label(bg_lbl, image= self.btn_img5)
        b5_img.place(x=240,y=400,width=250,height=220)
        #button
        b5_txt = Button(bg_lbl,text='Assistant',command=self.chatbot, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b5_txt.place(x=240,y=600,width=250,height=40)

        #  button image 6
        btn_img6 = Image.open(r'Images\feedback.jpg')  # declaring image
        btn_img6 = btn_img6.resize((250,220),Image.Resampling.LANCZOS)  
        self.btn_img6 = ImageTk.PhotoImage(btn_img6)

        b6_img = Label(bg_lbl, image= self.btn_img6)
        b6_img.place(x=600,y=400,width=250,height=220)
        #button
        b6_txt = Button(bg_lbl,text='Feedback', cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white',command=self.feedback)
        b6_txt.place(x=600,y=600,width=250,height=40)

        #  button image 7
        btn_img7 = Image.open(r'Images\exit_img.png')  # declaring image
        btn_img7 = btn_img7.resize((250,220),Image.Resampling.LANCZOS)  
        self.btn_img7 = ImageTk.PhotoImage(btn_img7)

        b7_img = Label(bg_lbl, image= self.btn_img7)
        b7_img.place(x=960,y=400,width=250,height=220)
        #button
        b7_txt = Button(bg_lbl,text='Exit App',command=self.close, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b7_txt.place(x=960,y=600,width=250,height=40)

        # #  button image 8
        # btn_img8 = Image.open(r'Images\backg.jpg')  # declaring image
        # btn_img8 = btn_img4.resize((220,220),Image.Resampling.LANCZOS)  
        # self.btn_img8 = ImageTk.PhotoImage(btn_img8)

        # b8_img = Label(bg_lbl, image= self.btn_img8)
        # b8_img.place(x=1100,y=400,width=220,height=220)
        # #button
        # b8_txt = Button(bg_lbl,text='Developer', cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        # b8_txt.place(x=1100,y=600,width=220,height=40)


    # ____________________________________________ Button on click Functions________________________________________

    def student_details(self):
        self.new_window = Toplevel(self.root) 
        self.app = Student(self.new_window)

    def take_attendance(self):
        self.new_window = Toplevel(self.root) 
        self.app = Take_attendance(self.new_window)

    def attendance_record(self):
        self.new_window = Toplevel(self.root) 
        self.app = Attendance_Record(self.new_window)

    def chatbot(self):
        self.new_window = Toplevel(self.root) 
        self.app = Chatbot(self.new_window)
    
    def feedback(self):
        self.new_window = Toplevel(self.root)
        self.app = Feedback_Section(self.new_window)

    def close(self):
        self.root.destroy()




if __name__ == '__main__':
    root = Tk()
    obj = Face_recognition(root)   # create an instance of class 
    root.mainloop()      # starts the main loop
    
