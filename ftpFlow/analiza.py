"""
	version: 0.0.1
	Author: Enrique Nieto
	Date: 16/09/14
	Description:Comando que analiza FS remoto y genera una lista de descargas a partir
				de los siguientes parametros.

				-h   Help command

			Conexion:
				-s | --host : Especifica el nombre o ip del host a analizar
				-u | --user : Especifica el usuario FTP
				-p | --pass : Especifica el password FTP

			Busqueda:
				-d | --path : Especifica la ubicacion del directorio root
				-b | --base-date: Fecha minima del directorio root
				-m | --min-date: Fecha minima para buscar material
			File List
				-j | --json Nombre del archivo json final
				-jp| --json-path ubicacion del archivo json final


"""

import sys
import getopt
sys.path.append('/mnt/Noticias/VBackup/Noticias/ftpFlow/lib')
from l_analisis import *

def showHelp():
	print ""
	print ""
	print "CONNECTION DATA"
	print "-s | --host : Especifica el nombre o ip del host a analizar"
	print "-u | --user : Especifica el usuario FTP"
	print "-p | --pass : Especifica el password FTP"
	print ""
	print ""
	print "FIND DATA"
	print "-d | --path : Especifica la ubicacion del directorio root"
	print "-b | --base-date: Fecha minima del directorio root"
	print "-m | --min-date: Fecha minima para buscar material"
	print ""
	print ""
	print "File List"
	print "-j | --json Nombre del archivo json final"
	print "-jp| --json-path ubicacion del archivo json final"
	
				
				

def proceso(cmdDict):
	con = ftplib.FTP(cmdDict["host"])
	con.login(cmdDict["user"],cmdDict["pass"])

	path = cmdDict["path"]

	result = []
	
	s = con.retrlines('LIST '+path, callback=result.append)

	data = []
	for i in result:
		data.append(dataFromFtpLine(i))

	raiz = listFromObject(data,cmdDict["baseDate"],path)
	for item in raiz:
		print item["modifiedDate"]," ",item['path'],"-",item["name"]
	listaGrande =  runListFind(raiz,cmdDict["minDate"])
	for elemnto in listaGrande:
		print elemnto
	saveJson(listaGrande,cmdDict["jsonPath"],cmdDict["jsonFile"])
	con.quit()


def main(argv):
	host = "192.168.196.139"
	user = "mxfmovie"
	passw = ""

	path = ""
	baseDate = "2012-09-13T00:00:00"
	minDate = "2014-09-16T15:40:00"
	jsonFile ="DownloadList.json"
	jsonPath = ""
	try:
		opts, args = getopt.getopt(argv,"hs:u:p:d:b:m",["host=","user=","pass=","path=","base-date=","min-date="])
	except getopt.GetoptError:
		showHelp()
		sys.exit(2)

	for opt, arg in opts:

		if opt == '-h':
			showHelp()
			sys.exit()
		elif opt in ("-s","--host"):
			host = arg
		elif opt in ("-u","--user"):
			user = arg
		elif opt in ("-p","--pass"):
			passw = arg
		elif opt in ("-d","--path"):
			path = arg
		elif opt in ("-b","base-date"):
			baseDate = arg
		elif opt in ("-m","--min-date"):
			minDate = arg
		elif opt in ("-j","--json"):
			jsonFile = arg
		elif opt in ("-jp","--json-path"):
			jsonPath = arg

	cmdDict = {"host":host,"user":user,"pass":passw,"path":path,"baseDate":baseDate,"minDate":minDate,"jsonFile":jsonFile,"jsonPath":jsonPath}
	print cmdDict
	proceso(cmdDict)


if __name__ == "__main__":
	main(sys.argv[1:])