import threading
import time
import datetime
import os
import sys
import random
import math
sys.path.append('lib')
from l_dirchar import *
from l_workJson import *
from l_workList import *

#print dirChar

class GameLoop:

	exitFile = "endLoop.txt"
	pathExit = ""
	exitFileTxt =""

	isPlaying = True
	isPaused = False

	exitCode = 0
	pauseCode = 2
	playCode = 1

	exitFileVal = 1

	delayTime = 0.5

	def __init__(self):

		if(self.pathExit == ""):
			self.exitFileTxt = self.exitFile
		else:
			self.exitFileTxt = self.pathExit+dirChar+self.exitFile
			self.preReq()

		if(not os.path.exists(self.exitFileTxt)):
			self.writeNewExitFile()
		else:
			print "existe El log: "+self.exitFileTxt
			
		print "GameLoop Creado!"

	

	def onPlay(self):
		print "En pleno loop"

	def onPause(self):
		print "Paused"

	def preReq(self):
		try:
			if(not os.path.exists(self.pathExit)):
				print "Making "+self.pathExit
				os.makedirs(self.pathExit)
		except WindowsError,e:
			print e	

	def preReqStart(self):
		print "pre start"

	def writeNewExitFile(self):
		print "creando Log"
		f = open(self.exitFileTxt,"w")
		f.write(str(self.playCode))
		f.close()
		return True

	def readExitFile(self):
		f = open(self.exitFileTxt,"r")
		val = f.read()
		f.close()
		intv = int(val)
		return intv

	def start(self):
		self.preReqStart()
		while (self.exitFileVal != self.exitCode):

			if(self.isPlaying):
				self.onPlay()

			elif(self.isPaused):
				self.onPause()

			if(self.exitFileVal == self.pauseCode):
				self.isPaused = True
				self.isPlaying = False
			elif(self.exitFileVal == self.playCode):
				self.isPaused = False
				self.isPlaying = True
			

			self.exitFileVal = self.readExitFile()
			print self.exitFileVal 
			time.sleep(self.delayTime)


#mainLoop = GameLoop()
#mainLoop.start()