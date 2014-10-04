import time
import datetime
import os
import sys
"""
dateFilter = "%Y-%m-%dT%H:%M:%S"
#horas
pollerTime = 1
ahorita = datetime.datetime.now()
quitale = datetime.timedelta(hours=pollerTime)
haceUnRato = ahorita - quitale

print "ahorita: ",ahorita.strftime(dateFilter)
print "haceUnRato: ", haceUnRato.strftime(dateFilter)
"""
def haceUnRatoFormat(nowDate,pollerTime):
	dateFilter = "%Y-%m-%dT%H:%M:%S"

	#horas

	ahorita = datetime.datetime.now()
	quitale = datetime.timedelta(hours=pollerTime)
	haceUnRato = ahorita - quitale

	#print "ahorita: ",ahorita.strftime(dateFilter)
	#print "haceUnRato: ", haceUnRato.strftime(dateFilter)
	return haceUnRato.strftime(dateFilter)

f = haceUnRatoFormat(datetime.datetime.now(),2)

print "Hace Rato: ",f