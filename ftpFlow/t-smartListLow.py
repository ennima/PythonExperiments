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


quotaObj = sizeDownListByQuotaLow(formatList,gibToBytes(4))


quota = bytesToFormatSize(quotaObj["size"])
print "\n \n Tu lista quota pesa: " + str(quota["value"])+" "+quota["unit"]
print "Elementos por descargar quota: "+ str(len(quotaObj["downList"]))
for item in quotaObj["downList"]:
	print item["name"]+" "+str(item["sizeValue"])+" "+item["sizeUnit"]
print "\n \n"
sizeGb = 20
sizeBy = gibToBytes(sizeGb)
newSizeGb = bytesToGiB(sizeBy)

print newSizeGb
#downloadItems(quotaObj["downList"],destFolder,ftpObj)