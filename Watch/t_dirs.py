import os
import datetime
import sys
import time
import json
from time import mktime
from stat import *
from l_workJson import *
from History import History
#### Object File
#				modififiedDate
#				name
#				path
#				type
#				size


dateMin = "2014-09-30T00:40:00"
dateMax = datetime.datetime.now()
dateFilter = "%Y-%m-%dT%H:%M:%S"

#Return datetime convierte una cadena tipo "2014-09-30T00:40:00" a datetime
def stringToTime(strl):
	minDate = time.strptime(strl,dateFilter)
	newDate = datetime.datetime.fromtimestamp(mktime(minDate))
	return newDate

#Return datetime convierte una cadena tipo "2014-09-30T00:40:00" a datetime
def stringToTime2(strl,dateFilter):
	minDate = time.strptime(strl,dateFilter)
	newDate = datetime.datetime.fromtimestamp(mktime(minDate))
	return newDate


def dateInRange(date,dateMin,dateMax):
	dato = "nada"
	if(dateMax > date):
		if(date > dateMin):
			dato = "in"
		else:
			dato = "out"
	else:
		dato = "future"
	return dato


def fechaMayor(modifiedDate,createdDate):
	workingDate = modifiedDate

	if(modifiedDate > createdDate):
		print "Correcto"
	elif(modifiedDate < createdDate):
		print "Copiado desde otro lado"
		workingDate = createdDate
	elif(modifiedDate == createdDate):
		print "Acabado de crear"
	else:
		print "Mira que raro"

	return workingDate


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


#Clase que analiza la media y genera la lista que cumple 
#Las condiciones fechaMin y path
class Analizer:

	dateMin = "2014-09-30T00:40:00"
	dateMax = datetime.datetime.now()
	totalFiles = 0
	downFiles = 0
	downList = []
	jsonName = "DownLoadList.json"
	basePath = "V:\\media\\"

	#Datos publicos Analizador
	totalFiles = 0
	downloadFiles = 0

	def walktreeDir(self, top, callback):
		print "-++-+-+-+TOP: ",top
		for f in os.listdir(top):
			pathname = os.path.join(top,f)
			mode = os.stat(pathname).st_mode
			
			if S_ISDIR(mode):
				#print "---------------------------------------"
				#print "NOMBRE: "+os.path.basename(pathname)
				ext = os.path.basename(pathname).split(".")
				nombre = ext[0]
				
				if((len(ext)-1)>0):
					#print "Es Conformable: "+ext[1]
					callback(pathname)
				else:
					walktree(pathname, callback)
				
			elif S_ISREG(mode):
				callback(pathname)
			else:
				print 'Skiping %s' % pathname
		#print "\n\n"
		#print self.downList
		saveJson(self.downList,"",self.jsonName)
		#print "-totalFiles: ",self.totalFiles
		#print "downFiles: ",self.downFiles


	def visitfile(self,filea):
		fileItem = {}

		self.totalFiles+= 1
		#print "\n \n"
		#print 'Visitng ', filea
		fileNameList= filea.split(".")
		extension = fileNameList[1]

		statFile = os.stat(filea)
		#print datetime.datetime.fromtimestamp(statFile.st_mtime)
		#print "###################################################"
		#print datetime.datetime.fromtimestamp(statFile.st_atime)
		#print datetime.datetime.fromtimestamp(statFile.st_ctime)

		modifiedDate = datetime.datetime.fromtimestamp(statFile.st_mtime)
		createdDate = datetime.datetime.fromtimestamp(statFile.st_atime)

		#print "modifiedDate: " +dateInRange(modifiedDate,stringToTime(dateMin),dateMax)
		#print "createdDate: " +dateInRange(createdDate,stringToTime(dateMin),dateMax)
		fileItem["modifiedDate"] = modifiedDate.strftime(dateFilter)
		fileItem["name"] = os.path.basename(fileNameList[0])
		fileItem["path"] = os.path.dirname(filea).replace("V:\\media\\","")
		fileItem["type"] = "file"
		fileItem["size"] = get_size(filea)

		#print "size: ",get_size(filea)
		#workingDate = fechaMayor(modifiedDate,createdDate)
		#print "workingDate: ", workingDate
		#print dateInRange(workingDate,stringToTime(dateMin),dateMax)
		
		if(dateInRange(modifiedDate,self.dateMin,self.dateMax)=="in"):
			#print "Agrega a la lista de descarga"
			#print fileItem
			print modifiedDate,"---",self.dateMin,"---",self.dateMax
			self.downList.append(fileItem)
			self.downFiles+= 1


		#print "totalFiles: ",self.totalFiles
		#print "downFiles: ",self.downFiles


