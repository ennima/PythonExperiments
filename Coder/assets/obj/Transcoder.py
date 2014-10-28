import os
import sys
import subprocess
import datetime
import shutil
import time
import json
import ftplib
from time import mktime
class Transcoder:
	
	threads = 48
	prevDir = ""
	defaultEngine = "engine"
	enginePath = "C:\Users\enrique.nieto\Desktop\PythonExperiments\Watch\Coder\\assets\engines"
	mov = ""
	dateFilter = "%Y-%m-%dT%H:%M:%S"
	filtro = "mp=eq2=1:1.68:0.3:1.25:1:0.96:1"
	#destFolder = "..\..\dest"
	destFolder ="default"
	#Dest Types local, ftp, unc
	destType = "ftp"
	preset = "MXF-MPEG"

	#Ftp
	ftpObj = {"host":"192.168.196.92","user":"mxfmovie","pass":""}

	#unc
	uncObj = {"user":"GVAdmin","pass":"adminGV!","path":"\\\\192.168.196.92"}

	def __init__(self):
		print "Transcoder Created..."
		print "Engine: ",self.defaultEngine
		print "Threads:",self.threads

	def cmfToMxf(self,path,cmf):
		inicio1 = datetime.datetime.now()
		cmfSplit = cmf.split(".")
		#obtengo mov
		self.mov = cmfSplit[0]+".mov"
		print cmfSplit
		#prevdir
		self.prevDir = os.getcwd()
		
		#inject engine
		if(os.path.exists(path+"\\"+cmf+"\\"+self.defaultEngine+".exe")):
			print "existe"
		else:
			print "Copiando Engine"
			shutil.copy(self.enginePath+"\\"+self.defaultEngine + ".exe",path+"\\"+cmf)
			print "shutill"
		os.chdir(path+"\\"+cmf)
		print os.getcwd()

		if(os.path.exists(self.mov)):
			print "existe mov"
			self.mxfSummit(self.mov)
		final1 = datetime.datetime.now()
		delta1 = final1 - inicio1
		transcodingObject = {"name":cmfSplit[0],"transcodingTime":str(delta1),"transcodigDate":final1.strftime(self.dateFilter)}

	def cmfToMxfFilter(self,cmf):
		inicio1 = datetime.datetime.now()
		cmfSplit = cmf.split(".")
		#obtengo mov
		self.mov = cmfSplit[0]+".mov"
		
		#prevdir
		self.prevDir = os.getcwd()
		
		#inject engine
		if(os.path.exists(cmf+"\\"+self.defaultEngine+".exe")):
			print "existe"
		else:
			print "Copiando Engine"
			shutil.copy(self.defaultEngine + ".exe",cmf)
			print "shutill"
		os.chdir(cmf)
		if(os.path.exists(self.mov)):
			print "existe mov"
			mxfSummitFilter(self.mov)
		final1 = datetime.datetime.now()
		delta1 = final1 - inicio1
		transcodingObject = {"name":cmfSplit[0],"transcodingTime":str(delta1),"transcodigDate":final1.strftime(dateFilter)}

	def mxfSummit(self,video):
		nombreSp = video.split(".")
		new = nombreSp[0]+".mxf"
		
		if(self.preset == "MXF-MPEG"):
			summitPreset = [self.defaultEngine,"-threads",str(self.threads),"-i",video,"-vcodec","mpeg2video","-vtag","xd5b","-s","1920x1080","-pix_fmt","yuv420p","-b:v","50000k","-dc","9","-flags","+ilme+ildct","-top","1","-aspect","16:9","-acodec","pcm_s16le","-ac","2","-f","mxf","-threads",str(self.threads),new] 
		else:
			summitPreset = [self.defaultEngine,"-threads",str(self.threads),"-i",video,"-vcodec","mpeg2video","-vtag","xd5b","-s","1920x1080","-pix_fmt","yuv420p","-b:v","50000k","-dc","9","-flags","+ilme+ildct","-top","1","-aspect","16:9","-acodec","pcm_s16le","-ac","2","-f","mxf","-threads",str(self.threads),new] 
		exito = False
		print "convierte mov"
		
		if(os.path.exists(new)):
			print "Existe el "+new
			exito = False
		else:
			inicio = datetime.datetime.now()

			p = subprocess.Popen(summitPreset)
			p.wait()
			finP = datetime.datetime.now()
			deltap = finP -inicio
			print "--->",deltap
			if(self.destType=="local"):
				print "Sending "+new+"..."+self.destFolder
				self.localSend(self.destFolder,new)
				print "Send Succes"
			elif(self.destType=="ftp"):
				self.ftpSend(self.ftpObj["host"],self.ftpObj["user"],self.ftpObj["pass"],self.destFolder,new)
			elif(self.destType=="unc"):
				self.uncSend(self.uncObj["user"],self.uncObj["pass"],self.destFolder,new)


			fin = datetime.datetime.now()
			delta = fin - inicio
			print "listo tardo: ",delta
			exito = True

	def mxfSummitFilter(self,video):
		nombreSp = video.split(".")
		new = nombreSp[0]+".mxf"
		
		summitPreset = ["ffmpeg","-threads",self.threads,"-i",video,"-vcodec","mpeg2video","-vtag","xd5b","-s","1920x1080","-pix_fmt","yuv420p","-b:v","50000k","-dc","9","-flags","+ilme+ildct","-top","1","-aspect","16:9","-vf",self.filtro,"-acodec","pcm_s16le","-ac","2","-f","mxf","-threads",self.threads,new] 
		#summitPreset = ["ffmpeg","-threads",self.threads,"-i",video,"-vcodec","mpeg2video","-vtag","xd5b","-s","1920x1080","-pix_fmt","yuv420p","-b:v","50000k","-dc","9","-flags","+ilme+ildct","-top","1","-aspect","16:9","-acodec","pcm_s16le","-ac","2","-f","mxf","-threads",self.threads,new] 
		
		exito = False
		print "convierte mov"
		
		if(os.path.exists(new)):
			print "Existe el "+new
			exito = False
		else:
			inicio = datetime.datetime.now()
			ffQuery = "ffmpeg -i "+self.mov+" "+new
			print ffQuery
			p = subprocess.Popen(summitPreset)
			p.wait()
			fin = datetime.datetime.now()
			delta = fin - inicio
			print "listo tardo: ",delta
			exito = True

	############# Dest Functions ############
	def ftpSend(self,host,user,passs,destFolder,newFile):
		#Login FTP to Summit
		#host = "192.168.196.92"
		#user = "mxfmovie"
		passs = ""
		ftp = ftplib.FTP(host)
		ftp.login(user,passs)
		ftp.cwd(destFolder)
		#print ftp.pwd()
		print "Enviando "+os.path.basename(newFile) +" a ftp Dest..."
		ftp.storbinary('STOR '+os.path.basename(newFile),open(newFile,'rb'))
		ftp.quit()
		print "Listo."

	def localSend(self,destFolder,newFile):
		newFinal = destFolder+"\\"+newFile
		shutil.copy(newFile,newFinal)

	def uncSend(self,user,passs,destFolder,newFile):
		print "UNC"


#trans = Transcoder()

#origen = "..\..\origin"
#cmf = "COPYRIGHT4.cmf"

#testCmf = origen+"\\"+cmf
#trans.cmfToMxf(origen,cmf)

