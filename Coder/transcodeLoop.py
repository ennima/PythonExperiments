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
sys.path.append('assets\\obj')
from GameLoop import *
from JobStatus import *
from Analizer import *
from Transcoder import *
from transLoop import *
from Mover import *

class transcodeLoop(TransLoop):
	maxThreads = 5
	mover = Mover()
	origin_path = ""
	destination_path = ""

	def onTranscoding(self,obj):
		print "# New transcodeLoop: "+obj["name"]
		#Paso1 Mover
		self.mover.origin_path = self.origin_path
		self.mover.destination_path = self.destination_path
		cmf = obj["name"]+".cmf"
		self.mover.move(cmf)


trans = transcodeLoop()
trans.origin_path = "V:\\media\\PlayToAir"
trans.destination_path = "E:\Shares\B_Workflow\PlayToAir"
trans.start()
