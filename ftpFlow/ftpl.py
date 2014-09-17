import ftplib

ftp = ftplib.FTP("192.168.196.139")
ftp.login("movie","")
data = []
ftp.dir(data.append)
#filess = ftp.dir()
ftp.quit()
print data[1]
#for line in data:
#	print "-", line