import datetime
import time
import json
import os
from l_dirchar import *
from l_workList import *

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
