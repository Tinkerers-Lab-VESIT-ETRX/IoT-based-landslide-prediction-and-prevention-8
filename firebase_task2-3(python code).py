import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

ports=serial.tools.list_ports.comports()
for port,desc,hwid in sorted(ports):
    print("{}: {} [{}]".format(port,desc,hwid))

ser=serial.Serial("COM4",9600)
print(ser.readline())
#print("cc")
res=1
i=0
time=datetime.now().strftime("%d-%m-%y %H:%M:%S")
print(time)
while res:
    #cc=str(1234)
    #print(cc)
    #val=cc
    firebase1=firebase.FirebaseApplication("https://sensordata-8b704-default-rtdb.firebaseio.com/",None)

    for i in range(0,4):
        #string1="123"
        string1=str(ser.readline())
        string1=string1[11:][:-25]
        a=int(string1)
        data={ "date":datetime.now().strftime("%Y-%m-%d"),
               "reading":a,
               "time":datetime.now().strftime("%H:%M")
      }
        result = firebase1.patch('https://sensordata-8b704-default-rtdb.firebaseio.com/'+ '/Moisture_data/'+ str(i), data)
        print(result)

    for i in range(0,4):
        #string2="vvcf"
        string1=str(ser.readline())
        string1=string1[20:][:-16]
        b=int(string1)
        data={ "date":datetime.now().strftime("%Y-%m-%d"),
               "reading":b ,
               "time":datetime.now().strftime("%H:%M")
      }
        result1 = firebase1.patch('https://sensordata-8b704-default-rtdb.firebaseio.com/'+'/Temperature_data/'+ str(i),data)
        print(result1)

    for i in range(0,4):
        string1=str(ser.readline())
        string1=string1[30:][:-5]
        c=int(string1)
        data={"date":datetime.now().strftime("%Y-%m-%d"),
            "reading":c,
            "time":datetime.now().strftime("%H:%M")
      }
        result2=firebase1.patch('https://sensordata-8b704-default-rtdb.firebaseio.com/'+'/Humidity_data/'+ str(i),data)
        print(result2)
      
    res=0
        
    
       
              
                                             
