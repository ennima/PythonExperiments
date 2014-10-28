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
sys.path.append('assets\\obj')
from GameLoop import *
from JobStatus import *
from Analizer import *


class QueuedLoop(GameLoop):
	exitFile = "endWatchLoop.txt"
	watchingTime = 10
	basePath = "V:\\media\\PlayToAir"
	def preReqStart(self):
		self.delayTime = self.watchingTime

	def onPlay(self):
		#print "A Webo papa eres una pistola "
		self.wacha()
		self.addQueue()

	def onAddQueue(self):
		print "onAddQueue..."
	###############################################
	#    Acciones de watching
	###############################################
	def wacha(self):
		#### Paso1 Obtener lista de posibles descargas
		
		analiza = Analizer()
		analiza.jsonName = "queuedTmp.json"
		analiza.jsonPath = "assets\\app\\JobStatus"
		analiza.basePath = self.basePath
		
		#deltaPast = datetime.timedelta(seconds=self.watchingTime)
		deltaPast = datetime.timedelta(minutes=30)
		ahora = datetime.datetime.now()
		miniDatePast = ahora - deltaPast
		
		#miniDate = "2014-10-16T00:40:00"
		miniDate = miniDatePast.strftime("%Y-%m-%dT%H:%M:%S")

		analiza.dateMin = miniDate
		analiza.walktreeDir(analiza.basePath,analiza.visitfile)

	def addQueue(self):
		#### Paso2 Agregar a cola
	
		queuedCompare = JobStatus()
		queuedCompare.path = "assets\\app\\JobStatus"
		queuedCompare.log = "queuedTmp.json"
		queuedCompare.items()

		queued = JobStatus()
		queued.path = "assets\\app\\JobStatus"
		queued.log = "queued.json"
		queued.items()
		for item in queuedCompare.jobs:
			#print item
			if (queued.find(item)):
				print "Existe en queued"
			else:
				print "Agrega a queued"
				queued.add(item)
				self.onAddQueue()
		
		

watchLoop = QueuedLoop()
watchLoop.start()