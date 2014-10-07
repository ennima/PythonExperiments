import datetime
import time
import json
import os
from l_workJson import *
from l_workList import *

from time import mktime

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

	key_id = "id"
	key_criteria = "datetime:"
	key_criteria2 = "datetime:"
	
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
		appendJson(self.mergedList,self.backupPath,self.mergedListJson,"id","name","size")
		#appendJson(self.mergedList,self.backupPath,self.mergedListJson,"id","name")
		
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
			reindexedList.append(tmpField)

		print "\n \n"
		for linea in reindexedList:
			print linea

	


