import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


observer = Observer()

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


class MyHandler(FileSystemEventHandler):
    tmpSize = 0
    lastFileModified = ""
    
    def on_modified(self, event):
        print "on_modified"
        

        
        if event.is_directory:
            #Step 1
            print "dir"
            print os.path.dirname(event.src_path)
            print os.path.basename(event.src_path)
            filepath, ext = os.path.splitext(event.src_path)
            print ext
            pathToSend = os.path.dirname(event.src_path)
            dirCmf = os.path.basename(event.src_path)
            dirToFile = dirCmf.split(".")
            fileToSend = dirToFile[0]
            print fileToSend
            print pathToSend

            #Step2
            print "Last created: "+self.lastFileModified
            if (self.lastFileModified ==""):
                self.lastFileModified = fileToSend
                print "##############################################"
                
            elif(self.lastFileModified != fileToSend):
                self.lastFileModified = fileToSend
                time.sleep(1)

            elif(self.lastFileModified == fileToSend):
                
                print "fileSize: "+str(get_size(event.src_path)) +" bytes"
                if(self.tmpSize == get_size(event.src_path)):
                    print "Chau"
                    self.lastFileModified = ""
                    self.tmpSize = 0
                    time.sleep(1)
                    
                  

            #a = raw_input()

        else: 
            print event.src_path
            filepath, ext = os.path.splitext(event.src_path)
            print filepath
            print ext

    def on_deleted(self, event):
        print "Delete"

    def on_created(self, event):
        print "created"
        if event.is_directory:
            #Step 1
            print "dir"
            print os.path.dirname(event.src_path)
            print os.path.basename(event.src_path)
            filepath, ext = os.path.splitext(event.src_path)
            print ext
            pathToSend = os.path.dirname(event.src_path)
            dirCmf = os.path.basename(event.src_path)
            dirToFile = dirCmf.split(".")
            fileToSend = dirToFile[0]
            print fileToSend
            print pathToSend

            #Step2
            self.lastFileModified = fileToSend


        else: 
            print event.src_path
            filepath, ext = os.path.splitext(event.src_path)
            print filepath
            print ext


if __name__ == "__main__":
    event_handler = MyHandler()
    
    observer.schedule(event_handler, path='V:\media\PlayToAir', recursive=False)
    
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()