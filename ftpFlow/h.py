import os
import ftplib
dataTransferQuery = {}


def listFtpDir(ftpServer,user,passw):
	ftp = ftplib.FTP(ftpServer)
	ftp.login(user,passw)
	carpetas = []
	ftp.dir(carpetas.append)
	ftp.quit()
	return carpetas

def arrayPrint(arr):
	for  lines in arr:
		print lines

def getRoutes(dataQueryList):

	print "Hola Free NAS"
	os.system("ls")
	print "\n Listo"

	carpetaDestino = raw_input("Escribe el directorio de destino: ")
	#print carpetaDestino
	dataQueryList.update({'carpetaDestino':carpetaDestino})

	#servidorCopiar = raw_input("Escribe la IP del Servidor de Media: ")
	#servidorCopiarUser = raw_input("Usuario: ")
	#servidorCopiarPass = raw_input("Password: ")
	servidorCopiar = "192.168.196.139"
	servidorCopiarUser = "mxfmovie"
	servidorCopiarPass = ""
	
	dataQueryList.update({'servidorCopiarUser':servidorCopiarUser})
	dataQueryList.update({'servidorCopiarPass':servidorCopiarPass})
	dataQueryList.update({'servidorCopiar':servidorCopiar})
	
	carpetas = []
	carpetas =  listFtpDir(servidorCopiar,servidorCopiarUser,"")
	arrayPrint(carpetas)
	carpetaCopiar = raw_input("Escribe la ruta del directorio a copiar: ")
	dataQueryList.update({'carpetaCopiar':carpetaCopiar})
	#print carpetaCopiar

	#data = carpetaDestino + "<---" + servidorCopiar + "\\" + carpetaCopiar
	#print data
	#for key, val in dataQueryList.items():
	#	print key
	#	for attribute, value in dataQueryList.items():
	#		print('{} : {}'.format(attribute, value))
	print dataQueryList
	return dataQueryList


def download_cb(block):
	file.write(block)

def ftpDownload(dataQueryList):
	log = dict()
	#ftp = ftplib.FTP("192.168.196.139")
	ftp = ftplib.FTP(dataQueryList["servidorCopiar"])
	ftp.login(dataQueryList["servidorCopiarUser"],dataQueryList["servidorCopiarPass"])
	#ftp.cwd("/Noticias")
	ftp.cwd("/"+dataQueryList["carpetaCopiar"])
	archivosEnCarpetaCopiar = ftp.nlst()
	for asset in archivosEnCarpetaCopiar:
		try:
			print "Transfering: "+asset
			ftp.retrbinary('RETR '+asset,open(dataQueryList["carpetaDestino"]+"/hT_"+asset+".mxf",'wb').write)
		except ftplib.error_perm:
			print "Este Archivo esta corrupto"
			log.update({"Archivo Corrupto":"/"+dataQueryList["carpetaCopiar"]+"/"+asset})
	
	ftp.quit()
	print log

rutas = dict()
rutas = getRoutes(dataTransferQuery)
ftpDownload(rutas)