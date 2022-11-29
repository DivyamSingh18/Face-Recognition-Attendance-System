import os
from datetime import datetime
from time import strftime

def mark_attendance(i,r,n,c):
        #Create File if not exist
        if not os.path.exists('Attendance_Record_dup.csv'):
            # messagebox.showerror('NO csv file, creating one')
            # header = ['Student_id', 'Name','Roll no', 'class', 'Date', 'Time', 'Attendance']
            with open('Attendance_Record_dup.csv', 'a+') as f:           # r+ doesnt create file , a+ creates
                # writer = csv.writer(f)
                # writer.writerow(header)
                f.close()

        with open('Attendance_Record_dup.csv','r+') as f:
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

            # if i not in datalist and date not in datalist:  
            #     f.writelines(f'{i},{n},{r},{c},{date},{time},Present\n')
            #     print("lines added")
            # elif i in datalist and date in datalist:
            #     print('lines not added')




i = 1
r = 12
n = "Divyam"
c = "r6"

if __name__ == "__main__":

    mark_attendance(i,r,n,c)

