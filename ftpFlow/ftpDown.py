import os
import sys
sys.path.append('lib')
from l_ftpDownload import *

#l_ftpDownloadTest()
destFolder = "/mnt/Noticias/VBackup/Noticias/RESPALDO OFFLINE2"
if not os.path.exists(destFolder):
	os.makedirs(destFolder)
ftpObj = {"host":"192.168.196.139","user":"mxfmovie","pass":""}
downList = readJson("cleanDownloadList.json")
formatList = sizeItemDownList(ftpObj,downList)
sizeFormatList = bytesToFormatSize(sizeDownList(formatList))
print "Tu lista pesa: " + str(sizeDownList(formatList)) + " bytes"
print "Tu lista pesa: " + str(sizeFormatList["value"]) + " "+sizeFormatList["unit"]


print "\n \n"
sizeGb = 20
sizeBy = gbToBytes(sizeGb)
newSizeGb = bytesToGb(sizeBy)

print newSizeGb
#downloadItems(downList,destFolder,ftpObj)