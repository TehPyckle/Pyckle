#!/usr/bin/python

"""
tasks.py 
Coded by Donny and Logan
"""

class cumber:
	
	def SendMessage(self, message):
		self.SendPacket(['s', 'm#sm', self.mNum, self.penguinID, message])
	
	def SendSafeMessage(self, SafeID):
		self.SendPacket(['s','u#ss', self.mNum, SafeID])
	
	def SendEmote(self, emoteID):
		self.SendPacket(['s', 'u#se', self.mNum, emoteID])
		
	def SendPosition(self, x, y):
		self.SendPacket(['s','u#sp', self.mNum, x, y])
	
	def SendFrame(self, frameID):
		self.SendPacket(['s', 'u#sf', self.mNum, frameID])
		
	def JoinRoom(self, roomID):
		self.SendPacket(['s', 'j#jr', self.mNum, roomID, 0, 0])

	def AddStamp(self, stampID):
		self.SendPacket(['s','st#sse', self.mNum, stampID])
	
	def AddItem(self, itemID):
		self.SendPacket(['s', 'i#ai', self.mNum, itemID])
	
	def AddFurniture(self, furnitureID):
		self.SendPacket(['s','i#af', self.mNum, furnitureID])
		
	def SendSnowBall(self, x, y):
		self.SendPacket(['s', 'u#sb', self.mNum, x, y])