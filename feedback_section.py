from tkinter import *
from sentiment_predict import *
from tkinter import messagebox
import os
from datetime import datetime
import csv
from PIL import Image , ImageTk

class Feedback_Section:
	def __init__(self, root):
		# Set the background colour of GUI window
		self.root = root
		self.root.config(background = "#C9C9C9")
		# set the name of tkinter GUI window
		self.root.title("Feedback Section")
		# Set the configuration of GUI window
		self.root.geometry("636x400")
		self.root.iconphoto(False, ImageTk.PhotoImage(file='Images/appicon.ico'))

		# create a label : Enter Your Task
		self.enterText = Label(root, text = "Enter Your Feedback:",
										bg = "light green", font=('times new roman',16,'bold'))

		# create a text area for the root
		# with lunida 13 font
		# text area is for writing the content
		
		self.textArea = Text(root, height = 5, width = 47, font=('lucida 13',17,'bold'),wrap=WORD)

		# create a Submit Button and place into the root window
		# when user press the button, the command or
		# function affiliated to that button is executed
		self.check = Button(root, text = "Submit Feedback", fg = "Black",
							bg = "#CF9FFF", command = self.predict_sentiment, cursor="hand2", font=('times new roman',16,'bold'))

		

		# Create a overall : label
		self.overall = Label(root, text = "Your Feedback has been Rated As: ",
											bg = "light green", font=('times new roman',14,'bold'))


		# create a text entry box
		self.var_result = StringVar()
		self.overallField = Entry(root, font=('times new roman',19,'bold'),textvariable=self.var_result,bg='#C9C9C9')

		
		self.clear = Button(root, text = "Clear", fg = "Black",
						bg = "#87CEEB", command = self.clearAll,cursor="hand2", font=('times new roman',16,'bold'))

		self.show_text_var = StringVar()
		self.show_text = Label(root, text = "",fg='black', bg = "#C9C9C9",textvariable=self.show_text_var, font=('times new roman',14,'bold'))

		self.check_feedbacks = Button(root, text = "See All Feedbacks", fg = "Black",
						bg = "Orange",cursor="hand2", font=('times new roman',16,'bold'),command=self.open_feedback_file)
		


		self.show_text.place(x=350,y=10,width=200, height =50)
		self.enterText.place(x=5,y=20,width=200, height =50)  
		
		self.textArea.place(x=5,y=70,width=620, height =50) 
		
		self.check.place(x=320,y=140,width=305, height =50) 
		self.clear.place(x=5,y=140,width=305, height =50) 
		
		self.overall.place(x=25,y=200,width=300, height =50) 
		
		
		self.overallField.place(x=360,y=200,width=200, height =50) 

		self.check_feedbacks.place(x=10,y=280,width=613, height =100) 
		
		

	# clear text box
	def clearAll(self):

		# deleting the content from the entry box

		self.overallField.delete(0, END)

		# whole content of text area is deleted
		self.textArea.delete(1.0, END)

		self.show_text_var.set('')

	def submit_feedback(self):
		#Create File if not exist
		if not os.path.exists('Feedbacks.csv'):
			# messagebox.showerror('NO csv file, creating one')
			header = ['Feedback', 'Sentiment','Date', 'Time']
			with open('Feedbacks.csv', 'a+') as f:           # r+ doesnt create file , a+ creates
				writer = csv.writer(f)
				writer.writerow(header)
				f.close()

		with open('Feedbacks.csv','a', newline='\n') as f:
			now = datetime.now()
			date = now.strftime('%d-%m-%Y')
			time = now.strftime('%H:%M:%S')
			feedback = self.textArea.get(1.0, "end-1c")
			sentiment =  self.var_result.get()

			row = [feedback,sentiment,date,time]
			writer = csv.writer(f)
			writer.writerow(row)


		#last pe rkhna isse
		self.show_text_var.set('🗸 Feedback Submitted 🗸')

	def predict_sentiment(self):

		# get a whole input content from text box
		text = self.textArea.get("1.0", "end")
		if text == '\n':
			messagebox.showerror("Error","Please give an Input!")
		else:
			string = predict_class([text])

			self.var_result.set(string)

			self.submit_feedback() 
	
	def open_feedback_file(self):
		os.system(r"Feedbacks.csv")


# Driver Code
if __name__ == "__main__" :
	root = Tk()
	obj = Feedback_Section(root)
	root.mainloop()
