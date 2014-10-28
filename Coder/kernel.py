import os
import datetime
import sys
import shutil
sys.path.append('lib')
from l_dirchar import *
from l_workJson import *

kernelSettings = readJson("assets\\app\\kernel.json")

print kernelSettings[0]["watchs"]

watchs = readJson(kernelSettings[0]["watchs"])

print "\n",watchs

agents = readJson(kernelSettings[0]["agents"])

print "\n",agents
