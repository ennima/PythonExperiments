import threading
import time
import datetime
import os
import sys
import random
import math
sys.path.append('lib')
from l_dirchar import *
from l_workJson import *
from l_workList import *

class JobStatus:
	path = "test"
	log = "quequed.json"
	jobs = []

	def add(self,item):
		if(len(self.jobs)==0):
			self.items()
		if(findItemList(item,self.jobs)):
			print "Ya existe"
			
		else:
			print "Agrega"
			self.jobs.append(item)
			self.update()

	def items(self):
		fileOpen = self.path+dirChar+self.log

		try:
			if(not os.path.exists(self.path)):
				print "Making "+self.path
				os.makedirs(self.path)
		except WindowsError,e:
			print e	
		if(not os.path.exists(fileOpen)):
			self.update()

		self.jobs = readJson(fileOpen)
		print "totals: ",len(self.jobs)

	def delete(self,item):
		if(len(self.jobs)==0):
			self.items()

		if(findItemList(item,self.jobs)):
			print "elimina"
			self.jobs.remove(item)
			self.update()
		else:
			print "No existe"


	def update(self):
		saveJson(self.jobs,self.path,self.log)

queued = JobStatus()
queued.path = "assets\\app\\JobStatus"
queued.log = "queued.json"
#item = {"addTime": "2014-10-16T01:01:27", "name": "video10.cmf", "size": "252525"}
item = {"addTime": "2014-10-16T01:01:17", "name": "video19.cmf", "size": "252525"}
queued.add(item)
#queued.delete(item)