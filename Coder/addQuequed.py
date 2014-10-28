import threading
import time
import datetime
import os
import sys
import random
import math
from time import mktime
sys.path.append('lib')
from l_dirchar import *
from l_workJson import *
from l_workList import *
sys.path.append('assets\obj')
from JobStatus import *
from Analizer import *

#### Paso1 Obtener lista de posibles descargas
"""
analiza = Analizer()
analiza.jsonName = "queuedTmp.json"
analiza.jsonPath = "assets\\app\\JobStatus"
analiza.basePath = "V:\\media\\PlayToAir"
miniDate = "2014-10-16T00:40:00"

analiza.dateMin = miniDate
analiza.walktreeDir(analiza.basePath,analiza.visitfile)
"""



#### Paso2 Agregar a cola
"""
queuedCompare = JobStatus()
queuedCompare.path = "assets\\app\\JobStatus"
queuedCompare.log = "queuedTmp.json"
queuedCompare.items()

queued = JobStatus()
queued.path = "assets\\app\\JobStatus"
queued.log = "queued.json"
queued.items()
for item in queuedCompare.jobs:
	#print item
	if (queued.find(item)):
		print "Existe en queued"
	else:
		print "Agrega"
		queued.add(item)
"""
#### Paso3 Asignar Activos y quitarlos de cola

queued = JobStatus()
queued.path = "assets\\app\\JobStatus"
queued.log = "queued.json"
queued.items()

active = JobStatus()
active.path = "assets\\app\\JobStatus"
active.log = "active.json"
totalActivos = active.items()

maxActive = 5
countActive = totalActivos
for item in queued.jobs:
	#print item
	if (active.find(item)):
		print "Existe en active"
	else:
		print "Try Agrega"
		if(countActive<maxActive):
			active.add(item)
			countActive += 1
			queued.delete(item)
		else:
			print "Fail_Queda en espera hasta liberar jobs"

####Paso4 Quitar Terminados de Activos

active = JobStatus()
active.path = "assets\\app\\JobStatus"
active.log = "active.json"
totalActivos = active.items()

completed = JobStatus()
completed.path = "assets\\app\\JobStatus"
completed.log = "completed.json"
totalActivos = completed.items()

for item in completed.jobs:
	#print item
	if (active.find(item)):
		print "Existe en active ... Quitando ..."
		active.delete(item)
	else:
		print "En espera de mas completed"


####Paso5 Quitar Fallados de Activos
active = JobStatus()
active.path = "assets\\app\\JobStatus"
active.log = "active.json"
totalActivos = active.items()

failed = JobStatus()
failed.path = "assets\\app\\JobStatus"
failed.log = "failed.json"
totalActivos = failed.items()

for item in failed.jobs:
	#print item
	if (active.find(item)):
		print "Existe en active ... Quitando ..."
		active.delete(item)
	else:
		print "En espera de mas Fallados"

"""
item = {"path": "PlayToAir", "size": 1119535342, "type": "file", "modifiedDate": "2014-10-16T00:46:56", "name": "LA SEMANA-FT_DF000P0D"}
queued = JobStatus()
queued.path = "assets\\app\\JobStatus"
queued.log = "queued.json"
queued.delete(item)
"""

"""
queued = JobStatus()
queued.path = "assets\\app\\JobStatus"
queued.log = "queued.json"
item = {"modifiedDate": "2014-10-15T22:01:23","name": "INFORME RODRIGO MEDINA-_DF000OZH","path": "PlayToAir","size": 282886323,"type": "file"}
queued.add(item)
"""
"""
queued = JobStatus()
queued.path = "assets\\app\\JobStatus"
queued.log = "queued.json"
#item = {"addTime": "2014-10-16T01:01:27", "name": "video10.cmf", "size": "252525"}
item = {"addTime": "2014-10-16T01:01:17", "name": "video19.cmf", "size": "252525"}
queued.add(item)

active = JobStatus()
active.path = "assets\\app\\JobStatus"
active.log = "active.json"
item = {"addTime": "2014-10-16T01:01:27", "name": "video10.cmf", "size": "252525"}
#item = {"addTime": "2014-10-16T01:01:17", "name": "video19.cmf", "size": "252525"}
active.add(item)

"""