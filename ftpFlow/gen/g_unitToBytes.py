import os
import sys
import json

def readJson(jsonFile):
	with open(jsonFile) as json_file:
		json_data = json.load(json_file)
		#print json_data

	print "Total de Files: "+str(len(json_data))
	
	return json_data
#funciones de las que depende esta funcion


funciones =readJson("g_unitToBytes.json")

#generando contenido de funciones dependientes

contenido = []
mainFunc = []
base = 1024
prevFunction = {}
for funcion in funciones:
	print funcion

	if(funcion["prefix"] == "kib"):
		linea0 = "def "+funcion["prefix"]+funcion["sufix"]+"("+funcion["param"]+"):"
		linea1 = "	bytes = "+funcion["param"]+" * "+str(base)
		linea2 = "	return bytes"
		linea3 = "\n"
		contenido.append(linea0)
		contenido.append(linea1)
		contenido.append(linea2)
		contenido.append(linea3)
		mHead0 ="def unitToBytes(value,unit):"
		mLine0 = "	if (unit == \""+funcion["unit"]+"\"):"
		mLine1 = "		bytes = "+funcion["prefix"]+funcion["sufix"]+"(value)"
		mainFunc.append(mHead0)
		mainFunc.append(mLine0)
		mainFunc.append(mLine1)
	else:
		linea0 = "def "+funcion["prefix"]+funcion["sufix"]+"("+funcion["param"]+"):"
		funcTo =prevFunction["prefix"]+prevFunction["sufix"]+"("+prevFunction["param"]+")" 
		linea1 = "	bytes = "+funcTo+" * "+str(base)
		linea2 = "	return bytes"
		linea3 = "\n"
		contenido.append(linea0)
		contenido.append(linea1)
		contenido.append(linea2)
		contenido.append(linea3)
		mLinea = "	elif (unit == \""+funcion["unit"]+"\"):"
		mLine1 = "		bytes = "+funcion["prefix"]+funcion["sufix"]+"(value)"
		mainFunc.append(mLinea)
		mainFunc.append(mLine1)

	
	prevFunction = funcion
mLineEnd = "	return bytes"
mainFunc.append(mLineEnd)

f = open("gn_unitToBytes.py","w+")

for linea in contenido:
	print linea
	print>>f, linea

		
print "\n #################################### \n"
print>>f,"\n #################################### \n"
for linea in mainFunc:
	print linea
	print>>f, linea

f.close()



