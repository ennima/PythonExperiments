"""
	version: 0.0.1
	Author: Enrique Nieto
	Date: 16/09/14
	Description: Librería de analisis de elementos en File System remoto vía FTP


"""
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
	hoy = datetime.now()
	actualYear = (datetime.now().year)-2000
	pastYear = actualYear -1
	#print str(actualYear)
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

		fechaFile = str(actualYear)+" "+str(dataSplit[5])+" "+str(dataSplit[6])+" "+str(horaFile[0])+" "+str(horaFile[1])
		modifiedDate = time.strptime(fechaFile,"%y %b %d %H %M")
	modifiedDateDT = datetime.fromtimestamp(mktime(modifiedDate))
	if (modifiedDateDT>hoy):
		#print "Mames Es del pinche futuro"
		fechaFile = str(pastYear)+" "+str(dataSplit[5])+" "+str(dataSplit[6])+" "+str(horaFile[0])+" "+str(horaFile[1])
		modifiedDate = time.strptime(fechaFile,"%y %b %d %H %M")
		modifiedDateDT = datetime.fromtimestamp(mktime(modifiedDate))
	rowDict["modifiedDate"] = modifiedDateDT.strftime('%Y-%m-%dT%H:%M:%S')
	rowDict["path"]=""
	
	return rowDict
#minDateString format "2014-09-15T11:00:00","%Y-%m-%dT%H:%M:%S"
#Return Sub List in reverse range minDataString - now
def listFromObject(obj,minDateString,path):
	totalObjects = len(obj)
	newList = []
	tmpDic = {}
	newObj = sorted(obj,key=lambda orden:orden['modifiedDate'],reverse=True)
	#print totalObjects
	for i in newObj:
		tmpDic = i
		tmpDic["path"]=path
		#print tmpDic["modifiedDate"]+"----"+tmpDic['name']
		newDate= time.strptime(tmpDic["modifiedDate"],"%Y-%m-%dT%H:%M:%S")
		modifiedDateN = datetime.fromtimestamp(mktime(newDate))

		#minDate = time.strptime("2014-09-15 11:00:00","%Y-%m-%d %H:%M:%S")
		minDate = time.strptime(minDateString,"%Y-%m-%dT%H:%M:%S")
		minmodifiedDateDT = datetime.fromtimestamp(mktime(minDate))
		#print modifiedDateN," - ",datetime.now()
		dateIn = dateInRange(modifiedDateN,minmodifiedDateDT,datetime.now())
		#print dateIn
		if(dateIn == "in"):
			#print tmpDic["modifiedDate"]+"----"+tmpDic['name']
			newList.append(tmpDic)
	#print len(newList)," archivos"
	#print json.dumps(newList)
	return newList


#Obtiene una lista de items de descarga en un Host y dentro de un path
def findInServer(host,user,passw,path):
	data = []
	print "path: "+path
	con = ftplib.FTP(host)
	con.login(user,passw)
	
	result = []
	try:
		s = con.retrlines('LIST '+path, callback=result.append)
	except:
		print "LIST Error"
	print len(result)
	for item in result:
		data.append(dataFromFtpLine(item))
	con.quit()
	return data


#"2014-09-15T09:40:00"
#Genera la lista principal de descargas a 4 niveles de profundidad en un FS
def runListFind(obj,minDate):
	#print "Items a recorrer: ",len(obj)
	mainData = []
	data =[]
	inData = []
	for item in obj:
		#print item
		if(item["type"] == "dir"):
			#print "----------entra y busca------------"
			#obtiene Lista total
			data = findInServer('192.168.196.139','mxfmovie','',item["name"])
			#secciona la lista
			subData = listFromObject(data,minDate,item["name"])
			totalEncontrados = len(subData)
			#Si hay items
			if(totalEncontrados>0):
				#print "Encontrados: ",totalEncontrados," tipo: ",data[0]["type"]
				
				for subItem in subData:
					#print "|-->",subItem
					#Si es un directorio busca
					if (subItem["type"] == "dir"):
						#print" !-->"+subItem['modifiedDate']+" "+subItem['name']
						subSubPath = subItem["path"]+"/"+subItem["name"]
						#print "sPath: "+subSubPath
						subSubData = findInServer('192.168.196.139','mxfmovie','',subSubPath)
						sSubSubData= listFromObject(subSubData,minDate,subSubPath)
						#print "Total de elementos:",len(sSubSubData)
						for sSubItem in sSubSubData:
							#print "  1-->"+sSubItem["type"]+" "+sSubItem["modifiedDate"]+" "+sSubItem["name"]
							#mainData.append(sSubItem)
							if(sSubItem["type"]=="dir"):
								nsSubItemPath = sSubItem["path"]+"/"+sSubItem["name"]
								nsSubData = findInServer('192.168.196.139','mxfmovie','',nsSubItemPath)
								nssSubData = listFromObject(nsSubData,minDate,nsSubItemPath)
								for inItem in nssSubData:
									#print ">>>"+inItem["modifiedDate"]+" "+inItem["type"]+" "+inItem["path"]+"/"+inItem["name"]
									#raw_input()
									if(inItem["type"]=="dir"):
										print "dir"
										subInItemPath = inItem["path"]+"/"+inItem["name"]
										subItemData = findInServer('192.168.196.139','mxfmovie','',subInItemPath)
										sSubItemData = listFromObject(subItemData,minDate,subInItemPath)
										for sInItem in sSubItemData:
											mainData.append(sInItem)
											print sInItem["path"]+"/"+sInItem["name"]
											raw_input()
									else:
										if(inItem["type"]=="file"):
											print "file"
											mainData.append(inItem)
					else:			
						#si es un archivo
						if(subItem["type"]=="file"):
							#print "File"
							mainData.append(subItem)


			else:
				#Si no hay Items
				print "nada"

		else:
			if(item["type"]=="file"):
				#print "Agrega"
				mainData.append(item)

	return mainData