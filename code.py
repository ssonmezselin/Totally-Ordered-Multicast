from http.client import SWITCHING_PROTOCOLS
from multiprocessing import Process
from datetime import datetime


def local_time(counter):
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(counter,
                                                     datetime.now())

def event1(msg,counter):
    a=[input("Enter Message id: "),input("Enter message: ")]
    counter =0
    msg.append(a)
    c=a
    print("Your Message is: "+c[1]+"   "+" Your message id is :  "+c[0]+ local_time(counter))
    choose(msg)
    
def process_one(msg,data,counter):
    pn= "1"
    
    counter +=str(1)
    temp=[input("Enter Message id: "),input("Enter message: ")]
    msg.append(temp)
    data=temp
    print('Your Message: ' +  data[1] +"   "+ " Your message id is: "+ data[0]+'@'+pn + local_time(counter))
    choose(msg)

def process_two(msg,data,counter):
    pn= "2"
    counter +=str(2)
    temp=[input("Enter Message id: "),input("Enter message: ")]
    msg.append(temp)
    data=temp
    print('Your Message: ' +  data[1] +"   "+ " Your message id is: "+ data[0]+'@'+pn + local_time(counter))
    choose(msg)
    

def process_three(msg,data,counter):
    pn= "3"
    counter +=str(3)
    temp=[input("Enter Message id: "),input("Enter message: ")]
    msg.append(temp)
    data=temp
    print('Your Message: ' +  data[1] +"   "+ " Your message id is: "+ data[0]+'@'+pn + local_time(counter))
    choose(msg)

def process_four(msg,data,counter):
    pn= "4"
    counter +=str(4)
    temp=[input("Enter Message id: "),input("Enter message: ")]
    msg.append(temp)
    data=temp
    print('Your Message: ' +  data[1] +"   "+ " Your message id is: "+ data[0]+'@'+pn + local_time(counter))
    choose(msg)

def process_five(msg,temp,counter):
    pn= "5"
    counter +=str(5)
    temp=[input("Enter Message id: "),input("Enter message: ")]
    msg.append(temp)
    data=temp
    print('Your Message: ' +  data[1] +"   "+ " Your message id is: "+ data[0]+'@'+pn + local_time(counter))
    choose(msg)
    
      
def ev3_process_one(msg,data,counter):
    
    pn= "1"
    counter +=str(1)
    print("Your acknowledge messages is/are ↓")
    print(msg)
    data=input("Select the messages: ")
    temp=data
    for i in range (0,len(msg)):
        if temp in msg[i][1]:
            print('Selection process successful!' + " "+"Selected message is: "+ msg[i][1]+" "+"Selected message id is : "+ msg[i][0] + " " +"ACK") 
        else:
            print("!!! Choseen data not included in data set!!!!")
    choose(msg)
    
def ev3_process_two(msg,data,counter):
    pn= "2"
    counter +=str(2)
    print("Your acknowledge messages is/are ↓")
    print(msg)
    data=input("Select the messages: ")
    temp=data
    for i in range (0,len(msg)):
        if temp in msg[i][1]:
            print('Selection process successful!' + " "+"Selected message is: "+ msg[i][1]+" "+"Selected message id is : "+ msg[i][0] + " " +"ACK")
        else:
            print("!!! Choseen data not included in data set!!!!")
    choose(msg)
    
def ev3_process_three(msg,data,counter):
    pn= "3"
    counter +=str(3)
    print("Your acknowledge messages is/are ↓")
    print(msg)
    data=input("Select the messages: ")
    temp=data
    for i in range (0,len(msg)):
        if temp in msg[i][1]:
            print('Selection process successful!' + " "+"Selected message is: "+ msg[i][1]+" "+"Selected message id is : "+ msg[i][0] + " " +"ACK")
        else:
            print("!!! Choseen data not included in data set!!!!")
    choose(msg)
    
def ev3_process_four(msg,data,counter):
    pn= "4"
    counter +=str(4)
    print("Your acknowledge messages is/are ↓")
    print(msg)
    data=input("Select the messages: ")
    temp=data
    for i in range (0,len(msg)):
        if temp in msg[i][1]:
            print('Selection process successful!' + " "+"Selected message is: "+ msg[i][1]+" "+"Selected message id is : "+ msg[i][0] + " " +"ACK")
        else:
            print("!!! Choseen data not included in data set!!!!")
    choose(msg)
    
def ev3_process_five(msg,data,counter):
    pn= "5"
    counter +=str(5)
    print("Your acknowledge messages is/are ↓")
    print(msg)
    data=input("Select the messages: ")
    temp=data
    for i in range (0,len(msg)):
        if temp in msg[i][1]:
            print('Selection process successful!' + " "+"Selected message is: "+ msg[i][1]+" "+"Selected message id is : "+ msg[i][0] + " " +"ACK")
        else:
            print("!!! Choseen data not included in data set!!!!")
    choose(msg)  
    
    
def choose(msg):
    b=input("Choose Event: ")
    if b == "1":
        event1(msg,c)
    elif b == "2":
        pr= input("Choose Process 1 to 5: ")
        if pr == "1":
            process1 = Process(target=process_one(msg,data,counter))
            process1.start()
        elif pr == "2":
            process2 = Process(target=process_two(msg,data,counter))
            process2.start()
        elif pr == "3":
            process3 = Process(target=process_three(msg,data,counter))
            process3.start()
        elif pr == "4":
            process4 = Process(target=process_four(msg,data,counter))
            process4.start()
        elif pr == "5":
            process5 = Process(target=process_five(msg,data,counter))
            process5.start()
            
        else:
            print("Doesn't Exits")
    elif b == "3": 
        pr= input("Choose Process 1 to 5: ")
        if pr == "1":
            process1 = Process(target=ev3_process_one(msg,data,counter))
            process1.start()
        elif pr == "2":
            process2 = Process(target=ev3_process_two(msg,data,counter))
            process2.start()
        elif pr == "3":
            process3 = Process(target=ev3_process_three(msg,data,counter))
            process3.start()
        elif pr == "4":
            process4 = Process(target=ev3_process_four(msg,data,counter))
            process4.start()
        elif pr == "5":
            process5 = Process(target=ev3_process_five(msg,data,counter))
            process5.start()
        else:
            print("!!! Process Seçimi Hatalı!!!)") 
                
    elif b=="öl":
        print("Seçim işlemi sonlandı!")  
        
    else :
        print("!!! Event Seçimi Hatalı !!!")
        choose(msg)
    

if __name__ == '__main__':
    
    print("EVENT 1 = KULLANICIDAN MESAJ VE ID ALMA VE EKRANA YAZDIRMA İŞLEMİ YAPIYOR")
    print("EVENT 2 = PROCESS SEÇİMİ YAPTIRARAK KULLANICADAN MESAJ VE PROCESS ID ALIP  EKRANA  LOCAL TİME İLE BİRLİKTE BASTIRIYOR")
    print("EVENT 3 = ACKNOWLEDGEMENT MESAJ SEÇİM İŞLEMİ YAPIYOR")
    msg=[]
    c=[]
    data=""
    counter=str()
    choose(msg)
    
  