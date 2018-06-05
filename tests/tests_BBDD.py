# -*- coding: UTF-8 -*-

import sys
import unittest
from aplication.BBDD import gestorBBDD
sys.path.append("..")

class tester_text_data_miner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        gestorBBDD().r.zadd("tempTestData", 1, "a")

    def test_insert_data(self):
        lista = [["test", 1], ["data", 2]]
        gestorBBDD().addData("testData", lista)
        result = gestorBBDD().r.zrange("testData", 0, -1, desc=True, withscores=True)
        assert result == ["test", "1", "data", "2"]


    def test_get_data(self):
        result = gestorBBDD().showData("tempTestData")
        assert result == ["a", "1"]

    def test_delete_data(self):
        gestorBBDD().removeData("tempTestData")
        result = gestorBBDD().r.keys(pattern="tempTestData")
        assert result == ""

    @classmethod
    def tearDownClass(cls):
        gestorBBDD().r.delete("tempTestData")
        gestorBBDD().r.delete("testData")



if __name__ == '__main__':
    unittest.main()
