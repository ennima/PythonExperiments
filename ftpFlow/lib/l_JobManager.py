"""
	version: 0.0.1
	Author: Enrique Nieto
	Date: 16/09/14
	Description: Lib para apoyo en la creacion de Listas de Descarga


"""
from l_analisis import *

def test():
	print "Hello Manager"
	test_l_analisis()


def readJson(jsonFile):
	with open(jsonFile) as json_file:
		json_data = json.load(json_file)
		#print json_data

	print "Total de Files: "+str(len(json_data))
	
	return json_data

#Entrega una blackList de elementos
def discardDirs(dirsList,jsonData):
	mainList = []
	for item in jsonData:
		for carpeta in dirsList:
			if carpeta in item["path"]:
				pathSplitItem = item["path"].split(" ")
				lenSplitItem =len(pathSplitItem)
				pathSplitCarpeta = carpeta.split(" ")
				lenSplitCarpeta =len(pathSplitCarpeta)
				if(lenSplitCarpeta == lenSplitItem):
					#print item["path"]+"   "+carpeta+" "+item["name"]
					mainList.append(item)
	return mainList
	
#Entrega una lista sin los elementos de blackList
def cleanDownList(blackList,bruteList):
	mainList = []
	for item in bruteList:
		if not item in blackList:
			
			mainList.append(item)
	
	return mainList
		

