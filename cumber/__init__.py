#!/usr/bin/python

import socket, random, crypt, tasks, time

class cumber(tasks.cumber):
	def __init__(self):
		self.version = 2.5
		self.isConnected = False
		
	def getPort(self, username):
		self.ascii = 0
		for k in username:
			self.ascii += ord(k)
		return 3724 if self.ascii%2==0 else 6112
	
	def getLogin(self):
		self.ip_array = ['204.75.167.218', '204.75.167.219', '204.75.167.176', '204.75.167.177']
		return random.choice(self.ip_array)
	
	def SendPacket(self, rawPacket):
		self.packet = "%xt"
		for k in rawPacket:
			self.packet += '%' + ''.join(str(k))
		self.packet += "%" + chr(0)
		print "Sending packet : %s" % (self.packet)
		self.sock_server.send(self.packet)
		
	def RecvPacket(self):
		return self.sock_server.recv(1024)
		
	def decodePacket(self, rawPacket, needle):
		self.decodedPacket = []
		self.split = rawPacket.split(needle)
		for k in self.split:
			self.decodedPacket.append(k)
		return self.decodedPacket
		
	def Stribet(self, data, left, right):
		self.l = data.find(left) + len(left)
		self.r = data.find(right, self.l)
		return data[self.l:self.r]

	def Search(self, data, needle):
		return True if data.find(needle) == 0 else False
	
	def SendandWait(self, sock, data, needle):
		data = data + chr(0)
		#print "Sending data : %s" % (data)
		sock.send(data)
		self.dataBuffer = sock.recv(1024)
		while self.dataBuffer is None:
			if self.Search(self.dataBuffer, needle) == True:
				break 
		#print "Got response : %s" % (self.dataBuffer)
		return self.dataBuffer
		
	def Disconnect(self):
		self.sock_server.close()
	
	def Sleep(self, seconds):
		print "Program sleeping for %s seconds.." % (seconds)
		time.sleep(int(seconds))
	
	def Connect(self, username, password, server, port):
		print "Connecting to Club Penguin"
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.getLogin(), self.getPort(username)))
		self.SendandWait(self.sock, "<policy-file-request/>", "<cross-domain-policy/>")
		self.SendandWait(self.sock, "<msg t='sys'><body action='verChk' r='0'><ver v='153' /></body></msg>", "apiOK")
		self.rndKey = self.Stribet(self.SendandWait(self.sock, "<msg t='sys'><body action='rndK' r='-1'></body></msg>", "rndK"), "<k>", "</k>")
		#print "Obtained rndK : %s" % (self.rndKey)
		ObjC = crypt.crypt()
		self.key = ObjC.generateKey(password, self.rndKey)
		#print "Generated key : %s" % (self.key) 
		self.rawData = self.SendandWait(self.sock, "<msg t='sys'><body action='login' r='0'><login z='w1'><nick><![CDATA["+username+"]]></nick><pword><![CDATA["+self.key+"]]></pword></login></body></msg>", "%xt%l%-1")
		if self.Search(self.rawData, "%xt%l%-1"):
			self.isConnected = True
			print "Connected to Club Penguin"
		else:
			print "Couldn't connect to Club Penguin. Check the login details"
			exit(0)
		
		self.packet = self.decodePacket(self.rawData, "%")
		self.new_split = self.decodePacket(self.packet[4], "|")
		self.penguinID = self.new_split[0]
		self.raw = self.packet[4]
		self.confirmationKey = self.packet[5]
		self.loginKey = self.new_split[3]
		#print "penguin ID : %s" % (self.penguinID)
		#print "Raw : %s" % (self.raw)
		#print "Confirmation Key : %s" % (self.confirmationKey)
		#print "Login Key : %s" % (self.loginKey)
		self.sock.close()
		
		print "Joining server %s" % (server)
		self.sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock_server.connect((server, port))
		self.SendandWait(self.sock_server, "<policy-file-request>", "</cross-domain-policy>")
		self.SendandWait(self.sock_server, "<msg t='sys'><body action='verChk' r='0'><ver v='153' /></body></msg>", "apiOk")
		self.rndK = self.Stribet(self.SendandWait(self.sock_server, "<msg t='sys'><body action='rndK'r='-1'></body></msg>", "rndK"), "<k>", "</k>")
		#print "Obtained rndKey : %s" % (self.rndK)
		self.key2 = ObjC.swapMD5(ObjC.encryptPassword(self.loginKey + self.rndK))+self.loginKey
		#print "Key generated : %s" % (self.key2)
		self.SendandWait(self.sock_server, "<msg t='sys'><body action='login' r='0'><login z='w1'><nick><![CDATA["+self.raw+"]]></nick><pword><![CDATA["+self.key2+"#"+self.confirmationKey+"]]></pword></login></body></msg>", "%xt%l%-1%")
		self.SendandWait(self.sock_server, "%xt%s%j#js%-1%"+self.penguinID+"%"+self.loginKey+"%en%", "%-1%")
		self.loginData = self.SendandWait(self.sock_server, "%xt%s%g#gi%-1%", "gi")
		self.split_again = self.decodePacket(self.loginData, "%")
		self.mNum = self.split_again[44]
		print "%s joined server %s" % (username, server)