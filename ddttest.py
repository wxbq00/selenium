import unittest
from selenium import webdriver
import ddt
@ddt.ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        print('setup')
    @ddt.data(['data1', '123'], ['data2', '456'])
    @ddt.unpack
    def test_something(self,data,excepect):
        print(data)
        print(excepect)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


