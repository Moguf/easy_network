'''
downloader.py
=============


'''

import logging
import threading
from queue import Queue
from urllib.request import urlretrieve

from easyutil import MultiCmdAnimation

class Downloader:
    def __init__(self, urls, filenames, msgs, sizes):
        self.urls = urls
        self.MAX_THREAD = 30
        self.Queue = Queue()
        self.thread_args = []
        self.N = len(self.urls)
        self.filenames = filenames
        self.msgs = msgs
        self.sizes = sizes
        
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
        tmp = MultiCmdAnimation('progress', filenames=self.filenames, msg=self.msgs, sizes=self.sizes)
        tmp.start()
        self.Queue.join()

        [ thread.join() for thread in threads ]
        tmp.end()
        
    def _get(self):
        msg, filename, url, size = self.Queue.get(True, 0.01)
        urlretrieve(url, filename)

    def _getProgressBar(self):
        pass
        
if __name__ == '__main__' :
    url = ['http://www.google.com','http://yahoo.co.jp','https://github.com']
    tmp = Downloader(url)
    tmp.gets()
