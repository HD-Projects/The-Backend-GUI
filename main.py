import smtplib
import json
from tkinter import *
import cgi
import email

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
  def login():
    top = Tk()
    L1 = Label(top, text="Username").grid(row = 0)
    #L1.pack()
    L2 = Label(top, text="Password").grid(row = 1)
     # L2.pack()
    e1 = Entry(top).grid(column = 1, row = 0)
    #e1.pack()
    e2 = Entry(top).grid(column = 1, row = 1)
    #e2.pack()
    b1 =  Button(top, text = "Done", command = top.destroy())
    top.mainloop()
    username = str(e1)
    password = str(e2)
    if ("@gmail.com" in username):
      L1 = Label(top, text="Username Worked").grid(row = 0)
      L1.pack()
    elif("@outlook.com" in username):
      L1 = Label(top, text="Username Worked").grid(row = 0)
      L1.pack()
    else:
      print("this email does not come from a supported provider \ntry an @gmail.com or @outlook.com email\n more coming soon")
    password = input("Input that password\n")
    # start TLS for security 
    s.starttls()
    # Authentication 
    s.login(username, password) 
    try:
      print("Succesful you are now logged in and can send emails")
      s = smtplib.SMTP('smtp.gmail.com', 587) 
      # start TLS for security 
      s.starttls()
      # Authentication 
      s.login(username, password) 
    except SMTPAuthenticationError:
      print("Wrong password Please re-enter")
      password = input("")
    except:
      print("""You have to allow less secure connections\n in your google account\n the url of the wepage to fix it is \/\nhttps://myaccount.google.com/u/2/security\n You can still add and remove emails until then or retry login""")
    
email.login()

if(email.listCheck() == 0):
  B1 = Button(top, text = "Add Email To The sending list", command = email.addEmail)
  B1.pack()
B2 = tkinter.Button(top, text = "Remove Email From the Sending list", command = email.removeEmail)
B2.pack()
B3 = tkinter.Button(top, text = "Send Emails", command = email.sendEmail)
B3.pack()
top.mainloop()




