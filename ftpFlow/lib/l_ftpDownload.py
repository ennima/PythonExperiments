import os
from l_JobManager import *
from l_byteWork import *
from l_fileSystem import *
from l_downList import *


def l_ftpDownloadTest():
	test()


def copiaFile(ftp,destFolder,rootPath,item):
	#remoteFileSize =ftp.size(item["path"]+"/"+item["name"])
	try:
		newFile = destFolder+"/"+item["path"]+"/"+item["name"]+".mxf"
		print newFile
		
		if(os.path.exists(newFile)):
			
			print "Ya existe el Archivo: "+newFile+" "
			localFileSize = os.path.getsize(newFile)
			print "SIZE: "+str(localFileSize)
			if(localFileSize > 0):
				print "COOL"
			else:
				print "\n \n "
				print "KILL"
				os.remove(newFile)
				print "Killed:"+newFile
				print "FTP PWD: "+ftp.pwd()
				ftp.cwd(rootPath)
				ftp.cwd(item["path"])
				print "Copiar: "+item["path"]+"/"+item["name"]
				ftp.retrbinary('RETR '+item["name"],open(destFolder+"/"+item["path"]+"/"+item["name"]+".mxf",'wb').write)
				
		else:
			ftp.cwd(rootPath)
			ftp.cwd(item["path"])
			print "Copiar: "+item["path"]+"/"+item["name"]
			ftp.retrbinary('RETR '+item["name"],open(destFolder+"/"+item["path"]+"/"+item["name"]+".mxf",'wb').write)
			
	except ftplib.error_perm, msg:
		localFileSize = bytesToMb(os.path.getsize(newFile))
		print "Este Archivo esta corrupto: "+newFile+" "+str(localFileSize)+" Mb"
		print msg
		print "\n \n "
		print "---------------------------------"


	#raw_input()

#Agrega a una lista de descarga informacion del peso del archivo
def sizeItemDownList(ftpObj,downList):
	ftp = ftplib.FTP(ftpObj["host"])
	ftp.login(ftpObj["user"],ftpObj["pass"])

	for item in downList:
		remoteFileSize =ftp.size(item["path"]+"/"+item["name"])
		remoteFileSizeF = bytesToFormatSize(remoteFileSize)
		#print str(remoteFileSizeF["value"])+" "+remoteFileSizeF["unit"]
		item["sizeValue"] = remoteFileSizeF["value"]
		item["sizeUnit"] = remoteFileSizeF["unit"]
		item["sizeBytes"] = remoteFileSizeF["bytes"]
		print item["name"]+"  "+str(item["sizeValue"])+" "+item["sizeUnit"]+" "+str(item["sizeBytes"])
	ftp.quit()
	return downList



############### Trabajando con la Descarga ###############
#Descarga los elementos de una lista de descarga
def downloadItems(downList,destFolder,ftpObj):
	downLog = []
	downObj ={}
	#conectar FTP
	ftp = ftplib.FTP(ftpObj["host"])
	ftp.login(ftpObj["user"],ftpObj["pass"])
	inDir = ""
	rootPath = ftp.pwd()
	if not os.path.exists(destFolder):
		print "Error: No existe el directorio de destino"
	else:
		for item in downList:
			print "inDir: "+inDir
			print "item['path']: "+item["path"]
			print "PWD: "+ftp.pwd()
			print "item['name']: "+item["name"]

			if not os.path.exists(destFolder+"/"+item["path"]):
				print "Crear: "+item["path"]
				os.makedirs(destFolder+"/"+item["path"])
				
				if(inDir == item["path"]):
					print "in"
					copiaFile(ftp,destFolder,rootPath,item)
				else:
					inDir = item["path"]
					#rootPath = ftp.pwd()
					ftp.cwd(rootPath)
					ftp.cwd(item["path"])
					copiaFile(ftp,destFolder,rootPath,item)
			else:
				if(inDir == item["path"]):
					print "in"
					copiaFile(ftp,destFolder,rootPath,item)
				else:
					inDir = item["path"]

					#rootPath = ftp.pwd()
					ftp.cwd(rootPath)
					copiaFile(ftp,destFolder,rootPath,item)
	ftp.quit()
				
