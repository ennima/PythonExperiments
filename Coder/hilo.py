import threading
import time
import datetime

def worker():
	inicio = datetime.datetime.now()
	print "-"+threading.currentThread().getName()+ " Lanzado"
	
	for i in range(0,4):
		print "-"+threading.currentThread().getName()+ " -- "+str(i)
		time.sleep(5)
	print "-"+threading.currentThread().getName()+ " Detenido"
	fin = datetime.datetime.now()
	delta =fin - inicio
	print "###"+threading.currentThread().getName()+"Tardo: "+str(delta)
def servicio():
	inicio = datetime.datetime.now()
	print "-"+threading.currentThread().getName()+ " Lanzado"
	time.sleep(3)
	print "-"+threading.currentThread().getName()+ " Detenido"
	fin = datetime.datetime.now()
	delta =fin - inicio
	print "###"+threading.currentThread().getName()+"Tardo: "+str(delta)

t = threading.Thread(target=servicio,name="Servicio")
w = threading.Thread(target=worker,name="Worker")
z = threading.Thread(target=worker)

t.start()
w.start()
z.start()