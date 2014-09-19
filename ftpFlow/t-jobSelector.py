import sys
sys.path.append('lib')
from l_jobSelector import *

listt = [{"a":1,"b":"g"},{"a":1,"b":"g"},{"a":1,"b":"g"}]
lista = "DownloadList.json"

dirs = ["Noticias","PlayToAir","Ingesta Noticias","Estudio","Recycle Bin"]

jm = JobSelector(lista)

cleanList = jm.makeSubListByDiscard(dirs)

jm.makeSubListsByNumber(3)
#for item in cleanList:
#	print item
#jm.makeSublistsByNumber()