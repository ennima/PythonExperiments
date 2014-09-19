from l_byteWork import *
############### Trabajando con peso en disco #####################

#Suma el peso de los elementos de una lista de descarga con data de peso
def sizeDownList(downList):
	totalSizeBytes = 0
	for item in downList:
		totalSizeBytes += item["sizeBytes"]
	return totalSizeBytes

#Suma el peso de un rango de elementos en orden hasta completar una cuota de peso
#Entrega un objeto con el total en bytes y un objeto listaDescarga
def sizeDownListByQuota(downList,maxSizeBytes):
	miniListDict = {}
	miniList = []
	totalSizeBytes = 0
	for item in downList:
		if(totalSizeBytes <= maxSizeBytes):
			if(item["sizeBytes"] < maxSizeBytes):
				totalSizeBytes += item["sizeBytes"]
				miniList.append(item)
				if (totalSizeBytes > maxSizeBytes):
					totalSizeBytes -= item["sizeBytes"]
					miniList.remove(item)
					#break
			#print "totalSizeBytes: "+str(totalSizeBytes)
			#print "maxSizeBytes: "+str(maxSizeBytes)
		else:
			break
	miniListDict["size"] = totalSizeBytes
	miniListDict["downList"] = miniList
	return miniListDict


#Suma el peso de un rango de elementos en orden hasta completar una cuota
#de peso, buscando bajar la mayor cantidad de elementos de poco peso
#Entrega un objeto con el total en bytes y un objeto listaDescarga
def sizeDownListByQuotaLow(downList,maxSizeBytes):
	miniListDict = {}
	miniList = []
	tmpList = []
	totalSizeBytes = 0
	tmpTotalSizeBytes = 0
	difTotalSizeBytes = 0

	maxSizeObj = bytesToFormatSize(maxSizeBytes)

	for item in downList:
		if(totalSizeBytes <= maxSizeBytes):
			if(item["sizeBytes"] < maxSizeBytes):
				print "item['sizeUnit']: "+item['sizeUnit']
				if(item['sizeUnit'] == maxSizeObj['unit']):
					print "Descarta"
					tmpList.append(item)
				else:
					totalSizeBytes += item["sizeBytes"]
					miniList.append(item)
					if (totalSizeBytes > maxSizeBytes):
						totalSizeBytes -= item["sizeBytes"]
						miniList.remove(item)
						#break

			print "totalSizeBytes: "+str(totalSizeBytes)
			print "maxSizeBytes: "+str(maxSizeBytes)
		else:
			break

	difTotalSizeBytes = maxSizeBytes - totalSizeBytes
	difTotalSizeBytesObj = bytesToFormatSize(difTotalSizeBytes)
	print "Diferencia: "+str(difTotalSizeBytesObj["value"])+" "+difTotalSizeBytesObj["unit"]
	perCentDifTotalSizeBytes = float((difTotalSizeBytes * 100) / maxSizeBytes)
	print "Equivale a : "+str(perCentDifTotalSizeBytes)+"%"

	maxSizeObj = bytesToFormatSize(maxSizeBytes)
	maxUnitValBytes = unitToBytes(1,maxSizeObj["unit"])
	perCentUnitVal = float((maxUnitValBytes * 100) / maxSizeBytes)
	print "perCentUnitVal: "+str(perCentUnitVal)+"%"

	sumaDescBytes = 0.0
	for item in tmpList:
		#print item
		sumaDescBytes += item["sizeBytes"]
		if(sumaDescBytes < difTotalSizeBytes):
			#print "#### Agregar a lista principal"
			print "totalSizeBytes: "+str(totalSizeBytes)
			print "maxSizeBytes: "+str(maxSizeBytes)
			totalSizeBytes += item["sizeBytes"] 
			miniList.append(item)




	miniListDict["size"] = totalSizeBytes
	miniListDict["downList"] = miniList
	return miniListDict


#Suma el peso de un rango de elementos en orden hasta completar una cuota
#de peso, buscando bajar los objetos mas pesados
#Entrega un objeto con el total en bytes y un objeto listaDescarga
def sizeDownListByQuotaHi(downList,maxSizeBytes):
	miniListDict = {}
	miniList = []
	tmpList = []
	totalSizeBytes = 0
	tmpTotalSizeBytes = 0
	difTotalSizeBytes = 0

	maxSizeObj = bytesToFormatSize(maxSizeBytes)

	for item in downList:
		if(totalSizeBytes <= maxSizeBytes):
			if(item["sizeBytes"] < maxSizeBytes):
				print "item['sizeUnit']: "+item['sizeUnit']
				if(item['sizeUnit'] == maxSizeObj['unit']):
					totalSizeBytes += item["sizeBytes"]
					miniList.append(item)
					if (totalSizeBytes > maxSizeBytes):
						totalSizeBytes -= item["sizeBytes"]
						miniList.remove(item)
				else:
					print "Descarta"
					tmpList.append(item)
					
						#break

			print "totalSizeBytes: "+str(totalSizeBytes)
			print "maxSizeBytes: "+str(maxSizeBytes)
		else:
			break

	difTotalSizeBytes = maxSizeBytes - totalSizeBytes
	difTotalSizeBytesObj = bytesToFormatSize(difTotalSizeBytes)
	print "Diferencia: "+str(difTotalSizeBytesObj["value"])+" "+difTotalSizeBytesObj["unit"]
	perCentDifTotalSizeBytes = float((difTotalSizeBytes * 100) / maxSizeBytes)
	print "Equivale a : "+str(perCentDifTotalSizeBytes)+"%"

	maxSizeObj = bytesToFormatSize(maxSizeBytes)
	maxUnitValBytes = unitToBytes(1,maxSizeObj["unit"])
	perCentUnitVal = float((maxUnitValBytes * 100) / maxSizeBytes)
	print "perCentUnitVal: "+str(perCentUnitVal)+"%"

	sumaDescBytes = 0.0
	for item in tmpList:
		#print item
		sumaDescBytes += item["sizeBytes"]
		if(sumaDescBytes < difTotalSizeBytes):
			#print "#### Agregar a lista principal"
			print "totalSizeBytes: "+str(totalSizeBytes)
			print "maxSizeBytes: "+str(maxSizeBytes)
			totalSizeBytes += item["sizeBytes"] 
			miniList.append(item)




	miniListDict["size"] = totalSizeBytes
	miniListDict["downList"] = miniList
	return miniListDict
