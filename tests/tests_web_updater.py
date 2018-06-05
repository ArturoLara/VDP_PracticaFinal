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

    def other_method(self):
        return [("simple", 1)]

    def test_invalid_url(self):
        result = web_updater("invalidUrl")
        assert result == [["No se ha podido", "leer la pagina"]]

    @patch('aplication.web_updater.get_text_from_url', return_value=["simple"])
    @patch('aplication.web_updater.gestorBBDD.showData', return_value=[("simple",1)])
    def test_simple_text(self, mocked, mocked_2):
        result = web_updater("mok")
        print result
        assert result == [("simple", 1)]



if __name__ == '__main__':
    unittest.main()