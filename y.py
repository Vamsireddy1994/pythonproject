from x import *
import unittest
class Test_Demo(unittest.TestCase):
    def setup():
        pass
    def test(self):
        res=sum()
        assert res==30
    def tearDown(self):
        print("teardown executed")
        
unittest.main()
    
