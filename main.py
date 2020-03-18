import smtplib
import json
from tkinter import *
import cgi
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

nameList = open("names.json", "w")
emailList = open("emails.json", "w")

listToWrite = ["hi","this","is","a","test"]

names = ["Alex","Riley"]
emails = ["adickhans@gmail.com","rilesdk@gmail.com"]

print ("Content-type: text/html")

messages = """<html>
<head><title>My first Python CGI app</title></head>
<body>
<p>Hello, 'world'!</p>
</body>
</html>"""

s = smtplib.SMTP('smtp.gmail.com', 587) 



username = ""
password = ""

e1 = ""
e2 = ""

class email:
  def run():
    if(email.listCheck() == 0):
      B1 = Button(top, text = "Add Email To The sending list", command = email.addEmail).grid(row = 0)
    B2 = Button(top, text = "Remove Email From the Sending list", command = email.removeEmail).grid(row = 1)
    B3 = Button(top, text = "Send Emails", command = email.sendEmail).grid(row = 2)
    top.mainloop()
  def loginSMTP():
    top = Tk()
    L1 = Label(top, text="Username").grid(row = 0)
    L2 = Label(top, text="Password").grid(row = 1)
    e1 = Entry(top, textvariable = username).grid(column = 1, row = 0)
    e2 = Entry(top, textvariable = password).grid(column = 1, row = 1)
    Button(top, text = "Done", command = top.destroy).grid(row = 2)
    top.mainloop()
    # start TLS for security 
    s.starttls()
    # Authentication 
    s.login(username, password)
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
  def login():
    top = Tk()
    supportedList = "Gmail, Outlook, Yahoo(Yahoo plus not supported yet), Office 365, Hotmail and AOL"
    L1 = Label(top, text="Login to your email\nOur supported Email providers are\n"+supportedList).grid(row = 0)
    R1 = Button(top, text="Gmail", command = email.gmail).grid(row = 1)
    R2 = Button(top, text="Outlook", command = email.outlook).grid(row = 2)
    R3 = Button(top, text="Yahoo", command = email.yahoo).grid(row = 3)
    R4 = Button(top, text="Hotmail", command = email.hotmail).grid(row = 4)
    R5 = Button(top, text="AOL", command = email.AOL).grid(row = 5)
    R6 = Button(top, text="Yahoo UK",  command = email.yahooUK).grid(row = 6)
    Button(top, text = "Done", command = top.destroy).grid(row = 7)
    top.mainloop()
  def addEmail():
    top.destroy()
    top = Tk()
    L1 = Label(top, text="Username").grid(row = 0)
    L2 = Label(top, text="Password").grid(row = 1)
    e1 = Entry(top).grid(column = 1, row = 0)
    e2 = Entry(top).grid(column = 1, row = 1)
    names.append(names)
    emails.append(email)
    name.write(names)
    name.close()
    emailList.write(emails)
    emailList.close()
    Ename = open("names.json", "w")
    emailList = open("emails.json", "w")
  def removeEmail(names):
    removeNum = int(name.index(names))
    removeSTR = (email[1])
    name.remove(names)
    email.remove(removeSTR)
    print("Removed")
  def sendEmail(message):

    print("HI")
  def listCheck():
    if(len(emails)>500):
      print("You list of emails is too long to send in one day on a basic gmail account\n")
      return 1
    else:
      return 0;
    
email.login()
top = Tk()
