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
		val = False
		if(len(self.jobs)==0):
			self.items()
		if(findItemList(item,self.jobs)):
			#print "Ya existe"
			pass
			
		else:
			print "Agrega"
			self.jobs.append(item)
			self.update()
			val = True
		return val

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
		log_split = self.log.split(".")
		print log_split[0]+": ",len(self.jobs)
		return len(self.jobs)

	def delete(self,item):
		val = False
		if(len(self.jobs)==0):
			self.items()

		if(findItemList(item,self.jobs)):
			print "elimina"
			self.jobs.remove(item)
			self.update()
			val = True
		else:
			#print "No existe"
			pass
		return val

	def find(self,item):
		val = False
		#if(len(self.jobs)==0):
		#	self.items()

		if(findItemList(item,self.jobs)):
			#print "existe"
			val = True
		else:
			#print "No existe"
			pass

		return val

	def update(self):
		saveJson(self.jobs,self.path,self.log)
