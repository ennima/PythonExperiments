import datetime
import time
import json
import os
from l_dirchar import *
from l_workList import *

def readJson(jsonFile):
	try:
		with open(jsonFile) as json_file:
			json_data = json.load(json_file)
			#print json_data

		#print "Total de Files: "+str(len(json_data))
	except ValueError:
		print "Error: Error con el Json ",jsonFile

		json_data = []
	json_file.close()	
	return json_data

def saveJson(data,path,fileName):
	savingName = ""
	if(path != ""):
		if(not os.path.exists(path)):
			print "Making "+path
			os.makedirs(path)
		savingName = path+dirChar+fileName
		
	else:
		savingName = fileName
	f = open(savingName,"w+")
	json.dump(data,f)
	f.close()
	print "Saved: ",savingName

def appendJson(data,path,fileName,orderField,filterField,compareField):
	tempList = []
	dataList = data
	addeds = 0
	#orderField = "id"
	if(not os.path.exists(path)):
		print "Making "+path
		os.makedirs(path)
	fileToSave = path+dirChar+fileName
	if(os.path.exists(fileToSave)):

		print "Existe ",fileToSave
		tempList = readJson(fileToSave)
		print "tempList: ",len(tempList)
		if(len(tempList) != 0):
			

			sotTempList = sortList(tempList,orderField)
			lastRow = len(sotTempList)-1
			print lastRow
			lastId = sotTempList[lastRow][orderField]
			print "Last Id",sotTempList[lastRow][orderField]
			print sotTempList[lastRow]
			
			sortData = sortList(data,orderField)
			contId = lastId+1
			
			for item in sortData:
				print"\n","ITEM "+orderField+": ",item[orderField],"--- "+filterField+": ",item[filterField],"--",compareField,": ",item[compareField]
				existeBy2 = findInList2(sotTempList,orderField,item[orderField],filterField,item[filterField])
				
				if(existeBy2 != None):
					print "Existe SIZE: ",existeBy2[compareField]
					print "Existe"
					if(item[compareField] == existeBy2[compareField]):
						print "Equals "
					else:
						#print "DiFERENTESSSSSS"
						print "Modified Data"
						#print "MODE: ",item
						existeModif = findInList2(sotTempList,'mode',"modified",filterField,item[filterField])
						#print "Modified Exists: ",existeModif
						if(existeModif != None):
							if(item[compareField] == existeModif[compareField]):
								print "Ya se agrego"
							else:
								print "Cambio de nuevo"
						else:
							#Agrega al log
							print "AGREGANDo"
							item["mode"] = "modified"
							item[orderField] = contId
							sotTempList.append(item)
							contId += 1
							addeds += 1

				else:
					print item
					item[orderField] = contId
					item["mode"] = "created"
					sotTempList.append(item)
					contId += 1
					addeds += 1
			
		else:
			print "Alguien a borrado manualmente el log"
			print "Nuevoioi"
			sotTempList = data
			for item in sotTempList:
				item["mode"] = "created"
				addeds +=1


	else:
		print "Nuevoi"
		sotTempList = data
		for item in sotTempList:
			item["mode"] = "created"
		addeds +=1

	print "Total de archivos agregados: ",addeds
	f = open(path+dirChar+fileName,"w+")
	json.dump(sotTempList,f)
	f.close()
	print "saved",path+dirChar+fileName
