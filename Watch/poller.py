import time
import os
import json
import datetime
import subprocess
from time import mktime
from History import History
from l_workJson import *
from l_workList import *
"""##########################################
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
#Return datetime convierte una cadena tipo "2014-09-30T00:40:00" a datetime
def stringToTime(strl,dateFilter):
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



def poller(pollingTime,callback,downloadeds):

	print "Init Polling ....."

	"""for i in range(0,10):

		time.sleep(pollerTime)
		print "Poll Event"""
	try:
		while True:
			time.sleep(pollingTime)
			print "Polling"
			callback(downloadeds)
	except KeyboardInterrupt:
		print "Close Poller"

def cal(downloadeds):
	print "Poll Event"


class Watcher():
	path = ""
	logList = "WatchLog.json"
	pollingTime = 1
	initLogList = "DownLoadList.json"
	backList = []
	lastPollingTime = 0
	dateFilter = "%Y-%m-%dT%H:%M:%S"
	continuePoll = 0
	def beforePolling(self):
		print "Setting Poller"
		self.backList = readJson(self.initLogList)
		#Obtengo la fecha del ultimo polling
		if(os.path.exists(self.logList)):
			polingTime = readJson(self.logList)
			self.lastPollingTime =stringToTime(polingTime[0],self.dateFilter)
			deltaT = datetime.timedelta(days=1)
			ayer = datetime.datetime.now()-deltaT
			if(self.continuePoll==0):
				if(self.lastPollingTime < ayer):
					print "Mas de un dia sin ejecutar poller"
					self.lastPollingTime = 0
					self.continuePoll = 1
				else:
					print "Yea"
					self.continuePoll = 1

	def poller(self):

		print "Init Polling ....."

		try:
			while True:
				
				time.sleep(self.pollingTime)
				print "Time: ",self.lastPollingTime
				self.beforePolling()
				print "Time: ",self.lastPollingTime
				print "Polling"

				self.onPolling()
				print self.lastPollingTime
				#callback()

		except KeyboardInterrupt:
			print "Close Poller"
			poliTime = []
			poliTime.append(self.lastPollingTime.strftime(self.dateFilter))
			saveJson(poliTime,"",self.logList)
	
	def buscaPorFecha(self,fechaMin):
		fechaCmd = fechaMin.strftime(self.dateFilter)
		print fechaCmd
		#comando = "V:\media\PlayToAir "+fechaCmd
		
		
		#subprocess.call(["python t_dirs.py ",comando],shell=True)
		p = subprocess.Popen(['python','t_dirs.py','V:\media\PlayToAir',fechaCmd],shell=True)
		p.communicate()
		time.sleep(10)

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
			self.lastPollingTime = datetime.datetime.now()
			print "ActualPollTime: ",self.lastPollingTime
			
			self.buscaPorFecha(self.lastPollingTime)




downloadeds = readJson("DownLoadList.json")
testItem = {"modifiedDate": "2014-09-30T15:34:44", "name": "AF CORT 1 300914-FT_DF000MZ8", "path": "PlayToAir", "size": 75830627, "type": "file"}
pollerTime = 1

if (testItem in downloadeds):
	print "si esta"
else:
	print "nones"




watcher = Watcher()
watcher.poller()
