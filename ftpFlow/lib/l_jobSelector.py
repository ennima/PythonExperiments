"""
	version: 0.0.1
	Author: Enrique Nieto
	Date: 18/09/14
	Description: Lib para trabajo duro de optimizacion de listas de descarga


"""
from l_downList import *
from l_JobManager import *

class JobSelector():
	downPath = ""
	downList = []
	
	def __init__(self,downListPath):
		tipo =  type(downListPath)
		if(tipo is str):
			print "Es un Path falta downList"
			self.downPath = downListPath
			self.downList = readJson(downListPath)
			print "downList Loaded..."
		elif(tipo is list):
			print "downList Loaded"
			self.downList = downListPath
		else:
			print type(downListPath)
	
	#Entrega una version limpia de downList	
	def makeSubListByDiscard(self,dirsList):
		blackList = discardDirs(dirsList,self.downList)
		cleanList = cleanDownList(blackList,self.downList)
		return cleanList
	#Entrega un array de downLists con number elementos
	def makeSubListsByNumber(self,number):
		
		listDownList = []
		print "Elementos:" + str(len(self.downList))
		itemsPerList = float(len(self.downList) / number)
		
		itemsPerListFloat = float(len(self.downList) / float(number))
		difItemPerList = itemsPerListFloat - itemsPerList
		lastItemPerList = 0
		
		if(difItemPerList > 0):
			lastItemPerList = 1
		

		print "Salen "+str(number)+" de "+str(itemsPerList)+" items cada una"
	