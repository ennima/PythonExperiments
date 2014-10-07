import datetime
import time

from History import History


historial = History()

historial.path = "history\his"
historial.backupPath = "Bk"
historial.key_id = "id"
historial.key_criteria2 = "size"
historial.key_criteria = "name"




#### Object File
#				modififiedDate
#				name
#				path
#				type
#				size

baseList = []
baseB = []
baseFormat = []
for i in range(0,6):
	baseList.append({"id":i, "name":"FILdE_"+str(i),"path":"PlayToAir","type":"cmf","size":2923654568212,"modififiedDate":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})

historial.set(baseList)
historial.get()


historial.printStatus()

historial.save()