from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
#  from tqdm import tqdm # progress bar
from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from googlesearch import *
# import os
# import string
# from lxml import html
# from googlesearch import search
from bs4 import BeautifulSoup
import requests
import wikipedia
import datetime
import webbrowser
import psutil
import subprocess as sp
from decouple import config
from email_sender import Send_Email
import json
import re
import random_responses   # created file
import random


paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

class Chatbot:
    def __init__(self,root):
        self.root= root
        self.root.title('For your Assistance')
        self.root.geometry('857x565+390+20')
        self.root.resizable(False,False)
        self.root.bind('<Return>',self.send_with_enter)
        self.root.iconphoto(False, ImageTk.PhotoImage(file='Images/appicon.ico'))

        main_frame = Frame(self.root,bd=4,bg='powder blue',width=610,height=300)
        main_frame.place(x=0,y=0,width=600, height =420)

        chatbot_img = Image.open('Images/bot.png')
        chatbot_img = chatbot_img.resize((200,100),Image.LANCZOS)
        
        self.photoimage= ImageTk.PhotoImage(chatbot_img) 

        Title_label = Label(main_frame,bd=2,relief=RAISED,anchor='nw',compound=LEFT,width=730,image=self.photoimage,text='Here for your Assistance',font=('Times New roman',25,'bold'),fg='Blue',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text= Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('ariel',14),yscrollcommand=self.scroll_y.set,wrap='word')
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.place(x=0,y=105,width=573, height =327)
        

        self.scroll_y.config( command = self.text.yview )

        entry_frame = Frame(self.root,bd=4,width=730)
        entry_frame.place(x=10,y=420,width=600, height =220)

        label_ = Label(entry_frame,text='>>',font=('Times New roman',20,'bold'),fg='Blue')
        label_.grid(row=0,column=0,padx=5,sticky=W)

        self.entry = StringVar()
        self.entry1=ttk.Entry(entry_frame,width=48,textvariable=self.entry,font=('ariel',14,'bold'))
        self.entry1.grid(row=0,column=1 ,padx=5,sticky=W)


        btn_frame = Frame(self.root,bd=4,width=730)
        btn_frame.place(x=10,y=470,width=600, height =220)
        
        self.clr= Button(btn_frame,text='Clear',command=self.clear,font=('Times New roman',20,'bold'),width=17,bg='red' )
        self.clr.grid(row=1,column=0,padx=5,sticky=W)

        self.snd= Button(btn_frame,text='Send',command=self.send,font=('Times New roman',20,'bold'),width=17,bg='green' )
        self.snd.grid(row=1,column=1,padx=5,sticky=W)


        error_frame = Frame(self.root,bd=4,width=730)
        error_frame.pack()

        self.label4warning = Label(btn_frame,text='',font=('Times New roman',20,'bold'),fg='Blue')
        self.label4warning.grid(row=2,column=0,padx=5,sticky=W)

        # commands
        side_frame = Frame(self.root,bd=2,bg='#242F36')
        side_frame.place(x=605,y=5,width=250, height =558)

        commands_= Label(side_frame,text='Commands:',font=('Times New roman',15,'bold'),fg='white',bg='#242F36')
        commands_.grid(row=0,column=0,padx=5,sticky=W)

        command1_= Label(side_frame,text='1. battery > battery check',font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command1_.grid(row=1,column=0,padx=5,sticky=W)

        command2_= Label(side_frame,text="2. google 'topic' > google search",font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command2_.grid(row=2,column=0,padx=5,sticky=W)

        command3_= Label(side_frame,text="3. tell me about 'topic'",font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command3_.grid(row=3,column=0,padx=5,sticky=W)

        command4_= Label(side_frame,text='4. news > to see news',font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command4_.grid(row=4,column=0,padx=5,sticky=W)

        command5_= Label(side_frame,text='5. mail.send > to send mail',font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command5_.grid(row=5,column=0,padx=5,sticky=W)

        command6_= Label(side_frame,text='6. cal.open > opens calculator',font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command6_.grid(row=6,column=0,padx=5,sticky=W)

        command7_= Label(side_frame,text='7. cam.open > opens camera',font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command7_.grid(row=7,column=0,padx=5,sticky=W)

        # command8_= Label(side_frame,text="8. open 'site-name' > opens website",font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        # command8_.grid(row=8,column=0,padx=5,sticky=W)

        command9_= Label(side_frame,text="8. ip > get ip address ",font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command9_.grid(row=8,column=0,padx=5,sticky=W)

        command10_= Label(side_frame,text="9. jokes > tells a joke",font=('Times New roman',11,'bold'),fg='white',bg='#242F36')
        command10_.grid(row=9,column=0,padx=5,sticky=W)




        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.text.insert(END,"Bot: "+'Good Morning, how can I help you?'+'\n','bot')
        elif hour>= 12 and hour<16:
            self.text.insert(END,"Bot: "+'Good Afternoon, how can I help you?'+'\n','bot')
        else:
            self.text.insert(END,"Bot: "+'Good Evening, how can I help you?'+'\n','bot')


  #_______________________________________ Functions _______________________________________________________
        self.text.tag_config('bot',background='blue',foreground='white')     # tags for background colors of text
        self.text.tag_config('you',background='yellow')                      # tags for background colors of text 
 
    #-------------------------------------   TRAINING   --------------------------------------------------------


        # self.bot = ChatBot('Bot')   # our chatbot 
        # self.trainer = ListTrainer(self.bot)    #for training the chatbot

        # ************************** TRAINING FROM english corpus     *************************************
        #   loop for training the data  (comment the code after training the data)
        # for file in os.listdir('english/'):        
        #     self.data = open('english/'+file,'r',encoding='utf-8').readlines()
        #     self.trainer.train(self.data)     # training the data
        # **************************************************************************************************

    #  ^^^^^^^^^^^^^^^^^^^^^^^^^^^  Different functions for tasks ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       

    # def google(self,query, index=0):    #function 4  google search
    #     fallback = 'Sorry, I cannot think of a reply for that.'
    #     result = ''

    #     try:
    #         search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

    #         page = requests.get(search_result_list[index])

    #         tree = html.fromstring(page.content)

    #         soup = BeautifulSoup(page.content, features="lxml")

    #         article_text = ''
    #         article = soup.findAll('p')
    #         for element in article:
    #             article_text += '\n' + ''.join(element.findAll(text = True))
    #         article_text = article_text.replace('\n', '')
    #         first_sentence = article_text.split('.')
    #         first_sentence = first_sentence[0].split('?')[0]

    #         chars_without_whitespace = first_sentence.translate(
    #             { ord(c): None for c in string.whitespace }
    #         )

    #         if len(chars_without_whitespace) > 0:
    #             result = first_sentence
    #         else:
    #             result = fallback
    #         self.text.insert(END,"Bot: "+str(result)+'\n','bot')
            
    #     except Exception as e:
    #         print(e)
    #         if len(result) == 0: 
    #             result = fallback
    #         self.text.insert(END,"Bot: "+str(result)+'\n','bot')
    
        # Load JSON data
    def load_json(self,file):
        with open(file) as bot_responses:
            print(f"Loaded '{file}' successfully!")
            return json.load(bot_responses)

    def get_reply(self, input_string):
        
       
        split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
        score_list = []

        # Check all the responses
        for response in self.response_data:
            response_score = 0
            required_score = 0
            required_words = response["required_words"]

            # Check if there are any required words
            if required_words:
                for word in split_message:
                    if word in required_words:
                        required_score += 1

            # Amount of required words should match the required score
            if required_score == len(required_words):
                # print(required_score == len(required_words))
                # Check each word the user has typed
                for word in split_message:
                    # If the word is in the response, add to the score
                    if word in response["user_input"]:
                        response_score += 1

            # Add score to list
            score_list.append(response_score)
            # Debugging: Find the best phrase
            # print(response_score, response["user_input"])

        # Find the best response and return it if they're not all 0
        best_response = max(score_list)
        response_index = score_list.index(best_response)

        # Check if input is empty
        if input_string == "":
            return "Please type something so we can chat :("

        # If there is no good response, return a random one.
        if best_response != 0:
            list =self.response_data[response_index]["bot_response"]
            print('list',list)
            
            return random.choice(list)
            
        return random_responses.random_string()


    def email_func(self):
        self.new_window = Toplevel(self.root) 
        self.app = Send_Email(self.new_window)
    

    def wiki_search(self,question):
        try:
            result = wikipedia.summary(question, sentences = 2,auto_suggest=False)
            self.text.insert(END,"Bot: "+str(result)+'\n','bot')
        except:
            self.text.insert(END,"Bot: "+'I am Sorry, I dont know about that topic'+'\n','bot')

 

    def clear(self):
        self.text.delete(1.0,END)   # clear chat
        self.entry.set('')      # clear entry text box
        self.msg=''                                     # clear the warning msg
        self.label4warning.config(text=self.msg,fg='red')         


    def send_with_enter(self,event):
        self.send()
    

    def reply(self,text):
        self.text.insert(END,"Bot: "+text+'\n','bot')


    def send(self):
        send= 'You: '+self.entry.get()
        self.text.insert(END,send+'\n','you')        
        

        #--------------------------- msg for empty  ---------------------------------------------
        if self.entry.get()=='':
            self.text.see("end")
            self.msg = 'Plz give an input'
            self.label4warning.config(text=self.msg,fg='red')
            return       # return none if the input msg is empty 
            
        
        else:
            self.text.see("end")
            self.msg=''
            self.label4warning.config(text=self.msg,fg='red')

        #----------------------------------  MAIN WORKING      --------------------------------------------------------   

        if self.entry.get()=='hloo':    # testing hloo
            self.reply('hyy there')

        elif self.entry.get()=='ohh' or self.entry.get()=='ohk' or self.entry.get()=='ok' or self.entry.get()=='Ok' or self.entry.get()=='okay' or self.entry.get()=='I see' or self.entry.get()=='hm':    # reply of ok 
            self.reply('yupp!')

        elif 'tell me about' in self.entry.get().lower():    # wikipedia search with tell me about
            question = self.entry.get().lower().replace("tell me about ", "")
            self.wiki_search(question)

        # elif 'tell me ' in self.entry.get().lower():    # google search with tell me 
        #     self.reply(self.entry.get().lower())
        #     self.reply('found the word "Tell me "')
        #     question = self.entry.get().lower().replace("tell me  ", "")
        #     self.google(question)

        # elif 'open ' in self.entry.get().lower():          
        #     site = self.entry.get().lower().replace('open ','')
        #     webbrowser.open('http://'+site+'.com')  # Go to site.com
        #     self.text.insert(END,"Bot: "+'I opened '+site+'\n','bot')
        
        elif  'battery' in self.entry.get().lower():
            battery = psutil.sensors_battery()
            self.text.insert(END,"Bot: "+'Battery percentage : '+str(battery.percent)+'\n','bot')
            self.text.insert(END,"        "+'Power plugged in : '+str(battery.power_plugged)+'\n','bot')
        
        elif 'cam.open' in self.entry.get().lower():
            sp.run('start microsoft.windows.camera:', shell=True)
            self.text.insert(END,"Bot: "+'I opened the camera'+'\n','bot')
        
        elif 'cal.open' in self.entry.get().lower():
            self.text.insert(END,"Bot: "+'I opened the calculator'+'\n','bot')
            sp.Popen(paths['calculator'])

        elif ' ip ' in self.entry.get().lower() or ' ip' in self.entry.get().lower() or ' ip.' in self.entry.get().lower() or ' ip?' in self.entry.get().lower() or 'ip' in self.entry.get().lower() :
            ip_address = requests.get('https://api64.ipify.org?format=json').json()
            self.text.insert(END,"Bot: "+'Your Ip Address is: '+ip_address["ip"]+'\n','bot')
        
        elif 'google ' in self.entry.get().lower():
            query = self.entry.get().lower().replace("google ", "")
            self.text.insert(END,"Bot: "+'I have searched for "'+query+'" in google'+'\n','bot')
            # iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'news' in self.entry.get().lower() or 'latest news' in self.entry.get().lower():
            NEWS_API_KEY = config("NEWS_API_KEY")   # api key : 649f115f4684421fb31d6df8e22cef5c 
            news_headlines = []
            res = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
            articles = res["articles"]
            for article in articles:
                news_headlines.append(article["title"])
            news1= news_headlines[0]
            news2= news_headlines[1]
            news3= news_headlines[2]
            news4= news_headlines[3]
            news5= news_headlines[4]
            self.text.insert(END,"Bot: "+"Today's top headlines are:"+'\n','bot')
            self.text.insert(END,"     1."+str(news1)+'\n','bot')
            self.text.insert(END,"     2."+str(news2)+'\n','bot')
            self.text.insert(END,"     3."+str(news3)+'\n','bot')
            self.text.insert(END,"     4."+str(news4)+'\n','bot')
            self.text.insert(END,"     5."+str(news5)+'\n','bot')
        
        elif 'mail.send' in self.entry.get().lower():
            self.email_func()
        
        elif 'joke' in self.entry.get().lower() or 'make me laugh' in self.entry.get().lower() or  'jokes' in self.entry.get().lower():
            headers = {'Accept': 'application/json' }
            res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
            self.text.insert(END,"Bot: "+res["joke"]+'\n','bot')




        else:
            question = self.entry.get()
            # Store JSON data
            self.response_data = self.load_json("bot.json")
            answer = self.get_reply(question)
            self.text.insert(END,"Bot: "+str(answer)+'\n','bot')
            self.entry.set('')


        self.entry.set('')
        self.text.see("end")
    



if __name__ == '__main__':
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()

# 1. tell me about <topic-name>    
# 2. open <website>    
# 3. battery check 
# 4. open camera with cam.open
# 5. open calculator with cal.open
# 6. get ip address
# 7. google <topic-name>
# 8. news     
# 9. send email   email.send
# 10.joke   