from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk

from decouple import config
import json
from email.message import EmailMessage
import smtplib
from tkinter import messagebox

class Send_Email:
    def __init__(self,root):
        self.root= root
        self.root.title('Email Sender')
        self.root.geometry('510x520+390+20')
        self.root.resizable(False,False)
        self.root.iconphoto(False, ImageTk.PhotoImage(file='Images/appicon.ico'))

        main_frame = Frame(self.root,bd=4,bg='powder blue',width=510,height=300)
        main_frame.place(x=10,y=10,width=490, height =520)

        chatbot_img = Image.open('Images/bot.png')
        chatbot_img = chatbot_img.resize((200,100),Image.LANCZOS)
        
        self.photoimage= ImageTk.PhotoImage(chatbot_img) 

        Title_label = Label(main_frame,bd=2,relief=RAISED,anchor='nw',compound=LEFT,width=500,image=self.photoimage,text='I will send the Email for you!',font=('Times New roman',12,'bold'),fg='Blue',bg='white')
        Title_label.place(x=5,y=5,width=470, height =100)

        entry_frame = Frame(self.root,bd=4,width=500)
        entry_frame.place(x=10,y=130,width=490, height =70)

        #............................. Recipient   ...................................................................

        rec_label =Label(entry_frame,text='Recipient(s)',font=('times new roman',12,'bold'))
        rec_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.recipient = StringVar()
        rec = ttk.Entry(entry_frame,textvariable=self.recipient,width=45,font=('times new roman',12,'bold'))
        rec.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #............................. Subject   ...................................................................

        sub_label =Label(entry_frame,text='Subject',font=('times new roman',12,'bold'))
        sub_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        self.subject = StringVar()
        subj = ttk.Entry(entry_frame,textvariable=self.subject,width=45,font=('times new roman',12,'bold'))
        subj.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #.............................    ...................................................................
        

        text_frame = Frame(main_frame,bd=4,bg='powder blue',width=610,height=100)
        text_frame.place(x=0,y=190,width=480, height =245)

        
        message =Label(text_frame,text='Message',font=('times new roman',12,'bold'))
        message.place(x=0,y=0,width=80, height =20)


        self.text= Text(text_frame,width=65,height=10,bd=3,relief=RAISED,font=('ariel',14),wrap='word')
        self.text.place(x=0,y=20,width=475, height =220)

        self.message = self.text.get("1.0",'end-1c')   

        btn_frame = LabelFrame(self.root, bd=2,relief=RIDGE,font=('times new roman',12,'bold'))
        btn_frame.place(x=7 ,y=454,width=490, height=60)

        self.snd= Button(btn_frame,text='Send',font=('Times New roman',20,'bold'),command=self.send_mail,width=29,bg='orange' )
        self.snd.grid(row=1,column=0,padx=5,sticky=W)



    #========================================   Working  ==========================================================================

    def send_mail(self):

        EMAIL = config("EMAIL")
        PASSWORD = config("PASSWORD")
        receiver_address = self.recipient.get()
        subject = self.subject.get()
        message = self.text.get("1.0",'end-1c') 

    

        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        messagebox.showinfo('Success','The Email has been sent successfully')
        return True
        # except Exception as e:
        #     print(e)
        #     return False
        
        

        
if __name__ == '__main__':
    root = Tk()
    obj = Send_Email(root)
    root.mainloop()