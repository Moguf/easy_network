import os
import sys
import unittest

class TestDownloader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #sys.path.append(os.path.abspath('../easynetwork'))
        from easynetwork import downloader
        cls.urls = ['www.google.com','www.yahoo.co.jp']
        cls.testclass = downloader.Downloader(cls.urls)

    def setUp(self):
        pass

    def test_gets_Page(self):
        self.testclass.gets()


    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass




if __name__ == '__main__':
    unittest.main()
    
