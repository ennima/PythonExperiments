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



 #################################### 

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
