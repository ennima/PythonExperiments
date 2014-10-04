import datetime
import time
import json
import os
from l_workJson import *
from l_workList import *

from time import mktime
##########################################
"""
dirChar = "\\"
def readJson(jsonFile):
	with open(jsonFile) as json_file:
		json_data = json.load(json_file)
		#print json_data

	print "Total de Files: "+str(len(json_data))
	
	
	return json_data

def saveJson(data,path,fileName):
	if(not os.path.exists(path)):
		print "Making "+path
		os.makedirs(path)
	f = open(path+dirChar+fileName,"w+")
	json.dump(data,f)
	f.close()

def appendJson(data,path,fileName,orderField,filterField):
	tempList = []
	dataList = data
	#orderField = "id"
	if(not os.path.exists(path)):
		print "Making "+path
		os.makedirs(path)
	fileToSave = path+dirChar+fileName
	if(os.path.exists(fileToSave)):
		print "Existe ",fileToSave
		tempList = readJson(fileToSave)
		print "tempList: ",len(tempList)
		sotTempList = sortList(tempList,orderField)
		lastRow = len(sotTempList)-1
		print lastRow
		lastId = sotTempList[lastRow][orderField]
		print "Last Id",sotTempList[lastRow][orderField]
		print sotTempList[lastRow]
		
		sortData = sortList(data,orderField)
		contId = lastId+1
		
		for item in sortData:
			yaEsta = findInList(sotTempList,orderField,item[orderField])
			if(yaEsta != None):
				print "Existe en"
				coincide = findInList(sotTempList,orderField,item[filterField])
			else:
				print item
				item["id"] = contId
				sotTempList.append(item)
				contId += 1
		
	else:
		print "Nuevoi"
		sotTempList = data

	f = open(path+dirChar+fileName,"w+")
	json.dump(sotTempList,f)
	f.close()
"""

##########################################
"""
#Return Item From list that coincides item["Key"] = val
def findInList(lista,key,val):
	match = next((i for i in lista if i[key] == val),None)
	return match
def findItemList(item, lista):
	for linea in lista:
		print item
		print linea
		print "#######################\n"
#Return Sorted List from base list
def sortList(lista,keyy):
	newList = sorted(lista, key=lambda k:k[keyy])
	return newList

def diferenceList(lista1,lista2):
	listA =[]
	listB =[]
	diferencia = []
	if(len(lista1)>len(lista2)):
		#print "Lista1 Mayor"
		listA = lista2
		listB = lista1

	elif(len(lista1)<len(lista2)):
		#print "lista2 Mayor"
		listA = lista1
		listB = lista2
	elif(len(lista1)==len(lista2)):
		listA = lista1
		listB = lista2

	for lineaA in listA:
		#print lineaA,"\n"
		if(lineaA in listB):
			#print "Esta"
			pass
		else:
			#print "NONEs"
			diferencia.append(lineaA)
	return diferencia

"""

class History:

	baseList = []
	#Lista de versiones del historial
	#durante la ejecucion del programa
	historyList =[]
	#Lista de eventos Fusionada
	mergedList = []
	#Lista de movimientos en versiones
	versionMergedList = []

	#Ruta donde se almacenara el backup
	backupPath =""
	#Ruta donde se almacenara el historial
	path =""

	dateFilter = "%Y-%m-%dT%H:%M:%S"

	#Nombres de los archivos de Historial
	baseListJson = "baseList.json"
	historyListJson = "historyList.json"
	mergedListJson = "mergedList.json"
	versionMergedListJson = "versionMergedList.json"

	#Contador de adds
	addCounter = 0
	prevCounter = 0
	nextCounter = 0

	def __init__(self):
		print "History Created..."
		print "  baseList: "
		print self.baseList

	#Setea el historial a partir de un archivo guardado
	def openBaseList(self):
		pass

	#Set history from version merged List
	def openVersionMergedList(self):
		pass

	#Set history from merged list
	def openMergedList(self):
		pass


	def printStatus(self):
		print "\n ################ History Status ##############"
		print "baseList: ",len(self.baseList)
		print "historyList: ", len(self.historyList)
		print "mergedList: ", len(self.mergedList)
		print "versionMergedList: ", len(self.versionMergedList)
		
		#for linea in self.versionMergedList:
		#	print linea
		#print "\n \n"
	

	def restore(self):
		pass

	def delete(self):
		pass

	def addToMergedList(self,lista):
		for item in lista:

			self.mergedList.append(item)

	def add(self,lista):
		#self.baseList = lista
		#Agregar el registro
		historyItem = {"list":lista,"id":self.addCounter}
		self.historyList.append(historyItem)
		self.addCounter+=1

		#Generar las versiones

		#obteniendo diferencia o sea nuevos +
		diferencia = diferenceList(lista,self.baseList)
		self.addToMergedList(diferencia)

		#generando el version merge list
		versionHistoryItem = historyItem
		versionHistoryItem["news"]=diferencia
		versionHistoryItem["olds"]=self.baseList

		self.versionMergedList.append(versionHistoryItem)

		#setea Historial
		self.baseList = lista

	def getBaseList(self):
		print self.baseList
	
	def get(self):
		for linea in self.historyList:
			print linea
	
	def getVersion(self,version):
		versionItem = findInList(self.historyList,"id",version)
		return versionItem["list"]

	def prev(self):
		#Obtengo id de la version anterior
		self.prevCounter = self.addCounter - 1
		if(self.prevCounter < 0):
			self.prevCounter = 0
		
		print "Prev Version ID: ",self.prevCounter
		returnList = self.getVersion(self.prevCounter)

	#Para usar un History Nuevo a partir de una lista
	def set(self,lista):
		self.baseList = lista
		historyItem = {"list":lista,"id":self.addCounter}
		self.historyList.append(historyItem)
		self.addCounter+=1

		self.addToMergedList(lista)

		versionHistoryItem = historyItem
		versionHistoryItem["news"] = lista
		versionHistoryItem["olds"] = []
		self.versionMergedList.append(versionHistoryItem)
		
	def save(self):
		appendJson(self.mergedList,self.backupPath,self.mergedListJson,"id","datetime:")
		
	def reindexList(self,lista,indexKey):
		finOfList=len(lista)-1
		for index in range(0,finOfList):
			print lista[index]

		orderList = sortList(lista,indexKey)
		
		print "\n \n"
		
		reindexedList = []
		for index in range(0,finOfList):
			print orderList[index]
			tmpField = orderList[index]
			tmpField[indexKey] = index
			reindexedList.append(tmpField

				)

		print "\n \n"
		for linea in reindexedList:
			print linea

	




############# Implementacion de la clase
baseList = []
baseB = []
baseFormat = []
baseList.append({"id":0,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":5,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":2,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":3,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":4,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":9,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":6,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":7,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})

baseB = baseList
baseB.append({"id":18,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseB.append({"id":1,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})

historial = History()
historial.path = "history\his"
historial.backupPath = "Bk"
historial.set(baseList)
historial.get()

historial.printStatus()

baseList = baseFormat
baseList.append({"id":10,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})
baseList.append({"id":11,"datetime:":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})

historial.add(baseList)

print "Status historial"
historial.printStatus()

print "olds version 0 Len: ",len(historial.getVersion(0))

historial.prev()

historial.save()

historial.reindexList(historial.mergedList,"id")
"""
print "Test diferencia: "
print len(baseList)," , ",len(baseB)
dif = diferenceList(baseB,baseList)

for linea in dif:
	print linea"""