import sys
sys.path.append('lib')
from l_JobManager import *
dirs = ["Noticias","PlayToAir","Ingesta Noticias","Estudio","Cepropie","Recycle Bin"]
js = readJson("DownloadList.json")
blackList = discardDirs(dirs,js)
downList = cleanDownList(blackList,js)
print "Original :",len(js)
print "Descartados :",len(blackList)
print "Descargables :",len(downList)
saveJson(downList,"","cleanDownloadList.json")