import os
############### Trabajando con peso en disco del File System Local#####################

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

