import sys
import os
import ftplib

filea= ""
filed = ""
for arg in sys.argv:
	#print arg
	#print os.path.basename(arg)
	#print os.path.abspath(arg)
	#print os.path.dirname(arg)
	filea = os.path.abspath(arg)
	filed = os.path.dirname(arg)

#cambiando nombre
print "Nombre: "
a = raw_input()
#print filea,"+----+ ",filed+"\\"+a+".mxf"

newFile = filed+"\\"+a+".mxf"
os.rename(filea,newFile)


#Login FTP to Summit
host = "192.168.196.92"
user = "mxfmovie"
passs = ""
ftp = ftplib.FTP(host)
ftp.login(user,passs)
ftp.cwd("default")
#print ftp.pwd()
print "Enviando "+os.path.basename(newFile) +" a summit standalone..."
ftp.storbinary('STOR '+os.path.basename(newFile),open(newFile,'rb'))
ftp.quit()
print "Listo."
#b= raw_input()

