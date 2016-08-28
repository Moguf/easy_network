'''
downloader.py
=============


'''

import logging
import threading
from queue import Queue
from urllib.request import urlretrieve

class Downloader:
    def __init__(self, urls):
        self.urls = urls
        self.MAX_THREAD = 30
        self.Queue = Queue()
        self.thread_args = []
        self.N = len(self.urls)
        self.filenames = [ 'index-'+str(i)+'.html' for i in range(self.N) ]        
        self.msgs = [ '' for i in range(self.N) ]
        self.sizes = [ 0 for i in range(self.N) ]
        
    def _init(self):
        pass
    
    def setFilename(self, names=[]):
        if names:
            for i, name in enumerate(names):
                self.filename[i] = name

    def setMsg(self, msgs=[]):
        if msgs:
            for i, msg in enumerate(msgs):
                self.msgs[i] = msg
                
    def setSize(self, sizes=[]):
        if sizes:
            for i, size in enumerate(sizes):
                self.sizes[i] = size

    def _setArgs(self):
        for i, url in enumerate(self.urls):
            self.Queue.put((self.msgs[i], self.filenames[i], url, self.sizes[i]))
        
    def gets(self):
        self._setArgs()
        threads = [ threading.Thread(daemon=True, target=self._get,
                                     args=()) for i in range(self.N) ]
        [ thread.start() for thread in threads ]
        self.Queue.join()
        [ thread.join() for thread in threads ]
        
    def _get(self):
        msg, filename, url, size = self.Queue.get(True, 0.01)
        urlretrieve(url, filename)

    def _getProgressBar(self):
        pass
        
if __name__ == '__main__' :
    url = ['http://www.google.com','http://yahoo.co.jp','https://github.com']
    tmp = Downloader(url)
    tmp.gets()
