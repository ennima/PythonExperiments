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


class Randomsito:
	lastRand = 0
	def genRand(self):
		print "lastRand: "+str(self.lastRand)
		val = (random.randint(1,10))/10.0
		if (val == self.lastRand):
			val = val +1
		self.lastRand = val
		return val

def addFile(path,fileName):
	#dirChar = "\\"
	try:
		if(not os.path.exists(path)):
			print "Making "+path
			os.makedirs(path)
	except WindowsError,e:
		print e	
	fileToSave = path+dirChar+fileName
	if(os.path.exists(fileToSave)):

		print "Existe ",fileToSave
	else:
		print "No existe ",fileToSave

def addObjToFile(path,fileName,obj):
	#dirChar = "\\"
	document = []
	try:
		if(not os.path.exists(path)):
			print "Making "+path
			os.makedirs(path)
	except WindowsError,e:
		print e	
	fileToSave = path+dirChar+fileName
	if(os.path.exists(fileToSave)):

		print "Existe ",fileToSave
		tmpDocument = readJson(fileToSave)
		for item in tmpDocument:
			print item
			document.append(item)

		document.append(obj)
		saveJson(document,path,fileName)

	else:
		print "No existe ",fileToSave
		document.append(obj)
		saveJson(document,path,fileName)



def worker(rando):
	inicio = datetime.datetime.now()
	print "-"+threading.currentThread().getName()+ " Lanzado"
	
	for i in range(0,4):
		print "-"+threading.currentThread().getName()+ " -- "+str(i)
		time.sleep(5)
	print "-"+threading.currentThread().getName()+ " Detenido"
	fin = datetime.datetime.now()

	elemento = {"name":threading.currentThread().getName()+ " -- "+str(i),"addDate":fin.strftime("%Y-%m-%dT%H:%M:%S")}
	eventos.append(elemento)
	duerme = rando.genRand()
	print duerme
	time.sleep(duerme)
	print "Adding to log"
	addFile("test","log.json")

	delta =fin - inicio
	print "###"+threading.currentThread().getName()+"Tardo: "+str(delta)
def servicio():
	inicio = datetime.datetime.now()
	print "-"+threading.currentThread().getName()+ " Lanzado"
	time.sleep(3)
	print "-"+threading.currentThread().getName()+ " Detenido"
	fin = datetime.datetime.now()
	delta =fin - inicio
	print "###"+threading.currentThread().getName()+"Tardo: "+str(delta)
"""
hilos = []
num = 5
eventos = []
rando = Randomsito()
for i in range(0,num):
	t = threading.Thread(target=worker,args=(rando),name="Worker_"+str(i))
	hilos.append(t)

for proc in hilos:
	proc.start()
"""
class Agente:
	threadNumber = 5
	hilos = []
	eventos = []
	rando = Randomsito()
	jobs = [{"name":"video1.cmf","size":"252525"},{"name":"video12.cmf","size":"252525"},{"name":"video13.cmf","size":"252525"},{"name":"video14.cmf","size":"252525"},{"name":"video15.cmf","size":"252525"},{"name":"video16.cmf","size":"252525"},{"name":"video17.cmf","size":"252525"},{"name":"video18.cmf","size":"252525"},{"name":"video19.cmf","size":"252525"},{"name":"video10.cmf","size":"252525"}]
	pasadas = 0.0
	rangos = []
	actualJob = 0
	afterPassTime = 10
	tempPath = "tmp"
	tempThread = "tempThread.txt"

	def jobsEnd(self):
		intv = 0
		jobFile = self.tempPath+dirChar+self.tempThread
		try:
			if(not os.path.exists(self.tempPath)):
				print "Making "+self.tempPath
				os.makedirs(self.tempPath)
		except WindowsError,e:
			print e	
		if(not os.path.exists(jobFile)):
			intv = 0
			f = open(jobFile,"w")
			f.write(str(intv))
			f.close()
		else:
			f = open(jobFile,"r")
			val = f.read()
			intv = int(val)
			f.close()
		return intv

	def jobFree(self):
		intv = 0
		jobFile = self.tempPath+dirChar+self.tempThread
		try:
			if(not os.path.exists(self.tempPath)):
				print "Making "+self.tempPath
				os.makedirs(self.tempPath)
		except WindowsError,e:
			print e	
		if(not os.path.exists(jobFile)):
			intv = 1
			f = open(jobFile,"w")
			f.write(str(intv))
			f.close()
		else:
			f = open(jobFile,"r")
			val = f.read()
			intv = int(val)
			f.close()
			intv += 1
			f = open(jobFile,"w")
			f.write(str(intv))
			f.close()


	def onJob(self):
		print "###Working in thread"

	def start(self):
		jobstotal=len(self.jobs)
		pasadas = float(jobstotal) / float(self.threadNumber)
		self.pasadas = int(math.ceil(pasadas))
		print "Pasadas: ",self.pasadas,"--",pasadas
		
		for pasada in range(0,self.pasadas):
			valMin = pasada * self.threadNumber
			valMax = valMin + self.threadNumber
			if(valMax>jobstotal):
				valMax = jobstotal
			print "range(",valMin,",",valMax,")"

			self.rangos.append(range(valMin,valMax))

		for pasada in range(0,self.pasadas):
			print "pasada: ",pasada,"\n",self.rangos[pasada]
			for line in self.rangos[pasada]:
				print self.jobs[line]
				self.actualJob = line
				#self.onJob()
				t = threading.Thread(target=self.onJob,name="Worker_"+str(line))
				self.hilos.append(t)
			
			for proc in self.hilos:
				proc.start()
				proc.join()
			time.sleep(self.afterPassTime)

			
			self.hilos = []



