import os
import datetime
import sys
import time
import json
from time import mktime
from stat import *
from JobStatus import *
sys.path.append('..\..\lib')
from l_workJson import *


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
	jsonPath = ""
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
		#saveJson(self.downList,"",self.jsonName)
		log = JobStatus()
		log.log = self.jsonName
		log.path = self.jsonPath
		log.jobs = self.downList
		log.update()
		return self.downList
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
		
		if(dateInRange(modifiedDate,stringToTime(self.dateMin),self.dateMax)=="in"):
			#print "Agrega a la lista de descarga"
			#print fileItem
			print modifiedDate,"---",self.dateMin,"---",self.dateMax
			self.downList.append(fileItem)
			self.downFiles+= 1


		#print "totalFiles: ",self.totalFiles
		#print "downFiles: ",self.downFiles

