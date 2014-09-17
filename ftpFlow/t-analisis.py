"""
	Test l_analisis
"""
import sys
sys.path.append('lib')
from l_analisis import *

fileName = "Camarografos/Salvador/CONFERENCIA MORENA"

ftpCredentials = {'host':'192.168.196.139','user':'mxf','passwd':''}

con = ftplib.FTP('192.168.196.139')
con.login('mxfmovie','')

path = ""

result = []
#wtf = lamda x: result.append(x)
s = con.retrlines('LIST '+path, callback=result.append)

data = []
for i in result:
	#print i
	#print dataFromFtpLine(i)
	data.append(dataFromFtpLine(i))

#print data
#saveJson(data,"","DownList.json")
raiz = listFromObject(data,"2012-09-13T00:00:00",path)
for item in raiz:
	print item["modifiedDate"]," ",item['path'],"-",item["name"]
listaGrande =  runListFind(raiz,"2014-09-16T15:40:00")
for elemnto in listaGrande:
	print elemnto
saveJson(listaGrande,"","DownList.json")
con.quit()