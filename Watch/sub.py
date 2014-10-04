import time
import os
import json
import datetime
import subprocess
from time import mktime


#Return datetime convierte una cadena tipo "2014-09-30T00:40:00" a datetime
def stringToTime(strl,dateFilter):
	minDate = time.strptime(strl,dateFilter)
	newDate = datetime.datetime.fromtimestamp(mktime(minDate))
	return newDate



fechaCmd = "2014-09-30T22:59:59"
p= subprocess.Popen(['python','t_dirs.py','V:\media\PlayToAir',fechaCmd],shell=True)
print p.communicate()
print "next"