import smtplib
import json
from lists import (emails, names)
from tkinter import *
import cgi
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

listToWrite = ["hi","this","is","a","test"]

print ("Content-type: text/html")

messages = """<html>
<head><title>My first Python CGI app</title></head>
<body>
<p>Hello, 'world'!</p>
</body>
</html>"""

s = smtplib.SMTP('smtp.gmail.com', 587) 


supportedList = "Gmail, Outlook, Yahoo(Yahoo plus not supported yet), Office 365, Hotmail, AOL, O2, O2 UK, AT&T, \nNTL, BT Connect, BT Open World, BT Internet, Orange, Orange UK, Wanadoo UK, O2 Online Dutch, T-Online Dutch,\n1 and 1, 1 and 1 Dutch, Comcast, Verizon, Verizon Yahoo, YoHo, Mail or USANet"

username = ""
password = ""

name = ""
email = ""

e1 = ""
e2 = ""

class email:
  def save():
    theLists = open("lists.py", "w")
    stringToSave = 'names = ['
    for i in range(len(names)-2):
      stringToSave = stringToSave+'"'+names[i]+'",'
    stringToSave = stringToSave+'"'+names[(len(names)-1)]+'"]\nemails = ['
    i = 1
    for i in range(len(emails)-2):
      stringToSave = stringToSave+'"'+emails[i]+'",'
    stringToSave = stringToSave+'"'+emails[(len(emails)-1)]+'"]'
    theLists.write(stringToSave)
    print(stringToSave)
  def run():
    top = Tk()
    B1 = Button(top, text = "Add Email To The sending list", command = email.addEmail).grid(row = 0)
    B2 = Button(top, text = "Remove Email From the Sending list", command = email.removeEmail).grid(row = 1)
    B3 = Button(top, text = "Send Emails", command = email.sendEmail).grid(row = 2)
    B4 = Button(top, text = "Save email list", command = email.save).grid(row = 2)
    B5 = Button(top, text = "Done", command = top.destroy).grid(row = 3)
    top.mainloop()
  def getCredentials():
     username = e1
     password = e2
     print(username+" "+password)
  def loginSMTP():
    top = Tk()
    L1 = Label(top, text="Username").grid(row = 0)
    L2 = Label(top, text="Password").grid(row = 1)
    e1 = Entry(top, textvariable = username,).grid(column = 1, row = 0)
    e2 = Entry(top, textvariable = password).grid(column = 1, row = 1)
    Button(top, text = "Done", command = email.getCredentials).grid(row = 2)
    Button(top, text = "Done, closes window", command = top.destroy).grid(row = 3)
    top.mainloop()
    # start TLS for security 
    print("Debug Info: Username, "+  username+" Password, "+password)
    try:
       s.starttls()
       print("Debug Info: TLS Worked")
    except:
       print("Debug Info: TLS Failed")
    # Authentication 
    s.login(str(username), str(password))
    print("Succesful you are now logged in and can send emails")
    email.run()
  def gmail():
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    email.loginSMTP()
  def outlook():
    s = smtplib.SMTP('smtp-mail.outlook.com', 587)
    email.loginSMTP()
  def yahoo():
    s = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    email.loginSMTP()
  def hotmail():
    s = smtplib.SMTP('smtp.live.com', 25)
    email.loginSMTP()
  def AOL():
    s = smtplib.SMTP('smtp.aol.com', 587)
    email.loginSMTP()
  def yahooUK():
    s = smtplib.SMTP('smtp.mail.yahoo.co.uk', 25)
    loginSMTP()
  def O2():
    s = smtplib.SMTP('smtp.o2.ie', 25) 
    email.loginSMTP()
  def O2UK():
    s = smtplib.SMTP('smtp.o2.co.uk', 25) 
    email.loginSMTP()
  def ATT():
    s = smtplib.SMTP('smtp.att.yahoo.com', 465) 
    email.loginSMTP()
  def NTL():
    s = smtplib.SMTP('	smtp.ntlworld.com', 465)
    email.loginSMTP()
  def BTConnect():
    s = smtplib.SMTP('mail.btconnect.com', 25) 
    email.loginSMTP()
  def BTOpenworld():
    s = smtplib.SMTP('mail.btopenworld.com', 25) 
    email.loginSMTP()
  def BTInternet():
    s = smtplib.SMTP('mail.btinternet.com', 25) 
    email.loginSMTP()
  def Orange():
    s = smtplib.SMTP('smtp.orange.net', 25) 
    email.loginSMTP()
  def OrangeUK():
    s = smtplib.SMTP('smtp.orange.co.uk', 25) 
    email.loginSMTP()
  def WanadooUK():
    s = smtplib.SMTP('smtp.wanadoo.co.uk', 25) 
    email.loginSMTP()
  def O2OnlineDutch():
    s = smtplib.SMTP('mail.o2online.de', 25) 
    email.loginSMTP()
  def TDutch():
    s = smtplib.SMTP('securesmtp.t-online.de', 587) 
    email.loginSMTP()
  def OneAnd1():
    s = smtplib.SMTP('smtp.1and1.com', 587) 
    email.loginSMTP()
  def OneAnd1Dutch():
    s = smtplib.SMTP('smtp.1und1.de', 587) 
    email.loginSMTP()
  def comcast():
    s = smtplib.SMTP('smtp.comcast.net', 587) 
    email.loginSMTP()
  def Verizon():
    s = smtplib.SMTP('outgoing.verizon.net', 465) 
    email.loginSMTP()
  def VerizonYahoo():
    s = smtplib.SMTP('outgoing.yahoo.verizon.net', 587) 
    email.loginSMTP()
  def yoho():
    s = smtplib.SMTP('smtp.zoho.com', 465) 
    email.loginSMTP()
  def mail():
    s = smtplib.SMTP('smtp.mail.com', 587) 
    email.loginSMTP()
  def USANet():
    s = smtplib.SMTP('smtp.postoffice.net', 465) 
    email.loginSMTP()
  def login():
    top = Tk()
    L1 = Label(top, text="Login to your email\nOur supported Email providers are\n"+supportedList).grid(row = 0)
    R1 = Button(top, text="Gmail", command = email.gmail).grid(row = 1)
    R2 = Button(top, text="Outlook", command = email.outlook).grid(row = 2)
    R3 = Button(top, text="Yahoo", command = email.yahoo).grid(row = 3)
    R4 = Button(top, text="Hotmail", command = email.hotmail).grid(row = 4)
    R5 = Button(top, text="AOL", command = email.AOL).grid(row = 5)
    R6 = Button(top, text="Yahoo UK",  command = email.yahooUK).grid(row = 6)
    R7 = Button(top, text="O2",  command = email.O2).grid(row = 7)
    R8 = Button(top, text="O2 UK",  command = email.O2).grid(row = 8)
    R9 = Button(top, text="AT&T",  command = email.ATT).grid(row = 9)
    R10 = Button(top, text="NTL",  command = email.NTL).grid(row = 10)
    R11 = Button(top, text="BT Connect",  command = email.BTConnect).grid(row = 11)
    R12 = Button(top, text="BT Open World",  command = email.BTOpenworld).grid(row = 12)
    R13 = Button(top, text="BT Internet",  command = email.BTInternet).grid(row = 13)
    R14 = Button(top, text="Orange",  command = email.Orange).grid(row = 1, column = 1)
    R15 = Button(top, text="Orange UK",  command = email.OrangeUK).grid(row = 2, column = 1)
    R16 = Button(top, text="Wanadoo UK",  command = email.WanadooUK).grid(row = 3, column = 1)
    R17 = Button(top, text="O2 Online Dutch",  command = email.O2OnlineDutch).grid(row = 4, column = 1)
    R18 = Button(top, text="T-Online Dutch",  command = email.TDutch).grid(row = 5, column = 1)
    R19 = Button(top, text="1 and 1",  command = email.OneAnd1).grid(row = 6, column = 1)
    R20 = Button(top, text="1 and 1 Dutch",  command = email.OneAnd1Dutch).grid(row = 7, column = 1)  
    R21 = Button(top, text="Comcast",  command = email.comcast).grid(row = 8, column = 1)
    R22 = Button(top, text="Verizon",  command = email.Verizon).grid(row = 9, column = 1)
    R23 = Button(top, text="Verizon, yahoo",  command = email.VerizonYahoo).grid(row = 10, column = 1)
    R24 = Button(top, text="YoHo",  command = email.yoho).grid(row = 11, column = 1)
    R25 = Button(top, text="Mail",  command = email.TDutch).grid(row = 12, column = 1)
    R26 = Button(top, text="USANet",  command = email.TDutch).grid(row = 13, column = 1)
    Button(top, text = "Done", command = top.destroy).grid(row = 14)
    top.mainloop()
  def addEmail():
    top = Tk()
    L1 = Label(top, text="Name").grid(row = 0)
    L2 = Label(top, text="Email").grid(row = 1)
    e1 = Entry(top, textvariable = "name").grid(column = 1, row = 0)
    e2 = Entry(top, textvariable = "email").grid(column = 1, row = 1)
    Button(top, text = "Done", command = top.destroy).grid(row = 9)
    top.mainloop()



    names.append(str(e1))
    emails.append(str(e2))
  def removeEmail(names):
    removeNum = int(name.index(names))
    removeSTR = (email[removeNum])
    name.remove(names)
    email.remove(removeSTR)
    print("Removed")
  def sendEmail():
    top = Tk()
    L1 = Label(top, text="Message").grid(row = 0)
    L2 = Label(top, text="Subject").grid(row = 1)
    e1 = Entry(top, textvariable = username,).grid(column = 1, row = 0)
    e2 = Entry(top, textvariable = password).grid(column = 1, row = 1)
    done = Button(top,text = "Done, you will have to close the window after you press this", command = email.getCredentials)
    top.mainloop()
    i = 0
    for i in range(len(names)):
      msg = MIMEMultipart()       # create a message
      # setup the parameters of the message
      msg['From']=usernames
      msg['To']=emails[i]
      msg['Subject']="This is TEST"
      msg['Body']="Dear "+names[i]+",\n"+messages
      s.send_message(msg)
      print("Send, "+msg)
      msg.destroy()

email.login()
email.run()