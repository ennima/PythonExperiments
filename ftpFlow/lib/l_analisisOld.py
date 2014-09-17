from datetime import datetime
from time import mktime
import os.path, time, json
import ftplib

def ftpElementType(dataString):
	dataType = "Corrupto"
	if (dataString =="drwxr-xr-x"):
		#print "Directorio"
		dataType = "dir"
	else:
		#print "File"
		dataType = "file"

	return dataType

def ftpElementName(dataSplit):
	nombre = ""
	#Los 7 primeros son fecha y tipo del 8 al final son nombre
	if(len(dataSplit)>9):

		for palabra in range(8,len(dataSplit)):
			#print dataSplit[palabra]
			
			if(palabra == len(dataSplit)-1):
				nombre += dataSplit[palabra]
			else:
				nombre += dataSplit[palabra]+" "
	else:
		nombre = dataSplit[8]
		#print "----------"

	return nombre

def saveJson(data,path,fileName):
	f = open(path+fileName,"w")
	json.dump(data,f)
	f.close()

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

def timeFromFtpLine(ftpline):
	dataSplit = ftpline.split()
	modifiedDate = time

	print dataSplit
	thisYear = len(dataSplit[7].split(":"))
	horaFile = dataSplit[7].split(":")
	if(thisYear == 1):
		print thisYear
		fechaFile = dataSplit[7]+" "+str(dataSplit[5])+" "+str(dataSplit[6])
		modifiedDate = time.strptime(fechaFile,"%Y %b %d")
	else:
		fechaFile = "14 "+str(dataSplit[5])+" "+str(dataSplit[6])+" "+str(horaFile[0])+" "+str(horaFile[1])
		modifiedDate = time.strptime(fechaFile,"%y %b %d %H %M")
	modifiedDateDT = datetime.fromtimestamp(mktime(modifiedDate))
	return modifiedDateDT

def dataFromFtpLine(ftpline):
	rowDict = {}
	dataSplit = ftpline.split()
	modifiedDate = time
	nombre = ""

	#Obteniendo Tipo de elemento
	rowDict["type"] = ftpElementType(dataSplit[0])
	#Obteniendo Nombre de elemento
	rowDict["name"] = ftpElementName(dataSplit)
	

	#Obteniendo ModifiedDate
	thisYear = len(dataSplit[7].split(":"))
	horaFile = dataSplit[7].split(":")
	if(thisYear == 1):
		#print thisYear
		fechaFile = dataSplit[7]+" "+str(dataSplit[5])+" "+str(dataSplit[6])
		modifiedDate = time.strptime(fechaFile,"%Y %b %d")
	else:
		fechaFile = "14 "+str(dataSplit[5])+" "+str(dataSplit[6])+" "+str(horaFile[0])+" "+str(horaFile[1])
		modifiedDate = time.strptime(fechaFile,"%y %b %d %H %M")
	modifiedDateDT = datetime.fromtimestamp(mktime(modifiedDate))
	
	rowDict["modifiedDate"] = modifiedDateDT.strftime('%Y-%m-%dT%H:%M:%S')
	rowDict["path"]=""
	
	return rowDict

