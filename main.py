import smtplib
import json
import tkinter
import cgi
from tkinter

name = open("names.json", "w")
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

class email:
  def addEmail(email, names=[""]):
    names.append(names)
    emails.append(email)
  def removeEmail(names):
    removeNum = int(name.index(names))
    removeSTR = (email[1])
    name.remove(names)
    email.remove(removeSTR)
    print("Removed")
  def sendEmail(message):
    print("HI")


top = Tkinter.Tk()
while(1):
  B1 = Tkinter.Button(top, text = "Add Email To The Sending list", command = hello)
  B1.pack()
  B1 = Tkinter.Button(top, text = "Remove Email From the Sending list", command = hello)
  B1.pack()
