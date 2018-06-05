# -*- coding: UTF-8 -*-

import sys
from aplication.web_updater import web_updater
from aplication.get_text_from_url import get_text_from_url
import unittest
import mock

import aplication.get_text_from_url

from mock import patch

sys.path.append("..")

class tester_text_data_miner(unittest.TestCase):

    def pass_method(self, now):
        pass

    def test_invalid_url(self):
        result = web_updater("invalidUrl")
        assert result == [["No se ha podido", "leer la pagina"]]

    @patch('aplication.web_updater.get_text_from_url', return_value=["simple"])
    @patch('aplication.web_updater.gestorBBDD.showData', return_value=[("simple",1)])
    @patch('aplication.web_updater.gestorBBDD.addData', side_effect=pass_method)
    def test_simple_text(self, mocked, mocked_2, mocked_3):
        result = web_updater("mock")
        assert result == [["simple", 1]]



    @patch('aplication.web_updater.get_text_from_url', return_value=["simple pero cierto simple pero cierto"])
    @patch('aplication.web_updater.gestorBBDD.showData', return_value=[("simple",1)])
    @patch('aplication.web_updater.gestorBBDD.addData', side_effect=pass_method)
    def test_complex_text(self, mocked, mocked_2, mocked_3):
        result = web_updater("mock")
        assert result == [['simple', 2], ['cierto', 2]]



if __name__ == '__main__':
    unittest.main()