from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
import csv   # for writing and reading csv
from PIL import Image , ImageTk

class Take_attendance:
    def __init__(self, root):
        self.root= root
        self.root.geometry('1600x790+0+0')   # width x height + x_start + y_start
        self.root.title("Attendance")
        self.root.iconphoto(False, ImageTk.PhotoImage(file='Images/appicon.ico'))

        #title
        title_lbl = Label(self.root, text="Take Attendance",font=('times new roman',35,'bold'),bg='red',fg='white')
        title_lbl.place(x=0,y=0,width=1600, height=55,)

        # background image----------------------------------------------------------------------------------------------------
        bg_img = Image.open(r'C:Images\backg2.webp')  # declaring image
        bg_img = bg_img.resize((1600,790),Image.Resampling.LANCZOS)  
        self.bg_img = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root,image=self.bg_img)  #creating label
        bg_lbl.place(x=0,y=55,width=1600, height =790)  # placing label on window

        #  button image 1  (ROW 1)
        btn_img = Image.open(r'Images\see_data.jpg')  # declaring image
        btn_img = btn_img.resize((220,220),Image.Resampling.LANCZOS)  
        self.btn_img = ImageTk.PhotoImage(btn_img)

        b1_img = Label(bg_lbl, image= self.btn_img)
        b1_img.place(x=250,y=100,width=220,height=220)
        #button
        b1_txt = Button(bg_lbl,text='See Data', cursor='hand2',command=self.open_img_folder,font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_txt.place(x=250,y=300,width=220,height=40)

        #  button image 2  (ROW 2)
        btn_img2 = Image.open(r'Images\train_data.jpg')  # declaring image
        btn_img2 = btn_img2.resize((220,220),Image.Resampling.LANCZOS)  
        self.btn_img2 = ImageTk.PhotoImage(btn_img2)

        b2_img = Label(bg_lbl, image= self.btn_img2)
        b2_img.place(x=250,y=400,width=220,height=220)
        #button
        b1_txt = Button(bg_lbl,text='Train Data', cursor='hand2',command=self.train_model,font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_txt.place(x=250,y=600,width=220,height=40)

        #  button image 3  (ROW both rows)
        btn_img3 = Image.open(r'Images\take_attend.jpg')  # declaring image
        btn_img3 = btn_img3.resize((500,500),Image.Resampling.LANCZOS)  
        self.btn_img3 = ImageTk.PhotoImage(btn_img3)

        b3_img = Label(bg_lbl, image= self.btn_img3)
        b3_img.place(x=550,y=100,width=500,height=500)
        #button
        b3_txt = Button(bg_lbl,text='Face Recognize ( Take attendance )',command=self.face_recognition, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b3_txt.place(x=550,y=600,width=500,height=40)

        #  Subject image
        subj_img = Image.open(r'Images\subject.jpg')  # declaring image
        subj_img = subj_img.resize((300,220),Image.Resampling.LANCZOS)  
        self.subj_img = ImageTk.PhotoImage(subj_img)

        subject_img = Label(bg_lbl, image= self.subj_img)
        subject_img.place(x=1150,y=300,width=300,height=220)
        
        # subject Label
        subject_label =Label(bg_lbl,text='Subject',font=('times new roman',20,'bold'),bg='#FFFBC1')
        subject_label.place(x=1150,y=270,width=300,height=40)

        self.var_subject = StringVar()
        subject_ =ttk.Combobox(bg_lbl,textvariable=self.var_subject,font=('times new roman',17,'bold'),state='readonly')
        subject_['values']= ('Select Subject','Maths','English','Computer','Science')
        subject_.current(0) 
        subject_.place(x=1150,y=510,width=300,height=40)
        
        hour = int(datetime.now().hour)

        if hour >= 9 and hour < 10:
            self.var_subject.set('Maths')
        elif hour >= 10 and hour < 11:
            self.var_subject.set('Science')
        elif hour >= 11 and hour < 12:
            self.var_subject.set('English')
        elif hour >= 12 and hour < 1:
            self.var_subject.set('Computer')

    #--------------------------------- functions ------------------------------------------------    

       # open data function
    def open_img_folder(self):
        os.startfile('data')

       # train model function 
    def train_model(self):
        data_dir =('data')    
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]  # getting data path of images from data folder

        faces = []
        ids =[]

        for image in path:
            img= Image.open(image).convert('L')   # convert image to greyscale

            img_np = np.array(img,'uint8')     # numpy array gives better performance while training the model, uint8 is datatype

            id = int(os.path.split(image)[1].split('_')[1])
                    #   C:\Users\Divyam Singh\Desktop\Mine\FinalProject\data\user_1_11.jpg  => user _ 1 _  11.jpg
                    #   |___________________________________________________||___________|     |__|  |_|    |_|  
                    #                        index 0                           index 1          0     1      2  

            faces.append(img_np)
            ids.append(id)

            cv2.imshow('Training',img_np)
            cv2.waitKey(1) == 13    # close window with key 13(enter key)

        ids = np.array(ids) 

        #--------------------------------------------- train the model ---------------------------------
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces, ids)       # face is independent feature and id is dependent feature
        clf.write('classifier_model.xml')

        cv2.destroyAllWindows()
        messagebox.showinfo('Result','Data Training is successfully completed.')

    #  face recognition function 
    def face_recognition(self):
        def draw_boundary(img,classifier,scalefactor, minNeighbors, color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # img to greyscale
            features = classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)

            coord =[]   # coordinates

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)   # green rectangle
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])   # predicting the image

                confidence =int(100*(1-predict/300))   # formula of confidence

                conn = mysql.connector.connect(host='localhost',username='root',password='987@Cs',database='data')
                my_cursor = conn.cursor()

                my_cursor.execute('select Name from student where ID='+str(id))     # fetching details from database
                n = my_cursor.fetchone()
                n = '+'.join(n)

                my_cursor.execute('select Roll_No from student where ID='+str(id))
                r = my_cursor.fetchone()
                r = '+'.join(r)

                my_cursor.execute('select Class from student where ID='+str(id))
                c = my_cursor.fetchone()
                c = '+'.join(c)

                my_cursor.execute('select ID from student where ID='+str(id))
                i = my_cursor.fetchone()
                i = '+'.join(i)


                if confidence > 77:
                    cv2.putText(img,f'Stu_ID:{i}',(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Roll:{r}',(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)      # writing details
                    cv2.putText(img,f'Name:{n}',(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Class:{c}',(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,c )
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)  # red rectangle
                    cv2.putText(img,'Unknown Face',(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord =[x,y,w,h]

            return coord

        def recognize(img,clf,faceCasecade):
            coord= draw_boundary(img,faceCasecade,1.1,10,(255,25,255),'Face',clf)
                                #(img,classifier,scalefactor, minNeighbors, color,text,clf)
            return img
        
        faceCasecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')                                
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier_model.xml')

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCasecade)
            cv2.imshow('Welcome To Face Recognition', img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
    
    # attendance marking function

    def mark_attendance(self,i,r,n,c):
        if self.var_subject.get() == 'Select Subject':
            messagebox.showinfo('No subject Selected',"Please, select a subject to take attendance")
        elif self.var_subject.get() == 'Maths':
            #Create File if not exist
            if not os.path.exists('Attendance_Record-Maths.csv'):
                # messagebox.showerror('NO csv file, creating one')
                # header = ['Student_id', 'Name','Roll no', 'class', 'Date', 'Time', 'Attendance']
                with open('Attendance_Record-Maths.csv', 'a+') as f:           # r+ doesnt create file , a+ creates
                    # writer = csv.writer(f)
                    # writer.writerow(header)
                    f.close()

            with open('Attendance_Record-Maths.csv','r+', newline='\n') as f:
                now = datetime.now()
                date = now.strftime('%d-%m-%Y')
                time = now.strftime('%H:%M:%S')
                datalist = f.readlines()              
                name_list = []
                for line in datalist:                #putting data into list
                    entry= line.split(',')
                    name_list.append(entry[0]) 
                flag = 0
                for row in datalist:
                    if str(i) in row and date in row:
                        print(datalist)
                                                    # data is present 
                        flag = 1
                        break
                
                if flag == 1:
                    print('data is already present')
                else:
                    f.writelines(f'{i},{n},{r},{c},{date},{time},Present\n')
                    print("Data added")

                # if i not in datalist and date not in datalist:  
                #     f.writelines(f'{i},{n},{r},{c},{date},{time},Present\n')
                #     print("lines added")
                # elif i in datalist and date in datalist:
                #     print('lines not added')
        
        elif self.var_subject.get() == 'Science':
            #Create File if not exist
            if not os.path.exists('Attendance_Record-Science.csv'):
                # messagebox.showerror('NO csv file, creating one')
                # header = ['Student_id', 'Name','Roll no', 'class', 'Date', 'Time', 'Attendance']
                with open('Attendance_Record-Science.csv', 'a+') as f:           # r+ doesnt create file , a+ creates
                    # writer = csv.writer(f)
                    # writer.writerow(header)
                    f.close()

            with open('Attendance_Record-Science.csv','r+', newline='\n') as f:
                now = datetime.now()
                date = now.strftime('%d-%m-%Y')
                time = now.strftime('%H:%M:%S')
                datalist = f.readlines()              
                name_list = []
                for line in datalist:                #putting data into list
                    entry= line.split(',')
                    name_list.append(entry[0]) 
                flag = 0
                for row in datalist:
                    if str(i) in row and date in row:
                                                    # data is present 
                        flag = 1
                        break
                
                if flag == 1:
                    print('data is already present')
                else:
                    f.writelines(f'{i},{n},{r},{c},{date},{time},Present\n')
                    print("Data added")
        
        elif self.var_subject.get() == 'English':
            #Create File if not exist
            if not os.path.exists('Attendance_Record-Enlish.csv'):
                # messagebox.showerror('NO csv file, creating one')
                # header = ['Student_id', 'Name','Roll no', 'class', 'Date', 'Time', 'Attendance']
                with open('Attendance_Record-English.csv', 'a+') as f:           # r+ doesnt create file , a+ creates
                    # writer = csv.writer(f)
                    # writer.writerow(header)
                    f.close()

            with open('Attendance_Record-English.csv','r+', newline='\n') as f:
                now = datetime.now()
                date = now.strftime('%d-%m-%Y')
                time = now.strftime('%H:%M:%S')
                datalist = f.readlines()              
                name_list = []
                for line in datalist:                #putting data into list
                    entry= line.split(',')
                    name_list.append(entry[0]) 
                flag = 0
                for row in datalist:
                    if str(i) in row and date in row:
                                                    # data is present 
                        flag = 1
                        break
                
                if flag == 1:
                    print('data is already present')
                else:
                    f.writelines(f'{i},{n},{r},{c},{date},{time},Present\n')
                    print("Data added")

        elif  self.var_subject.get() == 'Computer':
            #Create File if not exist
            if not os.path.exists('Attendance_Record-Computer.csv'):
                # messagebox.showerror('NO csv file, creating one')
                # header = ['Student_id', 'Name','Roll no', 'class', 'Date', 'Time', 'Attendance']
                with open('Attendance_Record-Computer.csv', 'a+') as f:           # r+ doesnt create file , a+ creates
                    # writer = csv.writer(f)
                    # writer.writerow(header)
                    f.close()

            with open('Attendance_Record-Computer.csv','r+', newline='\n') as f:
                now = datetime.now()
                date = now.strftime('%d-%m-%Y')
                time = now.strftime('%H:%M:%S')
                datalist = f.readlines()              
                name_list = []
                for line in datalist:                #putting data into list
                    entry= line.split(',')
                    name_list.append(entry[0]) 
                flag = 0
                for row in datalist:
                    if str(i) in row and date in row:
                                                    # data is present 
                        flag = 1
                        break
                
                if flag == 1:
                    print('data is already present')
                else:
                    f.writelines(f'{i},{n},{r},{c},{date},{time},Present\n')
                    print("Data added")



            






if __name__ == '__main__':
    root = Tk()
    obj =Take_attendance(root)
    root.mainloop()
          