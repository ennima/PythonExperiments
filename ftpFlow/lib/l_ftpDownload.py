import os
from l_JobManager import *

def l_ftpDownloadTest():
	test()

# Trabajando con potencias 1024 bytes
def bytesToKiB(sizeBytes):
	kbs = float(sizeBytes/1024)
	return kbs

def bytesToMiB(sizeBytes):
	kbSize = bytesToKiB(sizeBytes)
	mbs = float(kbSize/1024)
	return mbs

def bytesToGiB(sizeBytes):
	mbs = bytesToMiB(sizeBytes)
	gbs = float(mbs/1024)
	return gbs

def bytesToTiB(sizeBytes):
	gbs = bytesToGiB(sizeBytes)
	tbs = float(gbs/1024)
	return tbs
	

def bytesToPiB(sizeBytes):
	tbs = bytesToTiB(sizeBytes)
	pbs = float(tbs/1024)
	return pbs

def bytesToEiB(sizeBytes):
	pbs = bytesToPiB(sizeBytes)
	ebs = float(pbs/1024)
	return ebs

def bytesToZiB(sizeBytes):
	ebs = bytesToEiB(sizeBytes)
	zbs = float(ebs/1024)
	return zbs

def bytesToYiB(sizeBytes):
	zbs = bytesToZiB(sizeBytes)
	ybs = float(zbs/1024)
	return ybs


def bytesToFormatSize(sizeBytes):
	formatSize = {"value":0,"unit":"bytes"}
	if (bytesToYiB(sizeBytes)<1):
		if (bytesToZiB(sizeBytes)<1):
			if (bytesToEiB(sizeBytes)<1):
				if (bytesToPiB(sizeBytes)<1):
					if (bytesToTiB(sizeBytes)<1):
						if(bytesToGiB(sizeBytes)<1):
							
							if(bytesToMiB(sizeBytes)<1):
								
								if(bytesToKiB(sizeBytes)<1):
									#print "Bytes"
									formatSize["value"] = sizeBytes
									formatSize["unit"] = "bytes"
								else:
									#print "Kb"
									formatSize["value"] = bytesToKiB(sizeBytes)
									formatSize["unit"] = "KiB"
							else:
								#print "Mb"
								formatSize["value"] = bytesToMiB(sizeBytes)
								formatSize["unit"] = "MiB"
						else:
							#print "Gb"
							formatSize["value"] = bytesToGiB(sizeBytes)
							formatSize["unit"] = "GiB"
					else:
						formatSize["value"] = bytesToTiB(sizeBytes)
						formatSize["unit"] = "TiB"
				else:
					formatSize["value"] = bytesToPiB(sizeBytes)
					formatSize["unit"] = "PiB"
			else:
				formatSize["value"] = bytesToEiB(sizeBytes)
				formatSize["unit"] = "EiB"
		else:
			formatSize["value"] = bytesToZiB(sizeBytes)
			formatSize["unit"] = "ZiB"
	else:
		formatSize["value"] = bytesToYiB(sizeBytes)
		formatSize["unit"] = "YiB"

	formatSize["bytes"] = sizeBytes
	
	return formatSize



def kbToBytes(sizeKb):
	bytes = sizeKb * 1024
	return bytes

def mbToBytes(sizeMb):
	bytes = (sizeMb * 1024) * 1024
	return bytes

def gbToBytes(sizeGv):
	bytes = ((sizeGv * 1024) * 1024) * 1024
	return bytes

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

#Suma el peso de los elementos de una lista de descarga con data de peso
def sizeDownList(downList):
	totalSizeBytes = 0
	for item in downList:
		totalSizeBytes += item["sizeBytes"]
	return totalSizeBytes

#Suma el peso de un rango de elementos en orden hasta completar una cuota de peso
def sizeDownListByQuota(downList,maxSizeBytes):
	totalSizeBytes = 0
	for item in downList:
		if(totalSizeBytes <= maxSizeBytes):
			totalSizeBytes += item["sizeBytes"]
		else:
			break


	
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
				
