import os

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

#Entrega Estadisticas de espacio en disco del path
#return fsStatObj
"""
	formatSize = {"value":0,"unit":"TiB","bytes":10000000}

	totalSize = FormatSize
	actualFreeBytes = FormatSize
	resSpace = FormatSize
	usedSpace = FormatSize

	usedSpacePerCent = int %
	freeSpacePerCent = int %
"""
def unixFsStat(pathFs):
	stat = os.statvfs(pathFs)

	totalSize = bytesToFormatSize(stat.f_frsize * stat.f_blocks)
	actualFreeBytes = bytesToFormatSize(stat.f_frsize * stat.f_bfree)
	resSpace = bytesToFormatSize(stat.f_frsize * stat.f_bavail)
	usedSpace = bytesToFormatSize(totalSize["bytes"] - actualFreeBytes["bytes"])

	usedSpacePerCent = (usedSpace["bytes"] *100) / totalSize["bytes"]
	freeSpacePerCent = 100 - usedSpacePerCent

	fsStatObj = {}
	fsStatObj["path"] = pathFs
	fsStatObj["totalSize"] = totalSize
	fsStatObj["actualFreeBytes"] = actualFreeBytes
	fsStatObj["resSpace"] = resSpace
	fsStatObj["usedSpace"] = usedSpace
	fsStatObj["usedSpacePerCent"] = usedSpacePerCent
	fsStatObj["freeSpacePerCent"] = freeSpacePerCent

	return fsStatObj

def printFsStatObj(fsStatObj):
	for attrib in fsStatObj:
		print attrib,":",fsStatObj[attrib]
		#print fsStatObj[attrib]
		#print "------------------------"

pathFs = "/mnt/Noticias/VBackup"
fsStatObj =  unixFsStat(pathFs)

#print fsStatObj["totalSize"]
printFsStatObj(fsStatObj)
"""
for attrib in fsStatObj:
	print attrib
	print fsStatObj[attrib]
	print "------------------------"
	"""