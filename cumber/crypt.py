#!/usr/bin/python

#Title: crypt.py
#The hashing library, used for generating key and hashing password.
#Coded by Donny.

import hashlib

class crypt:
	def swapMD5(self, md5):
		return md5[16:32]+md5[0:16]
		
	def encryptPassword(self, password):
		return hashlib.md5(password.encode('utf-8')).hexdigest()
	
	def generateKey(self, password, rndKey):
		self.key = self.swapMD5(self.encryptPassword(password)) .upper()
		self.key += rndKey
		self.key += 'a1ebe00441f5aecb185d0ec178ca2305Y(02.>\'H}t":E1_root'
		return self.swapMD5(self.encryptPassword(self.key))