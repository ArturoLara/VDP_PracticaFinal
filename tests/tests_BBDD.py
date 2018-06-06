# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
import unittest
from aplication.BBDD import gestorBBDD



class tester_text_data_miner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bbdd = gestorBBDD()

    def test_insert_data(self):
        lista = {"test":1, "data": 2}
        dict = {"test":2, "nuevo": 1}
        self.bbdd.r.zadd("testData", **dict)
        self.bbdd.addData("testData", **lista)
        result = self.bbdd.r.zrange("testData", 0, -1, desc=True, withscores=True)
        assert result == [('test', 3.0), ('data', 2.0), ('nuevo', 1.0)]


    def test_insert_data_with_no_data(self):
        lista = {"test": 1, "data": 2}
        self.bbdd.addData("testData", **lista)
        result = self.bbdd.r.zrange("testData", 0, -1, desc=True, withscores=True)
        assert result == [("data", 2.0), ("test", 1.0)]


    def test_get_data(self):
        dict = {"test":2, "data": 3}
        self.bbdd.r.zadd("testData", **dict )
        result = self.bbdd.showData("testData")
        assert result == [("data", 3.0), ("test", 2.0)]


    def test_get_empy_data(self):
        result = self.bbdd.showData("testData")
        assert result == []


    def test_delete_data(self):
        dict = {"test":2, "data": 3}
        self.bbdd.r.zadd("testData", **dict )
        self.bbdd.removeData("testData")
        result = self.bbdd.r.keys(pattern="testData")
        assert result == []


    def test_delete_empty_data(self):
        self.bbdd.removeData("testData")
        result = self.bbdd.r.keys(pattern="testData")
        assert result == []


    def tearDown(self):
        self.bbdd.r.delete("testData")



if __name__ == '__main__':
    unittest.main()
