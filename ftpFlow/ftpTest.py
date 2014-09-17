import ftplib
ftp = ftplib.FTP("192.168.196.139")
ftp.login("mxfmovie","")
ftp.cwd("/Camarografos/Alex  G/CAMARA DIPUTADOS")
ftp.retrbinary('RETR '+"CAMARA DIPUTADOS(2)",open("T_CAMARA DIPUTADOS(2).mxf",'wb').write)
ftp.quit()