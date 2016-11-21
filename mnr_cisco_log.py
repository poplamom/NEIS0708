from Exscript.protocols import SSH2
from Exscript import Account
import time
import os
import threading

def showrun(ip, user, password):

    dateformat = '%d%m%y'
    timeformat = '%H%M%S'
    if not os.path.isdir(ip):
        os.makedirs(ip)
    savepath = './' + ip + "/"

    account = Account(user, password)
    conn = SSH2()
    conn.connect(ip)
    conn.login(account)
    conn.execute('terminal length 0')

    conn.execute('show tech-support')
    shrun = conn.response
    s01 = open(savepath+"config-"+time.strftime(dateformat)+"-"+time.strftime(timeformat)+".txt", "w")
    s01.write(shrun)
    s01.close()

    conn.send('exit\r')
    conn.close()

numberdevice = raw_input("Enter Number Device : ")
device = []
user = []
password = []

for i in range(1, int(numberdevice)+1):

    tmpdev = raw_input("Enter IP Address Device {0} : ".format(i))
    tmpuser = raw_input("Enter User Device {0}: ".format(i))
    tmppass = raw_input("Enter Password Device {0} : ".format(i))

    device.append(tmpdev)
    user.append(tmpuser)
    password.append(tmppass)

print 'please waiting .. ..'
for i in range(1, int(numberdevice)+1):
    device[i-1] = t = threading.Thread(target=showrun, args=(device[i-1], user[i-1], password[i-1]))
    device[i - 1].start()
    device[i - 1].join()

print 'Success'

