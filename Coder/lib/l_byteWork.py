####################  Conversiones de  Bytes ################
# Trabajando con potencias 1024 bytes
#-------------------- Transformando Bytes a unidades --------#
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

#return formatSize{"value":"","unit":""}
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

#-------------------- Transformando unidades a bytes --------#
def kibToBytes(sizeBytes):
	bytes = sizeBytes * 1024
	return bytes


def mibToBytes(sizeBytes):
	bytes = kibToBytes(sizeBytes) * 1024
	return bytes


def gibToBytes(sizeBytes):
	bytes = mibToBytes(sizeBytes) * 1024
	return bytes


def tibToBytes(sizeBytes):
	bytes = gibToBytes(sizeBytes) * 1024
	return bytes


def pibToBytes(sizeBytes):
	bytes = tibToBytes(sizeBytes) * 1024
	return bytes


def eibToBytes(sizeBytes):
	bytes = pibToBytes(sizeBytes) * 1024
	return bytes


def zibToBytes(sizeBytes):
	bytes = eibToBytes(sizeBytes) * 1024
	return bytes


def yibToBytes(sizeBytes):
	bytes = zibToBytes(sizeBytes) * 1024
	return bytes


#Calcula valor en bytes de x cantidad de unidad x
def unitToBytes(value,unit):
	if (unit == "KiB"):
		bytes = kibToBytes(value)
	elif (unit == "MiB"):
		bytes = mibToBytes(value)
	elif (unit == "GiB"):
		bytes = gibToBytes(value)
	elif (unit == "TiB"):
		bytes = tibToBytes(value)
	elif (unit == "PiB"):
		bytes = pibToBytes(value)
	elif (unit == "EiB"):
		bytes = eibToBytes(value)
	elif (unit == "ZiB"):
		bytes = zibToBytes(value)
	elif (unit == "YiB"):
		bytes = yibToBytes(value)
	return bytes
####################  Conversiones de  Bytes ################