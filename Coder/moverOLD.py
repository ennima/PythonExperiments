import time
import datetime
import os
import sys

import shutil
sys.path.append('lib')
from l_dirchar import *
from l_workJson import *

class Mover:
	
	origin_path = ""
	#origin_file = ""

	destination_path = ""
	#destination_file = ""

	#fileName = ""
	def beforeMove(self):
		pass

	def afterMove(self):
		pass

	def move(self,fileName):
		print "moving: "+fileName

		beforeMove()
		desde = self.origin_path+dirChar+fileName
		hasta = self.destination_path+dirChar+fileName

		shutil.copytree(desde,hasta)
		afterMove()


