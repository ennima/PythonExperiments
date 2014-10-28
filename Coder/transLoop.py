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
from Transcoder import *

class Randomsito:
	lastRand = 0
	def genRand(self):
		print "lastRand: "+str(self.lastRand)
		val = (random.randint(1,10))/10.0
		if (val == self.lastRand):
			val = val +1
		self.lastRand = val
		return val

class TransLoop(GameLoop):
	exitFile = "endTransLoop.txt"
	
	active = JobStatus()
	completed = JobStatus()

	totalActivos = 0
	totalComplete = 0
	maxThreads = 2
	activeThreads = 0
	activeJobs = []
	workingHilosName = []
	hilos = []
	activeHilosName = []

	rando = Randomsito()

	def preReqStart(self):
		active = JobStatus()
		active.path = "assets\\app\\JobStatus"
		active.log = "active.json"

		completed = JobStatus()
		completed.path = "assets\\app\\JobStatus"
		completed.log = "completed.json"

		self.active = active
		self.completed = completed

		for i in range(0,self.maxThreads):
			self.activeHilosName.append(i)


	def onPlay(self):
		print "Trans Loop "+str(self.activeThreads)
		self.totalActivos = self.active.items()
		print " indicesDisponibles: "
		print self.activeHilosName
		if(self.totalActivos!=0):
			for job in self.active.jobs:
				print "-->",job
				if(job in self.activeJobs):
					print "En Proceso "+job["name"]
					if(len(self.activeHilosName) == self.maxThreads):
						print "####Atorado"
						
						self.activeJobs.remove(job)
						preReqStart()

				else:
					print "Agrega "+job["name"]
					self.activeJobs.append(job)
					#self.onAddThread()
					inidice = -1

					if(len(self.activeHilosName)>1):
						for index in range(0,len(self.activeHilosName)):
							print self.activeHilosName[index]

						indexItem = len(self.activeHilosName) - 1
						inidice = self.activeHilosName[indexItem]
						self.activeHilosName.remove(inidice)

					elif(len(self.activeHilosName)==1):
						print self.activeHilosName[0]
						inidice = self.activeHilosName[0]
						self.activeHilosName.remove(inidice)

					elif(len(self.activeHilosName)==0):
						print "No hay Disponibles"
					if(inidice != -1):
						print "Asigna un Hilo:"+str(inidice)
						t = threading.Thread(target=self.onJob,name="Transcoder_"+str(inidice))
						IndexHilos = len(self.hilos)
						self.hilos.append(t)
						self.hilos[IndexHilos].start()
						#self.hilos[IndexHilos].join()
						self.activeThreads += 1
					else:
						print "Todos los Hilos estan en uso"
				
		else:
			print "No hay trabajos por hacer"
		time.sleep(5)

		
	#################################################
	# Acciones propias del transcoder
	#################################################
	def onAddThread(self):
		print "Inicia onThread"
		time.sleep(1)
		print "fin onThread"

	def onTranscoding(self,obj):
		print "TRANSCODE ELEMENT in Thread"+obj["name"]

	def onJob(self):
		nombreHilo = threading.currentThread().getName()
		nombreHilo_split = nombreHilo.split("_")
		indice = int(nombreHilo_split[1])
		indiceJob = (self.maxThreads - indice) - 1
		print "#######onJob"+nombreHilo
		
		itemJob = self.activeJobs[indiceJob]
		print "Name of Work: ",itemJob["name"]
		self.onTranscoding(itemJob)
		time.sleep(5)


		duerme = self.rando.genRand()
		time.sleep(duerme)
		print "RANDOM: "+str(duerme)
		print "ending -- "+nombreHilo
		if(indice in self.activeHilosName):
			print "Existe "+str(indice)
		else:
			print "Libera este hilo "+str(indice)
			self.activeHilosName.append(indice)

			self.activeHilosName=sorted(self.activeHilosName,reverse = False)
			if(itemJob in self.activeJobs):
				print "Elimina"
				self.activeJobs.remove(itemJob)
				self.completed.add(itemJob)
			else:
				print "ya no esta"
			self.activeThreads -= 1
		time.sleep(10)

#transWork = TransLoop()
#transWork.start()