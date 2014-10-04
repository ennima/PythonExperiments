import datetime
import time

from History import History


historial = History()

historial.path = "history\his"
historial.backupPath = "Bk"




#### Object File
#				modififiedDate
#				name
#				path
#				type
#				size

baseList = []
baseB = []
baseFormat = []
for i in range(0,20):
	baseList.append({"name":"FILE_"+str(i),"path":"PlayToAir","type":"cmf","size":1923654568212,"modififiedDate":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})

historial.set(baseList)
historial.get()


historial.printStatus()
