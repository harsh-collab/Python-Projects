import pywhatkit
import datetime
a = input("Enter the number:")
b = input("Enter the message:")
c = datetime.datetime.now()
m= c.minute+1
for i in range(0,5):
    pywhatkit.sendwhatmsg(a,b,c.hour,m,10,5)
    m+=1