#agent implements
"""
agent1 = Agente()
agent1.jobs = [{"name":"video1.cmf","size":"252525"},{"name":"video12.cmf","size":"252525"},{"name":"video13.cmf","size":"252525"},{"name":"video14.cmf","size":"252525"},{"name":"video15.cmf","size":"252525"},{"name":"video16.cmf","size":"252525"},{"name":"video17.cmf","size":"252525"},{"name":"video18.cmf","size":"252525"},{"name":"video19.cmf","size":"252525"},{"name":"video10.cmf","size":"252525"},{"name":"video20.cmf","size":"252525"}]
agent1.jobs.append({"name":"video21.cmf","size":"45655"})
agent1.jobs.append({"name":"video22.cmf","size":"45655"})
agent1.jobs.append({"name":"video23.cmf","size":"45655"})
agent1.jobs.append({"name":"video24.cmf","size":"45655"})

agent1.jobs.append({"name":"video25.cmf","size":"d5655"})
agent1.jobs.append({"name":"video26.cmf","size":"g5655"})

agent1.start()"""

class CarbonAgent(Agente):
	nuevoVal = "Hola Nuevo"
	def onTranscoding(self,jobObj):
		print "Transcoding: "+jobObj["name"]
		time.sleep(10)

	def onJob(self):
		nombreHilo = threading.currentThread().getName()
		nombreHilo_split = nombreHilo.split("_")
		indice = nombreHilo_split[1]
		print "++"+nombreHilo+" Inicia"
		duerme = self.rando.genRand()

		
		time.sleep(duerme)
		print "RANDOM: "+str(duerme)
		ahora = datetime.datetime.now()
		addTime = ahora.strftime("%Y-%m-%dT%H:%M:%S")
		itemFile = self.jobs[int(indice)]
		itemFile["addTime"] = addTime
		#item = {"name":"file"+indice+".cmf","addTime":addTime}

		self.onTranscoding(itemFile)

		addObjToFile("test","file.json",itemFile)
		print "--"+nombreHilo+" Termina"
		self.jobFree()


carbon = CarbonAgent()
carbon.jobs = [{"name":"video1.cmf","size":"252525"},{"name":"video12.cmf","size":"252525"},{"name":"video13.cmf","size":"252525"},{"name":"video14.cmf","size":"252525"},{"name":"video15.cmf","size":"252525"},{"name":"video16.cmf","size":"252525"},{"name":"video17.cmf","size":"252525"},{"name":"video18.cmf","size":"252525"},{"name":"video19.cmf","size":"252525"},{"name":"video10.cmf","size":"252525"},{"name":"video20.cmf","size":"252525"}]
carbon.start()