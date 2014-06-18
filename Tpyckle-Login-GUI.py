#Coded by Logan @ Rile5.com

import cumber, ttk, threading
from Tkinter import *


#Tkinter Application
root = Tk()
root.title("TPykcle - Login")
root.minsize('230', '130')
root.maxsize('650', '435')

#Application Specifications
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Functions
def loginUser(*args):
	username = usernameVar.get()
	password = passwordVar.get()
	def Login():
		ObjPenguin = cumber.cumber()
		ObjPenguin.Connect(username, password, "204.75.167.37", int(3724))
		ObjPenguin.JoinRoom(100)
		while True:
			ObjPenguin.Sleep(1000)
	t = threading.Thread(target=Login)
	t.start()


#Values
usernameVar = StringVar(mainframe)
passwordVar = StringVar(mainframe)

#Labels

titleLabel = ttk.Label(mainframe, text="Simple Login - Version 1.0")
usernameLabel = ttk.Label(mainframe, text="Username: ")
passwordLabel = ttk.Label(mainframe, text="Password: ")

#Input

usernameEntry = ttk.Entry(mainframe, width=35, textvariable=usernameVar)
passwordEntry = ttk.Entry(mainframe, width=35, textvariable=passwordVar)

#Buttons

loginButton = Button(mainframe, text="Login", command=loginUser)


#Application Layout

titleLabel.grid(column = 1, row = 1, sticky = (W, E))
usernameLabel.grid(column = 1, row = 2, sticky = (W))
passwordLabel.grid(column = 1, row = 3, sticky = (W))
usernameEntry.grid(column = 1, row = 2, sticky = (E))
passwordEntry.grid(column = 1, row = 3, sticky = (E))

loginButton.grid(column = 1, row = 4, sticky = (W, E))

#Configure Layout
titleLabel.configure(font='sintony 18', foreground="#018DCE")
usernameLabel.configure(font='sintony 12', foreground="#018DCE")
passwordLabel.configure(font='sintony 12', foreground="#018DCE")
loginButton.configure(font='sintony 14',foreground="#018DCE")


#Start Script
root.mainloop()