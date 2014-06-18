#!/usr/bin/python
#Title: Test.py (Can be anything)
#Coded by Logan @ Rile5.com

import cumber

ObjPenguin = cumber.cumber()
username = raw_input("Enter username: ")
password = raw_input("Enter password: ")
print "Connecting"
ObjPenguin.Connect(username, password, "204.75.167.37", 3724)
print "Joining Room"
ObjPenguin.JoinRoom(100)
print "Joined room"
ObjPenguin.Sleep(3)
print "SENDING Message"
ObjPenguin.SendMessage("Hello")
ObjPenguin.Sleep(3)
print "SENDING Emote"
ObjPenguin.SendEmote(1)
ObjPenguin.Sleep(3)
print "SENDING Position"
ObjPenguin.SendPosition(200, 200)
ObjPenguin.Sleep(3)
print "SENDING SnowBall"
ObjPenguin.SendSnowBall(300,300)

while True:
	ObjPenguin.Sleep(1000)
