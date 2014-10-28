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

class MainLoop(GameLoop):
	maxActive = 5
	active = JobStatus()
	completed = JobStatus()
	queued = JobStatus()
	failed = JobStatus()

	totalActivos = 0
	totalQueued = 0
	totalCompleted = 0
	totalFailed = 0

	def onAddActive(self):
		print "onAddActive ..."

	def onDeleteActive(self):
		print "onDeleteActive ..."

	def onDeleteQueue(self):
		print "onDeleteQueue ..."

	def onFailAddActive(self):
		#print "onFailAddActive ..."
		pass



	def onPlay(self):
		#print "Chingonada de cabron que eres"
		self.totalActivos = self.active.items()
		self.totalQueued = self.queued.items()
		self.totalCompleted =self.completed.items()
		self.totalFailed = self.failed.items()

		self.newActives()
		self.newCompleted()
		self.newFailed()
		

	def preReqStart(self):
		queued = JobStatus()
		queued.path = "assets\\app\\JobStatus"
		queued.log = "queued.json"

		active = JobStatus()
		active.path = "assets\\app\\JobStatus"
		active.log = "active.json"

		completed = JobStatus()
		completed.path = "assets\\app\\JobStatus"
		completed.log = "completed.json"

		failed = JobStatus()
		failed.path = "assets\\app\\JobStatus"
		failed.log = "failed.json"

		self.queued = queued
		self.active = active
		self.completed = completed
		self.failed = failed

	########################################################
	#	Eventos de Items
	########################################################
	def newActives(self):
		#### Paso3 Asignar Activos y quitarlos de cola
			
		#print "Step3"
		countActive = self.totalActivos

		for item in self.queued.jobs:
			#print item
			if (self.active.find(item)):
				#print "Existe en active"
				pass
			else:
				#print "Try Agrega"
				if(countActive<self.maxActive):

					self.active.add(item)
					self.onAddActive()

					countActive += 1
					self.queued.delete(item)
					self.onDeleteQueue()

				else:
					#print "Fail_Queda en espera hasta liberar jobs"
					self.onFailAddActive()

	def newCompleted(self):
		####Paso4 Quitar Terminados de Activos
		#print "Step4"
		#totalActivos = self.active.items()
		for item in self.completed.jobs:
			#print item
			if (self.active.find(item)):
				#print "Existe en active ... Quitando ..."
				self.active.delete(item)
				self.onDeleteActive()
			else:
				#print "En espera de mas completed"
				pass

	def newFailed(self):
		####Paso5 Quitar Fallados de Activos
		#print "Step5"
		#totalActivos = self.active.items()
		for item in self.failed.jobs:
			#print item
			if (self.active.find(item)):
				#print "Existe en active ... Quitando ..."
				self.active.delete(item)
				self.onDeleteActive()
			else:
				#print "En espera de mas Fallados"
				pass


mainLoop = MainLoop()
mainLoop.start()