#Ejecuta un proceso cada cierto tiempo
class Watcher():
	path = ""
	logList = "WatchLog.json"
	pollingTime = 1
	initLogList = "DownLoadList.json"
	backList = []
	lastPollingTime = 0
	dateFilter = "%Y-%m-%dT%H:%M:%S"
	continuePoll = 0
	watchLogReaded = 0
	isFirstPolling = 1
	
	def __init__(self):
		print "Poller Created..."
		print "  backList: "
		print self.backList

	def saveActualPollingTime(self):
		poliTime = []
		poliTime.append(self.lastPollingTime.strftime(self.dateFilter))
		saveJson(poliTime,"",self.logList)

	def afterPolling(self):
		print "After Poll ...."

	def beforePolling(self):

		#Obteniendo La ultima fecha de polling
		print "Setting Poller"

		if(self.watchLogReaded == 0):
			if(os.path.exists(self.initLogList)):
				self.backList = readJson(self.initLogList)
			else:
				initList = []
				self.backList = initList
			#Obtengo la fecha del ultimo polling desde File
			if(os.path.exists(self.logList)):
				polingTime = readJson(self.logList)
				self.lastPollingTime =stringToTime2(polingTime[0],self.dateFilter)
				deltaT = datetime.timedelta(days=1)
				ayer = datetime.datetime.now()-deltaT
				
				if(self.lastPollingTime < ayer):
					print "Mas de un dia sin ejecutar poller"
					self.lastPollingTime = 0
				else:
					print "Yea"
					print "------>",self.lastPollingTime

			self.watchLogReaded = 1
		elif(self.watchLogReaded == 1):
				#Obtengo la fecha del ultimo polling desde RAM
			print "Normal Watch at: ",self.lastPollingTime


		print "\n ###########  STEP 1 #############\n \n"

	def poller(self):

		print "Init Polling ....."

		try:
			while True:
				
				#Determino si es realmente la primera vez
				#que se hara el polling
				if(self.isFirstPolling == 0):

					print "\nWaitin for next polling... "+str(self.pollingTime)+"seconds \n"
					time.sleep(self.pollingTime)

				elif(self.isFirstPolling==1):

					print "First Polling..."
					self.isFirstPolling = 0
				


				print ":Prepare Polling"
				self.beforePolling()

				print ":Polling"
				self.onPolling()

				print ":After Polling"
				self.afterPolling()

		except KeyboardInterrupt:
			print "Close Poller"
			self.saveActualPollingTime()
	
	def buscaPorFecha(self,fechaMin):
		fechaCmd = fechaMin.strftime(self.dateFilter)
		print fechaCmd
		print "########### Path:",self.path
		print "########## FechaMin: ",fechaMin
		analizador = Analizer()
		analizador.dateMin = fechaMin
		analizador.jsonName = self.initLogList
		analizador.walktreeDir(self.path, analizador.visitfile)

	def onPolling(self):
		print "pollEvent"
		
		#Open Last
		#print self.backList[0]


		if (self.lastPollingTime == 0):
			print "primer poll \n \n \n "
			self.lastPollingTime = datetime.datetime.now()
		else:
			print "LastPollTime: ",self.lastPollingTime
			print "poll N"
			self.buscaPorFecha(self.lastPollingTime)
			
			print "ActualPollTime: ",self.lastPollingTime
			self.lastPollingTime = datetime.datetime.now()
			print "********Change lastPollingTime: ",self.lastPollingTime
		
		print "\n ###########  STEP 2 #############\n \n"



if __name__ == '__main__':
	
	watcher = Watcher()
	watcher.pollingTime = 10
	watcher.path = sys.argv[1]
	Watcher.initLogList = "Down.json"
	
	watcher.poller()