import urllib2

urls=[url.strip() for url in open("urls.txt","rb").readlines() if url.strip()]
import threading
class DownloadUrl(threading.Thread):
     def __init__(self,queue):
         self.queue=queue
         threading.Thread.__init__(self)
     def run(self):
         while not self.queue.empty():
              url=self.queue.get()
              web=urllib2.urlopen(url,None,5)
import Queue
queue=Queue.Queue()
for url in urls: queue.put(url)
threadnumber=10
threads=[]
for i in xrange(threadnumber):
    threads.append(DownloadUrl(queue))
for i in xrange(threadnumber):
    threads[i].start()
for i in xrange(threadnumber):
    threads[i].join()