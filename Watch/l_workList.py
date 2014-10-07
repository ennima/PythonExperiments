##########################################
#Return Item From list that coincides item["Key"] = val
def findInList(lista,key,val):
	match = next((i for i in lista if i[key] == val),None)
	return match

def findInList2(lista,key,val,key2,val2):
	match = next((i for i in lista if i[key] == val if i[key2] == val2),None)
	return match

def findItemList(item, lista):
	for linea in lista:
		print item
		print linea
		print "#######################\n"
#Return Sorted List from base list
def sortList(lista,keyy):
	newList = sorted(lista, key=lambda k:k[keyy])
	return newList

def diferenceList(lista1,lista2):
	listA =[]
	listB =[]
	diferencia = []
	if(len(lista1)>len(lista2)):
		#print "Lista1 Mayor"
		listA = lista2
		listB = lista1

	elif(len(lista1)<len(lista2)):
		#print "lista2 Mayor"
		listA = lista1
		listB = lista2
	elif(len(lista1)==len(lista2)):
		listA = lista1
		listB = lista2

	for lineaA in listA:
		#print lineaA,"\n"
		if(lineaA in listB):
			#print "Esta"
			pass
		else:
			#print "NONEs"
			diferencia.append(lineaA)
	return diferencia